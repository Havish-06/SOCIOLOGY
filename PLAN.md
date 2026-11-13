# Plan: how to carry it out — Team K

The working method: news protocol, every step in detail, comment protocol and spam audit, folder structure, open questions, timeline, glossary. Start from [README.md](README.md) for where everything is.

## News protocol

News articles do two jobs, and we keep them apart:
1. **Evidence of what happened** (dates, who complained, FIR sections, arrests, threats, apologies). Facts need
   two independent sources (PROJECT.md §9, Verification rules).
2. **Data on how the controversy was framed.** How outlets described the joke and the comedian is itself a
   finding (Entman, 1993; Semetko & Valkenburg, 2000; Ödmark, 2021), so framing is coded, not adopted.

**Which outlets.** English-language coverage is enough for every case. Search across these types so that no single kind of outlet sets the story:

| Type | Examples |
|---|---|
| National English dailies and TV sites | The Hindu, The Indian Express, Hindustan Times, The Times of India, NDTV |
| Digital-native outlets | Scroll, The Print, The News Minute, The Wire, Newslaundry, The Quint |
| Legal news | LiveLaw, Bar & Bench (FIRs, court orders) |
| Outlets with an explicit editorial stance | At least one outlet from each side of the political debate where the case was covered, to see opposing frames |
| *Optional:* Hindi or regional press | Only where it adds a frame the English outlets miss (e.g. Dainik Bhaskar, Amar Ujala) |

**How to search.** Comedian's name plus the controversy keywords (e.g. "Samay Raina parents joke", "Kunal Kamra
Shinde FIR"), in English and, where relevant, Hindi or Telugu; window from one week before the first complaint to
three months after the last legal step; Google News and each outlet's own search. Record the search terms and
date of search in `sources.md`.

**How many.** For framing, code **6–10 articles per case**, covering at least three outlet types and both the
first days and the later legal phase. All articles used for facts are listed in `sources.md` whether or not they
are coded for framing.

**Independence.** Wire copy (PTI, ANI, IANS) reprinted by several outlets counts as **one** source. An article that
only repeats another outlet's report counts as that outlet.

**What to code for each framing article** (`analysis/news_coding.csv`, one row per article):

| Field | Values |
|---|---|
| case_id, outlet, outlet_type, date, headline, url | |
| phase | first_week · legal_phase · aftermath |
| dominant_frame | hurt_sentiments · obscenity · insult_to_leader · free_speech · cancel_culture · legal_overreach · comedy_standards · other (Entman: what problem, whose fault, what remedy) |
| generic_frame | conflict · responsibility · morality · human_interest · economic (Semetko & Valkenburg, 2000) |
| joke_described_as | quoted verbatim · paraphrased neutrally · characterised ("obscene", "insulted gods") |
| comedian_labelled | none · deviant label (quote it) |
| attribution | claims attributed ("allegedly", "according to the complaint") · stated as fact |
| voices_quoted | complainant · politician · police · lawyer/court · comedian · other comedians · experts · public |
| first_to_report | yes · no (does this outlet appear to have broken the story?) |

**Coverage timing (optional).** `src/news.py` can count daily online news articles per case from GDELT to see
whether news coverage started before or after the online outrage and the complaint. GDELT under-covers
regional-language outlets, so treat it as national English attention only.


## The steps, in detail

Each step lists its goal, what it needs, what to do, what it produces, and when it counts as done.

### Step 0: Team alignment

- **Goal:** the whole team, including Havish, agrees on this plan before work starts.
- **Do:**
  1. Everyone reads this file.
  2. Meeting (about 1 hour). Decide:
     - approve or edit the main question and sub-questions (PROJECT.md §3)
     - confirm the target number of cases (20–30)
     - who owns which cases (Step 5)
     - whether to send the supervisor a short update (optional; see the note below)
  3. Record the decisions in DECISIONS.md (date, decision, reason).
