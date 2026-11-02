"""Authenticity audit: flag commercial spam, copy-paste campaigns, timing bursts,
co-timed account networks and throwaway accounts, then measure how concentrated
the commenting is (who is actually doing the talking).

Usage:
    python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv --out data/processed

Outputs (in --out):
    comments_flagged.csv   one row per comment with every signal
    accounts_flagged.csv   one row per commenting account with its category
    summary.csv            one row per video: volume, concentration, % by category

None of these signals proves a comment is fake. Each is a reason to look closer;
the category combines them conservatively and must be validated by hand-coding
(see src/sample.py).
"""
import argparse
import re
from collections import defaultdict
from itertools import combinations
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from sklearn.feature_extraction.text import TfidfVectorizer

COMMERCIAL = re.compile(
    r"https?://|www\.|\b(?:sub(?:scribe)? to my|check (?:out )?my (?:channel|video)|visit my channel"
    r"|whats ?app|telegram|crypto|bitcoin|forex|binary option|investment plan|earn \$?\d+|dm me)\b"
    r"|\+?\d[\d\s-]{9,}\d",
    re.I,
)
AUTO_HANDLE = re.compile(r"^@user-[a-z0-9]{6,}$", re.I)       # YouTube's auto-generated handles
NAME_DIGITS = re.compile(r"^@?[a-z]+[._-]?\d{4,}$", re.I)       # e.g. @rahul84629


def normalise(text):
    text = re.sub(r"https?://\S+", " URL ", str(text).lower())
    text = re.sub(r"[^\w\s]", " ", text)
    return re.sub(r"\s+", " ", text).strip()


# ---------- comment-level signals ----------

def near_duplicate_clusters(texts, authors, threshold=0.9, min_len=20, min_authors=3, chunk=2000):
    """Cluster comments whose character-n-gram TF-IDF cosine >= threshold.

    Returns (cluster_id, n_authors_in_cluster) arrays; cluster_id is -1 for comments that
    are too short or whose cluster was written by fewer than `min_authors` distinct accounts.
    Short comments ("lol", "🔥🔥") are excluded because they repeat naturally.
    """
    norm = pd.Series(texts).map(normalise)
    idx = np.flatnonzero(norm.str.len().to_numpy() >= min_len)
    cluster = np.full(len(norm), -1)
    n_auth = np.zeros(len(norm), dtype=int)
    if len(idx) < 2:
        return cluster, n_auth

    X = TfidfVectorizer(analyzer="char_wb", ngram_range=(3, 5), min_df=1).fit_transform(norm.iloc[idx])
    rows, cols = [], []
    for start in range(0, X.shape[0], chunk):
        sim = (X[start:start + chunk] @ X.T).tocoo()
        keep = sim.data >= threshold
        rows.append(sim.row[keep] + start)
        cols.append(sim.col[keep])
    r, c = np.concatenate(rows), np.concatenate(cols)
    graph = coo_matrix((np.ones(len(r)), (r, c)), shape=(len(idx), len(idx)))
    _, labels = connected_components(graph, directed=False)

    auth = pd.Series(np.asarray(authors)[idx])
    per_cluster = auth.groupby(labels).nunique()
    sizes = per_cluster.reindex(labels).to_numpy()
    ok = sizes >= min_authors
    cluster[idx[ok]] = labels[ok]
    n_auth[idx] = sizes
    return cluster, n_auth


def burst_flags(df, freq="10min", window=36, factor=5.0, min_count=20):
    """Flag comments posted in a time bin far above that video's trailing baseline.

    Baseline = median count of the previous `window` bins (6 hours at 10-min bins).
    A bin is a burst if count >= max(min_count, factor * (baseline + 1)).
    Organic virality also produces bursts, so this is a weak signal on its own.
    """
    flags = pd.Series(False, index=df.index)
    for _, g in df.groupby("video_id"):
        t = g["published_at"].dt.floor(freq)
        counts = t.value_counts().sort_index()
        counts = counts.reindex(pd.date_range(counts.index.min(), counts.index.max(), freq=freq), fill_value=0)
        base = counts.shift(1).rolling(window, min_periods=1).median().fillna(0)
        burst_bins = counts.index[(counts >= min_count) & (counts >= factor * (base + 1))]
        flags.loc[g.index] = t.isin(burst_bins).to_numpy()
    return flags


# ---------- account-level signals ----------

def cotiming_clusters(df, window_s=60, min_videos=2, max_bin_authors=50):
    """Accounts that repeatedly comment within the same `window_s` seconds on the same video,
    across at least `min_videos` different videos (co-timing coordination, after Pacheco et al. 2021).

    Bins with more than `max_bin_authors` accounts are skipped: those are ordinary viral rushes
    and would otherwise link thousands of unrelated people.
    Returns {author_channel_id: cluster_id}.
    """
    d = df.dropna(subset=["author_channel_id"]).copy()
    d["bin"] = d["published_at"].astype("int64") // (window_s * 10**9)
    pair_videos = defaultdict(set)
    for (vid, _), g in d.groupby(["video_id", "bin"]):
        authors = sorted(set(g["author_channel_id"]))
        if 2 <= len(authors) <= max_bin_authors:
            for a, b in combinations(authors, 2):
                pair_videos[(a, b)].add(vid)
    G = nx.Graph()
    G.add_edges_from(p for p, vids in pair_videos.items() if len(vids) >= min_videos)
    return {a: i for i, comp in enumerate(nx.connected_components(G)) for a in comp}


def gini(counts):
    x = np.sort(np.asarray(counts, dtype=float))
    if len(x) == 0 or x.sum() == 0:
        return np.nan
    n = len(x)
    return float((2 * np.arange(1, n + 1) @ x) / (n * x.sum()) - (n + 1) / n)


