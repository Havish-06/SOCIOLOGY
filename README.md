# Laughter Under Scrutiny: Joke Topics, Public Backlash and Escalation in India — Team K

Sociology project: which subjects of humour expose Indian stand-up comedians to public scrutiny, what
response follows (online only / legal / extra-legal / both), and how much of the online outrage
is real, widespread and organic. All styles of humour are included (dark, satire, crude, roast);
style is recorded as a variable. Comedians of every audience size are included (small <100K,
mid 100K–2M, large >2M subscribers); mid-range channels carry extra weight in the comment
analysis because their comment sections have less spam and fan-army noise.

- **Proposal (revised, current):** `Sociology_Proposal_Revised.docx`. The original is kept as `Sociology_Proposal_*.docx`.
- **Codebook:** [CODEBOOK.md](CODEBOOK.md): every joke and comment label, with decision rules and the prior work it builds on
- **Case table:** [data/cases.csv](data/cases.csv): 23 incidents with topic, genre, context, outcome, actors, sources, subscriber counts and verification status
- **Video table:** [data/videos.csv](data/videos.csv): candidate YouTube videos per case (original / reupload / news / response / commentary; case or control), checked to exist
- **Event timelines:** [data/events.csv](data/events.csv): dated FIRs, arrests, threats and cancellations per case
- **Dashboard:** open [dashboard/index.html](dashboard/index.html) in a browser (shows DEMO numbers until the pipeline has run)

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
copy .env.example .env            # then paste your YouTube Data API key into .env
```

## Pipeline

| Step | Command | Output |
|---|---|---|
| 1. Review `data/videos.csv`: watch each candidate, set `status` to `confirmed` or `rejected`, add control clips | — | — |
| 2. Collect comments + commenter account metadata | `python -m src.collect --videos data/videos.csv` | `data/raw/` |
| 3. Authenticity audit | `python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv` | `data/processed/` |
| 4. Hand-coding sheet (stratified, anonymised) | `python -m src.sample sheet --flagged data/processed/comments_flagged.csv --n 60` | `data/coding/sheet.csv` |
| 5. Inter-coder reliability | `python -m src.sample kappa --a data/coding/coder_A.csv --b data/coding/coder_B.csv` | kappa table |
| 6. Classifier → add a `label` column, save as `data/processed/comments_flagged_labelled.csv` | (to build: MuRIL / embeddings + logistic regression) | |
| 7. Reply threads: who pushes back, does it calm things | `python -m src.threads --flagged data/processed/comments_flagged_labelled.csv` | `threads*.csv` |
| 8. Comments vs news (GDELT) vs Google Trends | `python -m src.news --comments data/processed/comments_flagged_labelled.csv` | `attention_*.csv` |
| 9. Dashboard data | `python -m src.export_dashboard` | `dashboard/data.js` |

Tests: `python -m pytest -q` (synthetic data, including a planted 12-account campaign).

### Google Trends
pytrends is archived and the official Trends API is invite-only. Export by hand: trends.google.com →
search the comedian's name, region India, custom date range around the incident → ⋮ → Download CSV →
save as `data/trends/<case_id>.csv`. `src/news.py` picks it up automatically.

### GDELT
Free, no key, **max 1 request per 5 seconds** (the script waits). Covers online news from 2017;
regional-language outlets are under-covered, so treat it as an index of national attention.

### X / Twitter
No free tier for new developers (pay-per-use, about $0.005 per post read). Not part of the core design.

## Authenticity signals (`src/spam.py`)

| Signal | Level | Meaning |
|---|---|---|
| `commercial` | comment | links, "check my channel", WhatsApp/Telegram/crypto, phone numbers |
| `in_dup_campaign` | comment | near-identical text (char n-gram cosine ≥ 0.9) from ≥ 3 different accounts |
| `in_burst` | comment | posted in a 10-min bin ≥ 5× the video's trailing 6-hour median |
| `new_account` | account | channel created < 30 days before the comment |
| `auto_handle` | account | YouTube auto-handle (`@user-xxxx`) or name+4 digits |
| `cotiming` | account | repeatedly comments within the same minute as the same other accounts on ≥ 2 videos |

`likely_coordinated` = a coordination signal **plus** an account red flag. These are screening flags,
validated against the hand-coded `looks_inauthentic` column.

Data in `data/raw`, `data/processed`, `data/coding` is git-ignored. Do not commit commenter IDs or names.
