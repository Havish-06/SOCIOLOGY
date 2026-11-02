"""Reply-thread analysis: who argues with the backlash, and does pushback calm a thread down?

Needs a `label` column (from hand-coding or the classifier) on comments_flagged.csv.

    python -m src.threads --flagged data/processed/comments_flagged_labelled.csv --out data/processed

Outputs:
    threads.csv          one row per thread (top-level comment with >= 1 reply)
    threads_summary.csv  one row per case

Two estimates of whether pushback "calms" a hostile thread:
  1. First-reply design: among threads whose root is hostile, compare the hostile share of
     replies 2..n when reply 1 is pushback vs when it is not. Same position in every thread,
     so thread length and timing are held roughly constant.
  2. Within-thread: hostile share of the replies before vs after the first pushback.
YouTube replies are flat (no nesting), so a reply is read as responding to the thread, in time order.
"""
import argparse
from pathlib import Path

import numpy as np
import pandas as pd

HOSTILE = {"backlash", "threat", "demand_legal_action"}
DEFENDING = {"support", "mock_offended"}


def mark_regular_audience(df):
    """True if the author also commented on one of the comedian's control (non-controversial) videos.

    Pushback from regulars = the comedian's own audience defending them; pushback from
    newcomers = a wider public arguing back.
    """
    if "video_role" not in df:
        return pd.Series(False, index=df.index)
    regulars = set(zip(df.loc[df["video_role"] == "control", "case_id"],
                       df.loc[df["video_role"] == "control", "author_channel_id"]))
    return pd.Series([(c, a) in regulars for c, a in zip(df["case_id"], df["author_channel_id"])], index=df.index)


def thread_table(df):
    df = df.copy()
    df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
    df["hostile"] = df["label"].isin(HOSTILE)
    df["defending"] = df["label"].isin(DEFENDING)
    df["regular"] = mark_regular_audience(df)
    if "category" not in df:
        df["category"] = "unknown"

    roots = df[df["parent_id"].isna()].set_index("comment_id")
    replies = df[df["parent_id"].notna()].sort_values("published_at")
    rows = []
    for root_id, rep in replies.groupby("parent_id"):
        if root_id not in roots.index:
            continue
        root = roots.loc[root_id]
        # pushback = the opposite side replying: defenders against a hostile root, or vice versa
        opposing = rep["defending"] if root["hostile"] else rep["hostile"] if root["defending"] else pd.Series(False, index=rep.index)
        pos = int(np.argmax(opposing.to_numpy())) if opposing.any() else None
        h = rep["hostile"].to_numpy()
        row = {
            "case_id": root["case_id"], "video_id": root["video_id"], "thread_id": root_id,
            "root_label": root["label"], "root_hostile": bool(root["hostile"]),
            "root_category": root["category"], "root_likes": root.get("like_count", np.nan),
            "n_replies": len(rep), "n_reply_authors": rep["author_channel_id"].nunique(),
            "has_pushback": pos is not None, "pushback_pos": pos,
            "first_reply_pushback": bool(opposing.iloc[0]),
            "hostile_share_replies": h.mean(),
            "hostile_share_after_reply1": h[1:].mean() if len(h) > 1 else np.nan,
            "hostile_share_before_pushback": h[:pos].mean() if pos else np.nan,
            "hostile_share_after_pushback": h[pos + 1:].mean() if pos is not None and pos + 1 < len(h) else np.nan,
            "replies_after_pushback": len(h) - pos - 1 if pos is not None else np.nan,
        }
        if pos is not None:
            pb = rep.iloc[pos]
            row.update(pushback_category=pb["category"], pushback_regular=bool(pb["regular"]),
                       pushback_likes=pb.get("like_count", np.nan),
                       minutes_to_pushback=(pb["published_at"] - root["published_at"]).total_seconds() / 60)
        rows.append(row)
    return pd.DataFrame(rows)


def summarise_threads(t):
    out = []
    for case, g in t.groupby("case_id"):
        hr = g[g["root_hostile"]]
        with_pb, without_pb = hr[hr["first_reply_pushback"]], hr[~hr["first_reply_pushback"]]
        pb = hr[hr["has_pushback"]]
        out.append({
            "case_id": case,
            "n_threads": len(g),
            "pct_hostile_roots": g["root_hostile"].mean(),
            "pct_hostile_threads_with_pushback": hr["has_pushback"].mean() if len(hr) else np.nan,
            "median_minutes_to_pushback": pb["minutes_to_pushback"].median() if len(pb) else np.nan,
            "pushback_from_regulars": pb["pushback_regular"].mean() if len(pb) else np.nan,
            "pushback_from_organic": (pb["pushback_category"] == "organic").mean() if len(pb) else np.nan,
            # first-reply design
            "hostile_after_r1_if_pushback": with_pb["hostile_share_after_reply1"].mean(),
            "hostile_after_r1_if_no_pushback": without_pb["hostile_share_after_reply1"].mean(),
            "calming_effect_r1": without_pb["hostile_share_after_reply1"].mean() - with_pb["hostile_share_after_reply1"].mean(),
            # within-thread
            "hostile_before_pushback": pb["hostile_share_before_pushback"].mean() if len(pb) else np.nan,
            "hostile_after_pushback": pb["hostile_share_after_pushback"].mean() if len(pb) else np.nan,
            "mean_thread_len_hostile_root": hr["n_replies"].mean() if len(hr) else np.nan,
        })
    return pd.DataFrame(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--flagged", required=True, help="comments with category (src.spam) and label columns")
    ap.add_argument("--out", default="data/processed")
    args = ap.parse_args()
    df = pd.read_csv(args.flagged)
    if "label" not in df:
        raise SystemExit("needs a 'label' column: run hand-coding / the classifier first")
    t = thread_table(df)
    s = summarise_threads(t)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    t.to_csv(out / "threads.csv", index=False)
    s.to_csv(out / "threads_summary.csv", index=False)
    print(s.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
