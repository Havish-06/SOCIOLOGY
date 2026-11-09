import numpy as np
import pandas as pd
import pytest

from src.news import lead_lag, load_trends_csv, onset, parse_gdelt
from src.threads import summarise_threads, thread_table

T0 = pd.Timestamp("2025-03-01", tz="UTC")


def _c(cid, parent, label, minute, author, case="c1", category="organic", role="case"):
    return {"comment_id": cid, "parent_id": parent, "label": label, "case_id": case, "video_id": "v1",
            "author_channel_id": author, "category": category, "video_role": role, "like_count": 0,
            "published_at": T0 + pd.Timedelta(minutes=minute)}


def thread_corpus():
    rows = []
    # 10 hostile threads where reply 1 is pushback by a regular viewer and hostility then fades
    for i in range(10):
        r = f"p{i}"
        rows.append(_c(r, None, "backlash", 0, f"h{i}"))
        rows.append(_c(f"{r}a", r, "support", 5, "fan1"))
        rows += [_c(f"{r}{k}", r, "neutral_discussion", 10 + k, f"n{k}") for k in range(3)]
        rows.append(_c(f"{r}z", r, "backlash", 20, f"h{i}x"))
    # 10 hostile threads with no pushback: replies pile on
    for i in range(10):
        r = f"q{i}"
        rows.append(_c(r, None, "threat", 0, f"t{i}"))
        rows += [_c(f"{r}{k}", r, "backlash", 5 + k, f"m{k}") for k in range(4)]
    rows.append(_c("ctrl1", None, "support", 0, "fan1", role="control"))  # fan1 is a regular
    return pd.DataFrame(rows)


def test_thread_pushback_and_calming():
    t = thread_table(thread_corpus())
    assert len(t) == 20
    s = summarise_threads(t).set_index("case_id").loc["c1"]
    assert s["pct_hostile_threads_with_pushback"] == pytest.approx(0.5)
    assert s["hostile_after_r1_if_pushback"] == pytest.approx(0.25)
    assert s["hostile_after_r1_if_no_pushback"] == pytest.approx(1.0)
    assert s["calming_effect_r1"] == pytest.approx(0.75)
    assert s["pushback_from_regulars"] == pytest.approx(1.0)


def test_parse_gdelt_daily():
    payload = {"timeline": [{"series": "Article Count", "data": [
        {"date": "20250323T000000Z", "value": 3, "norm": 1000},
        {"date": "20250323T120000Z", "value": 2, "norm": 1000},
        {"date": "20250324T000000Z", "value": 40, "norm": 1000}]}]}
    s = parse_gdelt(payload)
    assert list(s.values) == [5, 40]


def test_lead_lag_detects_comments_leading_news():
    idx = pd.date_range("2025-03-01", periods=40, freq="D", tz="UTC")
    rng = np.random.default_rng(1)
    comments = pd.Series(rng.poisson(5, 40).astype(float), index=idx)
    comments.iloc[10:14] += [200, 400, 150, 50]
    news = comments.shift(3).fillna(0) / 10  # news echoes comments 3 days later
    ll = lead_lag(comments, news)
    assert ll.loc[ll["r"].idxmax(), "lag_days"] == 3
    assert (onset(news) - onset(comments)).days == 3


def test_load_trends_csv(tmp_path):
    p = tmp_path / "t.csv"
    p.write_text("Category: All categories\n\nDay,Kunal Kamra: (India)\n2025-03-22,2\n2025-03-23,<1\n2025-03-24,100\n",
                 encoding="utf-8")
    s = load_trends_csv(p)
    assert list(s.values) == [2, 0.5, 100]
