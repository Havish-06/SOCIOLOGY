import numpy as np
import pandas as pd
import pytest

from src.sample import kappa, make_sheet
from src.spam import audit, gini, summarise, top_share

T0 = pd.Timestamp("2025-03-01", tz="UTC")


def synthetic():
    """200 organic commenters spread over 2 days on two videos, plus a 12-account
    copy-paste campaign that hits both videos within the same minute."""
    rng = np.random.default_rng(0)
    rows = []
    words = ["funny", "boring", "classic", "brilliant", "offensive", "meh", "lol", "great", "sad", "cringe"]
    for i in range(200):
        vid = "v1" if i % 2 else "v2"
        rows.append({"case_id": "c1" if vid == "v1" else "c2", "video_id": vid, "comment_id": f"o{i}",
                     "author_channel_id": f"UCorg{i}", "author_name": f"@person{i}",
                     "text": " ".join(rng.choice(words, 6)) + f" take number {i}",
                     "like_count": int(rng.integers(0, 50)),
                     "published_at": T0 + pd.Timedelta(minutes=int(rng.integers(0, 2880)))})
    for j in range(12):
        for vid, offset in [("v1", 600), ("v2", 1500)]:
            rows.append({"case_id": "c1" if vid == "v1" else "c2", "video_id": vid, "comment_id": f"b{j}{vid}",
                         "author_channel_id": f"UCbot{j}", "author_name": f"@user-x{j}k2abcdq",
                         "text": f"This comedian insulted our faith, arrest him now!! boycott{'!' * (j % 3)}",
                         "like_count": 0,
                         "published_at": T0 + pd.Timedelta(minutes=offset, seconds=j)})
    rows.append({"case_id": "c1", "video_id": "v1", "comment_id": "s1", "author_channel_id": "UCspam",
                 "author_name": "@cryptoking", "text": "Earn daily, check out my channel https://x.y",
                 "like_count": 0, "published_at": T0})
    comments = pd.DataFrame(rows)
    channels = pd.DataFrame({
        "author_channel_id": [f"UCorg{i}" for i in range(200)] + [f"UCbot{j}" for j in range(12)] + ["UCspam"],
        "channel_published_at": ["2015-01-01T00:00:00Z"] * 200 + ["2025-02-25T00:00:00Z"] * 12 + ["2020-01-01T00:00:00Z"],
        "channel_custom_url": [None] * 213,
        "video_count": [3] * 200 + [0] * 12 + [5],
    })
    return comments, channels


def test_gini_and_top_share():
    assert gini([1, 1, 1, 1]) == pytest.approx(0)
    assert gini([0, 0, 0, 10]) == pytest.approx(0.75)
    assert top_share([10, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0.1) == pytest.approx(10 / 19)


def test_audit_catches_planted_campaign():
    comments, channels = synthetic()
    df, acc = audit(comments, channels)
    cat = acc.set_index("author_channel_id")["category"]

    bots = [f"UCbot{j}" for j in range(12)]
    assert (cat[bots] == "likely_coordinated").all()
    assert cat["UCspam"] == "commercial_spam"
    organic = cat[[f"UCorg{i}" for i in range(200)]]
    assert (organic == "organic").mean() > 0.95

    flagged = acc.set_index("author_channel_id")
    assert flagged.loc[bots, "dup_campaign"].all()
    assert flagged.loc[bots, "cotiming"].all()
    assert flagged.loc[bots, "new_account"].all()


def test_summary_reports_hostility_concentration():
    comments, channels = synthetic()
    df, _ = audit(comments, channels)
    df["label"] = np.where(df["author_channel_id"].str.startswith("UCbot"), "backlash", "support")
    s = summarise(df).set_index("video_id")
    assert s.loc["v1", "hostile_pct_non_organic"] == pytest.approx(1.0)
    assert s.loc["v1", "pct_likely_coordinated"] > 0


def test_sheet_and_kappa():
    comments, channels = synthetic()
    df, _ = audit(comments, channels)
    sheet = make_sheet(df, n_per_cell=5)
    assert "UCbot" not in " ".join(sheet["author"])  # anonymised
    assert set(sheet["category"]) >= {"organic", "likely_coordinated"}

    a = sheet[["comment_id"]].assign(reaction="support", target="comedian", taboo="religion", looks_inauthentic="no")
    b = a.copy()
    b.loc[b.index[:3], "reaction"] = "backlash"
    k = kappa(a, b).set_index("code")
    assert k.loc["reaction", "agreement"] < 1
