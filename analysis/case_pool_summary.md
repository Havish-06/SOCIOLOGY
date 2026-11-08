# Case Pool: Step 2 Results — Team K

**Date:** 2026-11-04
**Status:** draft for the Step 0 team meeting. Recommendations only; the team makes the final choice.
**Full data:** [`case_pool.csv`](case_pool.csv), one row per candidate (45 rows), with sources, coding, criteria check and recommendation.

## How this was built

1. Havish's 23 cases in `data/cases.csv` were fact-checked one by one against news sources.
2. A search was run for new candidates in the gaps named in `PLAN.md` Appendix B: dark comedy, cases that fizzled
   online, crude and roast cases, regional-language cases, and 2018–2019.
3. Every candidate was checked against the inclusion criteria in `PLAN.md` Step 2: Indian comedian; at least
   **two independent** sources (reprints of one PTI/ANI wire story count once); controversy between 2018 and 2026;
   enough material for the joke, a timeline and the outcome.
4. Each was given a recommendation: **include** (25), **reserve** (13) or **exclude** (7).

**Caution:** this research and coding was done by AI assistants. Genres, outcomes and dates are first-pass
judgements. They have **not** yet been verified by a team member (that happens in Step 5). A few source pages
could not be opened and were judged from search snippets (noted in the CSV).

---

## The suggested 25

`*` = comparison case (not a stand-up performance).

| # | case_id | Comedian | Year | Topic | Genre | Outcome |
|---|---|---|---|---|---|---|
| 1 | agrima_2020 | Agrima Joshua | 2020 | regional icon (Shivaji) | satire | both |
| 2 | fernandes_2024 | Daniel Fernandes | 2024 | religion (Jain) | satire; observational | both |
| 3 | fernandes_2025 | Daniel Fernandes | 2025 | national trauma (Pahalgam) | dark; satire | legal |
| 4 | more_2025 | Pranit More | 2025 | celebrity | roast | extra-legal |
| 5 | sachdeva_2025 | Swati Sachdeva | 2025 | family / sexuality | crude | online only |
| 6 | katikala_2026 | Anudeep Katikala | 2026 | politics (Pawan Kalyan) | satire; roast | both |
| 7 | sarat_2026 | Sarat Uday | 2026 | politics (Naidu, Lokesh) | satire | extra-legal |
| 8 | shah_2021 | Neville Shah | 2021 | caste (down) + disability | dark | online only |
| 9 | parithabangal_2025 `*` | Gopi & Sudhakar | 2025 | caste (up) | dark; satire | both |
| 10 | jain_univ_2023 `*` | Jain University students | 2023 | caste (down), Ambedkar | crude; dark | legal |
| 11 | munawar_2021 | Munawar Faruqui | 2021 | religion (alleged) | dark (alleged) | both |
| 12 | virdas_2021 | Vir Das | 2021 | nation | satire; dark | both |
| 13 | kamra_2025 | Kunal Kamra | 2025 | politics (Shinde) | satire | both |
| 14 | latent_2025 | Samay Raina / Ranveer Allahbadia | 2025 | family / sexuality | crude; roast | both |
| 15 | kapil_2024 `*` | Kapil Sharma | 2024 | looks | roast | online only |
| 16 | bharti_2022 `*` | Bharti Singh | 2022 | religion (Sikh) | observational; crude | legal |
| 17 | raina_sma_2025 | Samay Raina | 2025 | disability (SMA child) | dark | legal |
| 18 | more_2026 | Pranit More | 2026 | gender (crowd work) | crude | legal |
| 19 | virli_2026 | Madhur Virli | 2026 | gender (rape joke) | dark | legal |
| 20 | faruqui_2024 | Munawar Faruqui | 2024 | region (Konkani people) | crude | extra-legal |
| 21 | raina_2026 | Samay Raina / Sharon Verma | 2026 | region (Bihar, Kashmiri Pandits) | roast; dark | online only |
| 22 | mohanraj_2026 | Aishwarya Mohanraj (Comicstaan clip) | 2026 | gender / family | dark | online only |
| 23 | banerjee_2024 | Bunty Banerjee (as a Latent contestant; check that he is a working comedian, otherwise exclude like nabam_2025) | 2024 | mental health; RG Kar protests | dark; roast | online only |
| 24 | kamra_2018 | Kunal Kamra | 2018 | nation / politics | satire | extra-legal |
| 25 | rangeela_2021 | Shyam Rangeela | 2021 | politics (Modi mimicry) | satire | legal |