- **Note to the supervisor (optional; the supervisor has said the original proposal no longer binds us):**
  > We are carrying out a structured comparative case study of 20–30 Indian comedy controversies, asking which
  > topics bring stand-up comedians under scrutiny and why some controversies end in legal or extra-legal
  > action while others fizzle. Each case is interpreted with a toolkit of sociological lenses (stigma, context collapse, Durkheim, scandal, moral panic, mobilisation and others), using news,
  > official records and public comments.
- **Output:** DECISIONS.md.
- **Done when:** the questions above are decided and recorded.

### Step 1: Setup

- **Goal:** the tools and folders are ready.
- **Do:**
  1. **YouTube API key** (one team member, about 5 minutes):
     Google Cloud Console → create a project → APIs & Services → enable "YouTube Data API v3" →
     Credentials → Create credentials → API key. Copy `.env.example` to `.env` and paste the key after
     `YOUTUBE_API_KEY=`. Also set `ANON_SALT=` to any random string. **Never commit `.env`** (it is git-ignored).
  2. **Python environment:** `python -m venv .venv`, activate it, `pip install -r requirements.txt`.
  3. Create the folders in PLAN.md, Folder structure (`cases/`, `data/comments/`, `data/transcripts/`, `analysis/`).
  4. Copy `cases/_template.md` into `cases/_template.md`.
- **Free quota:** 10,000 units per day. One unit fetches up to 100 comments, so even the largest case
  (about 49,000 comments) needs only about 500–1,000 units. Quota is not a constraint.
- **Done when:** `python -m src.collect --video-ids <any id> --case-id test` downloads comments into `data/raw/`.

### Step 2: Build the case pool and select the cases

- **Goal:** a final list of 20–30 cases, chosen by written criteria so the selection cannot be called cherry-picking.
- **Do:**
  1. **Long-list (about 40 candidates).** Start from the 23 cases in `data/cases.csv` and the extra ideas in
     `analysis/case_pool_summary.md`. The AI assistant searches for further candidates. For each candidate, record:
     comedian, approximate date, topic, likely genre, likely outcome type, number of independent sources
     found, and whether a clip or comments are available.
  2. **Inclusion criteria** (a case must meet all):
     - (a) a joke or comic performance by an Indian comedian, or a clearly marked comparison case (TV show, sketch, college skit)
     - (b) covered by **at least two independent** news sources
     - (c) the controversy happened between 2018 and 2026
     - (d) enough material to fill the template (at minimum: a description of the joke, a dated timeline, the outcome)
  3. **Balance targets** (aim for, not rigid quotas):
     - **Topic (main):** at least 2–3 cases each for religion, caste (both directions), politics and the nation, gender and sexuality, and regional icons; at least one each for disability, celebrities and looks
     - **Outcome:** at least 4 each of online-only, legal, extra-legal, and both. **Online-only cases that fizzled are essential** (they are the contrast that makes escalation explainable)
     - **Genre (recorded, no quota):** note the spread of dark, satire, crude/shock, roast and observational; do not pick cases to fill genre slots
     - **Audience size:** small, mid and large comedians
     - **Pairs:** keep the matched pairs (same comedian twice; same week, different route; caste joke up vs down)
  4. **Fill a selection matrix** (topic × outcome) and look for empty cells. Empty cells are informative,
     but if an empty cell is due to missing research rather than reality, search for a case to fill it.
  5. Team picks the final 20–30. Record rejected candidates and the reason (e.g. "only one source").
- **Output:** `analysis/case_pool.csv` (all candidates, with included yes/no and reason) and the final list in DECISIONS.md.
- **Done when:** the final list is agreed and the matrix has no empty cells that are only due to missing research.

### Step 3: Finalise the template

- **Goal:** one fixed template that every case follows exactly.
- **Do:** review `cases/_template.md` as a team. Add or remove fields now, **not later**. Changing the template after
  cases are written means rewriting them.
