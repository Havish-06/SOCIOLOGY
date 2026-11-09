"""Authenticity audit: flag commercial spam, copy-paste and slogan campaigns, copied comments,
timing bursts, co-timed account networks, batch-created and throwaway accounts, then measure
how concentrated the commenting is (who is actually doing the talking).

Usage:
    python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv --out data/processed
    python -m src.spam --comments ... --channels ... --sensitivity        # do results survive other thresholds?
    python -m src.spam --validate data/coding/coded.csv --flagged data/processed/comments_flagged.csv

Outputs (in --out):
    comments_flagged.csv   one row per comment with every signal
    accounts_flagged.csv   one row per commenting account with its category
    summary.csv            one row per video: volume, concentration, % by category
    coordination_null.csv  co-timing accounts found in real vs shuffled data (expected false positives)
    sensitivity.csv        % likely_coordinated per video under a grid of thresholds (with --sensitivity)

Design follows the coordination-detection literature (methods and sources in LITERATURE.md,
"Detecting spam and coordinated commenting"): group-level behavioural traces rather than single
accounts (Cresci 2020; Pacheco et al. 2021), repeated co-action within a time window tested
against chance (Giglietto et al. 2020; Pacheco et al. 2021), pre-written text and slogans pushed
to many accounts (Jakesch et al. 2021), and validation against human judgement.

None of these signals proves a comment is fake. Each is a reason to look closer;
the category combines them conservatively and must be validated by hand-coding
(see src/sample.py and --validate).
"""
import argparse
import re
from collections import defaultdict
from itertools import combinations, product
from pathlib import Path

import networkx as nx
import numpy as np
import pandas as pd
from scipy.sparse import coo_matrix
from scipy.sparse.csgraph import connected_components
from sklearn.feature_extraction.text import TfidfVectorizer

COMMERCIAL = re.compile(
    r"https?://|www\.|\b(?:sub(?:scribe)? to my|check (?:out )?my (?:channel|video)|visit my channel"
    r"|whats ?app|telegram|crypto|bitcoin|forex|binary option|investment plan|earn \$?\d+|dm me"
    r"|sub ?4 ?sub|link in (?:my )?bio|paid promotion|free recharge|ghar baithe|paise kamao|paisa kamao"
    r"|online earning|join my)\b"
    r"|\+?\d[\d\s-]{9,}\d",
    re.I,
)
AUTO_HANDLE = re.compile(r"^@user-[a-z0-9]{6,}$", re.I)       # YouTube's auto-generated handles
NAME_DIGITS = re.compile(r"^@?[a-z]+[._-]?\d{4,}$", re.I)       # e.g. @rahul84629
HASHTAG = re.compile(r"#\w{3,}", re.U)                          # \w covers Devanagari and Telugu


def normalise(text):
    text = re.sub(r"https?://\S+", " URL ", str(text).lower())
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)                  # "sooooo" -> "soo", so stretched copies still match
    return re.sub(r"\s+", " ", text).strip()


# ---------- comment-level signals ----------

def near_duplicate_clusters(texts, authors, threshold=0.9, min_len=20, min_authors=3, chunk=2000):
    """Cluster comments whose character-n-gram TF-IDF cosine >= threshold.

    Returns (cluster_id, n_authors_in_cluster, group) arrays:
    - cluster_id is -1 unless the cluster was written by at least `min_authors` distinct accounts
      (a copy-paste campaign);
    - group is the raw cluster label for every comment long enough to compare (-1 otherwise),
      used to find comments copied by a single other account.
    Short comments ("lol", "🔥🔥") are excluded because they repeat naturally.
    """
    norm = pd.Series(texts).map(normalise)
    idx = np.flatnonzero(norm.str.len().to_numpy() >= min_len)
    cluster = np.full(len(norm), -1)
    group = np.full(len(norm), -1)
    n_auth = np.zeros(len(norm), dtype=int)
    if len(idx) < 2:
        return cluster, n_auth, group

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
    group[idx] = labels
    n_auth[idx] = sizes
    return cluster, n_auth, group