Row 17 replaces `disability_sc_2025`. That row bundled five comedians, but only Raina's SMA joke is documented
anywhere, so the case is narrowed to it.

### Balance of the 25

By topic (main comparison; each case placed under its main topic):

| Topic | online only | legal | extra-legal | both | total |
|---|---|---|---|---|---|
| Politics | 0 | 1 | 2 | 2 | 5 |
| Gender, sexuality, family | 2 | 2 | 0 | 1 | 5 |
| Religion | 0 | 1 | 0 | 2 | 3 |
| Caste | 1 | 1 | 0 | 1 | 3 |
| Region and regional icons | 1 | 0 | 1 | 1 | 3 |
| Nation and national trauma | 0 | 1 | 0 | 1 | 2 |
| Disability and mental health | 1 | 1 | 0 | 0 | 2 |
| Celebrity and looks | 1 | 0 | 1 | 0 | 2 |
| **total** | 6 | 7 | 4 | 8 | 25 |

Genre counts (a case can have more than one): dark 11 (including Munawar, alleged), satire 10, crude 6, roast 6, observational 2.

**Early patterns to test, not findings.** On this first-pass coding, **no politics or religion case stayed
online only**, and politics is the only topic where extra-legal action is common. **Gender and sexuality cases
never drew extra-legal action**: they went to commissions and courts, or fizzled. If this holds after
verification, it suggests that jokes touching leaders and the sacred bring in party workers and mobs, while
jokes about gender and family are handled through formal complaints. Genre is a secondary check: no dark
comedy case ended in extra-legal action only. This bears on SQ1 and the Durkheim expectations.

### Matched pairs built into the 25

| Pair or series | What stays the same | What differs |
|---|---|---|
| fernandes_2024 / fernandes_2025 | Comedian | Topic; apologised vs refused |
| more_2025 / more_2026 | Comedian | Roast of a celebrity vs crude crowd work; fans vs commission |
| munawar_2021 / faruqui_2024 | Comedian | Religion (alleged) vs region; jail vs threats |
| kamra_2018 / kamra_2025 | Comedian, satire | Campus cancellation vs vandalism plus FIRs |
| katikala_2026 / sarat_2026 | Same week, Andhra politics | State route vs mob route |
| latent_2025 / banerjee_2024 / raina_2026 | Same show | Crude joke → FIRs; dark jokes → fizzled |
| virli_2026 / mohanraj_2026 | Same week, dark gender jokes, both resurfaced | Legal vs online only |
| shah_2021 / jain_univ_2023 / parithabangal_2025 | Caste | Punching down (fizzled / arrests) vs punching up (complaints, threats) |
| raina_sma_2025 / shah_2021 | Dark jokes on disability | Court-led action vs fizzled |

---

## Reserves (13)

These can replace an included case, or be added if the team wants up to 30.

| case_id | Why it is a reserve |
|---|---|
| rafiq_2026 | Third Andhra case, very close to katikala_2026 |
| rajwani_2018 | Adds 2018 religion, but the joke is never quoted |
| fernandes_2021, fernandes_2023 | Would extend the Fernandes series with two dark jokes that fizzled; only 2 sources each |
| gujral_2025 | Crude, online only; only 2 sources |
| solanki_2024 | Roast of Ashneer Grover; legal action unconfirmed |
| subramanian_2018 | Observational joke about DJs that still drew threats and a cancellation; 2 sources |
| kamra_2020 | Supreme Court contempt case, but over tweets |
| roy_2020 `*` | Bengali, obscene Tagore parodies; parodist, not stand-up |
| abhishek_2024 `*` | Tagore parody on the Kapil Show; pairs with roy_2020 |
| bhattacharya_2025 `*` | Bengali satirical song; adds Bengal |
| aadi_2021 `*` | Telugu TV skit on the Bathukamma festival |
| khiladigalu_2025 `*` | Kannada TV skit on the Mahabharata |

**Regional gap.** The 25 are weak on Bengal and Karnataka. To fix this, swap in `roy_2020` + `abhishek_2024` (a
Tagore pair) and/or `khiladigalu_2025`. All of them are comparison cases rather than stand-up.

## Excluded (7)

| case_id | Reason |
|---|---|
| sachdeva_reservation | Social-media reply, thin material |
| gaur_2021, mathew_2021 | Old tweets, not comic performances |
| tangade_dalit | No single dated incident, only an ongoing pattern of trolling |
| nabam_2025 | Contestant on Latent, not a comedian |
| bassi_2023 | Supreme Court petition, but no specific joke reported |
| yakshagana_2019 | Performer unnamed, outcome unknown |