- **Output:** `cases/_template.md` (frozen; any later change recorded in DECISIONS.md and applied to all cases).
- **Done when:** the team approves the template.

### Step 4: Pilot case

- **Goal:** test the template and workflow on one case before scaling up.
- **Suggested pilot:** `latent_2025` (Samay Raina / Ranveer Allahbadia, India's Got Latent). It is well documented,
  has rich legal and online reactions, and triggered later cases, so it stress-tests every section.
- **Do:** run the full per-case workflow (Step 5) on this one case. Then the team reviews:
  - Which template fields were hard or impossible to fill?
  - Which fields were filled but did not help the comparison?
  - How long did it take?
  - Were the verification rules workable?
- **Output:** `cases/latent_2025/` complete, plus template fixes recorded in DECISIONS.md.
- **Optional:** a second pilot (`kamra_2025`) if the first shows big template changes.
- **Done when:** the template is adjusted and frozen.

### Step 5: Analyse every case, one by one

Each case goes through these sub-steps. The case owner (a team member) is responsible for the case reaching `final`.

| Sub-step | Who | What happens | Output |
|---|---|---|---|
| 5.1 Research | AI | Search news, legal reports and statements. Build the dated timeline and source list. | `cases/<case_id>/sources.md` |
| 5.2 Full clip and first read | Case owner, **before opening the draft** | Watch the **full** original performance (links in `analysis/clips.md`), not only the viral seconds. Copy the YouTube transcript ("Show transcript"); if there is none, write the key lines by hand. Write a first read: what the joke was, what came before and after, how the room reacted, how the viral clip was cut, topic, direction, what angered people, outcome. If no clip exists, use the best reported quotation and say so. | `data/transcripts/<case_id>__<video_id>.txt` (git-ignored); row in `analysis/first_read.csv` |
| 5.3 Comments | AI + team | AI pulls YouTube comments for up to 3 key videos and reads and themes them following PLAN.md, Comment protocol. | `data/comments/<case_id>_*.csv` (git-ignored), themes in section E |
| 5.4 Draft | AI | Fill every section of the template, including the theory reading (section H). | `cases/<case_id>/case.md` (`status: draft`) |
| 5.5 Compare | Case owner | Give the AI the transcript; compare the first read with the draft field by field; fix the draft where the clip or sources show it is wrong; mark in `first_read.csv` where the owner and the AI agreed. | `case.md` updated |
| 5.6 Verify | Verifier (never the owner) | Check every fact against sources (PROJECT.md §9, Verification rules). | `status: verified` |
| 5.7 Finalise | Case owner | Fix flagged items, update the master table. | `status: final`, row in `analysis/comparison.csv` |

- **Workload:** 24 cases and 4 people: 6 cases each to own and 6 to verify. Assignments in `analysis/assignments.md`
  (Havish, Yogansh, Pranav, Siddanth; verifiers rotate).
- **Order:** do matched pairs together (e.g. both Fernandes cases, both More cases, Katikala and Sarat Uday),
  so the comparison is easy to see while writing.
- **Done when:** every selected case is `final`.

### Step 6: Cross-case comparison

- **Goal:** turn the individual cases into findings. **This is the actual result of the project.**
- **Do:**
  1. **Master table** (`analysis/comparison.csv`): one row per case, one column per template field that
     can be compared (genre, topic, direction, form, collapse type, gap in months, accusatory caption,
     sacred object, who mobilised, channel used, highest stigma step, courtesy stigma, comedian's response,
     outcome, audience size, election period, and so on).
  2. **Agreement report:** share of cases where the owner's first read matched the AI draft on each
     judgement (`analysis/first_read.csv`). Report it honestly.
  3. **Answer each sub-question:**
     - SQ1: compare topics (and punching up vs down within a topic) on outcome and reaction framing; then check whether genre adds anything once topic is held constant
     - SQ2: compare collision cases with collusion cases on how far they escalated
     - SQ3: compare who mobilised, through which channel, how they framed the joke, and whether the comedian or venue was stigmatised; check the Durkheim expectations
  3b. **Mechanisms across cases:** tabulate the lens verdicts from section H of every case (`analysis/mechanisms.csv`)
     and ask which mechanisms recur with which outcomes, and which never appear
  4. **Paired comparisons:** for each matched pair, write what differed and what stayed the same, and which
     difference best explains the different outcomes.
  5. **Typology of escalation paths:** group cases into recurring paths (e.g. *resurfaced clip → party
     complaint → FIR*; *live show → fan group → assault*; *online anger → apology → fizzled*).
  6. **Look for counter-examples:** for every pattern, list the cases that do not fit and explain them.
     A pattern with no counter-examples checked is not a finding.
  7. **Optional, simple QCA-style truth table:** cases × 4–5 conditions × outcome, as a visual check of
     which combinations go with which outcome. Not as a formal causal claim.
- **Output:** `analysis/comparison.csv`, `analysis/mechanisms.csv`, `analysis/findings.md` (patterns, pairs, typology, counter-examples, agreement report), figures.
- **Done when:** each sub-question has an answer supported by named cases, with counter-examples addressed.

### Step 7: Interviews (dropped)

Not done: no time before the deadline (decided 2026-11-09). The chilling-effect question is answered from
comedians' public statements only.

### Step 8: Write up

- **Suggested structure of the final paper:**
  1. Introduction: open with *India's Got Latent* and the Rs 370 biryani clip; the puzzle (why some jokes end
     in FIRs, some in mobs, some in nothing); why it matters
  2. Conceptual framework (topic and genre, stigma, context, Durkheim, the interpretive toolkit; PROJECT.md §5)
  3. Literature and gaps (from LITERATURE.md), ending with how each stream is used in our method
  4. Method (this plan's PROJECT.md §7–9, including the AI disclosure and limitations)
  5. Cases overview (table of all cases)
  6. Findings by sub-question, with paired comparisons and the typology
  7. Discussion (led by the findings, not by a fixed list of theories):
     - restate the main answer in one paragraph
     - interpret each major finding: *why* it happens, using whichever lenses in the toolkit (PROJECT.md §4–5) the
       evidence supports: scandal, moral panic, strategic offence, mobilisation, law as a weapon, organised online
       publics, platforms, context collapse, stigma, Durkheim, humour theory, identity and power, fandom, apology
       (e.g. whether different groups defend their "sacred" through different channels: party cadres, formal
       complaints, commissions), and saying so where a theory fails to predict
     - explain the counter-examples and surprises
     - relate to previous work (LITERATURE.md): where we agree with, extend or contradict it
     - rival explanations (elections, fame, platform, amount of news coverage)
     - implications: self-censorship, the state as referee or instrument, platforms and clipping
     - the limits of the interpretation (then the full limitations section)
  8. Limitations
  9. Conclusion
  - Appendix: one-page summary of each case
- **Also:** presentation slides; a tidy repository.
- **Optional bonus:** rebuild the dashboard from `analysis/comparison.csv` as a visual case map.


## Comment protocol

**Why we collect comments.** News and legal records tell us what institutions did; comments are the only
place we can see how ordinary viewers received the joke. They answer specific parts of the research questions:

| What comments show | Question it answers |
|---|---|
| Who reacted, and whether they were the comedian's usual audience or newcomers arriving through a clip or news story | SQ2: degree of context collapse, collusion vs collision |
| Whether people treated it as a joke ("it's comedy") or as an insult or crime ("hurting sentiments") | SQ2: did the comic frame survive the move to a new audience? |
| The norm people said was broken, the sacred object they invoked, the intent they attributed | SQ1 and SQ3: what made this topic sensitive, and *whose* sacred |
| Whether attacks targeted the joke or the comedian's identity (religion, caste, gender) | SQ3: stigma and labelling |
| Calls for FIRs, arrests or boycotts, and when they appeared relative to the complaint | SQ3: mobilisation; did online anger come before or after the legal route? |
| Who defended the comedian and how | Counter-mobilisation |
| **Whether there was detectable coordinated activity in the YouTube comments** | Strategic-offence and online-publics lenses: supporting evidence only (see below) |

The last row is why spam and coordination detection matters, and also what it **cannot** do. If many hostile
comments come from copy-paste campaigns, batch-created accounts or accounts acting in lockstep, that is evidence of
**coordinated amplification** (George, 2016; Jakesch et al., 2021). But the audit cannot show that outrage was
organic: real supporters mobilised on WhatsApp who write their own comments look organic to it; most outrage happened
on X, Instagram, WhatsApp and TV, not in YouTube comments; YouTube removes much spam before we see it; and the API
gives no IP or device data. So a flag is evidence of coordination, and **no flag is not evidence of organic outrage**.
Whether outrage was organised is answered mainly from the case evidence (who complained, who mobilised, who
publicised it); the comment audit is a lower bound on coordination in one platform.

Comments are **one source of evidence about how people framed the joke**. They are **not** treated as a
representative sample of public opinion, and no percentages from them are presented as "what India thinks".

**Which videos (up to 3 per case), in order of priority:**
1. the original clip on the comedian's own channel
2. a reupload of the original
3. the comedian's response or apology video
4. news coverage (only if nothing above exists; mark it, because its commenters are news viewers)

**Which comments:**
- Download all comments with `src/collect.py` (it pulls every top-level comment and reply).
- **Read sample:** per video, the 50 most-liked top-level comments plus 50 random top-level comments
  (fixed random seed so the sample can be reproduced), with the collection date recorded.
- For very large comment sections, the full set can still be searched for specific phrases
  ("hurt sentiments", "anti-national", "just a joke") to check how common a theme is.

**What to record for each read comment** (light version of CODEBOOK.md, C2):
- reaction: support · mock the offended · neutral · backlash · threat · demand legal action · spam
- frame: play ("it's just a joke") · serious ("this is not comedy", "hurting sentiments") · none
- target: comedian · joke · offended group · platform · state
- stigmatises the comedian: yes (attacks their religion, caste, region, gender) · no
- sacred object invoked: from the fixed list in PROJECT.md §4–5, or none
- norm invoked: religious feeling · national honour · women's dignity · family/parents · caste dignity · decency · leader's honour · none (Rost et al., 2016)
- intent attributed to the comedian: meant harm · meant it as a joke · not stated (Graefer & Das, 2020: audiences judge offence by inferred intent)

**What goes into the case file:** the main themes, how often each appeared in the read sample, 2–3
**paraphrased** examples per theme (never usernames), and anything surprising.

**Spam and coordination detection (`src/spam.py`).** Run on every case's comments before any comment is read,
counted or quoted. Methods follow the coordination-detection literature (LITERATURE.md, stream 11):

| Signal | What it catches | Based on |
|---|---|---|
| Commercial patterns | Links, "check my channel", WhatsApp/Telegram, crypto, phone numbers, Hinglish money scams | YouTube comment-spam research (Alberto et al., 2015) |
| Copy-paste campaign | Near-identical text (character n-gram similarity ≥ 0.9, works for Hindi and Telugu scripts) from ≥ 3 accounts | Pre-written "toolkit" text (Jakesch et al., 2021); text-reuse coordination (Pacheco et al., 2021) |
| Copied comment | An account re-posting someone else's earlier comment (like-farming bots) | Comment-copying spam |
| Hashtag / slogan push | The same hashtag from ≥ 5 accounts on one video within an hour | Hashtag campaigns (Jakesch et al., 2021) |
| Co-timing network | Accounts that repeatedly comment within the same minute on the same videos, across ≥ 2 videos | Pacheco et al. (2021); Giglietto et al. (2020) |
| Burst | Comments in a 10-minute bin far above the video's normal rate | Temporal anomaly detection (Kirdemir et al.) |
| New account | Channel created < 30 days before the comment | Account-level bot features (Cresci, 2020) |
| Batch-created accounts | ≥ 5 commenters on a case whose channels were created on the same recent day | Group-level detection (Cresci, 2020) |
| Auto handle | YouTube's `@user-xxxx` or name+digits handles | Account-level features |

**How flags become categories.** No single signal labels an account, because organic virality can produce
any one of them. An account is `likely_coordinated` only with a coordination signal **plus** an account red flag,
or two independent coordination signals; `commercial_spam` for commercial patterns or copying by a red-flag
account; `uncertain` for one weak signal; otherwise `organic`.

**How we make sure it works** (following the warnings in Cresci et al., 2023, about hyped bot-detection results):
1. **Chance check:** the co-timing signal is rerun on data where authors are shuffled within each video;
   `coordination_null.csv` reports how many accounts would be flagged by chance. If that share is not small,
   the window is tightened.
2. **Sensitivity check:** `--sensitivity` reruns everything across a grid of thresholds. A result that only
   appears at one setting is not reported as a finding.
3. **Human validation:** coders judge a stratified sample (`looks_inauthentic` in the coding sheet), and
   `--validate` reports how often humans agree with each category. This precision figure is reported.
4. **Results with and without flagged comments:** comment themes are reported for organic comments, and the
   share of hostility coming from non-organic accounts is reported separately.

**Limits.** YouTube already removes much spam before we see it; deleted accounts and comments are invisible;
the API gives no IP or device data, so a determined campaign using aged, real-looking accounts can pass. The flags
are therefore evidence of coordination, never proof, and the case file says so.

**Ethics:** only public comments; no usernames or IDs in any committed file; quotes paraphrased so they
cannot be searched back to the author; raw comment files stay git-ignored.


## Folder structure

```
README.md                   the single guide: project, method, codebook, previous work, decisions
cases/
  _template.md              the frozen template
  <case_id>/                one folder per final case (24), created from the template
    case.md                 the full case analysis
    sources.md              searches and numbered source list with dates accessed
analysis/
  case_pool.csv             all 45 candidates, final yes/no, reason
  case_pool_summary.md      how the list was built; balance; matched pairs; reserves
  final_cases.csv           the 24 final cases
  assignments.md            who owns and who verifies each case
  clips.md                  links to watch and transcribe for every case
  first_read.csv            owners' first reads, made before reading the AI draft
  comparison.csv            master comparison table, one row per case
  mechanisms.csv            lens verdicts from section H of every case
  news_coding.csv           framing codes for 6–10 news articles per case
  findings.md               cross-case findings (Step 6)
data/
  cases.csv, events.csv, videos.csv   earlier case, event and video tables (case_pool.csv supersedes cases.csv)
  comments/                 downloaded and sampled comments    (git-ignored, contains IDs)
  transcripts/              transcripts of the clips (git-ignored)
  raw/, processed/          outputs of src/ scripts            (git-ignored)
src/
  collect.py                download YouTube comments and commenter account data
  spam.py                   spam and coordination audit, chance check, sensitivity, validation
  sample.py                 coding sheets and Cohen's kappa
  news.py                   optional GDELT news-coverage timing
tests/                      tests for src/ on synthetic data (python -m pytest -q)
```

Case IDs follow the pattern `<comedian>_<year>` (e.g. `kamra_2025`).


## Open questions

To be settled in Step 0 or as noted.

1. ~~Approve the main question and sub-questions~~ Settled: approved with topic as the focus (PROJECT.md §3).
2. ~~Does the supervisor need to approve the change in method?~~ Settled: no. The original proposal no longer binds us; a short update is optional.
3. **Deadline.** Presentation on 14–15 November 2026 (PLAN.md, Timeline). Final paper deadline still to be confirmed.
4. **Number of cases:** 20, 25 or 30? (Recommended: 25.)
5. ~~Sacred-objects list~~ Settled: family and parents count.
6. **Bundled or non-stand-up cases:** keep `disability_sc_2025` as one case or split it; keep `tangade_dalit`, which is a pattern of trolling rather than one incident?
7. ~~Languages~~ Settled: everyone reads Hindi and English (see PROJECT.md §14).
8. ~~Interviews~~ Settled: not done (no time).
9. ~~Course AI policy~~ Settled: unlimited AI use allowed.
10. ~~Havish's pipeline work~~ Settled: kept or dropped as in PLAN.md, Folder structure.


## Timeline

### Presentation sprint: 9–15 November 2026

The first deliverable is a **presentation on 14–15 November**. The team aims to take **all 24 cases** through the
workflow before it, so the presentation can show real cross-case results.

| Date | Work | Milestone |
|---|---|---|
| Sun 9 – Mon 10 | Everyone reads PROJECT.md, PLAN.md and LITERATURE.md; short team meeting on the remaining open questions; API keys set up | Plan agreed |
| Sun 9 – Mon 10 | AI collects comments for all cases and runs the spam audit; AI drafts `latent_2025` as the pilot; team reviews it and fixes the template | Template frozen |
| Mon 10 – Wed 12 | AI drafts the other 23 cases; each owner watches the full clips, pastes the transcripts and writes a first read before checking their 6; each verifier fact-checks their 6 (`analysis/assignments.md`, `analysis/clips.md`) | All cases `verified` |
| Wed 12 – Thu 13 | Fill `comparison.csv` and `mechanisms.csv`; cross-case comparison (Step 6) into `findings.md`; build the slides | Findings and slides drafted |
| Fri 14 | Rehearse; fix slides | Ready to present |
| 14–15 Nov | **Presentation** | |

**Suggested slides (about 12–15):** the puzzle (*Latent* and the Rs 370 biryani clip); research question and
sub-questions; key concepts; framework and interpretive toolkit; previous work and the gap; how previous work
shapes our method; research design and case selection; the 24 cases and matched pairs; the per-case workflow and
template; verification and reliability; cross-case results (patterns, matched pairs, typology, organic vs organised
outrage); what comes next and final outputs;
limitations.

### Full project

Weeks counted from after the presentation. Adjust once the final paper deadline is known.

| Week | Steps | Milestone |
|---|---|---|
| 1 | Step 0, Step 1, Step 2 | Plan agreed; API key working; final case list chosen |
| 2 | Step 3, Step 4 | Template frozen after the pilot case |
| 3–5 | Step 5 (about 8 cases per week across the team) | All cases `final` |
| 5–6 | Step 6 | `findings.md` complete |
| 7 | Step 8 | Paper draft |
| 8 | Step 8 | Final paper, slides, repository cleaned |


## Glossary

- **API:** a service that lets a program request data directly (here, YouTube comments) instead of a person copying it.
- **Case:** one controversy, the unit we analyse and compare.
- **Cohen's kappa:** a score for how much two coders agree beyond chance (1 = perfect, 0 = chance level; 0.6–0.8 is usually considered good).
- **FIR:** First Information Report, the document that opens a police case in India.
- **Matched pair:** two cases that are alike in most respects but differ in one, so the difference can be studied.
- **QCA:** Qualitative Comparative Analysis, a method for finding which combinations of conditions go with an outcome across a small number of cases. Used here only as an optional visual check.
- **Structured, focused comparison:** asking the same set of questions of every case, focused on the research question, so that cases can be compared (George & Bennett, 2005).
- **Typology:** a set of recurring types, here recurring paths a controversy can take.
