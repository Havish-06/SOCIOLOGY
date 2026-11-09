# Project Plan: Structured Comparative Case Study — Team K

**Status:** adopted 2026-11-08 (written 2026-11-03; research question revised to focus on joke topic, see `DECISIONS.md`)
**Supersedes:** the *methodology* (Section 5) and *deliverables* (Section 6) of the revised proposal (removed from the repository; in git history).
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
11. [Folder structure](#11-folder-structure)
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
| **Original proposal** (`Sociology_Proposal_25e2c07a2c042fbbc1c92091ea1ca304.docx`, removed; in git history) | Titled *"How Online Outrage Against Indian Dark Comedy Escalates"*. Three research questions: range of reactions to dark comedy (RQ1), legal vs extra-legal escalation (RQ2), whether online outrage represents wider opinion (RQ3). No methodology section; "dark comedy" not defined. |
| **Supervisor feedback** | *"What is dark comedy? Read on sociology of stigma. How do you treat context? Think through the idea of context collapse. Read on Durkheim."* |
| **Revised proposal** (`Sociology_Proposal_Revised.docx`, Havish, 2026-11-02; removed, in git history) | Added a conceptual framework answering every feedback point (dark comedy defined; stigma; four layers of context; collusion vs collision; Durkheim). Widened the scope from dark comedy to all comedy genres, with genre recorded per joke. Added a large computational methodology: YouTube comment collection, bot/spam audit, hand-coding with kappa, a machine-learning classifier, reply-thread statistics, news lead-lag analysis, QCA, a 150–300-person survey and a dashboard. |
| **Code and data** (same commits) | 23 researched cases (`data/cases.csv`), 25 dated events (`data/events.csv`), 78 candidate YouTube videos (`data/videos.csv`), Python pipeline in `src/`, tests, and a dashboard showing demo (fake) numbers. **Nothing has been run on real data yet.** |
| **Video review and fixes** (2026-11-04) | 73 videos confirmed and 5 rejected in `data/videos.csv`; date-parsing and anonymisation fixes in `src/` |
| **This plan** (2026-11-03 to 11-08) | Proposed as a case study; research question changed from dark comedy to **joke topic** (genre kept as a secondary variable); supervisor confirmed the original proposal no longer binds us; plan adopted |
| **Previous work** (2026-11-08) | `LITERATURE.md` reviews humour studies and comedy-controversy research and maps each study onto our method; the borrowed fields were added to the case template |

The proposal has already been submitted and graded, and the supervisor has said we are free to choose our
direction. This plan is about **carrying out the project**.

**Why this topic.** Two controversies led us here: *India's Got Latent* (2025), where one remark brought FIRs in
several states, the removal of every episode and the Supreme Court, and Pranit More's "Rs 370 biryani" crowd
work (2026), where a short clip from a Gurugram room became a women's-commission complaint and an FIR. Both are
in the case pool; *Latent* is the suggested pilot.

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

### Main question

> **Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a
> controversy, why does it end so differently (online criticism only, legal action, extra-legal action,
> or both)? How do the joke's topic, its target and its context shape that outcome?**

### Sub-questions

| # | Sub-question | Theory it uses | Where the answer comes from |
|---|---|---|---|
| SQ1 | Which **topics** (religion, caste, politics and the nation, gender and sexuality, regional icons, disability, and others) appear in controversies, and do the topic and the direction of the joke (punching up or down) go with different reactions and outcomes? Genre (dark comedy, satire, crude humour, roast) is recorded for every joke and checked as a secondary factor. | Durkheim on the sacred; benign-violation theory; punching up/down | Template sections B and F across all cases |
| SQ2 | How does **context**, and especially context *collision* (someone else resurfacing or reframing a clip) vs *collusion* (the comedian publishing it), relate to how far a controversy escalates? | Goffman's frames; Marwick & boyd; Davis & Jurgenson | Template sections C and F |
| SQ3 | **Who mobilises, through which channel, and how do they frame the joke?** Is the comedian (and their venue or organisers) stigmatised? Was something treated as sacred, and *whose* sacred? | Goffman and Link & Phelan on stigma; Becker on labelling; Durkheim on the sacred and punishment | Template sections D, E, G and H |

### Why topic, not genre, is the focus

The project asks what comedians are scrutinised *for*. A controversy is almost always about what a joke was
about and whom it touched (a deity, a caste group, a political leader, parents), not about its comic style.
Genre is still recorded for every joke using the definitions in Appendix C, so we can check whether, for
example, dark comedy behaves differently from satire on the same topic. But it is not the main comparison,
and the case list is not balanced by genre. Team decision, 2026-11-05 (see `DECISIONS.md`).

### What we do *not* claim

All our cases are jokes that already became controversies. We therefore **cannot** say that a topic is
"risky" in general (that would need the jokes on the same topic that caused no trouble). We can say how
controversies differ from one another and what is associated with each outcome. See Limitation L1.

---

## 4. Conceptual framework (summary)

Full text is in PROJECT.md Sections 4–5. The parts every case analysis must apply:

**Topic and genre.** The **topic** is what the joke is about and whom it touches (religion, caste, politics
and the nation, gender and sexuality, regional icons, disability, celebrities, looks); it is the main
variable. **Genre** (dark comedy, satire, crude/shock, roast, observational; Appendix C) is recorded as a
secondary variable. Benign-violation theory (McGraw & Warren, 2010): humour needs a violation that also seems
harmless, and what counts as harmless depends on the topic and on who is listening, which is why topic and
context are analysed together.

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
the family and parents (decided 2026-11-09). This list is set before outcomes are compared
and is changed only by recorded team decision.

### Interpretive toolkit

Stigma, context collapse and Durkheim are the core framework, but they are not the only lenses. We interpret
every case with whatever helps answer the research question, drawing on the full toolkit below. Sources and
detail: `LITERATURE.md`, stream 10.

| Lens | Question it asks of a case | Mainly helps with | Key sources |
|---|---|---|---|
| **Scandal** | Who turned a transgression into a public accusation, and how did publicity make it a scandal? Who gained and who lost? | SQ2, SQ3 | Adut (2008); Thompson (2000); Kuipers (2011) |
| **Moral panic and moral entrepreneurs** | Was the comedian cast as a "folk devil"? Was the reaction out of proportion? Who acted as moral entrepreneur? Did one panic set off a wave of cases? | SQ3; clustering of cases | Cohen (1972); Goode & Ben-Yehuda (1994); Becker (1963) |
| **Strategic offence ("hate spin")** | Was offence manufactured or amplified by political entrepreneurs for gain? Who claimed hurt, and who benefited? | SQ3; legal outcomes | George (2016); Nair (2023) |
| **Mobilisation: framing, resources, political opportunity** | Did the objectors have organisations, cadres and allies in power? Did an election or a friendly government open an opportunity? How did they frame the grievance? | SQ3; why some go to the police and others to the street | Benford & Snow (2000); McCarthy & Zald (1977); Tarrow (2011) |
| **Law as a weapon; "the process is the punishment"** | Was the legal route used to punish through FIRs, travel and court dates, even when the case later failed? | Legal outcomes | Feeley (1979); Bhatia (2016); Nair (2023) |
| **Digital nationalism and organised online publics** | Did organised online networks drive the backlash? Did they use humour and "fun" themselves? | SQ2, SQ3 | Udupa (2019); Udupa & Pohjonen (2019) |
| **Moral outrage and platforms** | Did moralised clips, captions and algorithms spread the outrage? Was the backlash norm enforcement? | SQ2 | Crockett (2017); Brady et al. (2017); Rost, Stahel & Frey (2016) |
| **Context collapse** | What changed in the joke's meaning as it travelled? Collusion or collision? | SQ2 | Marwick & boyd (2011); Davis & Jurgenson (2014) |
| **Stigma and labelling** | Was the comedian relabelled as deviant? How far up the stigma ladder did it go? Did it spread to venues? | SQ3 | Goffman (1963); Link & Phelan (2001); Becker (1963) |
| **Durkheim: the sacred, punishment, boundaries** | Was something sacred touched, and whose? Was the reaction formal (state) or passionate and collective (crowd)? | SQ1, SQ3 | Durkheim (1893, 1912); Erikson (1966) |
| **Humour theory** | Why did the joke stop seeming harmless for some audiences? Did its function shift from uniting to dividing? Which "humour regime" did it break? | SQ1, SQ2 | McGraw & Warren (2010); McGraw et al. (2012); Meyer (2000); Kuipers (2011) |
| **Identity and power: who may joke about whom** | Did the comedian's religion, caste, gender or region shape the reaction? Was the joke punching up or down? | SQ1, SQ3 | Krefting (2014); Shivaprasad (2020); Crenshaw (1991) |
| **Fandom and anti-fandom** | Was the backlash driven by fans defending a celebrity, or anti-fans of the comedian? | SQ3 (celebrity cases) | Gray (2003); Gray, Sandvoss & Harrington (2007) |
| **Apology and image repair** | Did the comedian's apology, refusal or deletion calm or inflame the controversy? | Comedian's response | Goffman (1971); Benoit (1995) |
| **Chilling effect** | What does the case teach other comedians about which topics to avoid? | Implications; interviews | Schauer (1978) |

**How we interpret, following earlier comparative case studies.**

1. **Process tracing within each case** (George & Bennett, 2005; Collier, 2011; Beach & Pedersen, 2013). The dated
   timeline is used to reconstruct *how* the controversy unfolded, step by step, and to check which lens's expected
   traces actually appear. For example, strategic offence predicts that a political actor resurfaces the clip and
   files the complaint; a moral panic predicts disproportionate media coverage and a wave of copycat complaints.
2. **Rival explanations for every case** (Yin, 2018). Each case is read against several lenses, and the case file
   records which ones the evidence supports, partly supports or contradicts. A lens is never assumed to fit.
3. **Analytic eclecticism** (Sil & Katzenstein, 2010). Controversies have several causes, so we combine lenses where
   the evidence demands it instead of forcing every case into one theory.
4. **Cross-case comparison of mechanisms.** In the comparison stage we ask which mechanisms recur with which outcomes
   (for example, whether "organised party cadres + political opportunity" goes with extra-legal action).

Earlier studies of this kind interpret cases in the same way: Cohen (1972) traces the stages of a moral panic;
Adut (2008) compares scandals by who made the accusation public; George (2016) compares offence campaigns across
India, Indonesia and the United States by who manufactured the offence and how the state responded; Kuipers (2011)
asks who won and lost in a humour scandal; Ödmark (2021) compares how the function of humour changed across three
controversies.

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
| Grounding in previous work | Design, template fields and comment codes are borrowed from earlier studies; the mapping is in `LITERATURE.md` ("How previous work shapes our methodology") |
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

### News protocol

News articles do two jobs, and we keep them apart:
1. **Evidence of what happened** (dates, who complained, FIR sections, arrests, threats, apologies). Facts need
   two independent sources (Section 8).
2. **Data on how the controversy was framed.** How outlets described the joke and the comedian is itself a
   finding (Entman, 1993; Semetko & Valkenburg, 2000; Ödmark, 2021), so framing is coded, not adopted.

**Which outlets.** English-language coverage is enough for every case. Search across these types so that no single kind of outlet sets the story:

| Type | Examples |
|---|---|
| National English dailies and TV sites | The Hindu, The Indian Express, Hindustan Times, The Times of India, NDTV |
| Digital-native outlets | Scroll, The Print, The News Minute, The Wire, Newslaundry, The Quint |
| Legal news | LiveLaw, Bar & Bench (FIRs, court orders) |
| Outlets with an explicit editorial stance | At least one outlet from each side of the political debate where the case was covered, to see opposing frames |
| *Optional:* Hindi or regional press | Only where it adds a frame the English outlets miss (e.g. Dainik Bhaskar, Amar Ujala; Punjabi papers for a Sikh case, read by Siddanth) |

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
The course allows unlimited AI use; the disclosure is kept for transparency.

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
     - who owns which cases (Step 5)
     - whether to do the optional interviews (Step 7)
     - whether to send the supervisor a short update (optional; see the note below)
  3. Record the decisions in `DECISIONS.md` (date, decision, reason).
- **Note to the supervisor (optional; the supervisor has said the original proposal no longer binds us):**
  > We are carrying out a structured comparative case study of 20–30 Indian comedy controversies, asking which
  > topics bring stand-up comedians under scrutiny and why some controversies end in legal or extra-legal
  > action while others fizzle. Each case is interpreted with a toolkit of sociological lenses (stigma, context collapse, Durkheim, scandal, moral panic, mobilisation and others), using news,
  > official records and public comments.
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
     - **Topic (main):** at least 2–3 cases each for religion, caste (both directions), politics and the nation, gender and sexuality, and regional icons; at least one each for disability, celebrities and looks
     - **Outcome:** at least 4 each of online-only, legal, extra-legal, and both. **Online-only cases that fizzled are essential** (they are the contrast that makes escalation explainable)
     - **Genre (recorded, no quota):** note the spread of dark, satire, crude/shock, roast and observational; do not pick cases to fill genre slots
     - **Audience size:** small, mid and large comedians
     - **Pairs:** keep the matched pairs (same comedian twice; same week, different route; caste joke up vs down)
  4. **Fill a selection matrix** (topic × outcome) and look for empty cells. Empty cells are informative,
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

- **Workload:** with 24 cases and 4 people, 6 cases each to own and 6 to verify.
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
  1. Introduction: open with *India's Got Latent* and the Rs 370 biryani clip; the puzzle (why some jokes end
     in FIRs, some in mobs, some in nothing); why it matters
  2. Conceptual framework (topic and genre, stigma, context, Durkheim; adapted from the revised proposal)
  3. Literature and gaps (from `LITERATURE.md`), ending with how each stream is used in our method
  4. Method (this plan's Sections 5–8, including the AI disclosure and limitations)
  5. Cases overview (table of all cases)
  6. Findings by sub-question, with paired comparisons and the typology
  7. Discussion (led by the findings, not by a fixed list of theories):
     - restate the main answer in one paragraph
     - interpret each major finding: *why* it happens, using whichever lenses in the toolkit (Section 4) the
       evidence supports: scandal, moral panic, strategic offence, mobilisation, law as a weapon, organised online
       publics, platforms, context collapse, stigma, Durkheim, humour theory, identity and power, fandom, apology
       (e.g. whether different groups defend their "sacred" through different channels: party cadres, formal
       complaints, commissions), and saying so where a theory fails to predict
     - explain the counter-examples and surprises
     - relate to previous work (`LITERATURE.md`): where we agree with, extend or contradict it
     - rival explanations (elections, fame, platform, amount of news coverage)
     - implications: self-censorship, the state as referee or instrument, platforms and clipping
     - the limits of the interpretation (then the full limitations section)
  8. Limitations
  9. Conclusion
  - Appendix: one-page summary of each case
- **Also:** presentation slides; a tidy repository.
- **Optional bonus:** rebuild the dashboard from `analysis/comparison.csv` as a visual case map.

---

## 10. Comment-reading protocol

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
| **Whether the outrage was organic or organised** | Strategic-offence and online-publics lenses: was the backlash a spontaneous public reaction, or pushed by coordinated accounts? |

The last row is why spam and coordination detection matters. If a large share of hostile comments come from
copy-paste campaigns, batch-created accounts or accounts acting in lockstep, that is evidence that offence was
**manufactured or amplified** (George, 2016; Jakesch et al., 2021), not just felt. If the hostility is organic,
the "manufactured offence" explanation is weakened for that case. Either result is a finding.

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
- norm invoked: religious feeling · national honour · women's dignity · family/parents · caste dignity · decency · leader's honour · none (Rost et al., 2016)
- intent attributed to the comedian: meant harm · meant it as a joke · not stated (Graefer & Das, 2020: audiences judge offence by inferred intent)

**What goes into the case file:** the main themes, how often each appeared in the read sample, 2–3
**paraphrased** examples per theme (never usernames), and anything surprising.

**Spam and coordination detection (`src/spam.py`).** Run on every case's comments before any comment is read,
counted or quoted. Methods follow the coordination-detection literature (`LITERATURE.md`, stream 11):

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

---

## 11. Folder structure

```
README.md                   front page: what the project is, where to start
PROJECT.md                  the whole project in one document
PLAN.md                     this file: step-by-step instructions
DECISIONS.md                dated log of team decisions
LITERATURE.md               previous work and how it shapes the method
CODEBOOK.md                 joke and comment labels with decision rules
cases/
  _template.md              the frozen template (Appendix A)
  <case_id>/                one folder per final case (24), created from the template
    case.md                 the full case analysis
    sources.md              searches and numbered source list with dates accessed
analysis/
  case_pool.csv             all 45 candidates, final yes/no, reason
  case_pool_summary.md      how the list was built; balance; matched pairs; reserves
  final_cases.csv           the 24 final cases
  second_coding.csv         blind second coding of key judgements
  comparison.csv            master comparison table, one row per case
  mechanisms.csv            lens verdicts from section H of every case
  news_coding.csv           framing codes for 6–10 news articles per case
  findings.md               cross-case findings (Step 6)
data/
  cases.csv, events.csv, videos.csv   earlier case, event and video tables (case_pool.csv supersedes cases.csv)
  comments/                 downloaded and sampled comments    (git-ignored, contains IDs)
  manual/                   manually copied Instagram comments (git-ignored)
  raw/, processed/          outputs of src/ scripts            (git-ignored)
src/
  collect.py                download YouTube comments and commenter account data
  spam.py                   spam and coordination audit, chance check, sensitivity, validation
  sample.py                 coding sheets and Cohen's kappa
  news.py                   optional GDELT news-coverage timing
tests/                      tests for src/ on synthetic data (python -m pytest -q)
interviews/                 anonymised interview summaries only (optional)
```

Case IDs follow the pattern `<comedian>_<year>` (e.g. `kamra_2025`).

---

## 12. What happens to the existing repository

| Item | Decision | Reason |
|---|---|---|
| Revised proposal, Section 2 (framework) | **Reused** in PROJECT.md and the template; file removed | Answers the supervisor's feedback |
| Revised proposal, Sections 5–6 (method, deliverables) | **Replaced** by this plan; file removed | See Section 2 |
| Original proposal | Removed | Superseded |
| `CODEBOOK.md` | **Use** | Part A for template section B; Part B for reading comments |
| `data/cases.csv`, `data/events.csv` | **Keep** | Starting point for timelines; `analysis/case_pool.csv` supersedes `cases.csv` |
| `data/videos.csv` | **Use** | Starting list of videos for comment collection |
| `src/collect.py` | **Use** | Downloads YouTube comments |
| `src/spam.py` | **Use, every case** | Spam and coordination audit before comments are read (Section 10) |
| `src/sample.py` | **Use** | Coding sheets; kappa for the agreement report |
| `src/news.py` | **Optional** | GDELT coverage timing per case (Section 6, news protocol) |
| `tests/` | **Use** | Tests the tools above on synthetic data |
| `src/threads.py`, `src/export_dashboard.py` | Removed | Belonged to the earlier statistical design |
| `dashboard/` | Removed | Showed demo numbers; a visual case map can be built from `analysis/comparison.csv` as an optional bonus |

Removed files (both proposals, the dashboard, the thread analysis and its test, the dashboard exporter) remain in the
git history: `git checkout 32e24f1 -- archive/` restores them.

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
| L11 | **Languages** | Comments and clips are mostly in Hindi, Hinglish and English, with some Marathi, Telugu and Tamil | Everyone on the team reads Hindi and English, so most material is read directly; Tamil, Marathi and Telugu material is read with AI translation plus English coverage, and the case file says which material lacked a native-reader check |
| L12 | **Audience size is a weak proxy for fame** | YouTube subscribers understate TV and streaming stars (Kapil Sharma, Vir Das, Munawar Faruqui after Bigg Boss) | Use subscriber counts at the time of the incident (Social Blade), and add a note on other fame |
| L13 | **Mixed case types** | Some cases are not stand-up (TV, sketch, college skit) or bundle several comedians | Mark them as comparison cases; decide in Step 2 whether to split or drop bundled cases |
| L14 | **Not representative of opinion** | Comments, Reddit and interviews do not represent Indian public opinion | Never present them as such; original RQ3 (representativeness) is dropped |

---

## 14. Open questions and decisions still needed

To be settled in Step 0 or as noted.

1. ~~Approve the main question and sub-questions~~ Settled: approved with topic as the focus (Section 3).
2. ~~Does the supervisor need to approve the change in method?~~ Settled: no. The original proposal no longer binds us; a short update is optional.
3. **Deadline.** Presentation on 14–15 November 2026 (Section 15). Final paper deadline still to be confirmed.
4. **Number of cases:** 20, 25 or 30? (Recommended: 25.)
5. ~~Sacred-objects list~~ Settled: family and parents count.
6. **Bundled or non-stand-up cases:** keep `disability_sc_2025` as one case or split it; keep `tangade_dalit`, which is a pattern of trolling rather than one incident?
7. ~~Languages~~ Settled: everyone reads Hindi and English; Siddanth also Punjabi (see L11).
8. **Interviews:** do them or not? Is ethics approval needed?
9. ~~Course AI policy~~ Settled: unlimited AI use allowed.
10. ~~Havish's pipeline work~~ Settled: kept or dropped as in Section 12.

---

## 15. Timeline

### Presentation sprint: 9–15 November 2026

The first deliverable is a **presentation on 14–15 November**. It shows the plan, the framework, previous work
and early results from three pilot cases. The full project continues afterwards on the week plan below.

| Date | Work | Milestone |
|---|---|---|
| Sun 9 – Mon 10 | Everyone reads PROJECT.md, PLAN.md and LITERATURE.md; short team meeting on the remaining open questions; API keys set up | Plan agreed |
| Mon 10 – Wed 12 | Three pilot cases taken through the full workflow (Step 5): `latent_2025` and `more_2026` (the two cases that motivated the project) and `kamra_2025` (a politics case with both legal and extra-legal action, for contrast) | Three cases `final`; template fixes recorded |
| Wed 12 – Thu 13 | Early comparison of the three cases (what differs in topic, context, who mobilised, route, outcome); build the slides | Slides drafted |
| Fri 14 | Rehearse; fix slides | Ready to present |
| 14–15 Nov | **Presentation** | |

**Suggested slides (about 12–15):** the puzzle (*Latent* and the Rs 370 biryani clip); research question and
sub-questions; key concepts; framework and interpretive toolkit; previous work and the gap; how previous work
shapes our method; research design and case selection; the 24 cases and matched pairs; the per-case workflow and
template; verification and reliability; early results from the three pilot cases; what comes next and final outputs;
limitations.

### Full project

Weeks counted from after the presentation. Adjust once the final paper deadline is known.

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
  - setting: club | auditorium | college | online special | tv | social_post; ticketed? approx. audience size
    (Brodie 2014: stand-up licence rests on intimacy with a co-present audience)
  - language and register: English | Hindi/Hinglish | regional language (Kuipers 2006; Friedman 2014: humour taste marks class)
- Circulation: collusion | collision | live_only
  - who first spread it beyond the original audience:
  - months between performance and controversy:
  - caption / title of the most-viewed circulating version: neutral | accusatory (quote it)
- Reception: who reacted; how far they were from the original audience (summary; detail in E)
  - distance of the objectors (McGraw & Warren 2010; McGraw et al. 2012: a violation stops being benign when it is close):
    temporal (months since performance) | social (objectors are the target group | speak for the target group | third party)
- Societal: elections, recent related events, other controversies in the preceding month

## D. Timeline
| Date | Event | Actor type | Confidence | Sources |
|---|---|---|---|---|
Event types: performance, upload, resurfaced, viral, statement, complaint, fir, arrest, summons, court,
threat, vandalism, disruption, violence, cancellation, apology, refusal, release, resolution.
Actor types: comedian, fan_group, individual, party_worker, politician, religious_org, community_org,
police, court, commission, platform, venue, media.
- Days from first viral spread to peak attention:        to fading (Pfeffer et al. 2014: firestorms rise and fade fast)

## E. Reaction
- Who objected (organisations, politicians, communities) and their exact framing words:
- Norm the objectors said was broken (Rost et al. 2016: firestorms as norm enforcement; Durkheim):
  religious_feeling | national_honour | women_dignity | family_parents | caste_dignity | decency_obscenity | leader_honour | other
- Humour function, before and after travelling (Meyer 2000; Ödmark 2021):
  for the original audience: identification | clarification | enforcement | differentiation
  as framed by the objectors: identification | clarification | enforcement | differentiation
- Who defended the comedian:
- How the media framed it (6–10 articles across at least three outlet types, coded in `analysis/news_coding.csv`;
  PLAN.md Section 6, news protocol; Entman 1993; Semetko & Valkenburg 2000; Ödmark 2021):
  - who broke the story, and how the framing changed between the first week and the legal phase:
  dominant frame: hurt_sentiments | obscenity | insult_to_leader | free_speech | cancel_culture | legal_overreach | other
- Comments (Section 10 of PLAN.md):
  - videos / reels read, with type and collection date:
  - main themes, how often each appeared in the read sample, 2–3 paraphrased examples each:
  - play frame vs serious frame:
  - attacks on the joke vs attacks on the comedian's identity:
  - anything notable (copy-paste waves, sudden floods, language shifts):

## F. Outcome
- Outcome type: online_only | legal | extralegal | both
- Legal actions against the comedian (complaint, FIR with sections, arrest, summons, court orders; administrative
  action such as permission refused or venue sealed, marked `administrative`). Action against attackers goes in D only:
  - complainant, their affiliation, and whether they claimed to speak for a group (Nair 2023):
  - legal basis (Bhatia 2016): religious_offence (IPC 295A / BNS 299) | enmity_hate (IPC 153A / BNS 196) |
    obscenity (IT Act 67, IPC 292–294 / BNS 294–296) | defamation | sc_st_act | contempt | other
- Extra-legal actions (threats, vandalism, disruption, cancellation, assault, forced or pressured apology):
- Highest stigma step reached: 1 labelling/stereotyping | 2 separation (boycott) | 3 status loss | 4 discrimination (ban, arrest, violence)
- Courtesy stigma (venue, organiser, platform, co-performers affected)? yes / no, details:
- How it ended:
- Winners and losers (Kuipers 2011): who gained visibility, followers, votes or authority; who lost:

## G. Comedian's response
- Response: apology | refusal | clarification | deletion | silence | combination
- When (relative to the escalation):
- Did the response change the course of events? Evidence:
- Comedian's own narrative (Vásquez; Nicolaï & Maeseele 2024): contrition | defiance | humourless_audience |
  blames_clipping_or_social_media | free_speech | none

## H. Interpretation
Use the timeline (D) to trace how the controversy unfolded, then read the case against the interpretive toolkit
(PLAN.md Section 4). For each lens: **supported | partly | not supported | not relevant**, with the evidence.
Never assume a lens fits; record where it fails.

| Lens | Verdict | Evidence (with source numbers) |
|---|---|---|
| Scandal: who made the accusation public; winners and losers | | |
| Moral panic: folk devil, disproportion, moral entrepreneurs, wave of cases | | |
| Strategic offence: offence manufactured or amplified for political gain | | |
| Mobilisation: organisation, resources, political opportunity, framing | | |
| Law as a weapon: the process as punishment | | |
| Organised online publics / digital nationalism | | |
| Moral outrage and platform amplification | | |
| Context collapse: meaning change; collusion or collision | | |
| Stigma and labelling: label, ladder step, courtesy stigma | | |
| Durkheim: whose sacred; formal punishment vs collective reaction | | |
| Humour theory: why it stopped seeming harmless; function shift | | |
| Identity and power: comedian's publicly stated identity; up or down | | |
| Fandom / anti-fandom (celebrity cases) | | |
| Apology and image repair | | |
| Other explanation not in the toolkit | | |

- **Best explanation of this outcome** (one paragraph, combining lenses where needed):
- **Topic:** what made this topic sensitive here: a sacred object, a group's standing, a political leader? Did the
  genre (e.g. a dark joke's gravity, a roast's personal target) change how it travelled?
- **Rival explanations ruled out, and why:**

## I. Comparison notes
- Matched pair(s): which cases this should be compared with, and why
- What this case adds to the overall comparison

## J. Sources and confidence
Numbered list in `sources.md`: outlet, outlet type, title, date published, URL, date accessed, independent of which
others (wire copy counts once). Record the search terms and date of each search.
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
- Jokes on the most-scrutinised topics (religion, caste, politics) that drew **little or no** backlash, to sharpen the topic comparison
- Further regional-language cases (Tamil, Telugu, Kannada, Malayalam, Bengali, Marathi)

**Gaps in the current pool to fill in Step 2:**
- only one case each for regional icon, national trauma and looks
- few online-only cases on religion and politics
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
| **Legal action** | Action by the state or a statutory body **against the comedian**: police complaint, FIR, arrest, summons, court case, commission action, formal legal notice, and administrative action (permission refused, venue sealed, demolition; sub-label `administrative`). Police action against the comedian's attackers or threateners is not counted; it goes in the timeline |
| **Extra-legal action** | Threats, vandalism, show disruption, forced cancellation, assault, and forced or pressured apologies by non-state actors |
| **Comic performance** | A joke in a show, set, sketch, roast, TV programme or video. Tweets and social-media replies do not count (reserves only) |
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

All other references are listed in `PROJECT.md` and `LITERATURE.md`.
