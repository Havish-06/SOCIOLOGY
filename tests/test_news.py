import numpy as np
import pandas as pd
import pytest

from src.news import lead_lag, load_trends_csv, onset, parse_gdelt

T0 = pd.Timestamp("2025-03-01", tz="UTC")


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
