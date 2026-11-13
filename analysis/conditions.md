# A non-circular test of the main finding

**Status: 2026-11-13. Coded by AI from the final case files (`independent_analysis/cases/`); each owner checks the
coding of their 6 cases (the table in `conditions.csv`, one row per case). 13 Nov: Pranav recoded kamra_2018
(sacred: no) and virdas_2021 (mocks a ruler: no) after rewatching the clips; the counts below reflect this.**

## The problem

The earlier headline, "a controversy escalates when someone with organisation or legal standing takes it up", is close
to true by definition: a case is coded "legal" *because* someone filed a complaint. It explains the outcome with the
outcome.

## The fix

Explain the outcome only with conditions that can be judged **before anyone reacts**, from the joke as performed, its
butt, and who held office where. Never from who reacted, how, or what happened next. Then check how well those
conditions predict the outcome, and name the cases where they fail.

| Condition | Coded from | Definition |
|---|---|---|
| **Mocks a ruler** | the joke's target and the political map | The joke mocks a named leader or party (not the state of the country in general) that holds office in that state or at the centre |
| **Defended butt** | the joke's butt | The butt is a group with a dedicated statutory body or protective law: women (NCW), SC/ST (SC/ST Act), persons with disabilities (RPwD Act), notified religious minorities (NCM) |
| **Sacred in the joke** | the joke as performed | An item on the fixed sacred list (deities and religious symbols, regional icons, Ambedkar, the nation, the family, collective trauma) appears in the joke itself, not only in objectors' claims |
| **Own group** | the joke's butt | The comedian mocks their own family or community |

Escalated = any outcome other than online only (legal, extra-legal or both).

## Results (24 cases)

| Condition | Escalated | Route when escalated | Exceptions |
|---|---|---|---|
| Mocks a ruler | **7 of 7** | both 3, legal 3, extra-legal 1 | none |
| Defended butt | **5 of 6** | legal 3, both 1, extra-legal 1 | shah_2021 (online only) |
| Sacred in the joke, other people's group | **4 of 5** | both 3, legal 1 | raina_2026 (online only) |
| Sacred in the joke, own group | **0 of 2** | — | both stayed online: sachdeva_2025, mohanraj_2026 |
| None of the above | 3 of 4 | extra-legal 2, legal 1 | kapil_2024 stayed online, as predicted; the other three are counter-examples |

**One rule:** *a controversy escalates if the joke mocks a ruling-party leader, or targets a group with a statutory
defender, or touches the sacred of a group other than the comedian's own.* It predicts **19 of the 24** outcomes
(16 of 18 predicted escalations; 3 of 6 predicted online-only cases).

## Where the rule fails (and what that tells us)

| Case | Predicted | Actual | Why |
|---|---|---|---|
| shah_2021 | escalate (defended butt: SC/ST, disabled) | online only | Nobody used the statute: the clip was five years old, and the Dalit-Bahujan response was an online call-out, not a complaint. A protective law opens a route only if someone chooses to use it |
| bharti_2022 | online only (no condition in the joke) | legal | The joke names no religion; the Sikh reading was **added in circulation** (reupload titles "Sikh beard"). Collision can create the sacred condition after the fact |
| faruqui_2024 | online only | extra-legal | A regional jibe answered with religious threats by a BJP MLA before a state election. The comedian's **prior stigma and identity** (munawar_2021), not the joke, drew the response |
| more_2025 | online only | extra-legal | **Fans** of a film star assaulted him. Fandom is a separate route the conditions do not cover |
| raina_2026 | escalate (sacred of another group: Sharon Verma's Kashmiri Pandit exodus joke at Raina) | online only | Politicians and the J&K Peace Forum objected publicly, but nobody filed anything. The roast was mutual on a show whose host is himself a Kashmiri Pandit, so the in-group licence may have covered both comedians. Coding checked by Havish (13 Nov): Raina jokes about Pandits with Orry (own group), Verma makes the objected joke (another's group) |

The failures point to three things the conditions leave out: whether anyone **chooses** to use an available tool
(shah_2021), **circulation that reframes** a joke (bharti_2022), and the **comedian's identity and record**
(faruqui_2024), plus fandom (more_2025).

## How this changes the headline

- **Old (circular):** controversies escalate when someone with standing takes them up.
- **New (testable):** controversies escalate when the joke mocks a ruling-party leader (7/7), targets a group with a
  statutory defender (5/6), or touches the sacred of a group other than the comedian's own (4/5, against 0/2 for the
  comedian's own group). Mobilising actors (parties, commissions, police, activist groups) are the **mechanism** that
  turns these conditions into outcomes, traced case by case in the case files; they are not the explanation.
- **Route:** jokes at rulers mostly end in "both" (party workers on the street plus FIRs); jokes at defended groups
  mostly end in the legal route (commissions, protective statutes).

## Limits of this test

1. **Selection on the outcome.** All 24 are controversies. The test compares controversies; it cannot say that a joke
   meeting a condition is risky in general. Many jokes about rulers never become controversies at all.
2. **The own-group condition was noticed after looking at the cases** (now 2 cases). Treat it as a hypothesis to test on
   new cases, not as a result.
3. **Small numbers.** 7 of 7 and 4 of 4 are patterns, not statistics.
4. **AI coding.** The conditions were coded by AI from the final case files; each owner checks their rows. Borderline
   codings are marked in `conditions.csv` (virdas_2021: whether criticism of the state of the country counts as "the nation" in the joke; munawar_2021: deities and Amit Shah
   alleged, not recorded; raina_sma_2025: the family is a secondary element).
5. **Conditions overlap.** Several cases meet two conditions (jain_univ_2023, katikala_2026), so the
   conditions cannot be separated from each other with 24 cases.

The data: `analysis/conditions.csv` (one row per case: each condition, a note on why, direction, outcome).
