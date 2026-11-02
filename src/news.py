"""News attention vs comment activity: do comment spikes come before or after media coverage?

News volume: GDELT DOC 2.0 API (free, no key, max 1 request / 5 s, coverage from 2017).
Search interest: Google Trends CSV exported by hand from trends.google.com (pytrends is
archived and the official Trends API is invite-only alpha), saved as data/trends/<case_id>.csv.

    python -m src.news --cases data/cases.csv --comments data/processed/comments_flagged.csv --out data/processed

Outputs:
    attention_daily.csv   case_id, date, comments, hostile, news_articles, trends
    attention_summary.csv onset/peak dates per series, lead days, best cross-correlation lag
"""
import argparse
import re
import time
from pathlib import Path

import numpy as np
import pandas as pd
import requests

GDELT = "https://api.gdeltproject.org/api/v2/doc/doc"
HOSTILE = {"backlash", "threat", "demand_legal_action"}


def gdelt_daily(query, start, end, country="india", retries=5):
    """Daily count of news articles matching `query` from outlets in `country`."""
    params = {"query": f"{query} sourcecountry:{country}" if country else query,
              "mode": "timelinevolraw", "format": "json", "TIMELINESMOOTH": 0,
              "startdatetime": pd.Timestamp(start).strftime("%Y%m%d%H%M%S"),
              "enddatetime": pd.Timestamp(end).strftime("%Y%m%d%H%M%S")}
    for attempt in range(retries):
        r = requests.get(GDELT, params=params, timeout=60)
        if r.status_code == 200 and r.text.strip().startswith("{"):
            return parse_gdelt(r.json())
        time.sleep(6 * (attempt + 1))  # 429 = rate limit; back off
    raise RuntimeError(f"GDELT failed for {query!r}: {r.status_code} {r.text[:120]}")


def parse_gdelt(payload):
    timeline = payload.get("timeline") or []
    if not timeline:
        return pd.Series(dtype=float, name="news_articles")
    data = timeline[0]["data"]
    s = pd.Series([d["value"] for d in data],
                  index=pd.to_datetime([d["date"] for d in data], format="%Y%m%dT%H%M%SZ", utc=True))
    return s.resample("D").sum().rename("news_articles")


def load_trends_csv(path):
    """Google Trends 'Interest over time' export: a couple of header lines, then Day,<term>."""
    lines = Path(path).read_text(encoding="utf-8-sig").splitlines()
    start = next(i for i, l in enumerate(lines) if l.split(",")[0] in ("Day", "Week", "Time"))
    df = pd.read_csv(path, skiprows=start, encoding="utf-8-sig")
    s = pd.to_numeric(df.iloc[:, 1].astype(str).str.replace("<1", "0.5"), errors="coerce")
    s.index = pd.to_datetime(df.iloc[:, 0], utc=True)
    return s.rename("trends")


def incident_start(value):
    """First day of an incident date written as 'YYYY-MM', 'YYYY-MM-DD' or 'YYYY (note)'; None if no year."""
    m = re.match(r"(\d{4})(?:-(\d{2}))?", str(value))
    return pd.Timestamp(f"{m.group(1)}-{m.group(2) or '01'}-01") if m else None


def onset(series, frac=0.1):
    """First day the series reaches `frac` of its peak: when attention 'starts'."""
    s = series.fillna(0)
    if s.max() <= 0:
        return pd.NaT
    return s.index[np.argmax(s.to_numpy() >= frac * s.max())]


def lead_lag(a, b, max_lag=7):
    """Correlation of a[t] with b[t + k] for k in -max_lag..max_lag.

    Positive best lag => `a` leads `b` by k days (e.g. comments rise before news).
    Uses day-to-day changes so a shared slow trend doesn't create a spurious correlation.
    """
    a, b = a.align(b, fill_value=0)
    da, db = a.diff().fillna(0), b.diff().fillna(0)
    out = []
    for k in range(-max_lag, max_lag + 1):
        r = da.corr(db.shift(-k))
        out.append({"lag_days": k, "r": r})
    return pd.DataFrame(out)


def daily_comments(comments):
    c = comments.copy()
    c["date"] = pd.to_datetime(c["published_at"], utc=True).dt.floor("D")
    c["is_hostile"] = c["label"].isin(HOSTILE) if "label" in c else False
    g = c.groupby(["case_id", "date"]).agg(comments=("comment_id", "size"), hostile=("is_hostile", "sum"))
    return g.reset_index()


def case_attention(case, comments_daily, news, trends=None):
    d = comments_daily[comments_daily["case_id"] == case].set_index("date")
    idx = pd.date_range(min(d.index.min(), news.index.min()), max(d.index.max(), news.index.max()), freq="D")
    frame = pd.DataFrame(index=idx)
    frame["comments"] = d["comments"].reindex(idx, fill_value=0)
    frame["hostile"] = d["hostile"].reindex(idx, fill_value=0)
    frame["news_articles"] = news.reindex(idx, fill_value=0)
    frame["trends"] = trends.reindex(idx) if trends is not None else np.nan

    on_c, on_n = onset(frame["comments"]), onset(frame["news_articles"])
    ll = lead_lag(frame["comments"], frame["news_articles"])
    best = ll.loc[ll["r"].abs().idxmax()] if ll["r"].notna().any() else {"lag_days": np.nan, "r": np.nan}
    summary = {
        "case_id": case,
        "comments_onset": on_c, "news_onset": on_n,
        "comments_peak": frame["comments"].idxmax(), "news_peak": frame["news_articles"].idxmax(),
        # > 0: comments took off before the media did (bottom-up); < 0: media first (top-down)
        "comments_lead_days": (on_n - on_c).days if pd.notna(on_c) and pd.notna(on_n) else np.nan,
        "best_lag_days": best["lag_days"], "best_lag_r": best["r"],
    }
    if trends is not None:
        summary["trends_onset"] = onset(frame["trends"])
    return frame.rename_axis("date").reset_index().assign(case_id=case), summary


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cases", default="data/cases.csv")
    ap.add_argument("--comments", required=True)
    ap.add_argument("--trends-dir", default="data/trends")
    ap.add_argument("--days-before", type=int, default=30)
    ap.add_argument("--days-after", type=int, default=90)
    ap.add_argument("--out", default="data/processed")
    args = ap.parse_args()

    cases = pd.read_csv(args.cases)
    cd = daily_comments(pd.read_csv(args.comments))
    frames, summaries = [], []
    for _, c in cases.iterrows():
        if c["case_id"] not in set(cd["case_id"]) or pd.isna(c.get("news_query")):
            continue
        t0 = incident_start(c["incident_date"])
        if t0 is None:
            print(f"skip {c['case_id']}: no usable incident_date")
            continue
        news = gdelt_daily(c["news_query"], t0 - pd.Timedelta(days=args.days_before), t0 + pd.Timedelta(days=args.days_after))
        tpath = Path(args.trends_dir) / f"{c['case_id']}.csv"
        trends = load_trends_csv(tpath) if tpath.exists() else None
        f, s = case_attention(c["case_id"], cd, news, trends)
        frames.append(f)
        summaries.append(s)
        print(s)
        time.sleep(6)

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    if frames:
        pd.concat(frames).to_csv(out / "attention_daily.csv", index=False)
        pd.DataFrame(summaries).to_csv(out / "attention_summary.csv", index=False)


if __name__ == "__main__":
    main()
