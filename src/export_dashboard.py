"""Bundle pipeline outputs into dashboard/data.js for the friction-map dashboard.

    python -m src.export_dashboard            # real data if data/processed has it, else demo
    python -m src.export_dashboard --demo     # force demo data (clearly flagged in the UI)

Reads (all optional except cases.csv):
    data/cases.csv, data/events.csv
    data/processed/comments_flagged_labelled.csv  (src.spam output + `label` column)
    data/processed/threads_summary.csv            (src.threads)
    data/processed/attention_daily.csv            (src.news)
Writes dashboard/data.js as `window.DASHBOARD_DATA = {...}` so index.html works when opened
straight from disk (browsers block fetch() of local JSON files).
"""
import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd

from src.spam import gini, top_share

REACTIONS = ["support", "mock_offended", "neutral_discussion", "backlash", "threat",
             "demand_legal_action", "spam_irrelevant"]
HOSTILE = {"backlash", "threat", "demand_legal_action"}
CATEGORIES = ["organic", "uncertain", "likely_coordinated", "commercial_spam"]
PROCESSED = Path("data/processed")


def lorenz(counts, points=40):
    x = np.sort(np.asarray(counts, dtype=float))
    if len(x) == 0:
        return []
    cum = np.concatenate([[0], np.cumsum(x) / x.sum()])
    pos = np.linspace(0, len(x), points + 1).astype(int)
    return [[round(p / len(x), 4), round(float(cum[p]), 4)] for p in pos]


def _clean(v):
    if isinstance(v, (np.floating, float)) and np.isnan(v):
        return None
    if isinstance(v, (np.integer,)):
        return int(v)
    if isinstance(v, (np.floating,)):
        return round(float(v), 4)
    if isinstance(v, pd.Timestamp):
        return v.strftime("%Y-%m-%d")
    return v


def real_metrics(cases):
    path = PROCESSED / "comments_flagged_labelled.csv"
    if not path.exists():
        return None
    df = pd.read_csv(path)
    if "video_role" in df:
        df = df[df["video_role"] == "case"]
    df["hostile"] = df["label"].isin(HOSTILE)
    out = {}
    for case, g in df.groupby("case_id"):
        per_author = g.groupby("author_channel_id").size()
        hostile = g[g["hostile"]]
        out[case] = {
            "n_comments": len(g), "n_accounts": len(per_author),
            "reaction_mix": {r: (g["label"] == r).mean() for r in REACTIONS},
            "authenticity": {c: (g["category"] == c).mean() for c in CATEGORIES},
            "hostile_non_organic": (hostile["category"] != "organic").mean() if len(hostile) else None,
            "gini": gini(per_author), "top5_share": top_share(per_author, 0.05),
            "hostile_top5_share": top_share(hostile.groupby("author_channel_id").size(), 0.05) if len(hostile) else None,
            "lorenz": lorenz(per_author),
            "hostile_mean_likes": hostile["like_count"].mean() if len(hostile) else None,
            "other_mean_likes": g.loc[~g["hostile"], "like_count"].mean(),
        }
    att = PROCESSED / "attention_daily.csv"
    if att.exists():
        a = pd.read_csv(att)
        for case, g in a.groupby("case_id"):
            out.setdefault(case, {})["timeline"] = {
                "dates": g["date"].str[:10].tolist(),
                **{k: g[k].fillna(0).tolist() for k in ["comments", "hostile", "news_articles", "trends"] if k in g}}
    th = PROCESSED / "threads_summary.csv"
    if th.exists():
        for _, r in pd.read_csv(th).iterrows():
            out.setdefault(r["case_id"], {})["threads"] = {k: _clean(v) for k, v in r.items() if k != "case_id"}
    return out


