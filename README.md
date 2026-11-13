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
| [independent_analysis/assignments.md](independent_analysis/assignments.md) | Who owns and who verifies each case | Before starting your cases |
| [independent_analysis/](independent_analysis/README.md) | **Final AI analysis of all 24 cases** made from the clip transcripts and checked against the first drafts: case files, comparison table, findings, and what humans must still check | To see the current analysis and findings |
| [independent_analysis/clips.md](independent_analysis/clips.md) | The YouTube links to watch and transcribe for every case, and how | Step 5.2 of every case |

## Where things are

| Path | What it is |
|---|---|
**Current work is all in `independent_analysis/`.**

| Path | What it is |
|---|---|
| `independent_analysis/cases/<case_id>.md` | **The final analysis of each case** (24), made from the clip transcripts and checked against the first drafts |
| `independent_analysis/comparison.csv` | **Master table**: the final coding of all 24 cases |
| `independent_analysis/findings.md` | **Cross-case findings** |
| `independent_analysis/conditions.md`, `conditions.csv` | The non-circular test: conditions judged before any reaction, against outcomes |
| `independent_analysis/key_fact_checks.md` | The key facts per case, checked against sources (AI) and by people |
| `independent_analysis/first_read.csv` | Each owner's own reading of the case, written before opening the AI draft |
| `independent_analysis/human_checks.md` | What each owner still has to check in their cases |
| `independent_analysis/assignments.md`, `clips.md` | Who owns which case; links to watch every clip |
| `independent_analysis/final_cases.csv`, `case_pool.csv`, `case_pool_summary.md` | The 24 final cases and how they were chosen from 45 |
| `independent_analysis/news_coding.csv` | Framing codes for news articles (coded from the first drafts' sources) |
| `independent_analysis/method/` | How the final analysis was made (instructions, transcript and table scripts) |

**Old, kept for reference (do not present from these):**

| Path | What it is |
|---|---|
| `cases/` | The first AI drafts (9 Nov), written from news only, before anyone watched the clips. Superseded by `independent_analysis/cases/` |
| `analysis/` | The first drafts' tables and findings (`comparison.csv`, `mechanisms.csv`, `findings.md`). `comparison.csv` is still read by `independent_analysis/method/build_tables.py` to compare drafts with the final analysis |
| `data/` | Earlier case, event and video tables (`videos.csv` lists the YouTube videos for comment collection) |
| `src/`, `tests/` | Comment collection, spam and coordination audit, coding sheets, news timing; tests |

## Status (2026-11-09)

- All 24 cases drafted by AI from news (`cases/`, `status: draft`), then **re-analysed from the clip transcripts and
  checked against those drafts** (`independent_analysis/`, final AI analysis). Owners now verify each case
  (`independent_analysis/human_checks.md`).
- Comment collection and the spam audit are pending: the pipeline is being checked first.
- Findings: `independent_analysis/findings.md` (supersedes the first draft in `analysis/findings.md`); working findings until verification is done.
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
