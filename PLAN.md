# Project Plan: Structured Comparative Case Study — Team K

**Status:** proposed, awaiting team agreement (written 2026-11-03)
**Supersedes:** the *methodology* (Section 5) and *deliverables* (Section 6) of `Sociology_Proposal_Revised.docx`.
The *conceptual framework* (Section 2) of that proposal is kept and reused.

This document is meant to be read by any team member or AI assistant picking up the project cold.
It explains what has happened so far, what we are going to do, exactly how each step works, what each
step produces, and what the known limitations and open questions are.

---

## Contents

1. [Background: how we got here](#1-background-how-we-got-here)
2. [Why we are changing the approach](#2-why-we-are-changing-the-approach)
3. [Research question](#3-research-question)
4. [Conceptual framework (summary)](#4-conceptual-framework-summary)
5. [Method in one page](#5-method-in-one-page)
6. [Data sources: what, how, and limits](#6-data-sources-what-how-and-limits)
7. [Who does what: AI and humans](#7-who-does-what-ai-and-humans)
8. [Verification rules](#8-verification-rules)
9. [The steps, in detail](#9-the-steps-in-detail)
10. [Comment-reading protocol](#10-comment-reading-protocol)
11. [Folder structure for the new work](#11-folder-structure-for-the-new-work)
12. [What happens to the existing repository](#12-what-happens-to-the-existing-repository)
13. [Limitations](#13-limitations)
14. [Open questions and decisions still needed](#14-open-questions-and-decisions-still-needed)
15. [Timeline](#15-timeline)
- [Appendix A: Case template](#appendix-a-case-template)
- [Appendix B: Starting case pool](#appendix-b-starting-case-pool)
- [Appendix C: Definitions quick reference](#appendix-c-definitions-quick-reference)
- [Appendix D: Glossary](#appendix-d-glossary)

---

## 1. Background: how we got here

| Stage | What happened |
|---|---|
| **Original proposal** (`Sociology_Proposal_25e2c07a2c042fbbc1c92091ea1ca304.docx`) | Titled *"How Online Outrage Against Indian Dark Comedy Escalates"*. Three research questions: range of reactions to dark comedy (RQ1), legal vs extra-legal escalation (RQ2), whether online outrage represents wider opinion (RQ3). No methodology section; "dark comedy" not defined. |
| **Supervisor feedback** | *"What is dark comedy? Read on sociology of stigma. How do you treat context? Think through the idea of context collapse. Read on Durkheim."* |
| **Revised proposal** (`Sociology_Proposal_Revised.docx`, Havish, 2026-11-02) | Added a conceptual framework answering every feedback point (dark comedy defined; stigma; four layers of context; collusion vs collision; Durkheim). Widened the scope from dark comedy to all comedy genres, with genre recorded per joke. Added a large computational methodology: YouTube comment collection, bot/spam audit, hand-coding with kappa, a machine-learning classifier, reply-thread statistics, news lead-lag analysis, QCA, a 150–300-person survey and a dashboard. |
| **Code and data** (same commits) | 23 researched cases (`data/cases.csv`), 25 dated events (`data/events.csv`), 78 candidate YouTube videos (`data/videos.csv`), Python pipeline in `src/`, tests, and a dashboard showing demo (fake) numbers. **Nothing has been run on real data yet.** |

The proposal has already been submitted and graded. This plan is about **carrying out the project**.

---

## 2. Why we are changing the approach

The revised proposal's theory is strong, but its method had problems that make the results hard to trust
and hard to defend:

1. **Too much rests on comments.** Comments cannot explain *why* Munawar Faruqui was jailed while Kapil
   Sharma faced only online criticism. That depends on who complained, in which state, at what political
   moment, and whether the clip was resurfaced. Those facts come from news, statements and court records.
2. **The data did not fit the design.** Of 78 candidate videos, 51 are news-channel videos, whose commenters
   are news viewers, not the comedian's audience. One case (Parithabangal) holds about 70% of all comments;
   several cases have under 100. The "mid-range comedians have cleaner comment sections" argument and the
   "share of newcomers" measure of context collapse both break under these conditions.
3. **Scale for its own sake.** A classifier, QCA, bot detection, thread statistics, news time series, a survey
   and a dashboard in about eight weeks would mean doing every part halfway.
4. **Weak link between theory and evidence.** The supervisor asked for stigma, context and Durkheim. These
   are best applied by reading each case carefully, not by counting labels.

**New approach:** a **structured, focused comparison** (George & Bennett, 2005) of **20–30 cases**. Every case is
analysed in full depth using **the same template**, and then all cases are compared side by side.

---

## 3. Research question

### Main question (draft; team to approve in Step 0)

> **When a joke by an Indian comedian becomes a public controversy, why does it end so differently
> (online criticism only, legal action, extra-legal action, or both), and how do the joke's topic, its genre
> (especially dark comedy compared with satire, crude humour and roasts) and its context shape that outcome?**

### Sub-questions

| # | Sub-question | Theory it uses | Where the answer comes from |
|---|---|---|---|
| SQ1 | Which topics and genres appear in controversies, and does **dark comedy** draw different reactions or outcomes from satire, crude humour and roasts? | Definition of dark comedy; benign-violation theory | Template sections B and F across all cases |
| SQ2 | How does **context**, and especially context *collision* (someone else resurfacing or reframing a clip) vs *collusion* (the comedian publishing it), relate to how far a controversy escalates? | Goffman's frames; Marwick & boyd; Davis & Jurgenson | Template sections C and F |
| SQ3 | **Who mobilises, through which channel, and how do they frame the joke?** Is the comedian (and their venue or organisers) stigmatised? Was something treated as sacred, and *whose* sacred? | Goffman and Link & Phelan on stigma; Becker on labelling; Durkheim on the sacred and punishment | Template sections D, E, G and H |

### Why the dark comedy focus stays

The supervisor's first question was *"What is dark comedy?"*. We answer it by defining dark comedy precisely
(Appendix C) and making it the **central comparison**: is dark comedy treated differently from other genres?
Political satire is **not** dark comedy under our definition (satire targets power; dark comedy draws its
laugh from something grave), so satire, crude humour and roasts serve as comparison groups. This keeps the
widened case set while still answering the supervisor directly.

### What we do *not* claim

All our cases are jokes that already became controversies. We therefore **cannot** say that a topic is
"risky" in general (that would need the jokes on the same topic that caused no trouble). We can say how
controversies differ from one another and what is associated with each outcome. See Limitation L1.

---

## 4. Conceptual framework (summary)

Full text is in Section 2 of `Sociology_Proposal_Revised.docx`. The parts every case analysis must apply:

**Dark comedy.** A joke is dark comedy when (1) its subject is grave (death, violence, suffering, disease or
disability, the sacred, or a stigmatised position in a hierarchy) **and** (2) the laugh comes *from* that
gravity rather than from merely mentioning it (Willinger et al., 2017). Benign-violation theory (McGraw &
Warren, 2010): humour needs a violation that also seems harmless; dark comedy sits closest to the point
where the violation stops seeming harmless, so we expect it to be most sensitive to context.

**Stigma.**
- Goffman (1963): stigma reduces a person "from a whole and usual person to a tainted, discounted one".
- Becker (1963), labelling: the backlash often relabels the *comedian* as deviant ("anti-Hindu", "anti-national", "obscene").
- Link & Phelan (2001): we use their components as an **escalation ladder**:
  1. labelling / stereotyping (in comments and statements)
  2. separation (boycott calls)
  3. status loss (cancelled shows, lost venues)
  4. discrimination (bans, arrests, violence)
- Courtesy stigma (Goffman): stigma spreading to venues and organisers.

**Context.** Four layers, each recorded per case:
- **Performance:** where, to whom, in what language and format
- **Circulation:** who moved the clip, when, with what caption; collusion vs collision; months between performance and controversy
- **Reception:** who reacted and how they framed it ("just a joke" vs "this is a crime")
- **Societal:** elections, recent events, other controversies at the time

**Durkheim.**
- The sacred is set apart and protected; joking about it is profanation.
- "We do not condemn an act because it is a crime; it is a crime because we condemn it."
- Punishment is a passionate collective reaction that reaffirms the group; deviance reveals moral boundaries.
- India is plural, so we always ask **whose** sacred was touched and who claimed to speak for the group.

**Sacred objects, fixed in advance** (to avoid circular reasoning, see L7): deities and religious symbols;
religious founders and texts; regional icons (e.g. Shivaji); Ambedkar; the nation, army, martyrs and flag;
the family and parents (a candidate, to be decided in Step 0). This list is set before outcomes are compared
and is changed only by recorded team decision.

---

## 5. Method in one page

| Item | Decision |
|---|---|
| Design | Structured, focused comparison of cases (George & Bennett, 2005), with paired comparisons of closely matched cases |
| Unit of analysis | One **case** = one controversy around one joke or set of jokes by one comedian (or group) at one time |
| Number of cases | **20–30.** Enough for several cases per genre and outcome type; few enough to analyse each in full |
| Depth | **Every** case is analysed in full using the template in Appendix A |
| Evidence per case | News reports, official statements, court and police records where reported, YouTube comments, manually copied Instagram comments, Reddit threads, the comedian's own statements |
| Comparison | One master comparison table, paired comparisons, pattern-finding across cases, a typology of escalation paths |
| Reliability | Two team members independently code the key judgements (genre, direction, collapse type, outcome, highest stigma step) for every case; disagreements are recorded and resolved |
| Optional | 3–6 short interviews with Hyderabad comedians or venue organisers (Step 7) |
| Dropped from the revised proposal | Machine-learning classifier, large-scale bot audit as a core result, reply-thread statistics, news lead-lag series, formal QCA as a heavy method, 150–300-person survey, dashboard as a deliverable |

---

## 6. Data sources: what, how, and limits

| Source | Used for | How we access it | Limits |
|---|---|---|---|
| **News reports** (national and regional) | Reconstructing what happened: dates, actors, FIRs, threats, responses | Web search; outlet websites | Outlets take sides; English national media over-represented; syndicated wire copy (PTI, ANI, IANS) repeated by many outlets counts as **one** source; paywalls; details conflict |
| **Official records** | FIR sections, court orders, police statements, commission letters | As quoted in news; court websites and legal news (Bar & Bench, LiveLaw) where available | Original documents often unavailable; we rely on reports of them |
| **YouTube** | Comments on the original clip, reuploads, the comedian's response, news coverage | Free YouTube Data API v3 via `src/collect.py` (needs an API key, see Step 1) | Originals often deleted; comments deleted by users or removed by YouTube are missing; news-channel commenters are not the comedian's audience |
| **Instagram** | Comments on reels where the clip or the response circulated | **Manually:** a team member opens the reel and copies the top 50–100 comments (or takes screenshots) | No free API for other people's posts; logged-out access is blocked; automated scraping breaks Instagram's terms, so we do not do it. The AI assistant cannot watch reels or open Instagram directly |
| **Reddit** (e.g. r/india, r/IndianStandUpComedy) | Longer public arguments about the controversy | Web; Reddit's limited free tier for non-commercial use (confirm current terms before relying on it) | Users skew urban, English-speaking and young |
| **X / Twitter** | Not used | Paid API (about US$0.005 per post read), no free tier for new developers | Out of budget; noted as a limitation |
| **Comedian's statements** | Apology, refusal or clarification; their account of events | Their own posts and videos; interviews reported in news | Self-serving by nature; treated as the comedian's framing, not fact |
| **Social Blade** | Subscriber counts at the time of the incident | Manual lookup at socialblade.com | History may be incomplete for small channels |
| **Interviews** (optional) | How comedians and venues experience and anticipate backlash | In person or by call, with consent | Small, convenience sample; Hyderabad only |

**The AI assistant cannot watch videos on any platform.** It can read captions or transcripts where they
exist, and it can read screenshots. Where the exact wording of a joke matters, a team member watches the
clip and writes down what was said.

---

## 7. Who does what: AI and humans

| Task | AI assistant | Team member |
|---|---|---|
| Find news, legal reports and Reddit threads | ✅ Main role | Spot-checks |
| Pull YouTube comments | ✅ Runs `src/collect.py` | Provides the API key |
| Copy Instagram comments | ❌ Cannot | ✅ Copies the top 50–100 into the case folder |
| Watch the clip and transcribe the joke | ❌ Cannot watch video | ✅ |
| Draft the full case analysis in the template | ✅ | — |
| Verify every fact against its sources | Drafts the source list | ✅ **Required** (see Section 8) |
| Independent second coding of key judgements | ❌ (the AI draft counts as coder 1) | ✅ A team member codes blind (see Step 5.5) |
| Read and theme comments | ✅ Drafts themes with example comments | ✅ Checks the themes against the comments |
| Cross-case comparison | ✅ Builds the table and proposes patterns | ✅ Decides which patterns hold and why |
| Final interpretation and writing | ✅ Drafts | ✅ Owns, edits and signs off |

**Disclosure.** The final paper's methodology will state: *"AI tools were used to gather sources, collect
public comments and draft case analyses. Every factual claim was verified by a team member against at least
two independent sources, and all interpretive conclusions were reviewed and agreed by the team."*
Check the course's AI policy before submission.

---

## 8. Verification rules

Every factual claim in a case file follows these rules.

1. **Two independent sources** for every important fact (dates, who complained, FIR sections, arrests,
   threats, cancellations, apologies). "Independent" means different organisations that did their own
   reporting. Five outlets reprinting the same PTI story count as **one** source.
2. **Confidence level** for every fact:
   - `confirmed`: two or more independent sources agree, or an official record is available
   - `reported`: only one source, or several that share one origin
   - `disputed`: sources disagree. Record **both** versions and which source says what. Do not pick one silently.
3. **Every claim links to its source** in the case file's source list, with the date accessed.
4. **Quotes of the joke** come from the clip itself (transcribed by a team member), a transcript, or a
   reliable quotation in news. Mark which.
5. **Framing is data, not fact.** When outlets describe the same event differently ("insulted Hindu gods"
   vs "allegedly made jokes"), record the framing in section E of the template; do not adopt either as fact.
6. **The verifier is a team member who did not draft the case.** They tick each fact as checked, or flag it.
   A case is not `final` until every important fact is `confirmed` or explicitly marked `reported` / `disputed`.

---

## 9. The steps, in detail

Each step lists its goal, what it needs, what to do, what it produces, and when it counts as done.

### Step 0: Team alignment

- **Goal:** the whole team, including Havish, agrees on this plan before work starts.
- **Do:**
  1. Everyone reads this file.
  2. Meeting (about 1 hour). Decide:
     - approve or edit the main question and sub-questions (Section 3)
     - confirm the target number of cases (20–30)
     - confirm the sacred-objects list (Section 4), especially whether "family and parents" counts
     - who owns which cases (Step 5)
     - whether to do the optional interviews (Step 7)
     - whether to tell the supervisor about the change (recommended; see the draft note below)
  3. Record the decisions in `DECISIONS.md` (date, decision, reason).
- **Draft note to the supervisor (optional):**
  > Following your feedback, we have defined dark comedy and built our framework on stigma, context collapse
  > and Durkheim. We are now carrying out a structured comparative case study of 20–30 Indian comedy
  > controversies, comparing dark comedy with satire, crude humour and roasts, and applying the framework to
  > each case through news, official records and public comments. We would welcome any comments on this direction.
- **Output:** `DECISIONS.md`.
- **Done when:** the questions above are decided and recorded.

### Step 1: Setup

- **Goal:** the tools and folders are ready.
- **Do:**
  1. **YouTube API key** (one team member, about 5 minutes):
     Google Cloud Console → create a project → APIs & Services → enable "YouTube Data API v3" →
     Credentials → Create credentials → API key. Copy `.env.example` to `.env` and paste the key after
     `YOUTUBE_API_KEY=`. Also set `ANON_SALT=` to any random string. **Never commit `.env`** (it is git-ignored).
  2. **Python environment:** `python -m venv .venv`, activate it, `pip install -r requirements.txt`.
  3. Create the folders in Section 11 (`cases/`, `data/comments/`, `data/manual/`, `analysis/`, `interviews/`).
  4. Copy Appendix A into `cases/_template.md`.
- **Free quota:** 10,000 units per day. One unit fetches up to 100 comments, so even the largest case
  (about 49,000 comments) needs only about 500–1,000 units. Quota is not a constraint.
- **Done when:** `python -m src.collect --video-ids <any id> --case-id test` downloads comments into `data/raw/`.

### Step 2: Build the case pool and select the cases

- **Goal:** a final list of 20–30 cases, chosen by written criteria so the selection cannot be called cherry-picking.
- **Do:**
  1. **Long-list (about 40 candidates).** Start from the 23 cases in `data/cases.csv` and the extra ideas in
     Appendix B. The AI assistant searches for further candidates. For each candidate, record:
     comedian, approximate date, topic, likely genre, likely outcome type, number of independent sources
     found, and whether a clip or comments are available.
  2. **Inclusion criteria** (a case must meet all):
     - (a) a joke or comic performance by an Indian comedian, or a clearly marked comparison case (TV show, sketch, college skit)
     - (b) covered by **at least two independent** news sources
     - (c) the controversy happened between 2018 and 2026
     - (d) enough material to fill the template (at minimum: a description of the joke, a dated timeline, the outcome)
  3. **Balance targets** (aim for, not rigid quotas):
     - **Genre:** at least 4 dark comedy cases; at least 3 each of satire, crude/shock and roast; a few observational or mixed
     - **Outcome:** at least 4 each of online-only, legal, extra-legal, and both. **Online-only cases that fizzled are essential** (they are the contrast that makes escalation explainable)
     - **Topic:** religion, caste (both directions), politics, gender and sexuality, regional or national icons, disability, celebrities, looks
     - **Audience size:** small, mid and large comedians
     - **Pairs:** keep the matched pairs (same comedian twice; same week, different route; caste joke up vs down)
  4. **Fill a selection matrix** (genre × outcome) and look for empty cells. Empty cells are informative,
     but if an empty cell is due to missing research rather than reality, search for a case to fill it.
  5. Team picks the final 20–30. Record rejected candidates and the reason (e.g. "only one source").
- **Output:** `analysis/case_pool.csv` (all candidates, with included yes/no and reason) and the final list in `DECISIONS.md`.
- **Done when:** the final list is agreed and the matrix has no empty cells that are only due to missing research.

### Step 3: Finalise the template

- **Goal:** one fixed template that every case follows exactly.
- **Do:** review Appendix A as a team. Add or remove fields now, **not later**. Changing the template after
  cases are written means rewriting them.
- **Output:** `cases/_template.md` (frozen; any later change recorded in `DECISIONS.md` and applied to all cases).
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
- **Output:** `cases/latent_2025/` complete, plus template fixes recorded in `DECISIONS.md`.
- **Optional:** a second pilot (`kamra_2025`) if the first shows big template changes.
- **Done when:** the template is adjusted and frozen.

### Step 5: Analyse every case, one by one

Each case goes through these sub-steps. The case owner (a team member) is responsible for the case reaching `final`.

| Sub-step | Who | What happens | Output |
|---|---|---|---|
| 5.1 Research | AI | Search news, legal reports, statements, Reddit. Build the dated timeline and source list. | `cases/<case_id>/sources.md` |
| 5.2 Joke wording | Team | Watch the clip (if available) and transcribe the key joke(s). If no clip exists, use the best reported quotation and say so. | Section B of `case.md` |
| 5.3 Comments | AI + team | AI pulls YouTube comments for up to 3 key videos; a team member copies Instagram comments where relevant. AI reads and themes them following Section 10. | `data/comments/<case_id>_*.csv` (git-ignored), themes in section E |
| 5.4 Draft | AI | Fill every section of the template, including the theory reading (section H). | `cases/<case_id>/case.md` (`status: draft`) |
| 5.5 Blind second coding | Team | A member who has **not** read the draft codes the key judgements from the sources alone: genre, topic, direction, form, collapse type, outcome type, highest stigma step, sacred object. | Row in `analysis/second_coding.csv` |
| 5.6 Verify | Team (not the owner if possible) | Check every fact against sources (Section 8); compare the second coding with the draft; resolve disagreements; record them. | `status: verified` |
| 5.7 Finalise | Case owner | Fix flagged items, update the master table. | `status: final`, row in `analysis/comparison.csv` |

- **Workload:** with 25 cases and 4 people, about 6 cases each to own and 6 to verify.
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
  2. **Agreement report:** share of cases where the blind second coding matched the draft on each
     judgement (and Cohen's kappa where the numbers allow, via `src/sample.py kappa`). Report it honestly.
  3. **Answer each sub-question:**
     - SQ1: compare dark comedy cases with satire, crude and roast cases on outcome and reaction framing
     - SQ2: compare collision cases with collusion cases on how far they escalated
     - SQ3: compare who mobilised, through which channel, how they framed the joke, and whether the comedian or venue was stigmatised; check the Durkheim expectations (Section 2.4 of the revised proposal)
  4. **Paired comparisons:** for each matched pair, write what differed and what stayed the same, and which
     difference best explains the different outcomes.
  5. **Typology of escalation paths:** group cases into recurring paths (e.g. *resurfaced clip → party
     complaint → FIR*; *live show → fan group → assault*; *online anger → apology → fizzled*).
  6. **Look for counter-examples:** for every pattern, list the cases that do not fit and explain them.
     A pattern with no counter-examples checked is not a finding.
  7. **Optional, simple QCA-style truth table:** cases × 4–5 conditions × outcome, as a visual check of
     which combinations go with which outcome. Not as a formal causal claim.
- **Output:** `analysis/comparison.csv`, `analysis/findings.md` (patterns, pairs, typology, counter-examples, agreement report), figures.
- **Done when:** each sub-question has an answer supported by named cases, with counter-examples addressed.

### Step 7 (optional): Interviews

- **Goal:** a view from inside the comedy scene that news and comments cannot give, especially on self-censorship.
- **Who:** 3–6 open-mic comedians, organisers or venue managers in Hyderabad.
- **Do:**
  1. Check with the supervisor whether ethics approval is needed.
  2. Prepare a short guide (about 20 minutes): Do you avoid certain topics? Which and why? Have you changed
     or dropped a joke after seeing a controversy? What happens differently in a club and online? Have you or
     your venue faced complaints?
  3. Get consent; offer anonymity; record notes (and audio only with permission).
  4. Summarise each interview and link the themes to the case findings.
- **Output:** `interviews/` (anonymised summaries only; no recordings in git).
- **Start early.** Scheduling takes time, so begin contacting people during Step 5.

### Step 8: Write up

- **Suggested structure of the final paper:**
  1. Introduction (puzzle, why it matters)
  2. Conceptual framework (dark comedy, stigma, context, Durkheim; from the revised proposal)
  3. Literature and gaps (trimmed from the revised proposal)
  4. Method (this plan's Sections 5–8, including the AI disclosure and limitations)
  5. Cases overview (table of all cases)
  6. Findings by sub-question, with paired comparisons and the typology
  7. Discussion: what the findings say about stigma, context collapse and Durkheim in a plural society
  8. Limitations
  9. Conclusion
  - Appendix: one-page summary of each case
- **Also:** presentation slides; a tidy repository.
- **Optional bonus:** rebuild the dashboard from `analysis/comparison.csv` as a visual case map.

---

## 10. Comment-reading protocol

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
  (fixed random seed so the sample can be reproduced). For Instagram, the top 50–100 shown by default,
  with the collection date recorded.
- For very large comment sections, the full set can still be searched for specific phrases
  ("hurt sentiments", "anti-national", "just a joke") to check how common a theme is.

**What to record for each read comment** (light version of `CODEBOOK.md` Part B):
- reaction: support · mock the offended · neutral · backlash · threat · demand legal action · spam
- frame: play ("it's just a joke") · serious ("this is not comedy", "hurting sentiments") · none
- target: comedian · joke · offended group · platform · state
- stigmatises the comedian: yes (attacks their religion, caste, region, gender) · no
- sacred object invoked: from the fixed list in Section 4, or none

**What goes into the case file:** the main themes, how often each appeared in the read sample, 2–3
**paraphrased** examples per theme (never usernames), and anything surprising.

**Optional quick check:** `src/spam.py` can be run on a case's downloaded comments to flag obvious
copy-paste campaigns. Treat its flags as a note in the case file, not as a finding.

**Ethics:** only public comments; no usernames or IDs in any committed file; quotes paraphrased so they
cannot be searched back to the author; raw comment files stay git-ignored.

---

## 11. Folder structure for the new work

```
PLAN.md                     this file
DECISIONS.md                dated log of team decisions (created in Step 0)
cases/
  _template.md              the frozen template (Appendix A)
  <case_id>/
    case.md                 the full case analysis
    sources.md              numbered source list with dates accessed
analysis/
  case_pool.csv             all candidates, included yes/no, reason
  second_coding.csv         blind second coding of key judgements
  comparison.csv            master comparison table, one row per case
  findings.md               cross-case findings
data/
  cases.csv, events.csv, videos.csv   existing tables (kept, updated as cases are finalised)
  comments/                 downloaded and sampled comments    (git-ignored, contains IDs)
  manual/                   manually copied Instagram comments (git-ignored)
  raw/, processed/          outputs of src/ scripts            (git-ignored)
interviews/                 anonymised interview summaries only
```

Case IDs follow the existing pattern `<comedian>_<year>` (e.g. `kamra_2025`).
`data/comments/` and `data/manual/` must be added to `.gitignore` in Step 1.

---

## 12. What happens to the existing repository

| Item | Decision | Reason |
|---|---|---|
| `Sociology_Proposal_Revised.docx`, Section 2 (framework) | **Keep** | Answers the supervisor's feedback; becomes Section 2 of the final paper and section H of the template |
| Revised proposal, Sections 5–6 (method, deliverables) | **Replaced** by this plan | See Section 2 |
| `CODEBOOK.md` Part A (joke labels) | **Keep** | Definitions for template section B |
| `CODEBOOK.md` Part B (comment labels) | **Keep, light use** | Used in the comment-reading protocol |
| `data/cases.csv`, `data/events.csv` | **Keep** | Starting point for the case pool and timelines |
| `data/videos.csv` | **Keep** | Starting list of videos for comment collection |
| `src/collect.py` | **Keep, use** | Downloads YouTube comments |
| `src/sample.py` | **Keep** | Its `kappa` command can report agreement in Step 6 |
| `src/spam.py` | **Optional** | Quick copy-paste check only |
| `src/threads.py`, `src/news.py`, `src/export_dashboard.py` | **Not used** | Belonged to the statistical design |
| `tests/` | **Not used** | Tests the unused pipeline on fake data |
| `dashboard/` | **Not used now** | Shows fake numbers; may be rebuilt as an optional bonus at the end |
| `.agent/` | **Unrelated** | Settings for an AI design tool; untracked, not part of the project |

Nothing is deleted. Unused parts simply stay in the repository.

---

## 13. Limitations

These go into the final paper's limitations section. Each lists what we do about it.

| # | Limitation | What it means | What we do |
|---|---|---|---|
| L1 | **Selection on the outcome** | Every case is already a controversy, so we cannot say how risky a topic is in general | Narrow claims to *differences among controversies*; include online-only cases that fizzled; say this openly |
| L2 | **Small number of cases** | 20–30 cases show patterns and mechanisms, not statistical proof | Present findings as patterns with named cases and counter-examples, not as causal effects |
| L3 | **News bias and gaps** | Outlets take sides; English national media dominate; regional coverage is thin; wire copy is repeated | Two independent sources rule; framing recorded as data; regional outlets searched where possible |
| L4 | **Survivorship of comments** | Deleted comments, removed spam and banned accounts are gone; older cases have lost more | Record collection dates; treat older cases' comments with extra caution |
| L5 | **Missing originals** | Many clips were taken down; comments then come from reuploads or news channels, whose audiences differ | Record the video type for every comment set; prefer the comedian's own videos |
| L6 | **Platform gaps** | No X/Twitter; Instagram only manually; WhatsApp mobilisation invisible | State it; use Instagram manual samples and Reddit where useful |
| L7 | **Risk of circular coding** | Deciding what is "sacred" after seeing the outcome would make the Durkheim test meaningless | Sacred-objects list fixed in advance (Section 4) |
| L8 | **Subjective judgements** | Genre, direction ("punching up/down") and collapse type involve interpretation | Written definitions (Appendix C); blind second coding; agreement reported |
| L9 | **AI errors** | The AI assistant can misread sources, mix up details or state something no source supports | Every fact verified by a team member against its sources (Section 8); AI use disclosed |
| L10 | **The AI cannot watch video** | Tone, delivery and audience laughter cannot be judged by the AI | A team member watches each available clip and transcribes the joke |
| L11 | **Languages** | Comments and clips are in Hindi, Hinglish, Marathi, Telugu, Tamil and others | AI can read most of these but may miss nuance or slang; a team member who reads the language checks themes where possible; state which cases lacked such a check |
| L12 | **Audience size is a weak proxy for fame** | YouTube subscribers understate TV and streaming stars (Kapil Sharma, Vir Das, Munawar Faruqui after Bigg Boss) | Use subscriber counts at the time of the incident (Social Blade), and add a note on other fame |
| L13 | **Mixed case types** | Some cases are not stand-up (TV, sketch, college skit) or bundle several comedians | Mark them as comparison cases; decide in Step 2 whether to split or drop bundled cases |
| L14 | **Not representative of opinion** | Comments, Reddit and interviews do not represent Indian public opinion | Never present them as such; original RQ3 (representativeness) is dropped |

---

## 14. Open questions and decisions still needed

To be settled in Step 0 or as noted.

1. **Approve the main question and sub-questions** (Section 3).
2. **Does the supervisor need to approve the change in method?** Is a resubmission or note expected? (Recommended: send the short note in Step 0.)
3. **Deadline.** The final submission date is not recorded in the repository. Fill it into Section 15.
4. **Number of cases:** 20, 25 or 30? (Recommended: 25.)
5. **Sacred-objects list:** confirm it, and decide whether family and parents count (relevant to India's Got Latent and Swati Sachdeva).
6. **Bundled or non-stand-up cases:** keep `disability_sc_2025` as one case or split it; keep `tangade_dalit`, which is a pattern of trolling rather than one incident?
7. **Languages:** who on the team reads which languages (Hindi, Telugu, Tamil, Marathi)?
8. **Interviews:** do them or not? Is ethics approval needed?
9. **Course AI policy:** confirm what disclosure is required.
10. **Havish's pipeline work:** agree as a team which parts are kept (Section 12).

---

## 15. Timeline

Relative to the start date agreed in Step 0. Adjust once the deadline is known.

| Week | Steps | Milestone |
|---|---|---|
| 1 | Step 0, Step 1, Step 2 | Plan agreed; API key working; final case list chosen |
| 2 | Step 3, Step 4 | Template frozen after the pilot case |
| 3–5 | Step 5 (about 8 cases per week across the team); start contacting interviewees | All cases `final` |
| 5–6 | Step 6; Step 7 interviews | `findings.md` complete |
| 7 | Step 8 | Paper draft |
| 8 | Step 8 | Final paper, slides, repository cleaned |

---

## Appendix A: Case template

Copy this into `cases/_template.md` in Step 1. Every case file uses exactly these headings.

```markdown
# <Case title>: <comedian>, <year>

case_id: <comedian_year>
status: draft | verified | final
owner: <team member>   drafter: <AI | name>   verifier: <team member>
last updated: <YYYY-MM-DD>

## A. Basic facts
- Comedian(s):
- Date of performance:            Date the controversy began:
- Venue / setting:                City / state:
- Platform where it first circulated:
- Language of the joke:
- Audience size at the time (subscribers, Social Blade, date checked):   tier: small | mid | large
- Other fame (TV, streaming, Bigg Boss, etc.):
- Comparison case (not stand-up)? yes / no

## B. The joke
- What was said (transcript or quotation):
- Source of the wording: clip watched by <name> | transcript | quoted in <source>
- Topic(s): religion | caste | gender_sexuality | family | politics_state | regional_national_icon |
  celebrity_public_figure | bodies_looks | death_violence_tragedy | disease_disability
- Genre(s): dark | satire_juvenalian | satire_horatian | crude_shock | roast | gallows | observational
- Why this genre (one or two sentences, using the definitions in Appendix C):
- Target:                  Direction: up | down | lateral | self | contested
- Form: standup_set | crowd_work | roast | sketch | song_parody | social_reply | tv_show | college_skit
- Main technique: irony_sarcasm | exaggeration | parody_impersonation | wordplay | story

## C. Context (four layers)
- Performance: who the original audience was; how clearly it was framed as comedy
- Circulation: collusion | collision | live_only
  - who first spread it beyond the original audience:
  - months between performance and controversy:
  - caption / title of the most-viewed circulating version: neutral | accusatory (quote it)
- Reception: who reacted; how far they were from the original audience (summary; detail in E)
- Societal: elections, recent related events, other controversies in the preceding month

## D. Timeline
| Date | Event | Actor type | Confidence | Sources |
|---|---|---|---|---|
Event types: performance, upload, resurfaced, viral, statement, complaint, fir, arrest, summons, court,
threat, vandalism, disruption, violence, cancellation, apology, refusal, release, resolution.
Actor types: comedian, fan_group, individual, party_worker, politician, religious_org, community_org,
police, court, commission, platform, venue, media.

## E. Reaction
- Who objected (organisations, politicians, communities) and their exact framing words:
- Who defended the comedian:
- How the media framed it (compare two or three outlets):
- Comments (Section 10 of PLAN.md):
  - videos / reels read, with type and collection date:
  - main themes, how often each appeared in the read sample, 2–3 paraphrased examples each:
  - play frame vs serious frame:
  - attacks on the joke vs attacks on the comedian's identity:
  - anything notable (copy-paste waves, sudden floods, language shifts):

## F. Outcome
- Outcome type: online_only | legal | extralegal | both
- Legal actions (complaint, FIR with sections, arrest, summons, court orders):
- Extra-legal actions (threats, vandalism, disruption, cancellation, assault):
- Highest stigma step reached: 1 labelling/stereotyping | 2 separation (boycott) | 3 status loss | 4 discrimination (ban, arrest, violence)
- Courtesy stigma (venue, organiser, platform, co-performers affected)? yes / no, details:
- How it ended:

## G. Comedian's response
- Response: apology | refusal | clarification | deletion | silence | combination
- When (relative to the escalation):
- Did the response change the course of events? Evidence:

## H. Theory reading
- Stigma: was the comedian labelled as deviant? With what label? Did the comedian's own identity matter?
  Did stigma spread to others?
- Context collapse: what changed in the joke's meaning as it travelled? Collusion or collision, and did that matter?
- Durkheim: was a sacred object (fixed list) touched? Whose sacred? Who claimed to speak for the group?
  Was the reaction formal punishment (state) or passionate collective reaction (crowd)?
- Dark comedy: if this is dark comedy, did its gravity make it more fragile out of context? If not, how did its genre matter?

## I. Comparison notes
- Matched pair(s): which cases this should be compared with, and why
- What this case adds to the overall comparison

## J. Sources and confidence
Numbered list in `sources.md`: outlet, title, date published, URL, date accessed, independent of which others.
Unresolved disputes:
Open questions about this case:
```

---

## Appendix B: Starting case pool

### Already researched (from `data/cases.csv`)

| case_id | Comedian | Year | Topic | Likely genre | Outcome |
|---|---|---|---|---|---|
| agrima_2020 | Agrima Joshua | 2020 | regional icon | satire (borderline dark) | both |
| fernandes_2024 | Daniel Fernandes | 2024 | religion (Jain) | dark | extra-legal |
| fernandes_2025 | Daniel Fernandes | 2025 | national trauma (Pahalgam) | dark; satire | legal (private notice) |
| more_2025 | Pranit More | 2025 | celebrity | roast | extra-legal |
| more_2026 | Pranit More | 2026 | gender | crude (crowd work) | legal |
| sachdeva_2025 | Swati Sachdeva | 2025 | gender / family | crude | online only |
| sachdeva_reservation | Swati Sachdeva | 2023? | caste | dark | online only |
| katikala_2026 | Anudeep Katikala | 2026 | politics | satire; crude | legal |
| rafiq_2026 | Rafiq (Visakhapatnam) | 2026 | politics | satire? | legal |
| sarat_2026 | Sarat Uday | 2026 | politics | satire | extra-legal |
| shah_2021 | Neville Shah | 2021 | caste (down) | dark | online only |
| gaur_2021 | Shubham Gaur | 2021 | caste, religion, gender | crude | online only |
| parithabangal_2025 | Gopi & Sudhakar | 2025 | caste (up) | dark; satire | legal |
| jain_univ_2023 | Jain University students | 2023 | caste (down) | dark; crude | legal |
| tangade_dalit | Ankur Tangade and others | c. 2022–23 | caste (up) | satire | extra-legal |
| munawar_2021 | Munawar Faruqui | 2021 | religion | dark (alleged) | both |
| rajwani_2018 | Masoom Rajwani | 2018 | religion | unknown | extra-legal |
| bharti_2022 | Bharti Singh | 2022 | religion (Sikh) | crude; observational | legal |
| virdas_2021 | Vir Das | 2021 | politics / nation | satire; dark | both |
| kamra_2025 | Kunal Kamra | 2025 | politics | satire | both |
| latent_2025 | Samay Raina / Ranveer Allahbadia | 2025 | gender / family | crude | legal |
| disability_sc_2025 | Samay Raina and four others | 2025 | disability | dark; crude | legal |
| kapil_2024 | Kapil Sharma | 2024 | looks | roast | online only |

Status, sources and details for each are in `data/cases.csv`. Several fields there are still `TODO`
(subscriber counts at the time of the incident, technique, some dates); these are filled during Step 5.

### Ideas to check in Step 2 (not yet verified; may not meet the criteria)

- Kunal Kamra and the Supreme Court contempt proceedings over his tweets (2020)
- Kunal Kamra's online dispute with Ola Electric's founder (2024), a possible online-only case
- Munawar Faruqui's remark about Konkani people (2024) and the apology that followed
- Abish Mathew and others in the May 2021 call-out wave that followed the Neville Shah clip
- Saloni Gaur ("Nazma Aapi") political satire videos
- Shyam Rangeela's Modi impressions (check whether any incident falls inside 2018–2026)
- Further dark comedy cases (jokes on death, disability, tragedy) that drew **little or no** backlash, to balance the genre comparison
- Further regional-language cases (Tamil, Telugu, Kannada, Malayalam, Bengali, Marathi)

**Gaps in the current pool to fill in Step 2:**
- only one case each for regional icon, national trauma and looks
- few clearly dark comedy cases with online-only outcomes
- the 2018–2019 period has a single case

---

## Appendix C: Definitions quick reference

Full definitions, decision rules and sources are in `CODEBOOK.md`.

| Term | Definition |
|---|---|
| **Dark comedy** | Grave subject **and** the laugh comes *from* that gravity (Willinger et al., 2017) |
| **Satire** (Juvenalian / Horatian) | Humour aimed at people or institutions with power; biting (Juvenalian) or gentle (Horatian) (Holbert et al., 2011) |
| **Crude / shock** | Transgression mainly for shock: sex, bodily functions, obscenity |
| **Roast** | Mocks a particular person |
| **Gallows humour** | Dark humour by or for people who are themselves suffering or oppressed (Obrdlik, 1942) |
| **Observational** | Everyday-life humour with no taboo subject |
| **Punching up / down** | The target has more / less power than the speaker, judged against **local** hierarchies (caste, majority vs minority religion, state power) |
| **Collusion** | The comedian deliberately puts the material in front of wider audiences (e.g. uploading a special) (Davis & Jurgenson, 2014) |
| **Collision** | Audiences are merged without the comedian's involvement (e.g. a third party resurfaces an old clip with a hostile caption) |
| **Legal action** | Police complaint, FIR, arrest, summons, court case, commission action, formal legal notice |
| **Extra-legal action** | Threats, vandalism, show disruption, forced cancellation, assault, forced apology by non-state actors |
| **Stigma ladder** | 1 labelling/stereotyping → 2 separation (boycott) → 3 status loss (cancellations) → 4 discrimination (bans, arrests, violence) (Link & Phelan, 2001) |
| **Courtesy stigma** | Stigma that spreads to people associated with the stigmatised person, such as venues and organisers (Goffman, 1963) |
| **Sacred (Durkheim)** | What a group sets apart and protects with prohibitions; see the fixed list in Section 4 |

---

## Appendix D: Glossary

- **API:** a service that lets a program request data directly (here, YouTube comments) instead of a person copying it.
- **Case:** one controversy, the unit we analyse and compare.
- **Cohen's kappa:** a score for how much two coders agree beyond chance (1 = perfect, 0 = chance level; 0.6–0.8 is usually considered good).
- **FIR:** First Information Report, the document that opens a police case in India.
- **Matched pair:** two cases that are alike in most respects but differ in one, so the difference can be studied.
- **QCA:** Qualitative Comparative Analysis, a method for finding which combinations of conditions go with an outcome across a small number of cases. Used here only as an optional visual check.
- **Structured, focused comparison:** asking the same set of questions of every case, focused on the research question, so that cases can be compared (George & Bennett, 2005).
- **Typology:** a set of recurring types, here recurring paths a controversy can take.

### References added by this plan

- George, A. L., & Bennett, A. (2005). *Case studies and theory development in the social sciences*. MIT Press.

All other references are listed in `Sociology_Proposal_Revised.docx`.
