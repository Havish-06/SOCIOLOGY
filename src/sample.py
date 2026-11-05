"""Build hand-coding sheets and check inter-coder reliability.

    python -m src.sample sheet --flagged data/processed/comments_flagged.csv --n 60 --out data/coding/sheet.csv
    python -m src.sample kappa --a data/coding/coder_A.csv --b data/coding/coder_B.csv

The sheet is stratified by video and by authenticity category so that rare groups
(likely_coordinated, commercial_spam) are not swamped by organic comments, which lets
us check whether the automatic flags agree with human judgement.
Author IDs are replaced by salted hashes so sheets can be shared safely.
"""
import argparse
import hashlib
import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sklearn.metrics import cohen_kappa_score

# Codebook v0 (definitions and sources in CODEBOOK.md): refine after the first pilot round of coding.
CODE_COLUMNS = {
    "reaction": "support | mock_offended | neutral_discussion | backlash | threat | demand_legal_action | spam_irrelevant",
    "target": "comedian | joke_content | offended_group | platform | state | other",
    "taboo": "religion | caste | gender_sexuality | family | politics_state | regional_national_icon | celebrity_public_figure | bodies_looks | death_violence_tragedy | disease_disability | none",
    "sacred_object": "deity | icon | nation | none",
    "frame": "play (\"it's just a joke\") | serious (insult / crime) | none",
    "stigmatises_comedian": "yes (attacks comedian's religion/caste/region/gender) | no",
    "intensity": "1 (mild) .. 5 (violent)",
    "pushback_type": "replies only: facts | hypocrisy | consequences | affiliation | denouncing | humour_sarcasm | positive_tone | hostile",
    "looks_inauthentic": "yes | no | unsure",
}


def anonymise(series, salt=None):
    salt = salt or os.environ.get("ANON_SALT", "change-me")
    return series.astype(str).map(lambda s: hashlib.sha256((salt + s).encode()).hexdigest()[:12])


def make_sheet(flagged, n_per_cell, seed=42):
    df = flagged.copy()
    df["author"] = anonymise(df["author_channel_id"])
    sample = df.sample(frac=1, random_state=seed).groupby(["video_id", "category"]).head(n_per_cell)
    sheet = sample[["comment_id", "case_id", "video_id", "author", "published_at", "like_count",
                    "category", "text"]].sample(frac=1, random_state=seed)  # shuffle so coders don't see strata in order
    for col in CODE_COLUMNS:
        sheet[col] = ""
    sheet["coder"] = ""
    return sheet


def kappa(a, b, columns=("reaction", "target", "taboo", "sacred_object", "frame", "stigmatises_comedian",
                         "looks_inauthentic")):
    m = a.merge(b, on="comment_id", suffixes=("_a", "_b"))
    rows = []
    for col in columns:
        if f"{col}_a" not in m or f"{col}_b" not in m:
            continue
        both = m[[f"{col}_a", f"{col}_b"]].dropna()
        both = both[(both[f"{col}_a"] != "") & (both[f"{col}_b"] != "")]
        if len(both):
            rows.append({"code": col, "n": len(both),
                         "agreement": (both[f"{col}_a"] == both[f"{col}_b"]).mean(),
                         "cohen_kappa": cohen_kappa_score(both[f"{col}_a"], both[f"{col}_b"])})
    return pd.DataFrame(rows)


def main():
    load_dotenv()
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sheet")
    s.add_argument("--flagged", required=True)
    s.add_argument("--n", type=int, default=60, help="comments per video x category cell")
    s.add_argument("--out", default="data/coding/sheet.csv")
    k = sub.add_parser("kappa")
    k.add_argument("--a", required=True)
    k.add_argument("--b", required=True)
    args = ap.parse_args()

    if args.cmd == "sheet":
        sheet = make_sheet(pd.read_csv(args.flagged), args.n)
        Path(args.out).parent.mkdir(parents=True, exist_ok=True)
        sheet.to_csv(args.out, index=False, encoding="utf-8-sig")  # utf-8-sig so Excel shows Hindi correctly
        print(f"{len(sheet)} comments -> {args.out}")
        print("codes:", *[f"  {c}: {v}" for c, v in CODE_COLUMNS.items()], sep="\n")
    else:
        print(kappa(pd.read_csv(args.a), pd.read_csv(args.b)).round(3).to_string(index=False))
        print("\nTarget: kappa >= 0.70 before scaling up with a classifier.")


if __name__ == "__main__":
    main()
