"""Collect YouTube comments and commenter-channel metadata via the YouTube Data API v3.

Usage:
    python -m src.collect --videos data/videos.csv          # every usable video in the video table
    python -m src.collect --video-ids abc123 def456 --case-id test

data/videos.csv has one row per video: case_id, video_id, role (case | control),
video_type (original | reupload | news | response | commentary), status. Rows whose
status starts with "unavailable" or "rejected" are skipped.

Needs YOUTUBE_API_KEY in the environment (or in a .env file).
Quota: commentThreads.list / comments.list / channels.list cost 1 unit per call
(100 comments or 50 channels per call), against a default 10,000 units/day.
"""
import argparse
import os
import time
from pathlib import Path

import pandas as pd
import requests
from dotenv import load_dotenv

API = "https://www.googleapis.com/youtube/v3"
RAW = Path("data/raw")


def _get(endpoint, params, key, retries=3):
    params = {**params, "key": key}
    for attempt in range(retries):
        r = requests.get(f"{API}/{endpoint}", params=params, timeout=30)
        if r.status_code == 200:
            return r.json()
        if r.status_code in (403, 404):
            # 403 commentsDisabled / quotaExceeded, 404 videoNotFound: report, don't retry
            reason = r.json().get("error", {}).get("errors", [{}])[0].get("reason", r.text[:200])
            raise RuntimeError(f"{endpoint} {params.get('videoId') or params.get('parentId') or ''}: {reason}")
        time.sleep(2 ** attempt)
    r.raise_for_status()


def _row(item, video_id, case_id, parent_id=None):
    s = item["snippet"]
    return {
        "case_id": case_id,
        "video_id": video_id,
        "comment_id": item["id"],
        "parent_id": parent_id,
        "author_channel_id": s.get("authorChannelId", {}).get("value"),
        "author_name": s.get("authorDisplayName"),
        "text": s.get("textOriginal", ""),
        "like_count": s.get("likeCount", 0),
        "published_at": s.get("publishedAt"),
        "updated_at": s.get("updatedAt"),
    }


def fetch_comments(video_id, key, case_id=""):
    """All top-level comments and all replies for one video."""
    rows, token = [], None
    while True:
        params = {"part": "snippet,replies", "videoId": video_id, "maxResults": 100,
                  "textFormat": "plainText", "order": "time"}
        if token:
            params["pageToken"] = token
        data = _get("commentThreads", params, key)
        for thread in data.get("items", []):
            top = thread["snippet"]["topLevelComment"]
            rows.append(_row(top, video_id, case_id))
            n_replies = thread["snippet"].get("totalReplyCount", 0)
            inline = thread.get("replies", {}).get("comments", [])
            # the thread only embeds up to 5 replies; page through the rest
            replies = inline if len(inline) >= n_replies else fetch_replies(top["id"], key)
            rows.extend(_row(c, video_id, case_id, parent_id=top["id"]) for c in replies)
        token = data.get("nextPageToken")
        if not token:
            break
    return pd.DataFrame(rows)


def fetch_replies(parent_id, key):
    out, token = [], None
    while True:
        params = {"part": "snippet", "parentId": parent_id, "maxResults": 100, "textFormat": "plainText"}
        if token:
            params["pageToken"] = token
        data = _get("comments", params, key)
        out.extend(data.get("items", []))
        token = data.get("nextPageToken")
        if not token:
            return out


def fetch_channels(channel_ids, key):
    """Account metadata for commenters: creation date, uploads, subscribers."""
    ids = [c for c in pd.unique(pd.Series(channel_ids).dropna())]
    rows = []
    for i in range(0, len(ids), 50):
        data = _get("channels", {"part": "snippet,statistics", "id": ",".join(ids[i:i + 50]),
                                 "maxResults": 50}, key)
        for ch in data.get("items", []):
            st, sn = ch.get("statistics", {}), ch.get("snippet", {})
            rows.append({
                "author_channel_id": ch["id"],
                "channel_published_at": sn.get("publishedAt"),
                "channel_custom_url": sn.get("customUrl"),
                "channel_country": sn.get("country"),
                "subscriber_count": pd.to_numeric(st.get("subscriberCount"), errors="coerce"),
                "hidden_subscriber_count": st.get("hiddenSubscriberCount", False),
                "video_count": pd.to_numeric(st.get("videoCount"), errors="coerce"),
                "view_count": pd.to_numeric(st.get("viewCount"), errors="coerce"),
            })
    return pd.DataFrame(rows)


def fetch_video_meta(video_ids, key):
    rows = []
    for i in range(0, len(video_ids), 50):
        data = _get("videos", {"part": "snippet,statistics", "id": ",".join(video_ids[i:i + 50])}, key)
        for v in data.get("items", []):
            sn, st = v["snippet"], v.get("statistics", {})
            rows.append({"video_id": v["id"], "title": sn.get("title"), "channel_id": sn.get("channelId"),
                         "channel_title": sn.get("channelTitle"), "video_published_at": sn.get("publishedAt"),
                         "views": st.get("viewCount"), "likes": st.get("likeCount"),
                         "comment_count": st.get("commentCount")})
    return pd.DataFrame(rows)


def videos_from_table(path):
    """(case_id, video_id, role, video_type) for every usable row of the video table."""
    v = pd.read_csv(path, dtype=str).fillna("")
    v = v[~v["status"].str.startswith(("unavailable", "rejected"))]
    return list(v[["case_id", "video_id", "role", "video_type"]].itertuples(index=False, name=None))


def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    ap.add_argument("--videos", help="video table, e.g. data/videos.csv")
    ap.add_argument("--video-ids", nargs="*", default=[])
    ap.add_argument("--case-id", default="adhoc")
    ap.add_argument("--out", default=str(RAW))
    args = ap.parse_args()

    key = os.environ.get("YOUTUBE_API_KEY")
    if not key:
        raise SystemExit("Set YOUTUBE_API_KEY (see .env.example)")

    triples = (videos_from_table(args.videos) if args.videos
               else [(args.case_id, v, "case", "unknown") for v in args.video_ids])
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    frames = []
    for case_id, vid, role, vtype in triples:
        try:
            df = fetch_comments(vid, key, case_id).assign(video_role=role, video_type=vtype)
        except RuntimeError as e:
            print(f"skip {vid}: {e}")
            continue
        df.to_csv(out / f"comments_{vid}.csv", index=False)
        print(f"{case_id} {vid} ({role}): {len(df)} comments")
        frames.append(df)
    if not frames:
        return

    comments = pd.concat(frames, ignore_index=True)
    comments.to_csv(out / "comments.csv", index=False)
    fetch_video_meta([t[1] for t in triples], key).to_csv(out / "video_meta.csv", index=False)
    channels = fetch_channels(comments["author_channel_id"], key)
    channels.to_csv(out / "channels.csv", index=False)
    print(f"total {len(comments)} comments, {len(channels)} commenter channels -> {out}")


if __name__ == "__main__":
    main()