def demo_metrics(cases):
    """Plausible-looking fake numbers so the dashboard can be built before data exists. NOT RESULTS."""
    out = {}
    for i, c in cases.iterrows():
        rng = np.random.default_rng(i)
        esc = {"none": 0, "legal": 1, "extralegal": 1, "both": 2}.get(c["outcome_type"], 0)
        mix = rng.dirichlet([6 - esc, 2, 3, 3 + 2 * esc, 0.5 + esc, 0.5 + esc, 0.6])
        coord = 0.02 + 0.05 * esc * rng.random()
        auth = [1 - coord - 0.04 - 0.01, 0.04, coord, 0.01]
        n_acc = int(rng.integers(2000, 20000))
        counts = rng.zipf(1.6 + 0.2 * (2 - esc), n_acc).clip(max=300)
        t0 = pd.Timestamp(str(c["incident_date"])[:7] + "-01") if str(c["incident_date"])[:4].isdigit() else pd.Timestamp("2025-01-01")
        dates = pd.date_range(t0 - pd.Timedelta(days=10), periods=60, freq="D")
        lag = int(rng.integers(-3, 4))
        base = np.exp(-0.5 * ((np.arange(60) - 14) / 3) ** 2)
        comments = (base * rng.integers(800, 6000) + rng.poisson(20, 60)).round()
        news = (np.roll(base, lag) * rng.integers(5, 80) + rng.poisson(1, 60)).round()
        out[c["case_id"]] = {
            "n_comments": int(counts.sum()), "n_accounts": n_acc,
            "reaction_mix": dict(zip(REACTIONS, mix)),
            "authenticity": dict(zip(CATEGORIES, auth)),
            "hostile_non_organic": min(0.9, coord * 2.5 + 0.02),
            "gini": gini(counts), "top5_share": top_share(counts, 0.05),
            "hostile_top5_share": min(0.95, top_share(counts, 0.05) * 1.3),
            "lorenz": lorenz(counts),
            "hostile_mean_likes": float(rng.gamma(2, 3)), "other_mean_likes": float(rng.gamma(2, 6)),
            "timeline": {"dates": [d.strftime("%Y-%m-%d") for d in dates],
                         "comments": comments.tolist(), "hostile": (comments * mix[3:6].sum()).round().tolist(),
                         "news_articles": news.tolist()},
            "threads": {"pct_hostile_threads_with_pushback": float(rng.uniform(0.2, 0.6)),
                        "calming_effect_r1": float(rng.uniform(-0.05, 0.3)),
                        "pushback_from_regulars": float(rng.uniform(0.3, 0.8)),
                        "median_minutes_to_pushback": float(rng.uniform(5, 120))},
        }
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--demo", action="store_true")
    ap.add_argument("--out", default="dashboard/data.js")
    args = ap.parse_args()

    cases = pd.read_csv("data/cases.csv")
    events = pd.read_csv("data/events.csv") if Path("data/events.csv").exists() else pd.DataFrame()
    metrics = None if args.demo else real_metrics(cases)
    demo = metrics is None
    if demo:
        metrics = demo_metrics(cases)

    keep = ["case_id", "comedian", "tier", "incident_date", "taboo_family", "taboo_detail", "trigger_platform",
            "state_legal_action", "nonstate_action", "outcome_type", "comedian_response", "status", "notes", "sources"]
    payload = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "demo": demo,
        "reactions": REACTIONS,
        "categories": CATEGORIES,
        "cases": [{k: _clean(v) if not isinstance(v, str) else v for k, v in r.items()}
                  for r in cases[keep].where(cases[keep].notna(), None).to_dict("records")],
        "events": events.where(events.notna(), None).to_dict("records") if len(events) else [],
        "metrics": json.loads(json.dumps(metrics, default=_clean)),
    }
    text = json.dumps(payload, ensure_ascii=False, default=_clean).replace("NaN", "null")
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out).write_text(f"window.DASHBOARD_DATA = {text};\n", encoding="utf-8")
    print(f"{'DEMO' if demo else 'REAL'} data for {len(metrics)} cases -> {args.out}")


if __name__ == "__main__":
    main()
