# Independent analysis — final AI analysis of all 24 cases

**Status (2026-11-10): final AI analysis, awaiting human verification.** This folder holds a second, independent
analysis of every case, built from the **clips themselves** (transcripts of the full performances), and then checked
point by point against the team's first AI drafts in `cases/`. Where the two disagreed, the disagreement was settled
against the transcripts and sources. The result is the most complete version of each case we have.

## Why this exists

The first drafts in `cases/<case_id>/case.md` were written from news and legal reports only: nobody had looked at
the jokes themselves. Since context is the core of the project, every case was redone starting from the clip.

## Read in this order

| File | What it is |
|---|---|
| [findings.md](findings.md) | **Cross-case findings**: the answer in one paragraph, topics, direction, genre, context and the clip, who mobilised and through which channel, the sacred, stigma, apologies, typology, matched pairs, counter-examples, answers to the research questions |
| [cases/](cases/) | **One final analysis per case** (24). Template sections A–J, plus **K** (the joke in the clip: timestamps, key lines, setup, room reaction, what the clip and news left out), **L** (human check list), **M** (check against the team draft: differences and how each was settled), and the **Final coding** |
| [comparison.csv](comparison.csv) | Master comparison table: the final coding of all 24 cases, one row per case |
| [vs_ai_draft.md](vs_ai_draft.md) | Case by case: what the team draft got wrong or missed, and the outcome before and after |
| [human_checks.md](human_checks.md) | **What each owner still has to check**, with timestamps |
| [agreement.csv](agreement.csv), [side_by_side.csv](side_by_side.csv) | Agreement between the independent analysis and the draft, per field |
| [method/](method/) | How it was done (below) |

## How it was done

1. **Transcripts.** YouTube's own captions (original language) were downloaded for 67 videos across the 24 cases
   with `method/fetch_transcripts.sh` (list in `method/transcript_videos.txt`) and converted to text with
   `method/vtt2txt.py`. They are saved in `data/transcripts/` and **not committed** (copyright; regenerate them with
   the script). Some cases have only reuploads, short clips or no recording; each case file says which.
2. **Independent analysis.** Six AI analysts, 4 cases each, analysed every case from scratch from the transcripts
   plus fresh news and legal research. They were **not allowed to open** the team's drafts, comparison tables or
   findings (`method/analyst_instructions.md`; definitions in `method/analyst_brief.md`).
3. **Check against the draft.** Three AI checkers compared each independent analysis with the team draft and
   settled every difference against the transcripts and sources, under fixed rules: only confirmed facts (two
   independent sources) change a code; a "forced" apology needs a named actor with a threat
   (`method/checker_instructions.md`). Each case file ends with section M and the Final coding.
4. **Consistency.** Three rules the codebook lacked (stigma step for FIRs, audience tiers, election period) were
   applied to all 24 (`method/consistency_rules.md`, `method/normalise.py`).
5. **Tables and findings.** `method/build_tables.py` builds `comparison.csv`, `side_by_side.csv` and
   `agreement.csv` from the case files; `findings.md` was written from the table and the case files.

## What it still needs

Human verification of every case (`human_checks.md`), the comment collection and spam audit (detectable coordination in YouTube
comments), and team decisions on the consistency rules. Commenter usernames do not appear in any file.
