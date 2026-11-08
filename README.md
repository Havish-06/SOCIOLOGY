# Laughter Under Scrutiny: Joke Topics, Public Backlash and Escalation in India — Team K

**Question.** Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a
controversy, why does it end so differently: online criticism only, legal action, extra-legal action, or both?

**Method.** A structured, focused comparison (George & Bennett, 2005) of about 25 controversies from 2018–2026.
Every case is analysed with the same template, using news, legal records, YouTube and Instagram comments and the
comedian's own statements, and then all cases are compared side by side. **Topic** is the main comparison; genre
(dark comedy, satire, crude, roast) is recorded for every joke as a secondary variable. Comedians of every audience
size are included. Cases are interpreted with a toolkit of sociological lenses, used wherever the evidence supports them: stigma,
context collapse, Durkheim, scandal, moral panic, strategic offence, mobilisation, law as a weapon, organised online
publics, platform outrage, humour theory, identity and power, fandom and apology (PLAN.md Section 4).

**Where it started.** *India's Got Latent* (2025) and Pranit More's "Rs 370 biryani" crowd work (2026) are the two
controversies that led us to this topic; *Latent* is the suggested pilot case.

## Start here

| File | What it is |
|---|---|
| [PROJECT.md](PROJECT.md) | **The whole project in one document:** question, framework, previous work, method, cases, outputs, ethics, limitations, timeline |
| [PLAN.md](PLAN.md) | **The project plan (adopted).** Question, framework, method, every step, roles, verification rules, limitations, timeline |
| [DECISIONS.md](DECISIONS.md) | Dated log of team decisions, plus the questions still open for the team meeting |
| [LITERATURE.md](LITERATURE.md) | Previous work in humour studies and comedy controversies, and **how each study shapes our method** |
| [analysis/case_pool_summary.md](analysis/case_pool_summary.md) | The suggested 25 cases, reserves and exclusions, balance by topic × outcome, matched pairs |
| [analysis/case_pool.csv](analysis/case_pool.csv) | All 45 candidate cases with sources, first-pass coding and recommendation |
| [cases/_template.md](cases/_template.md) | The case template every case file follows |
| [CODEBOOK.md](CODEBOOK.md) | Definitions and decision rules for every joke and comment label, with their sources |

Supporting data:

| File | What it is |
|---|---|
| [data/cases.csv](data/cases.csv) | First 23 researched cases (fact-checked in `analysis/case_pool.csv`, which supersedes it where they differ) |
| [data/events.csv](data/events.csv) | Dated FIRs, arrests, threats, apologies per case |
| [data/videos.csv](data/videos.csv) | Candidate YouTube videos per case; 73 confirmed, 5 rejected |

Superseded, kept for reference: `Sociology_Proposal_Revised.docx` (its conceptual framework is reused; its
method and deliverables are replaced by PLAN.md) and the original proposal `Sociology_Proposal_*.docx`.

## What happens next

1. **Everyone reads** PLAN.md, LITERATURE.md and the case pool summary, and checks them.
2. **Team meeting (PLAN.md Step 0):** settle the open questions in DECISIONS.md (deadline, number of cases,
   final case list, languages, case owners, interviews, edge-case rules).
3. **Setup (Step 1):** each person who collects comments makes their own YouTube API key (below).
4. **Pilot case (Step 4):** `latent_2025`, then freeze the template.
5. **All cases (Step 5)**, cross-case comparison (Step 6), write-up (Step 8).

## Final output

- The final paper (structure in PLAN.md Step 8)
- About 25 verified case files in `cases/<case_id>/`
- `analysis/comparison.csv` (master comparison table) and `analysis/findings.md` (patterns, matched pairs,
  typology of escalation paths, counter-examples, agreement report)
- Presentation slides; optional interview summaries; optional dashboard rebuilt from the comparison table

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
copy .env.example .env            # then paste your own YouTube Data API key and any random ANON_SALT into .env
```

**Never commit `.env`.** It is git-ignored; keep your key there only.

## Tools we use

| Tool | Command | Use in the plan |
|---|---|---|
| Download comments | `python -m src.collect --videos data/videos.csv` (or `--video-ids <id> --case-id <case>`) | Step 5.3 |
| Quick copy-paste / spam check | `python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv` | Optional, before quoting comments |
| Coding sheet and agreement (Cohen's kappa) | `python -m src.sample sheet ...` / `python -m src.sample kappa --a A.csv --b B.csv` | Steps 5.5 and 6 |

Not used in the current plan (kept in the repository): `src/threads.py`, `src/news.py`,
`src/export_dashboard.py`, `dashboard/` (demo numbers only) and `tests/`. See PLAN.md Section 12.

**Platforms.** YouTube Data API v3 is free (10,000 units/day). Instagram comments are copied by hand (no scraping).
X/Twitter has no free API (about US$0.005 per post read) and is not used. Google Trends and GDELT are not part of
the current plan.

## Ethics

Only public material. No commenter usernames or IDs in any committed file; quotes are paraphrased. Raw comment
files (`data/raw/`, `data/comments/`, `data/manual/`) are git-ignored.
