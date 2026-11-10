# Instructions given to each checker (step 2: compare with the team's AI draft and settle the final coding)

Given 2026-11-09 to three AI checkers, 8 cases each.

## Goal

For each assigned case there are now two analyses made independently of each other:
- **Independent analysis:** `independent_analysis/cases/<case_id>.md` (made from the clip transcripts plus fresh
  research, without seeing the draft).
- **Team AI draft:** `cases/<case_id>/case.md`, its sources in `cases/<case_id>/sources.md`, and its row in
  `analysis/comparison.csv` (made from news only, without the clips).

Compare them, settle every disagreement against the evidence, and record the **final** analysis.

## Steps for each case

1. Read both analyses completely. Also allowed: `data/transcripts/txt/<case_id>__*.txt`, the definitions in
   `independent_analysis/method/analyst_brief.md`, and the web.
2. List every **factual** difference (dates, who did what, legal steps, the joke's wording or source) and every
   **coding** difference (topic, genre, target, direction, form, collapse type, sacred object, mobilising actor,
   outcome type, stigma step, courtesy stigma, response, key lenses, best explanation).
3. **Settle each difference** by checking the transcript or opening the sources (and searching further if needed).
   Say which side is right and why, in one or two sentences. If neither can be confirmed, say "unresolved" and
   what a human must check. Do not side with an analysis because it is longer or more confident.
4. Note facts or sources that one analysis has and the other missed, if they matter.
5. Note any outright **error** in either analysis (a wrong date, a misattributed joke, a claim the transcript
   contradicts).

## Consistency rules (apply to every case the same way)

- Only **confirmed** events (two independent sources; wire copy counts once) count when choosing the outcome type.
  Single-source events are noted but do not change the code.
- Outcome types: `online_only`, `legal`, `extralegal`, `both`. Legal = FIR, police complaint taken up, summons,
  arrest, court case, statutory commission action, legal notice from lawyers (sub-label it), and **administrative**
  action by a state body (permission refused, demolition, venue booking cancelled by a public institution).
  Extra-legal = threats, vandalism, assault, disruption, cancellations forced by private actors, institutional
  discipline by a private body (e.g. a university suspending students), and **forced apologies**.
- An apology counts as **forced** only when a named actor demanded it with a threat or sanction (e.g. on stage
  under pressure, or to meet a party's ultimatum). An apology after online criticism alone is voluntary.
- Police action against attackers or threateners is not "legal" for the comedian; record it in the timeline only.
- Family and parents count as sacred objects. Tweets are not comic performances.
- Direction: `up` (at those with more power), `down` (at a less powerful or stigmatised group), `lateral`, `self`
  (the comic's own group), `contested` (readings genuinely differ: say which readings).
- Lenses: `supported` only with specific evidence. The final file names the 2–4 lenses that best explain the ending.

## Output

Append to the end of `independent_analysis/cases/<case_id>.md` (do not rewrite the earlier sections):

```
## M. Check against the team's AI draft

### Agreement
(one short paragraph: what both analyses agree on)

### Differences and how they were settled
| # | Point | Independent analysis | Team draft | Settled | Evidence |
|---|---|---|---|---|---|

### Errors found
- In the team draft: ...
- In the independent analysis: ...

### What the clip changed
(2–4 sentences: what we know now that a news-only analysis could not show)

## Final coding
```
(a fenced block with exactly the same keys, in the same order, as the Coding summary, holding the **settled**
values; where nothing changed, copy the value)
```

Also, at the top of the file, change the status line to:
`status: final AI analysis (independent analysis checked against the team draft); awaiting human verification`

When done, reply with one line per case: the outcome type (and whether it changed), the most important correction
to the team draft, and anything left for humans.