def copied_flags(df, group_col="dup_group"):
    """Comments that repeat an *earlier* comment by a different account (copy bots re-post
    popular comments to farm likes). The first comment of each near-duplicate group is the
    original and is never flagged."""
    d = df[df[group_col] >= 0]
    first = d.sort_values("published_at").groupby(group_col)["author_channel_id"].transform("first")
    copied = d["author_channel_id"] != first.reindex(d.index)
    return copied.reindex(df.index, fill_value=False)


def hashtag_campaign_flags(df, min_authors=5, window="60min"):
    """Comments carrying a hashtag that at least `min_authors` distinct accounts used on the same
    video within one `window` (slogan pushes such as pre-written 'toolkit' hashtags)."""
    flags = pd.Series(False, index=df.index)
    tags = df["text"].fillna("").str.lower().str.findall(HASHTAG)
    exploded = tags.explode().dropna()
    if exploded.empty:
        return flags
    t = df.loc[exploded.index, ["video_id", "published_at", "author_channel_id"]].assign(tag=exploded.values)
    span = pd.Timedelta(window)
    for _, g in t.groupby(["video_id", "tag"]):
        if g["author_channel_id"].nunique() < min_authors:
            continue
        g = g.sort_values("published_at")
        times, authors = g["published_at"].to_numpy(), g["author_channel_id"].to_numpy()
        lo = 0
        for hi in range(len(g)):
            while times[hi] - times[lo] > span:
                lo += 1
            if len(set(authors[lo:hi + 1])) >= min_authors:
                flags.loc[g.index[lo:hi + 1]] = True
    return flags


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
    # floor() is unit-safe; astype("int64") is not (pandas 3 may store microseconds, not nanoseconds)
    d["bin"] = d["published_at"].dt.floor(f"{window_s}s")
    pair_videos = defaultdict(set)
    for (vid, _), g in d.groupby(["video_id", "bin"]):
        authors = sorted(set(g["author_channel_id"]))
        if 2 <= len(authors) <= max_bin_authors:
            for a, b in combinations(authors, 2):
                pair_videos[(a, b)].add(vid)
    G = nx.Graph()
    G.add_edges_from(p for p, vids in pair_videos.items() if len(vids) >= min_videos)
    return {a: i for i, comp in enumerate(nx.connected_components(G)) for a in comp}


def cotiming_null(df, n_shuffles=20, seed=0, **kwargs):
    """How many co-timing accounts would appear by chance?

    Shuffles which account wrote which comment within each video (keeping every video's timing
    and every account's activity level), reruns cotiming_clusters, and compares with the real data.
    expected_false_share = mean shuffled count / observed count: the share of flagged accounts
    we would expect even with no coordination at all. Tune window_s/min_videos until it is small.
    """
    rng = np.random.default_rng(seed)
    observed = len(cotiming_clusters(df, **kwargs))
    shuffled = []
    groups = list(df.groupby("video_id").indices.values())  # row positions per video
    for _ in range(n_shuffles):
        authors = df["author_channel_id"].to_numpy().copy()
        for pos in groups:
            authors[pos] = rng.permutation(authors[pos])
        shuffled.append(len(cotiming_clusters(df.assign(author_channel_id=authors), **kwargs)))
    mean = float(np.mean(shuffled)) if shuffled else np.nan
    return {"observed_accounts": observed, "shuffled_mean": mean,
            "shuffled_max": int(np.max(shuffled)) if shuffled else np.nan,
            "expected_false_share": mean / observed if observed else np.nan}


def batch_created_accounts(df, min_accounts=5, recent_days=180):
    """Accounts created on the same calendar day as at least `min_accounts - 1` other accounts
    commenting on the same case, when that day is within `recent_days` before their comment.
    Batches of fresh accounts are a classic sign of purchased or farmed accounts."""
    if "channel_published_at" not in df or df["channel_published_at"].isna().all():
        return set()
    d = df.dropna(subset=["channel_published_at"])
    d = d[(d["published_at"] - d["channel_published_at"]).dt.days.between(0, recent_days)]
    d = d.assign(created=d["channel_published_at"].dt.floor("D"))
    per_day = d.groupby(["case_id", "created"])["author_channel_id"].nunique()
    batches = per_day[per_day >= min_accounts].index
    hit = d.set_index(["case_id", "created"]).index.isin(batches)
    return set(d.loc[hit, "author_channel_id"])


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

