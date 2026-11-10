# Instructions given to each independent analyst

These are the exact instructions given to the six AI analysts (2026-11-09). Each analyst received 4 cases, a
one-line description of each, and these instructions. Analysts started with no knowledge of the team's AI drafts.

## Goal

Analyse each assigned comedy controversy **from scratch and independently**, for a sociology project that compares
24 Indian comedy controversies. The research questions, concepts, lenses, codebook and case template are in
`independent_analysis/method/analyst_brief.md`. Read it first.

## What you may and may not read

**Allowed:**
- `independent_analysis/method/analyst_brief.md` (definitions, framework, codebook, template)
- `data/transcripts/txt/<case_id>__<video_id>.txt`: YouTube auto-captions of videos about the case. They are
  noisy machine captions (Hindi in Devanagari, sometimes Hinglish or Telugu or Tamil). Some are the performance
  itself; others are news reports, reuploads, commentary or the comedian's response. Work out which is which.
  `[हंसी]` / `[Laughter]` = laughter, `[प्रशंसा]` / `[तालियाँ]` / `[Applause]` = applause, `[संगीत]` = music.
- The web: search and read news reports, legal reporting (LiveLaw, Bar & Bench, court orders), statements by the
  comedian and the objectors, and the YouTube pages themselves.

**Forbidden (to keep the analysis independent):** every other file in the repository: `cases/`, `analysis/`,
`data/*.csv`, `PROJECT.md`, `PLAN.md`, `DECISIONS.md`, `README.md`, `LITERATURE.md`, `CODEBOOK.md` (its content
is already in the brief), other files in `independent_analysis/`, and git history. Do not open them.

## How to analyse each case

1. **Research what happened.** Build a dated timeline from news and legal sources. Rules: each fact needs 2
   independent sources (wire copy such as PTI/ANI/IANS carried by several outlets counts once); mark each fact
   `confirmed` (2+ independent sources), `reported` (1 source) or `disputed` (sources disagree). Record every source
   (outlet, title, date, URL) in a numbered list.
2. **Understand the joke from the clip, not from the news.** Read the transcripts. Find the joke(s) that caused the
   controversy and give timestamps. Quote only the key lines (short: one or two lines each), in the original
   language plus an English translation. Then describe:
   - the setup before the joke and what follows it (is it part of a longer bit? is there a callback? a twist?)
   - how the room reacted (laughter/applause markers, silence, the comedian's comments on the reaction)
   - how the viral clip differs from the full performance (what it cuts out; does the cut change the meaning?)
   - whether the news described the joke accurately
   - **if the transcripts do not contain the joke the news reports, say so plainly** and say what that implies
     (different show? cut from the upload? no recording?). Do not invent wording.
   Captions are machine-made: if a word is unclear, say so.
3. **Code the case** using the codebook and template definitions. Justify topic, genre, target and direction with a
   quoted line or a source. Decision rules: police action against attackers or threateners (not the comedian) is
   **not** "legal" (timeline only); administrative action (permission refused, demolition, venue sealed) **is**
   legal, sub-label `administrative`; forced or pressured apologies **are** extra-legal; tweets are not comic
   performances; the family and parents count as sacred objects. Outcome types: `online_only`, `legal`,
   `extralegal`, `both`.
4. **Interpret strictly.** For each lens in the toolkit give a verdict: `supported` only with specific evidence
   from this case (cite it), otherwise `partly`, `not supported` or `not relevant`. Most cases should have only a
   few lenses truly supported. Then name the **2–4 lenses that best explain how this case ended**, and consider at
   least two rival explanations (e.g. fame, elections, timing waves, platform, the comedian's identity).
5. **Say what a human must still check:** exact timestamps to watch, things a transcript cannot show (tone,
   gestures, the room), claims you could not confirm.

## Output: one file per case

Write `independent_analysis/cases/<case_id>.md` with this structure (follow the template sections A–J from the
brief, filled completely, plus the additions below):

```
# <case_id>: <short title>

status: independent AI analysis (not compared with the team draft)
analyst: independent AI analyst, 2026-11-09
transcripts used: <file names, and what each video is: performance / reupload / news / commentary / response>

## Summary (5–8 sentences, plain English)
## A. Basic facts  ...  ## J. Sources and confidence   (template sections, all filled)
## K. The joke in the clip
   (timestamps, key lines with translation, setup and follow-up, room reaction, clip vs full performance,
    news accuracy, what the transcript does NOT show)
## L. Human check list
## Coding summary
```

The **Coding summary** must be a fenced block of `key: value` lines, exactly these keys in this order (use `unknown`
where you cannot tell; separate multiple values with `;`):

```
case_id:
comedian:
performance_date:
controversy_date:
setting:                 club | theatre_special | tv_or_streaming | online_video | campus | other
form:                    scripted_standup | crowd_work | sketch | roast | tv_banter | song | mimicry | other
language:
clip_status:             full_performance | partial_clip | no_recording
joke_found_in_transcript: yes | partly | no
topic:
sacred_object:           none | <what>
genre:
target:
direction:               up | down | lateral | self | contested
collapse_type:           collusion | collision | live_only
gap_months:
first_spreader:
objectors:
objector_distance:       targeted | social | political | none
norm_invoked:
mobilising_actor:        <who took it beyond online anger, or none>
actor_type:              party | statutory_body | police | court | religious_body | activist_group | fans | business | none
channel:                 complaint_fir | commission | court | threats | vandalism | disruption | cancellation | assault | none
legal_actions:
extralegal_actions:
outcome_type:            online_only | legal | extralegal | both
highest_stigma_step:     0-4
courtesy_stigma:         yes | no
comedian_response:       apology | refusal | clarification | silence | mixed
response_changed_course: yes | no | unclear
audience_size_tier:      small | medium | large | very_large
election_period:         yes | no | unknown
key_lenses:              <2-4 lenses>
best_explanation:        <one sentence>
confidence:              high | medium | low
```

## Style and ethics

Plain English, short sentences. No commenter usernames anywhere. Quote jokes only as much as needed to analyse them.
Be neutral and precise about sensitive material (sexual, caste, religious content): describe it analytically.
When done, reply with a short note per case: the most important thing the clip showed that news coverage did not,
and anything you could not resolve.
