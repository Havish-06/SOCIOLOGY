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
| [analysis/clips.md](analysis/clips.md) | The YouTube links to watch and transcribe for every case, and how | Step 5.2 of every case |

## Where things are

| Path | What it is |
|---|---|
| `cases/<case_id>/case.md` | One analysis per case (24), written on the template `cases/_template.md` |
| `cases/<case_id>/sources.md` | The searches and the numbered source list for that case |
| `analysis/final_cases.csv` | The 24 final cases; `case_pool.csv` and `case_pool_summary.md` show how they were chosen from 45 |
| `analysis/assignments.md` | Who owns and who verifies each case |
| `analysis/comparison.csv` | One row per case: topic, genre, context, who mobilised, route, outcome, stigma, response |
| `analysis/mechanisms.csv` | The verdict for every interpretive lens, per case |
| `analysis/news_coding.csv` | Framing codes for the news articles of each case |
| `analysis/clips.md` | For every case, the YouTube links to watch and transcribe (original or reupload) |
| `analysis/first_read.csv` | Each owner's own reading of the case, written before opening the AI draft (to fill) |
| `analysis/findings.md` | Cross-case findings |
| `data/` | Earlier case, event and video tables (`videos.csv` lists the YouTube videos for comment collection) |
| `src/`, `tests/` | Comment collection, spam and coordination audit, coding sheets, news timing; tests |

## Status (2026-11-09)

- All 24 cases drafted by AI (`status: draft`); owners and verifiers still check each one (PLAN.md, Step 5).
- Comment collection and the spam audit are pending: the pipeline is being checked first.
- First findings are in `analysis/findings.md`; they are working findings until verification is done.
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