def top_share(counts, frac):
    """Share of all comments written by the most active `frac` of accounts."""
    x = np.sort(np.asarray(counts, dtype=float))[::-1]
    if len(x) == 0:
        return np.nan
    k = max(1, int(np.ceil(frac * len(x))))
    return float(x[:k].sum() / x.sum())


# ---------- pipeline ----------

def audit(comments, channels=None, dup_threshold=0.9, new_account_days=30):
    df = comments.copy()
    df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
    df["author_channel_id"] = df["author_channel_id"].fillna("unknown:" + df["author_name"].fillna(""))

    df["commercial"] = df["text"].fillna("").str.contains(COMMERCIAL)
    df["dup_cluster"], df["dup_cluster_authors"] = near_duplicate_clusters(
        df["text"].fillna(""), df["author_channel_id"], threshold=dup_threshold)
    df["in_dup_campaign"] = df["dup_cluster"] >= 0
    df["in_burst"] = burst_flags(df)

    handle = df["author_name"].fillna("")
    if channels is not None and len(channels):
        ch = channels.copy()
        ch["channel_published_at"] = pd.to_datetime(ch["channel_published_at"], utc=True)
        df = df.merge(ch, on="author_channel_id", how="left")
        df["account_age_days"] = (df["published_at"] - df["channel_published_at"]).dt.days
        handle = df["channel_custom_url"].astype(object).fillna(df["author_name"]).fillna("")
    else:
        df["account_age_days"] = np.nan
        df["video_count"] = np.nan
    df["new_account"] = df["account_age_days"] < new_account_days
    df["auto_handle"] = handle.str.match(AUTO_HANDLE) | handle.str.match(NAME_DIGITS)

    coord = cotiming_clusters(df)
    df["cotiming_cluster"] = df["author_channel_id"].map(coord).fillna(-1).astype(int)

    acc = df.groupby("author_channel_id").agg(
        n_comments=("comment_id", "size"),
        n_videos=("video_id", "nunique"),
        n_cases=("case_id", "nunique"),
        commercial=("commercial", "any"),
        dup_campaign=("in_dup_campaign", "any"),
        burst_share=("in_burst", "mean"),
        new_account=("new_account", "any"),
        auto_handle=("auto_handle", "any"),
        no_uploads=("video_count", lambda s: bool((s == 0).any())),
        account_age_days=("account_age_days", "min"),
        cotiming_cluster=("cotiming_cluster", "max"),
        total_likes=("like_count", "sum"),
    )
    acc["cotiming"] = acc["cotiming_cluster"] >= 0
    acc["mostly_burst"] = acc["burst_share"] > 0.5

    coordination = acc["dup_campaign"] | acc["cotiming"]
    account_red_flag = acc["new_account"] | acc["auto_handle"] | acc["mostly_burst"]
    acc["suspicion_score"] = acc[["dup_campaign", "cotiming", "new_account", "auto_handle", "mostly_burst"]].sum(axis=1)
    acc["category"] = np.select(
        [acc["commercial"],
         (coordination & account_red_flag) | (acc["dup_campaign"] & acc["cotiming"]),
         coordination | (acc["new_account"] & acc["mostly_burst"])],
        ["commercial_spam", "likely_coordinated", "uncertain"],
        default="organic",
    )
    df = df.merge(acc[["category", "suspicion_score"]], left_on="author_channel_id", right_index=True, how="left")
    return df, acc.reset_index()


def summarise(df, hostile_labels=("backlash", "threat")):
    rows = []
    for vid, g in df.groupby("video_id"):
        per_author = g.groupby("author_channel_id").size()
        row = {
            "case_id": g["case_id"].iloc[0],
            "video_id": vid,
            "n_comments": len(g),
            "n_accounts": len(per_author),
            "gini": gini(per_author),
            "top1pct_share": top_share(per_author, 0.01),
            "top5pct_share": top_share(per_author, 0.05),
            "pct_dup_campaign": g["in_dup_campaign"].mean(),
            "pct_in_burst": g["in_burst"].mean(),
        }
        for cat in ["organic", "uncertain", "likely_coordinated", "commercial_spam"]:
            row[f"pct_{cat}"] = (g["category"] == cat).mean()
        if "label" in g:  # after hand-coding / classification: who produces the hostility?
            hostile = g[g["label"].isin(hostile_labels)]
            if len(hostile):
                h_auth = hostile.groupby("author_channel_id").size()
                row["pct_hostile"] = len(hostile) / len(g)
                row["hostile_top5pct_share"] = top_share(h_auth, 0.05)
                row["hostile_pct_non_organic"] = (hostile["category"] != "organic").mean()
                row["hostile_mean_likes"] = hostile["like_count"].mean()
                row["other_mean_likes"] = g.loc[~g.index.isin(hostile.index), "like_count"].mean()
        rows.append(row)
    return pd.DataFrame(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comments", required=True)
    ap.add_argument("--channels")
    ap.add_argument("--out", default="data/processed")
    ap.add_argument("--dup-threshold", type=float, default=0.9)
    args = ap.parse_args()

    comments = pd.read_csv(args.comments)
    channels = pd.read_csv(args.channels) if args.channels else None
    df, acc = audit(comments, channels, dup_threshold=args.dup_threshold)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "comments_flagged.csv", index=False)
    acc.to_csv(out / "accounts_flagged.csv", index=False)
    summary = summarise(df)
    summary.to_csv(out / "summary.csv", index=False)
    print(summary.round(3).to_string(index=False))
    print("\naccounts by category:\n", acc["category"].value_counts().to_string())


if __name__ == "__main__":
    main()
