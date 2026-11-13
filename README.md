# Laughter Under Scrutiny: Joke Topics, Public Backlash and Escalation in India — Team K

This README is the starting point: what the project is in brief, which file to read for what, and how to set up.

**Question.** Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a controversy,
why does it end so differently: online criticism only, legal action, extra-legal action, or both?

**Method.** A structured, focused comparison (George & Bennett, 2005) of 24 controversies from 2018–2026, each analysed
with the same template and then compared side by side. Topic is the main comparison; genre is recorded as a secondary
variable. Team: Havish, Yogansh, Pranav, Siddanth.

## Start here: what to read

| File | What it is | Read it when |
|---|---|---|
| [README.md](README.md) | This guide: where things are, status, setup, tools | First |
| [PROJECT.md](PROJECT.md) | **The whole project in one document:** question, concepts, framework, design, cases, data, analysis, outputs, roles, ethics, limitations, references | To understand what we are doing and why |
| [PLAN.md](PLAN.md) | **How to carry it out:** news protocol, every step in detail (Step 5 is the per-case work), comment protocol and spam audit, folder structure, timeline, glossary | Before working on a case |
| [DECISIONS.md](DECISIONS.md) | Dated log of every team decision, and the questions still open | To see what was decided and why |
| [CODEBOOK.md](CODEBOOK.md) | Definitions and decision rules for every joke and comment label | While coding a case or comments |
| [LITERATURE.md](LITERATURE.md) | Previous work and how each study shapes our method | For the framework and the write-up |
| [analysis/assignments.md](analysis/assignments.md) | Who owns and who verifies each case | Before starting your cases |
| [analysis/conditions.md](analysis/conditions.md) | **The main finding**: conditions judged from the joke before anyone reacts, tested against the 24 outcomes (19 of 24 predicted) | For the headline |
| [independent_analysis/](independent_analysis/README.md) | **The final analysis of all 24 cases** (made from the clips, checked by the owners): case files, comparison table, findings | To see a case or the findings |
| [analysis/key_fact_checks.md](analysis/key_fact_checks.md) | The key facts of each case, checked by a second person | When doing your checks |
| [analysis/clips.md](analysis/clips.md) | The YouTube links to watch for every case | When watching a clip |

## Where things are

| Path | What it is |
|---|---|
| `independent_analysis/cases/<case_id>.md` | **The final analysis of each case** (24). Sources in section J; the owner's check in section N |
| `independent_analysis/comparison.csv` | One row per case: topic, genre, direction, who mobilised, route, outcome, stigma, response |
| `independent_analysis/findings.md` | Cross-case findings: patterns, matched pairs, typology, counter-examples |
| `independent_analysis/vs_ai_draft.md` | What the first news-only drafts (9 Nov, now deleted) got wrong |
| `independent_analysis/method/` | How the analysis was made: brief with the case template, instructions, consistency rules, scripts |
| `analysis/conditions.md`, `conditions.csv` | The main finding and its table |
| `analysis/key_fact_checks.md` | Key facts per case, checked by a second person |
| `analysis/first_read.csv` | Each owner's own reading of their clips |
| `analysis/sacred_recode_collective_trauma.md` | Proposed recoding for the new sacred object (collective trauma) |
| `analysis/final_cases.csv` | The 24 final cases; `case_pool.csv` and `case_pool_summary.md` show how they were chosen from 45 |
| `analysis/assignments.md` | Who owns and who verifies each case |
| `analysis/clips.md` | For every case, the YouTube links to watch |
| `analysis/news_coding.csv` | Framing codes for the news articles of each case |
| `data/` | Earlier case and video tables (`videos.csv` lists the YouTube videos for comment collection) |
| `src/`, `tests/` | Comment collection, spam and coordination audit, coding sheets, news timing; tests (not yet run on our cases) |

## Status (2026-11-14)

- All 24 cases analysed from the clips (`independent_analysis/`) and checked by their owners after watching
  (section N of each case file). The first news-only drafts were deleted on 14 Nov (still in the git history).
- Key-fact checks by a second person: in progress (`analysis/key_fact_checks.md`).
- Main finding: `analysis/conditions.md`; detailed findings: `independent_analysis/findings.md`.
- Comment collection and the spam audit have not been run; reported as a limitation.
- First deliverable: a presentation on 14–15 November 2026.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
copy .env.example .env            # then paste your own YouTube Data API key and any random ANON_SALT into .env
```

**Never commit `.env`.** It is git-ignored; keep your key there only.

## Tools

| Tool | Command | Use |
|---|---|---|
| Download comments | `python -m src.collect --videos data/videos.csv` (or `--video-ids <id> --case-id <case>`) | PLAN.md, Step 5.3 |
| Spam and coordination audit (with chance check; add `--sensitivity`) | `python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv` | Every case, before reading comments |
| Check the spam flags against hand-coding | `python -m src.spam --validate data/coding/coded.csv --flagged data/processed/comments_flagged.csv` | After coding |
| Comment coding sheet and agreement (Cohen's kappa) | `python -m src.sample sheet ...` / `python -m src.sample kappa --a A.csv --b B.csv` | Comment coding (PLAN.md, Comment protocol) |
| News-coverage timing from GDELT (optional) | `python -m src.news --comments data/processed/comments_flagged.csv` | Did news start before or after the outrage? |
| Tests | `python -m pytest -q` | Check the tools still work |

**Platforms.** YouTube Data API v3 is free (10,000 units/day). Only YouTube comments are used.
X/Twitter (no free API), Instagram and Reddit are not used. GDELT is optional; Google Trends is not used.

**Ethics.** Only public material. No commenter usernames or IDs in any committed file; quotes are paraphrased. Raw comment
files (`data/raw/`, `data/comments/`) and clip transcripts (`data/transcripts/`) are git-ignored.