Rejected during the search (did not meet the criteria): Kamra vs Ola Electric (not a joke), Saloni Gaur (no single
dated incident), Shyam Rangeela 2017 and Sourav Ghosh (before 2018), Bharath Balaji (joke not described), Jabardasth
Venu skit (2014), Harsh Gujral's Operation Sindoor skit (one source), Abhishek Upmanyu 2025 (an X reply),
Rohan Joshi 2022 (a comment, not a joke), Mallika Dua 2019 (one source, not clearly comic), and others listed in the
agents' notes.

---

## Errors found in `data/cases.csv`

To be corrected in Step 5. The corrected values are already in `case_pool.csv`.

| Case | Error |
|---|---|
| several | Outcome "none" is not a valid category → `online_only` (sachdeva_2025, shah_2021, sachdeva_reservation, kapil_2024, gaur_2021) |
| fernandes_2024 | A police complaint was filed in Chennai → outcome `both`, not extra-legal. "Dark" is a weak genre fit |
| fernandes_2025 | Date is 2025-05, not 2025-06 (video days after the 22 April attack; notice dated 29 May) |
| agrima_2020 | Gap is about 15 months, not 12 (set performed April 2019). No FIR against Joshua was found |
| katikala_2026, rafiq_2026 | Threats and pressure from party workers also occurred → `both` |
| sarat_2026 | Gap is about 16 months, not 24. He **did** apologise. The "use legal processes" line was the TDP's, not his |
| shah_2021 | Row omits that the joke also mocked the doctor's limp (ableism) |
| parithabangal_2025 | A counter-complaint cites threats of violence → `both` |
| virdas_2021 | "Multiple FIRs" is not supported: police **complaints** in Mumbai and Delhi; reports say no FIR. Show dates: Bengaluru called off 2022-11-10; Hyderabad postponed from 2022-11-20 |
| latent_2025 | Allahbadia reported death threats and intrusion at his mother's clinic → `both`. Raina deleted the episodes himself (2025-02-12) |
| munawar_2021 | Date 2021-01-01. Bengaluru cancellation was by police order. The "12 shows in 2 months" figure needs dating (Oct–Nov 2021) |
| kamra_2025 | BMC demolition was on 2025-03-24, the day after the vandalism |
| bharti_2022 | Second FIR (Adampur) came from Ravidas Tiger Force, not the SGPC |
| rajwani_2018 | Date 2018-04-15. A police complaint was filed that night → `both`. Better coded as a collision (video released Nov 2018) |
| disability_sc_2025 | Bundles five comedians; only Raina's joke is documented. Date in row is the summons date, not the joke date |
| more_2026 | Bundles a separate KEM student clip. "Placed on leave" is unconfirmed |
| more_2025 | Collapse type should be the standard value `live_only` |

**General lesson:** several rows said "none found" where sources do report threats or complaints. Outcomes need
a careful check in every case analysis.

---

## New rule questions for the team

Copied to `DECISIONS.md`. These change how several cases are coded, so they must be settled before Step 5.

1. **Actions against third parties.** When police arrest the people who **threatened or attacked** the comedian
   (Agrima, Pranit More 2025), does that count as "legal action" in the case? Recommendation: no. Code only actions
   taken against the comedian, show or venue, and record the rest in the timeline.
2. **Administrative action.** Is a municipal demolition (Kamra's studio) or a police refusal of permission "legal",
   or a separate "administrative" category? Recommendation: code it as legal (state action) with a sub-label `administrative`.
3. **Forced apologies.** Is a forced on-camera apology (Rajwani) or pressure into an apology (Rafiq) extra-legal
   action? Recommendation: yes.
4. **Tweets and social-media replies.** Do they count as comic performances? Recommendation: no, except as reserves.
5. **Comparison cases.** How many non-stand-up cases (TV, sketch, skit, parody) to allow? The suggested 25 have 4.
   Adding the regional reserves would raise this to 6–7.
6. **Total number:** keep 25, or go to 28–30 with reserves for regional coverage?

## What happens next

1. **Step 0 team meeting:** go through this summary, `PLAN.md` and `DECISIONS.md`; decide the list and the rule questions.
2. Step 3: freeze the template.
3. Step 4: pilot case (`latent_2025` is suggested).