def audit(comments, channels=None, dup_threshold=0.9, new_account_days=30, cotiming_window_s=60):
    df = comments.copy()
    df["published_at"] = pd.to_datetime(df["published_at"], utc=True)
    df["author_channel_id"] = df["author_channel_id"].fillna("unknown:" + df["author_name"].fillna(""))

    df["commercial"] = df["text"].fillna("").str.contains(COMMERCIAL)
    df["dup_cluster"], df["dup_cluster_authors"], df["dup_group"] = near_duplicate_clusters(
        df["text"].fillna(""), df["author_channel_id"], threshold=dup_threshold)
    df["in_dup_campaign"] = df["dup_cluster"] >= 0
    df["copied"] = copied_flags(df) & ~df["in_dup_campaign"]  # campaigns are scored as coordination instead
    df["in_hashtag_campaign"] = hashtag_campaign_flags(df)
    df["in_burst"] = burst_flags(df)

    handle = df["author_name"].fillna("")
    if channels is not None and len(channels):
        ch = channels.copy()
        ch["channel_published_at"] = pd.to_datetime(ch["channel_published_at"], utc=True, format="ISO8601")
        df = df.merge(ch, on="author_channel_id", how="left")
        df["account_age_days"] = (df["published_at"] - df["channel_published_at"]).dt.days
        handle = df["channel_custom_url"].astype(object).fillna(df["author_name"]).fillna("")
    else:
        df["account_age_days"] = np.nan
        df["video_count"] = np.nan
    df["new_account"] = df["account_age_days"] < new_account_days
    df["auto_handle"] = handle.str.match(AUTO_HANDLE) | handle.str.match(NAME_DIGITS)
    df["batch_created"] = df["author_channel_id"].isin(batch_created_accounts(df))

    coord = cotiming_clusters(df, window_s=cotiming_window_s)
    df["cotiming_cluster"] = df["author_channel_id"].map(coord).fillna(-1).astype(int)

    acc = df.groupby("author_channel_id").agg(
        n_comments=("comment_id", "size"),
        n_videos=("video_id", "nunique"),
        n_cases=("case_id", "nunique"),
        commercial=("commercial", "any"),
        dup_campaign=("in_dup_campaign", "any"),
        copied=("copied", "any"),
        hashtag_campaign=("in_hashtag_campaign", "any"),
        burst_share=("in_burst", "mean"),
        new_account=("new_account", "any"),
        auto_handle=("auto_handle", "any"),
        batch_created=("batch_created", "any"),
        no_uploads=("video_count", lambda s: bool((s == 0).any())),
        account_age_days=("account_age_days", "min"),
        cotiming_cluster=("cotiming_cluster", "max"),
        total_likes=("like_count", "sum"),
    )
    acc["cotiming"] = acc["cotiming_cluster"] >= 0
    acc["mostly_burst"] = acc["burst_share"] > 0.5

    # Coordination = acting together with other accounts; red flag = something odd about the account itself.
    # A category needs both kinds of evidence (or two independent coordination signals), so that a single
    # signal, which organic virality can also produce, never labels an account on its own.
    coordination = acc["dup_campaign"] | acc["cotiming"] | acc["hashtag_campaign"]
    account_red_flag = acc["new_account"] | acc["auto_handle"] | acc["mostly_burst"] | acc["batch_created"]
    n_coord = acc[["dup_campaign", "cotiming", "hashtag_campaign"]].sum(axis=1)
    signals = ["dup_campaign", "cotiming", "hashtag_campaign", "copied",
               "new_account", "auto_handle", "batch_created", "mostly_burst"]
    acc["suspicion_score"] = acc[signals].sum(axis=1)
    acc["category"] = np.select(
        [acc["commercial"] | (acc["copied"] & account_red_flag),
         (coordination & account_red_flag) | (n_coord >= 2),
         coordination | acc["copied"] | (acc["new_account"] & acc["mostly_burst"])],
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
            "pct_copied": g["copied"].mean() if "copied" in g else np.nan,
            "pct_hashtag_campaign": g["in_hashtag_campaign"].mean() if "in_hashtag_campaign" in g else np.nan,
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


def sensitivity(comments, channels=None, dup_thresholds=(0.85, 0.9, 0.95), windows_s=(30, 60, 120)):
    """% of comments by likely-coordinated accounts per video under every threshold combination.
    A finding that holds only at one setting should not be reported as a finding."""
    rows = []
    for th, w in product(dup_thresholds, windows_s):
        df, _ = audit(comments, channels, dup_threshold=th, cotiming_window_s=w)
        for vid, g in df.groupby("video_id"):
            rows.append({"video_id": vid, "case_id": g["case_id"].iloc[0], "dup_threshold": th,
                         "cotiming_window_s": w,
                         "pct_likely_coordinated": (g["category"] == "likely_coordinated").mean(),
                         "pct_non_organic": (g["category"] != "organic").mean()})
    return pd.DataFrame(rows)


def validate(flagged, coded, truth_col="looks_inauthentic"):
    """Compare automatic categories with human judgement from the coding sheet.

    The sheet is stratified by category, so the useful numbers are per category:
    share_human_inauthentic = how often coders agreed the flagged comments look inauthentic
    (precision for flagged categories; the miss rate for 'organic').
    """
    c = coded[["comment_id", truth_col]].dropna()
    c = c[c[truth_col].astype(str).str.strip() != ""]
    m = c.merge(flagged[["comment_id", "category"]], on="comment_id", how="inner")
    m["human_inauthentic"] = m[truth_col].astype(str).str.lower().eq("yes")
    m["human_unsure"] = m[truth_col].astype(str).str.lower().eq("unsure")
    out = m.groupby("category").agg(n_coded=("comment_id", "size"),
                                    share_human_inauthentic=("human_inauthentic", "mean"),
                                    share_unsure=("human_unsure", "mean")).reset_index()
    flagged_pred = m["category"].isin(["likely_coordinated", "commercial_spam"])
    tp = (flagged_pred & m["human_inauthentic"]).sum()
    out.attrs["precision_flagged"] = tp / flagged_pred.sum() if flagged_pred.sum() else np.nan
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--comments")
    ap.add_argument("--channels")
    ap.add_argument("--out", default="data/processed")
    ap.add_argument("--dup-threshold", type=float, default=0.9)
    ap.add_argument("--cotiming-window", type=int, default=60, help="seconds")
    ap.add_argument("--shuffles", type=int, default=20, help="shuffles for the co-timing null model (0 = skip)")
    ap.add_argument("--sensitivity", action="store_true", help="also rerun under a grid of thresholds")
    ap.add_argument("--validate", metavar="CODED_CSV", help="compare --flagged categories with a hand-coded sheet")
    ap.add_argument("--flagged", help="comments_flagged.csv, for --validate")
    args = ap.parse_args()

    if args.validate:
        if not args.flagged:
            ap.error("--validate needs --flagged")
        v = validate(pd.read_csv(args.flagged), pd.read_csv(args.validate))
        print(v.round(3).to_string(index=False))
        print(f"\nprecision of flagged categories (coder says inauthentic): {v.attrs['precision_flagged']:.2f}")
        return
    if not args.comments:
        ap.error("--comments is required")

    comments = pd.read_csv(args.comments)
    channels = pd.read_csv(args.channels) if args.channels else None
    df, acc = audit(comments, channels, dup_threshold=args.dup_threshold, cotiming_window_s=args.cotiming_window)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    df.to_csv(out / "comments_flagged.csv", index=False)
    acc.to_csv(out / "accounts_flagged.csv", index=False)
    summary = summarise(df)
    summary.to_csv(out / "summary.csv", index=False)
    print(summary.round(3).to_string(index=False))
    print("\naccounts by category:\n", acc["category"].value_counts().to_string())

    if args.shuffles:
        null = cotiming_null(df, n_shuffles=args.shuffles, window_s=args.cotiming_window)
        pd.DataFrame([null]).to_csv(out / "coordination_null.csv", index=False)
        print(f"\nco-timing accounts: {null['observed_accounts']} observed vs {null['shuffled_mean']:.1f} "
              f"expected by chance (expected false share {null['expected_false_share']:.2f})")
    if args.sensitivity:
        sens = sensitivity(comments, channels)
        sens.to_csv(out / "sensitivity.csv", index=False)
        print("\nsensitivity (pct_likely_coordinated, min-max across settings):")
        print(sens.groupby("video_id")["pct_likely_coordinated"].agg(["min", "max"]).round(3).to_string())


if __name__ == "__main__":
    main()
