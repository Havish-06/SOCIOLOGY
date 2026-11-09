# Laughter Under Scrutiny: Joke Topics, Public Backlash and Escalation in India — Team K

This README is the project's single guide: what the project is, how to carry it out, the codebook, the previous work it
builds on, and every team decision. Everything a reviewer needs to check the process is here or in the folders it points to.

**Question.** Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a controversy,
why does it end so differently: online criticism only, legal action, extra-legal action, or both?

**Method.** A structured, focused comparison (George & Bennett, 2005) of 24 controversies from 2018–2026, each analysed
with the same template and then compared side by side. Topic is the main comparison; genre is recorded as a secondary
variable. Team: Havish, Yogansh, Pranav, Siddanth.

## Contents

- [Quick start](#quick-start): files, status, setup, tools
- [Part A — The project](#part-a--the-project): summary, questions, concepts, theory, previous work in brief, design,
  cases, data, case analysis, comparison, outputs, roles, ethics, limitations, timeline, references
- [Part B — How to carry it out](#part-b--how-to-carry-it-out): news protocol, the steps, comment protocol and spam
  audit, folder structure, open questions, timeline, glossary
- [Part C — Codebook](#part-c--codebook): every joke and comment label with its decision rules and sources
- [Part D — Previous work](#part-d--previous-work): the literature review and how each study shapes the method
- [Part E — Decisions log](#part-e--decisions-log): dated decisions and the questions still open

## Quick start

### Where things are

| Path | What it is |
|---|---|
| `cases/<case_id>/case.md` | One analysis per case (24), written on the template `cases/_template.md` |
| `cases/<case_id>/sources.md` | The searches and the numbered source list for that case |
| `analysis/final_cases.csv` | The 24 final cases; `case_pool.csv` and `case_pool_summary.md` show how they were chosen from 45 |
| `analysis/assignments.md` | Who owns and who verifies each case |
| `analysis/comparison.csv` | One row per case: topic, genre, context, who mobilised, route, outcome, stigma, response |
| `analysis/mechanisms.csv` | The verdict for every interpretive lens, per case |
| `analysis/news_coding.csv` | Framing codes for the news articles of each case |
| `analysis/clips.md` | For every case, the YouTube links to watch and transcribe (original or reupload) |
| `analysis/first_read.csv` | Each owner's own reading of the case, written before opening the AI draft (to fill) |
| `analysis/findings.md` | Cross-case findings |
| `data/` | Earlier case, event and video tables (`videos.csv` lists the YouTube videos for comment collection) |
| `src/`, `tests/` | Comment collection, spam and coordination audit, coding sheets, news timing; tests |

### Status (2026-11-09)

- All 24 cases drafted by AI (`status: draft`); owners and verifiers still check each one (Part B, Step 5).
- Comment collection and the spam audit are pending: the pipeline is being checked first.
- First findings are in `analysis/findings.md`; they are working findings until verification is done.
- First deliverable: a presentation on 14–15 November 2026.

### Setup

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows  (source .venv/bin/activate on Mac/Linux)
pip install -r requirements.txt
copy .env.example .env            # then paste your own YouTube Data API key and any random ANON_SALT into .env
```

**Never commit `.env`.** It is git-ignored; keep your key there only.

### Tools

| Tool | Command | Use |
|---|---|---|
| Download comments | `python -m src.collect --videos data/videos.csv` (or `--video-ids <id> --case-id <case>`) | Part B, Step 5.3 |
| Spam and coordination audit (with chance check; add `--sensitivity`) | `python -m src.spam --comments data/raw/comments.csv --channels data/raw/channels.csv` | Every case, before reading comments |
| Check the spam flags against hand-coding | `python -m src.spam --validate data/coding/coded.csv --flagged data/processed/comments_flagged.csv` | After coding |
| Coding sheet and agreement (Cohen's kappa) | `python -m src.sample sheet ...` / `python -m src.sample kappa --a A.csv --b B.csv` | Steps 5.5 and 6 |
| News-coverage timing from GDELT (optional) | `python -m src.news --comments data/processed/comments_flagged.csv` | Did news start before or after the outrage? |
| Tests | `python -m pytest -q` | Check the tools still work |

**Platforms.** YouTube Data API v3 is free (10,000 units/day). Only YouTube comments are used.
X/Twitter (no free API), Instagram and Reddit are not used. GDELT is optional; Google Trends is not used.

**Ethics.** Only public material. No commenter usernames or IDs in any committed file; quotes are paraphrased. Raw comment
files (`data/raw/`, `data/comments/`, `data/manual/`) are git-ignored.

---

## Part A — The project

### 1. Summary

Indian stand-up comedy has grown quickly through YouTube and live shows, and so have the controversies around
it. Some jokes end with an online storm that fades in days; others end with FIRs, arrests, court summons,
vandalised venues, cancelled shows or assault. This project asks **which topics bring Indian stand-up comedians
under public scrutiny, and why controversies end so differently**.

We compare about **25 controversies from 2018 to 2026** using a **structured, focused comparison** (George &
Bennett, 2005): every case is researched and written up with the same template, and the cases are then compared
side by side. Evidence comes from the original clips (watched in full and transcribed), news reports, legal
records, YouTube comments and the comedians' own statements. Cases are interpreted with a toolkit of sociological lenses, chosen for what helps answer the question: scandal,
moral panic, strategic offence, social mobilisation, law as a weapon, organised online publics, platform
outrage, context collapse, stigma, Durkheim on the sacred and punishment, humour theory, identity and power,
fandom, and apology.

The final output is a research paper, 24 verified case files, a master comparison table, and a findings
report with a typology of escalation paths.


### 2. Why this project

Two controversies led us to this topic.

- **India's Got Latent (February 2025).** One remark on a YouTube talent show produced FIRs in several states,
  the removal of every episode, death threats against a participant and an appearance before the Supreme Court.
- **Pranit More's "Rs 370 biryani" crowd work (June 2026).** A short clip of an exchange with an audience member
  at a Gurugram show spread online, drew a complaint from the National Commission for Women and led to a police
  FIR and two public apologies.

In both, a joke made for one room reached millions of people who were never its audience, and the response moved
from comments to the police. Other jokes on equally sensitive subjects fade without consequence. Explaining that
difference is the puzzle of this project.


### 3. Research questions

**Main question.** Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a
controversy, why does it end so differently (online criticism only, legal action, extra-legal action, or both)?
How do the joke's topic, its target and its context shape that outcome?

| | Sub-question | Theory used |
|---|---|---|
| **SQ1 Topic** | Which topics (religion, caste, politics and the nation, gender and sexuality, regional icons, disability, and others) appear in controversies? Do the topic and the direction of the joke (punching up or down) go with different reactions and outcomes? Does genre (dark comedy, satire, crude humour, roast) add anything once topic is held constant? | Durkheim on the sacred; benign-violation theory; punching up/down |
| **SQ2 Context** | How does context, especially *collision* (someone else resurfacing or reframing a clip) versus *collusion* (the comedian publishing it), relate to how far a controversy escalates? | Goffman's frames; context collapse |
| **SQ3 Mobilisation and stigma** | Who mobilises, through which channel, and how do they frame the joke? Is the comedian (and their venue or organisers) stigmatised? Was something treated as sacred, and whose sacred? | Stigma; labelling; Durkheim on punishment |

**What we will and will not claim.** Every case is a joke that already became a controversy, so we cannot say
that a topic is risky in general. We can say how controversies differ from one another and what is associated
with each outcome.


### 4. Key concepts

| Concept | Meaning in this project |
|---|---|
| **Case** | One controversy around one joke (or set of jokes) by one comedian or group at one time. The unit of analysis |
| **Topic** | What the joke is about and whom it touches: religion, caste, politics and the state, nation, gender and sexuality, family, regional icons, disability, celebrities, looks. **The main variable** |
| **Genre** | Comic style, recorded for every joke as a secondary variable: dark comedy, satire (Juvenalian or Horatian), crude/shock, roast, gallows humour, observational |
| **Dark comedy** | A grave subject (death, violence, suffering, disease, disability, the sacred, a stigmatised position) **and** the laugh comes from that gravity (Willinger et al., 2017) |
| **Direction** | Punching up (the target has more power than the comedian) or down (less), judged against local hierarchies: caste, majority and minority religion, state power |
| **Outcome type** | **Online only**; **legal** (action against the comedian by the state or a statutory body: complaint, FIR, arrest, summons, court case, commission action, legal notice, or administrative action such as a refused permission or sealed venue; police action against the comedian's attackers does not count); **extra-legal** (threats, vandalism, disruption, forced cancellation, assault, forced or pressured apology by non-state actors); **both** |
| **Context, four layers** | *Performance* (where, to whom, language, format); *circulation* (who moved the clip, when, with what caption); *reception* (who reacted and how they framed it); *societal* (elections, recent events, other controversies) |
| **Collusion / collision** | The comedian deliberately puts material before wider audiences (collusion), or audiences are merged without the comedian's involvement, e.g. a third party resurfaces an old clip with a hostile caption (collision) (Davis & Jurgenson, 2014) |
| **Stigma ladder** | 1 labelling and stereotyping → 2 separation (boycott calls) → 3 status loss (cancelled shows, lost venues) → 4 discrimination (bans, arrests, violence) (adapted from Link & Phelan, 2001) |
| **Courtesy stigma** | Stigma that spreads to venues, organisers and co-performers (Goffman, 1963) |
| **Sacred object** | What a group sets apart and protects (Durkheim). Fixed in advance to avoid circular reasoning: deities and religious symbols; religious founders and texts; regional icons such as Shivaji; Ambedkar; the nation, army, martyrs and flag; the family and parents |


### 5. Theoretical framework and interpretive toolkit

Four ideas run through the whole project (below). Around them sits a wider **toolkit of lenses**: each case is
interpreted with whichever lenses the evidence supports, not forced into a fixed set of theories.

**Stigma and labelling.** Goffman (1963) describes stigma as reducing a person "from a whole and usual person to
a tainted, discounted one". Becker (1963) shows that deviance is a label applied by others. In comedy
controversies the label often moves from the joke to the comedian ("anti-Hindu", "anti-national", "obscene").
Link and Phelan's (2001) components of stigma give us a ladder for measuring how far each case escalated.

**Context collapse.** Social media flattens many audiences into one (Marwick & boyd, 2011). Stand-up depends on
a licence granted by a co-present audience that accepts the comic frame (Mintz, 1985; Brodie, 2014). When a clip
leaves the room, the frame can be lost. Davis and Jurgenson (2014) distinguish deliberate *collusion* from
unintended *collision*; we test whether collisions escalate further.

**Durkheim.** The sacred is set apart and protected, and joking about it is profanation. "We do not condemn an act
because it is a crime; it is a crime because we condemn it." Punishment is a passionate collective reaction that
reaffirms a group, and deviance reveals moral boundaries (Durkheim, 1893, 1912; Erikson, 1966). India is plural,
so we always ask **whose** sacred was touched and who claimed to speak for the group.

**Humour theory.** Benign-violation theory (McGraw & Warren, 2010) holds that humour needs a violation that also
seems harmless; whether it seems harmless depends on psychological distance (McGraw et al., 2012). This explains
why the same joke can amuse one audience and enrage another.

#### The interpretive toolkit

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
| **Chilling effect** | What does the case teach other comedians about which topics to avoid? | Implications; comedians' statements | Schauer (1978) |

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


### 6. Previous work and how we use it

Full review: Part D.

**What has been done.**
- **Sociology of humour:** what counts as a joke is decided socially (Douglas, 1968); humour marks group and
  class boundaries (Kuipers, 2006; Friedman, 2014); ridicule disciplines (Billig, 2005).
- **Stand-up studies:** the comic's licence and its limits (Mintz, 1985; Krefting, 2014; Brodie, 2014; Smith, 2018).
- **Offence:** offence is judged by context and inferred intent, not content alone (Lockyer & Pickering, 2005;
  Graefer & Das, 2020).
- **Humour scandals:** Kuipers (2011) on the Danish Muhammad cartoons; Ödmark (2021) compares three Swedish humour
  controversies and shows that a change of media context turns uniting humour into dividing humour.
- **Online outrage:** firestorms as norm enforcement (Rost, Stahel & Frey, 2016).
- **South Asia:** "hurt sentiments" claims and Section 295A as political tools (Nair, 2023); offence and free
  speech in Indian law (Bhatia, 2016).
- **Indian stand-up:** stand-up as a public sphere (*Contemporary South Asia*, 2017; Bhargava & Singhal, 2023);
  caste and the margins (Shivaprasad, 2020; Ahmad, 2026); the edited volume by Chilana & Bhargava (2024).

**The gap.** Indian research studies what comedians say; humour-scandal research studies one to three European
cases through news framing. No study we found compares Indian comedy controversies to explain why one joke goes
to the police, another to a mob, and a third fizzles.

**How earlier studies shape our method.**

| Part of our method | Borrowed from |
|---|---|
| Same questions asked of every case; matched pairs | George & Bennett (2005) |
| Each case read as a "humour scandal": who mobilised, who gained, who lost | Kuipers (2011) |
| Framing analysis of news coverage; humour function before and after the clip travelled | Ödmark (2021); Meyer (2000) |
| Collusion or collision; months between performance and controversy | Marwick & boyd (2011); Davis & Jurgenson (2014) |
| Temporal and social distance of the objectors | McGraw & Warren (2010); McGraw et al. (2012) |
| Performance setting, audience intimacy, language | Mintz (1985); Brodie (2014); Kuipers (2006) |
| Norm the objectors said was broken | Rost et al. (2016); Durkheim |
| Complainant, whether they claim to speak for a group, legal basis | Nair (2023); Bhatia (2016) |
| Stigma ladder, labels, courtesy stigma | Link & Phelan (2001); Goffman (1963); Becker (1963) |
| Comedian's narrative in response | Vásquez; Nicolaï & Maeseele (2024) |
| Comment labels and intent attributed | Part C (TRAC, HASOC, SemEval, Benesch); Graefer & Das (2020) |


### 7. Research design

| Item | Decision |
|---|---|
| Design | Structured, focused comparison of cases, with paired comparisons of closely matched cases |
| Number of cases | 24 (final list decided 2026-11-09) |
| Period | Controversies between 2018 and 2026 |
| Depth | Every case analysed in full with the same template |
| Comparison | Master comparison table; matched pairs; typology of escalation paths; counter-examples for every pattern |
| Reliability | Each owner's own first read of the case, made before reading the AI draft; human–AI agreement reported |
| Not done | Interviews (no time); Instagram and Reddit comments |

#### Case selection

A case must meet all four criteria:
1. a joke or comic performance by an Indian comedian (non-stand-up comparison cases, such as a TV show or a
   college skit, are marked as such);
2. covered by **at least two independent** news sources (reprints of one wire story count once);
3. the controversy happened between 2018 and 2026;
4. enough material to describe the joke, build a dated timeline and identify the outcome.

The set is balanced across **topics** (at least two or three cases each for religion, caste in both directions,
politics and the nation, gender and sexuality, and regional icons) and across **outcomes** (at least four each of
online-only, legal, extra-legal and both). Cases that fizzled online are essential: they are the contrast that
makes escalation explainable. Comedians of every audience size are included (small under 100K, mid-range 100K–2M,
large over 2M YouTube subscribers at the time of the incident).

#### The 24 cases

Final list, decided 2026-11-09 (`analysis/final_cases.csv`). Topic, genre and outcome below are first-pass judgements, to be verified in each case analysis. `*` = comparison
case (not a stand-up performance). Full pool of 45 candidates with sources: [`analysis/case_pool.csv`](analysis/case_pool.csv).

| # | Case | Comedian | Year | Topic | Genre | Outcome |
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
| 19 | virli_2026 | Madhur Virli | 2026 | gender | dark | legal |
| 20 | faruqui_2024 | Munawar Faruqui | 2024 | region (Konkani people) | crude | extra-legal |
| 21 | raina_2026 | Samay Raina / Sharon Verma | 2026 | region (Bihar, Kashmiri Pandits) | roast; dark | online only |
| 22 | mohanraj_2026 | Aishwarya Mohanraj | 2026 | gender / family | dark | online only |
| 23 | kamra_2018 | Kunal Kamra | 2018 | nation / politics | satire | extra-legal |
| 24 | rangeela_2021 | Shyam Rangeela | 2021 | politics (Modi mimicry) | satire | legal |

**Matched pairs built into the set.**

| Pair | Held constant | What differs |
|---|---|---|
| fernandes_2024 / fernandes_2025 | Comedian | Topic; apologised vs refused |
| more_2025 / more_2026 | Comedian | Celebrity roast vs crude crowd work; fan mob vs women's commission |
| munawar_2021 / faruqui_2024 | Comedian | Religion vs region; jail vs threats |
| kamra_2018 / kamra_2025 | Comedian, satire | Campus cancellation vs vandalism and FIRs |
| katikala_2026 / sarat_2026 | Same week, Andhra Pradesh politics | Police route vs mob route |
| latent_2025 / raina_2026 | Same show | Crude remark → FIRs; dark jokes → fizzled |
| virli_2026 / mohanraj_2026 | Same week, gender jokes, both resurfaced | Legal vs online only |
| shah_2021 / jain_univ_2023 / parithabangal_2025 | Caste | Punching down vs punching up |
| raina_sma_2025 / shah_2021 | Jokes on disability | Court-led action vs fizzled |


### 8. Data sources

| Source | Used for | Access |
|---|---|---|
| News reports (national and regional) | Dates, actors, complaints, FIRs, threats, responses | Outlet websites; wire copy counts as one source |
| Legal records | FIR sections, court orders, police and commission statements | As reported; Bar & Bench, LiveLaw, court websites |
| YouTube comments | How people framed the joke | Free YouTube Data API v3 via `src/collect.py` |
| Original clips and transcripts | The full joke in its setting: what came before and after, the room's reaction, how the viral clip was cut | Watched by the owner; transcript copied from YouTube's "Show transcript" (`analysis/clips.md`) |
| Comedians' statements | Apology, refusal, clarification | Their own posts and videos; reported interviews |
| Social Blade | Subscriber counts at the time of the incident | Manual lookup |

Not used: X/Twitter (no free API); Reddit (API needs an approved app; threads may be read for understanding only,
not coded); Instagram (comments cannot be collected without copying by hand); interviews (no time).

**News articles** do two jobs: evidence of what happened (every important fact needs two independent sources;
wire copy counts once) and data on how the controversy was framed. For each case, 6–10 articles are coded for
framing, drawn from at least three outlet types of English-language coverage: national dailies, digital-native
outlets, legal news (LiveLaw, Bar & Bench), and outlets with an explicit editorial stance on each side (Hindi or
regional press only where it adds a frame the English outlets miss). Each coded article records its dominant frame (e.g. hurt
sentiments, obscenity, free speech, legal overreach), its generic frame (conflict, responsibility, morality, human
interest, economic; Semetko & Valkenburg, 2000), whether the joke is quoted or only characterised, whether the
comedian is labelled, whether claims are attributed or stated as fact, and whose voices are quoted (Entman, 1993;
Ödmark, 2021). Optionally, daily GDELT counts show whether national news coverage came before or after the online
outrage.


### 9. How each case is analysed

#### The case template

Every case is written up in [`cases/_template.md`](cases/_template.md) with the same sections:

| Section | Content |
|---|---|
| A. Basic facts | Comedian, dates, venue, city and state, first platform, language, audience size, other fame |
| B. The joke | Wording (transcribed from the clip where possible), topic, genre, target, direction, form, technique |
| C. Context | Four layers: performance setting and language; circulation (collusion or collision, gap in months, caption); reception and the objectors' temporal and social distance; societal context |
| D. Timeline | Dated events with actor type, confidence and sources; days to peak and to fading |
| E. Reaction | Who objected and their words; the norm they said was broken; who defended the comedian; dominant media frame; humour function before and after; comment themes |
| F. Outcome | Outcome type; legal actions with complainant and legal basis; extra-legal actions; highest stigma step; courtesy stigma; how it ended; winners and losers |
| G. Comedian's response | Apology, refusal, clarification, deletion or silence; timing; effect; the comedian's narrative |
| H. Interpretation | Process tracing of the timeline; a verdict and evidence for each lens in the toolkit; the best explanation of the outcome; rival explanations ruled out |
| I. Comparison notes | Matched pairs; what the case adds |
| J. Sources | Numbered sources with confidence; disputes; open questions |

#### Workflow for each case

| Step | Who | What happens |
|---|---|---|
| 1. Research | AI assistant | Gather news, legal reports and statements; build the timeline and source list |
| 2. Full clip and first read | Case owner | Watch the full original performance, paste its transcript, and write their own reading of the case **before** opening the AI draft |
| 3. Comments | AI and team | Download YouTube comments for up to three key videos; read and theme them |
| 4. Draft | AI assistant | Fill every section of the template |
| 5. Compare | Case owner | Compare the first read and the transcript with the draft; fix the draft; record agreements and disagreements |
| 6. Verification | Team member | Check every fact against its sources |
| 7. Final | Case owner | Fix flagged items; add the case to the master comparison table |

Matched pairs are analysed together. With four team members, each owns about six cases and verifies about six.

#### Reading comments

Comments are evidence of how people framed the joke. They are **never** treated as a measure of public opinion.

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

- **Videos (up to three per case), in order of priority:** the original clip on the comedian's channel; a
  reupload; the comedian's response; news coverage (marked, because its commenters are news viewers).
- **Sample per video:** the 50 most-liked top-level comments plus 50 random ones (fixed random seed).
- **Recorded for each comment** (Part C): reaction (support, mock the offended, neutral,
  backlash, threat, demand legal action, spam); frame (play or serious); target; whether it attacks the
  comedian's identity; sacred object invoked; norm invoked; intent attributed to the comedian.
- **Spam and coordination check:** run on every case before comments are read (details below).
- **Reported in the case file:** main themes, their frequency in the sample, two or three paraphrased examples
  each, and anything unusual.

**Spam and coordination detection (`src/spam.py`).** Run on every case's comments before any comment is read,
counted or quoted. Methods follow the coordination-detection literature (Part D, stream 11):

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

#### Verification rules

1. **Two independent sources** for every important fact (dates, complainants, FIR sections, arrests, threats,
   cancellations, apologies).
2. Every fact carries a **confidence level**: *confirmed* (two independent sources or an official record),
   *reported* (one source), or *disputed* (sources disagree; both versions recorded).
3. Every claim links to its source, with the date accessed.
4. **Framing is data, not fact:** when outlets describe the same event differently, the difference is recorded,
   not resolved silently.
5. The verifier is a team member who did not draft the case. A case is final only when every important fact is
   confirmed or explicitly marked as reported or disputed.


### 10. Cross-case analysis

0. **Mechanisms table** (`analysis/mechanisms.csv`): the lens verdicts from every case, showing which mechanisms
   recur with which outcomes.
1. **Master comparison table** (`analysis/comparison.csv`): one row per case, with topic, genre, direction, form,
   collapse type, gap in months, caption, sacred object, norm invoked, who mobilised, channel used, legal basis,
   highest stigma step, courtesy stigma, comedian's response, outcome, audience size and election period.
2. **Agreement report:** share of cases where the owner's first read matched the AI draft for each key judgement
   (`analysis/first_read.csv`).
3. **Answers to each sub-question,** supported by named cases.
4. **Paired comparisons:** for each matched pair, what differed, what stayed the same, and which difference best
   explains the different outcomes.
5. **Typology of escalation paths:** recurring routes such as *resurfaced clip → party complaint → FIR*,
   *live show → fan group → assault*, or *online anger → apology → fizzled*.
6. **Counter-examples:** every pattern lists the cases that do not fit and explains them. A pattern with no
   counter-examples checked is not a finding.
7. **Optional truth table:** cases × four or five conditions × outcome, as a visual check of which combinations
   go with which outcome, not as a causal claim.

**Early patterns to test** (from first-pass coding, not yet findings): no politics or religion case stayed online
only; politics is the only topic where extra-legal action is common; gender and sexuality cases went to
commissions and courts or fizzled, never to mobs.


### 11. Final outputs

| Output | Description |
|---|---|
| **Research paper** | Introduction (opening with *India's Got Latent* and the Rs 370 biryani case); conceptual framework; previous work and how we use it; method; overview of cases; findings by sub-question with matched pairs and the typology; discussion; limitations; conclusion; appendix with a one-page summary of each case |
| **Case files** | 24 verified case analyses in `cases/<case_id>/` (`case.md` and `sources.md`) |
| **Comparison table** | `analysis/comparison.csv` |
| **Findings report** | `analysis/findings.md`: patterns, matched pairs, typology, counter-examples, agreement report |
| **Presentation** | Slides summarising the question, method and findings |
| **Optional** | A visual case map built from the comparison table |

**The discussion section** is led by the findings. It restates the main answer; interprets each major finding
using whichever lenses in the toolkit the evidence supports (for example, whether different groups defend their
"sacred" through different channels: party cadres, formal complaints or commissions) and says so where a theory
fails; explains counter-examples; relates the results to previous work; considers rival explanations (elections,
fame, platform, news coverage); and draws out implications for self-censorship, the role of the state and the
effect of clipping and platforms.


### 12. Team roles and AI use

| Task | AI assistant | Team member |
|---|---|---|
| Find news and legal reports | Main role | Spot-checks |
| Download YouTube comments | Runs `src/collect.py` | Provides the API key |
| Watch the full clip and copy its transcript | Cannot watch video; reads the transcript | Yes |
| Draft case analyses | Yes | — |
| Verify every fact | Drafts the source list | **Required** |
| First read of each case, before the draft | — | Yes |
| Read and theme comments | Drafts themes | Checks themes against the comments |
| Cross-case comparison | Builds the table, proposes patterns | Decides which patterns hold |
| Interpretation and writing | Drafts | Owns, edits and signs off |

**Disclosure in the paper:** "AI tools were used to gather sources, collect public comments and draft case
analyses. Every factual claim was verified by a team member against at least two independent sources, and all
interpretive conclusions were reviewed and agreed by the team." The course allows unlimited AI use; the statement is
included for transparency.


### 13. Ethics

- Only public material is used.
- No commenter usernames or IDs appear in any shared file; quoted comments are paraphrased so they cannot be
  searched back to their authors.
- Raw comment files stay on team members' computers and are never committed.


### 14. Limitations

| Limitation | How we handle it |
|---|---|
| **Selection on the outcome:** every case is already a controversy | Claims limited to differences among controversies; fizzled cases included |
| **Small number of cases** | Findings presented as patterns with named cases and counter-examples, not statistical effects |
| **News bias and gaps:** outlets take sides; English national media dominate | Two-source rule; framing recorded as data; regional outlets searched |
| **Lost comments:** deleted comments and removed clips | Collection dates recorded; older cases treated with caution |
| **Missing originals:** comments may come from reuploads or news channels | Video type recorded for every comment set |
| **Platform gaps:** YouTube comments only; no X/Twitter, Instagram or Reddit; WhatsApp invisible | Stated openly |
| **Subjective judgements:** genre, direction, collapse type | Written definitions; owner's first read before the AI draft; agreement reported |
| **Circular coding of the sacred** | Sacred-objects list fixed before outcomes are compared |
| **AI errors** | Every fact verified by a team member; AI use disclosed |
| **Languages:** material is mostly Hindi, Hinglish and English, with some Marathi, Telugu and Tamil | Everyone on the team reads Hindi and English; other languages are read with AI translation plus English coverage, and the case file says so |
| **Audience size is a weak proxy for fame** | Subscribers at the time of the incident plus a note on TV and streaming fame |
| **Not representative of public opinion** | Comments never presented as what India thinks |


### 15. Timeline

**First milestone: presentation on 14–15 November 2026.** The team aims to analyse all 24 cases before it, starting
with *India's Got Latent* as the pilot, so the presentation can show cross-case results. Case owners: Havish,
Yogansh, Pranav and Siddanth, six cases each (`analysis/assignments.md`). The weeks below are the fallback plan if
the analysis continues after the presentation.

| Week | Work | Milestone |
|---|---|---|
| 1 | Team meeting; setup; final case list | Case list agreed; API keys working |
| 2 | Finalise template; pilot case (*India's Got Latent*) | Template frozen |
| 3–5 | Analyse all cases (about 8 per week across the team) | All cases final |
| 5–6 | Cross-case comparison | Findings report complete |
| 7 | Writing | Paper draft |
| 8 | Revision | Final paper, slides, tidy repository |

### References

Adut, A. (2008). *On scandal: Moral disturbances in society, politics, and art*. Cambridge University Press.
Ahmad, M. N. (2026). Can Dalit laugh? Humour as resistance and politics of Dalit-comedy in India. *Comedy Studies*, 17(1).
Beach, D., & Pedersen, R. B. (2013). *Process-tracing methods: Foundations and guidelines*. University of Michigan Press.
Becker, H. S. (1963). *Outsiders: Studies in the sociology of deviance*. Free Press.
Benford, R. D., & Snow, D. A. (2000). Framing processes and social movements. *Annual Review of Sociology*, 26, 611–639.
Benoit, W. L. (1995). *Accounts, excuses, and apologies: A theory of image restoration strategies*. SUNY Press.
Bhargava, R., & Singhal, A. (2023). Stand-up: The "comic" public sphere in India. *International Journal of Communication*, 17, 5852–5869.
Bhatia, G. (2016). *Offend, shock, or disturb: Free speech under the Indian Constitution*. Oxford University Press.
Billig, M. (2005). *Laughter and ridicule: Towards a social critique of humour*. Sage.
Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318.
Brodie, I. (2014). *A vulgar art: A new approach to stand-up comedy*. University Press of Mississippi.
Chilana, R., & Bhargava, R. (Eds.). (2024). *Politics of recognition and representation in Indian stand-up comedy*. Palgrave Macmillan.
Cohen, S. (1972). *Folk devils and moral panics*. MacGibbon & Kee.
Collier, D. (2011). Understanding process tracing. *PS: Political Science & Politics*, 44(4), 823–830.
Crenshaw, K. (1991). Mapping the margins. *Stanford Law Review*, 43(6), 1241–1299.
Crockett, M. J. (2017). Moral outrage in the digital age. *Nature Human Behaviour*, 1, 769–771.
Davis, J. L., & Jurgenson, N. (2014). Context collapse: Theorizing context collusions and collisions. *Information, Communication & Society*, 17(4), 476–485.
Douglas, M. (1968). The social control of cognition: Some factors in joke perception. *Man*, 3(3), 361–376.
Durkheim, É. (1893/1984). *The division of labour in society*. Macmillan.
Durkheim, É. (1912/1995). *The elementary forms of religious life*. Free Press.
Entman, R. M. (1993). Framing: Toward clarification of a fractured paradigm. *Journal of Communication*, 43(4), 51–58.
Erikson, K. T. (1966). *Wayward Puritans: A study in the sociology of deviance*. Wiley.
Feeley, M. M. (1979). *The process is the punishment: Handling cases in a lower criminal court*. Russell Sage Foundation.
Friedman, S. (2014). *Comedy and distinction: The cultural currency of a 'good' sense of humour*. Routledge.
George, C. (2016). *Hate spin: The manufacture of religious offense and its threat to democracy*. MIT Press.
George, A. L., & Bennett, A. (2005). *Case studies and theory development in the social sciences*. MIT Press.
Goffman, E. (1963). *Stigma: Notes on the management of spoiled identity*. Prentice-Hall.
Goffman, E. (1974). *Frame analysis*. Harper & Row.
Goffman, E. (1971). *Relations in public*. Basic Books.
Goode, E., & Ben-Yehuda, N. (1994). *Moral panics: The social construction of deviance*. Blackwell.
Graefer, A., & Das, R. (2020). Towards a contextual approach: Audiences, television and 'offensive' humour. *European Journal of Cultural Studies*.
Gray, J. (2003). New audiences, new textualities: Anti-fans and non-fans. *International Journal of Cultural Studies*, 6(1), 64–81.
Gray, J., Sandvoss, C., & Harrington, C. L. (Eds.). (2007). *Fandom: Identities and communities in a mediated world*. NYU Press.
Krefting, R. (2014). *All joking aside: American humor and its discontents*. Johns Hopkins University Press.
Kuipers, G. (2006). *Good humor, bad taste: A sociology of the joke*. Mouton de Gruyter.
Kuipers, G. (2011). The politics of humour in the public sphere: Cartoons, power and modernity in the first transnational humour scandal. *European Journal of Cultural Studies*, 14(1), 63–80.
Link, B. G., & Phelan, J. C. (2001). Conceptualizing stigma. *Annual Review of Sociology*, 27, 363–385.
Lockyer, S., & Pickering, M. (Eds.). (2005). *Beyond a joke: The limits of humour*. Palgrave Macmillan.
McCarthy, J. D., & Zald, M. N. (1977). Resource mobilization and social movements. *American Journal of Sociology*, 82(6), 1212–1241.
Marwick, A. E., & boyd, d. (2011). I tweet honestly, I tweet passionately. *New Media & Society*, 13(1), 114–133.
McGraw, A. P., & Warren, C. (2010). Benign violations: Making immoral behavior funny. *Psychological Science*, 21(8), 1141–1149.
McGraw, A. P., Warren, C., Williams, L. E., & Leonard, B. (2012). Too close for comfort, or too far to care? *Psychological Science*, 23(10), 1215–1223.
Meyer, J. C. (2000). Humor as a double-edged sword: Four functions of humor in communication. *Communication Theory*, 10(3), 310–331.
Mintz, L. E. (1985). Standup comedy as social and cultural mediation. *American Quarterly*, 37(1), 71–80.
Nair, N. (2023). *Hurt sentiments: Secularism and belonging in South Asia*. Harvard University Press.
Nicolaï, J., & Maeseele, P. (2024). Stand-up in the age of outrage. *European Journal of Humour Research*.
Ödmark, S. (2021). De-contextualisation fuels controversy: The double-edged sword of humour in a hybrid media environment. *European Journal of Humour Research*, 9(3), 49–64.
Rost, K., Stahel, L., & Frey, B. S. (2016). Digital social norm enforcement: Online firestorms in social media. *PLoS ONE*, 11(6), e0155923.
Schauer, F. (1978). Fear, risk and the First Amendment: Unraveling the chilling effect. *Boston University Law Review*, 58, 685–732.
Semetko, H. A., & Valkenburg, P. M. (2000). Framing European politics: A content analysis of press and television news. *Journal of Communication*, 50(2), 93–109.
Shivaprasad, M. (2020). Humour and the margins: Stand-up comedy and caste in India. *IAFOR Journal of Media, Communication & Film*, 7(1).
Sil, R., & Katzenstein, P. J. (2010). *Beyond paradigms: Analytic eclecticism in the study of world politics*. Palgrave Macmillan.
Smith, D. R. (2018). *Comedy and critique: Stand-up comedy and the professional ethos of laughter*. Bristol University Press.
Tarrow, S. (2011). *Power in movement* (3rd ed.). Cambridge University Press.
Thompson, J. B. (2000). *Political scandal: Power and visibility in the media age*. Polity.
Udupa, S. (2019). Nationalism in the digital age: Fun as a metapractice of extreme speech. *International Journal of Communication*, 13, 3143–3163.
Udupa, S., & Pohjonen, M. (2019). Extreme speech and global digital cultures. *International Journal of Communication*, 13, 3049–3067.
Willinger, U., et al. (2017). Cognitive and emotional demands of black humour processing. *Cognitive Processing*, 18, 159–167.
Yin, R. K. (2018). *Case study research and applications* (6th ed.). Sage.

Further references, including work on joke and comment classification, are in Part D
and Part C. Page numbers and editions should be checked against the original sources
before submission.

---

## Part B — How to carry it out

### News protocol

News articles do two jobs, and we keep them apart:
1. **Evidence of what happened** (dates, who complained, FIR sections, arrests, threats, apologies). Facts need
   two independent sources (Part A §9, Verification rules).
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


### The steps, in detail

Each step lists its goal, what it needs, what to do, what it produces, and when it counts as done.

#### Step 0: Team alignment

- **Goal:** the whole team, including Havish, agrees on this plan before work starts.
- **Do:**
  1. Everyone reads this file.
  2. Meeting (about 1 hour). Decide:
     - approve or edit the main question and sub-questions (Part A §3)
     - confirm the target number of cases (20–30)
     - who owns which cases (Step 5)
     - whether to send the supervisor a short update (optional; see the note below)
  3. Record the decisions in Part E (date, decision, reason).
- **Note to the supervisor (optional; the supervisor has said the original proposal no longer binds us):**
  > We are carrying out a structured comparative case study of 20–30 Indian comedy controversies, asking which
  > topics bring stand-up comedians under scrutiny and why some controversies end in legal or extra-legal
  > action while others fizzle. Each case is interpreted with a toolkit of sociological lenses (stigma, context collapse, Durkheim, scandal, moral panic, mobilisation and others), using news,
  > official records and public comments.
- **Output:** Part E.
- **Done when:** the questions above are decided and recorded.

#### Step 1: Setup

- **Goal:** the tools and folders are ready.
- **Do:**
  1. **YouTube API key** (one team member, about 5 minutes):
     Google Cloud Console → create a project → APIs & Services → enable "YouTube Data API v3" →
     Credentials → Create credentials → API key. Copy `.env.example` to `.env` and paste the key after
     `YOUTUBE_API_KEY=`. Also set `ANON_SALT=` to any random string. **Never commit `.env`** (it is git-ignored).
  2. **Python environment:** `python -m venv .venv`, activate it, `pip install -r requirements.txt`.
  3. Create the folders in Part B, Folder structure (`cases/`, `data/comments/`, `data/transcripts/`, `analysis/`).
  4. Copy `cases/_template.md` into `cases/_template.md`.
- **Free quota:** 10,000 units per day. One unit fetches up to 100 comments, so even the largest case
  (about 49,000 comments) needs only about 500–1,000 units. Quota is not a constraint.
- **Done when:** `python -m src.collect --video-ids <any id> --case-id test` downloads comments into `data/raw/`.

#### Step 2: Build the case pool and select the cases

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
- **Output:** `analysis/case_pool.csv` (all candidates, with included yes/no and reason) and the final list in Part E.
- **Done when:** the final list is agreed and the matrix has no empty cells that are only due to missing research.

#### Step 3: Finalise the template

- **Goal:** one fixed template that every case follows exactly.
- **Do:** review `cases/_template.md` as a team. Add or remove fields now, **not later**. Changing the template after
  cases are written means rewriting them.
- **Output:** `cases/_template.md` (frozen; any later change recorded in Part E and applied to all cases).
- **Done when:** the team approves the template.

#### Step 4: Pilot case

- **Goal:** test the template and workflow on one case before scaling up.
- **Suggested pilot:** `latent_2025` (Samay Raina / Ranveer Allahbadia, India's Got Latent). It is well documented,
  has rich legal and online reactions, and triggered later cases, so it stress-tests every section.
- **Do:** run the full per-case workflow (Step 5) on this one case. Then the team reviews:
  - Which template fields were hard or impossible to fill?
  - Which fields were filled but did not help the comparison?
  - How long did it take?
  - Were the verification rules workable?
- **Output:** `cases/latent_2025/` complete, plus template fixes recorded in Part E.
- **Optional:** a second pilot (`kamra_2025`) if the first shows big template changes.
- **Done when:** the template is adjusted and frozen.

#### Step 5: Analyse every case, one by one

Each case goes through these sub-steps. The case owner (a team member) is responsible for the case reaching `final`.

| Sub-step | Who | What happens | Output |
|---|---|---|---|
| 5.1 Research | AI | Search news, legal reports and statements. Build the dated timeline and source list. | `cases/<case_id>/sources.md` |
| 5.2 Full clip and first read | Case owner, **before opening the draft** | Watch the **full** original performance (links in `analysis/clips.md`), not only the viral seconds. Copy the YouTube transcript ("Show transcript"); if there is none, write the key lines by hand. Write a first read: what the joke was, what came before and after, how the room reacted, how the viral clip was cut, topic, direction, what angered people, outcome. If no clip exists, use the best reported quotation and say so. | `data/transcripts/<case_id>__<video_id>.txt` (git-ignored); row in `analysis/first_read.csv` |
| 5.3 Comments | AI + team | AI pulls YouTube comments for up to 3 key videos and reads and themes them following Part B, Comment protocol. | `data/comments/<case_id>_*.csv` (git-ignored), themes in section E |
| 5.4 Draft | AI | Fill every section of the template, including the theory reading (section H). | `cases/<case_id>/case.md` (`status: draft`) |
| 5.5 Compare | Case owner | Give the AI the transcript; compare the first read with the draft field by field; fix the draft where the clip or sources show it is wrong; mark in `first_read.csv` where the owner and the AI agreed. | `case.md` updated |
| 5.6 Verify | Verifier (never the owner) | Check every fact against sources (Part A §9, Verification rules). | `status: verified` |
| 5.7 Finalise | Case owner | Fix flagged items, update the master table. | `status: final`, row in `analysis/comparison.csv` |

- **Workload:** 24 cases and 4 people: 6 cases each to own and 6 to verify. Assignments in `analysis/assignments.md`
  (Havish, Yogansh, Pranav, Siddanth; verifiers rotate).
- **Order:** do matched pairs together (e.g. both Fernandes cases, both More cases, Katikala and Sarat Uday),
  so the comparison is easy to see while writing.
- **Done when:** every selected case is `final`.

#### Step 6: Cross-case comparison

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

#### Step 7: Interviews (dropped)

Not done: no time before the deadline (decided 2026-11-09). The chilling-effect question is answered from
comedians' public statements only.

#### Step 8: Write up

- **Suggested structure of the final paper:**
  1. Introduction: open with *India's Got Latent* and the Rs 370 biryani clip; the puzzle (why some jokes end
     in FIRs, some in mobs, some in nothing); why it matters
  2. Conceptual framework (topic and genre, stigma, context, Durkheim, the interpretive toolkit; Part A §5)
  3. Literature and gaps (from Part D), ending with how each stream is used in our method
  4. Method (this plan's Part A §7–9, including the AI disclosure and limitations)
  5. Cases overview (table of all cases)
  6. Findings by sub-question, with paired comparisons and the typology
  7. Discussion (led by the findings, not by a fixed list of theories):
     - restate the main answer in one paragraph
     - interpret each major finding: *why* it happens, using whichever lenses in the toolkit (Part A §4–5) the
       evidence supports: scandal, moral panic, strategic offence, mobilisation, law as a weapon, organised online
       publics, platforms, context collapse, stigma, Durkheim, humour theory, identity and power, fandom, apology
       (e.g. whether different groups defend their "sacred" through different channels: party cadres, formal
       complaints, commissions), and saying so where a theory fails to predict
     - explain the counter-examples and surprises
     - relate to previous work (Part D): where we agree with, extend or contradict it
     - rival explanations (elections, fame, platform, amount of news coverage)
     - implications: self-censorship, the state as referee or instrument, platforms and clipping
     - the limits of the interpretation (then the full limitations section)
  8. Limitations
  9. Conclusion
  - Appendix: one-page summary of each case
- **Also:** presentation slides; a tidy repository.
- **Optional bonus:** rebuild the dashboard from `analysis/comparison.csv` as a visual case map.


### Comment protocol

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
  (fixed random seed so the sample can be reproduced), with the collection date recorded.
- For very large comment sections, the full set can still be searched for specific phrases
  ("hurt sentiments", "anti-national", "just a joke") to check how common a theme is.

**What to record for each read comment** (light version of Part C, C2):
- reaction: support · mock the offended · neutral · backlash · threat · demand legal action · spam
- frame: play ("it's just a joke") · serious ("this is not comedy", "hurting sentiments") · none
- target: comedian · joke · offended group · platform · state
- stigmatises the comedian: yes (attacks their religion, caste, region, gender) · no
- sacred object invoked: from the fixed list in Part A §4–5, or none
- norm invoked: religious feeling · national honour · women's dignity · family/parents · caste dignity · decency · leader's honour · none (Rost et al., 2016)
- intent attributed to the comedian: meant harm · meant it as a joke · not stated (Graefer & Das, 2020: audiences judge offence by inferred intent)

**What goes into the case file:** the main themes, how often each appeared in the read sample, 2–3
**paraphrased** examples per theme (never usernames), and anything surprising.

**Spam and coordination detection (`src/spam.py`).** Run on every case's comments before any comment is read,
counted or quoted. Methods follow the coordination-detection literature (Part D, stream 11):

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


### Folder structure

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


### Open questions

To be settled in Step 0 or as noted.

1. ~~Approve the main question and sub-questions~~ Settled: approved with topic as the focus (Part A §3).
2. ~~Does the supervisor need to approve the change in method?~~ Settled: no. The original proposal no longer binds us; a short update is optional.
3. **Deadline.** Presentation on 14–15 November 2026 (Part B, Timeline). Final paper deadline still to be confirmed.
4. **Number of cases:** 20, 25 or 30? (Recommended: 25.)
5. ~~Sacred-objects list~~ Settled: family and parents count.
6. **Bundled or non-stand-up cases:** keep `disability_sc_2025` as one case or split it; keep `tangade_dalit`, which is a pattern of trolling rather than one incident?
7. ~~Languages~~ Settled: everyone reads Hindi and English (see Part A §14).
8. ~~Interviews~~ Settled: not done (no time).
9. ~~Course AI policy~~ Settled: unlimited AI use allowed.
10. ~~Havish's pipeline work~~ Settled: kept or dropped as in Part B, Folder structure.


### Timeline

#### Presentation sprint: 9–15 November 2026

The first deliverable is a **presentation on 14–15 November**. The team aims to take **all 24 cases** through the
workflow before it, so the presentation can show real cross-case results.

| Date | Work | Milestone |
|---|---|---|
| Sun 9 – Mon 10 | Everyone reads Part A, Part B and Part D; short team meeting on the remaining open questions; API keys set up | Plan agreed |
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

#### Full project

Weeks counted from after the presentation. Adjust once the final paper deadline is known.

| Week | Steps | Milestone |
|---|---|---|
| 1 | Step 0, Step 1, Step 2 | Plan agreed; API key working; final case list chosen |
| 2 | Step 3, Step 4 | Template frozen after the pilot case |
| 3–5 | Step 5 (about 8 cases per week across the team) | All cases `final` |
| 5–6 | Step 6 | `findings.md` complete |
| 7 | Step 8 | Paper draft |
| 8 | Step 8 | Final paper, slides, repository cleaned |


### Glossary

- **API:** a service that lets a program request data directly (here, YouTube comments) instead of a person copying it.
- **Case:** one controversy, the unit we analyse and compare.
- **Cohen's kappa:** a score for how much two coders agree beyond chance (1 = perfect, 0 = chance level; 0.6–0.8 is usually considered good).
- **FIR:** First Information Report, the document that opens a police case in India.
- **Matched pair:** two cases that are alike in most respects but differ in one, so the difference can be studied.
- **QCA:** Qualitative Comparative Analysis, a method for finding which combinations of conditions go with an outcome across a small number of cases. Used here only as an optional visual check.
- **Structured, focused comparison:** asking the same set of questions of every case, focused on the research question, so that cases can be compared (George & Bennett, 2005).
- **Typology:** a set of recurring types, here recurring paths a controversy can take.

---

## Part C — Codebook


Labels in C1 go into section B of each case file; labels in C2 are
used when reading comments (Part B, Comment protocol). How each label connects to previous work: Part D.

Every label below is adapted from earlier work, so our results can be compared with it. Each label notes
its source and what we changed. Full references are in Part D and Part A.

Rules for all coders:
- Code what the text **does**, not what you think the author meant.
- When unsure, pick `unclear` / `none` and add a note. Do not guess.
- Two coders code independently; disagreements are resolved by discussion, then the codebook is updated.
- Target before scaling up: Cohen's kappa ≥ 0.70 per label (`python -m src.sample kappa ...`).


### C1. Joke-level labels (one row per case in `data/cases.csv`)

The study covers **any topic that brings stand-up comedians under scrutiny**. Topic (A2) is the main variable;
genre (A1) records *how* the joke is told, so we can test whether scrutiny follows the topic or the style.

#### A1. Genre (more than one allowed)
| Code | Definition | Source |
|---|---|---|
| `dark` | **Both** (1) a grave subject (death, violence, suffering, disease, disability, the sacred, a stigmatised position in a hierarchy) **and** (2) the laugh comes *from* that gravity, not from merely mentioning it | Willinger et al. 2017 |
| `roast` | Mocks a particular person (a celebrity, a guest, an audience member) | — |
| `gallows` | Dark humour told by or for people who are themselves suffering or oppressed | Obrdlik 1942 |
| `satire_juvenalian` | Biting, contemptuous attack on people or institutions with power | Holbert et al. 2011 |
| `satire_horatian` | Gentle, playful mockery of power or social folly | Holbert et al. 2011 |
| `crude_shock` | Transgression mainly for shock (sex, bodily functions, obscenity) | — |
| `observational` | Everyday-life humour with no taboo subject | — |

#### A2. Taboo domain (more than one allowed)
`religion` · `caste` · `gender_sexuality` · `family` · `politics_state` · `regional_national_icon` · `celebrity_public_figure` · `bodies_looks` · `death_violence_tragedy` · `disease_disability` · `none`
Source: Allan & Burridge 2006 (taboo domains). **Added for India:** `caste` and `regional_national_icon`.

#### A3. Target and direction
- **target**: who the joke is aimed at, in free text (e.g. "reservation beneficiaries", "Deputy CM", "Shivaji statue supporters", "self").
- **direction**: judged against the **local** hierarchy (caste, majority/minority religion, state power), not a universal one.

| Code | Rule |
|---|---|
| `up` | Target has more power than the joke's speaker or the group they speak for (state, dominant caste or religion, celebrities) |
| `down` | Target is subordinated or stigmatised (Dalits, religious minorities, disabled people, women as a group) |
| `lateral` | Target has roughly equal standing |
| `self` | The comedian or their own group/family is the butt of the joke (self-defeating style, Martin et al. 2003) |
| `contested` | Coders disagree on who holds power in that context. Record both readings |

Sources: Zillmann & Cantor 1976; Ford & Ferguson 2004; Krefting 2014; Bhargava & Chilana 2022.

#### A4. Form and technique
- **form**: `standup_set` · `crowd_work` · `roast` · `sketch` · `song_parody` · `social_reply` · `tv_show` · `college_skit`
- **technique** (main one only): `irony_sarcasm` · `exaggeration` · `parody_impersonation` · `wordplay` · `story`
Sources: Long & Graesser 1988; Buijzen & Valkenburg 2004. We use only 5 techniques so that two coders can apply them reliably.

#### A5. Context (see proposal Section 2.3, Table 1)
`collapse_type`: `collusion` (the comedian put it out widely) · `collision` (someone else moved or resurfaced it) · `live_only` (no recording).
Also record: `gap_months`, who first reposted the clip, and whether the most-viewed circulating version has a neutral or accusatory title.
Sources: Marwick & boyd 2011; Davis & Jurgenson 2014.


### C2. Comment-level labels (coding sheet from `src.sample sheet`)

#### B1. reaction (exactly one)
| Code | Definition | Maps to |
|---|---|---|
| `support` | Defends or praises the comedian or joke | stance: favour |
| `mock_offended` | Ridicules the people who are offended | stance: favour |
| `neutral_discussion` | Discusses without taking a side | stance: none |
| `backlash` | Criticises or insults the comedian or joke, no threat | stance: against; TRAC covert/overt aggression |
| `threat` | Threatens harm, violence or disruption to the comedian, venue or family | TRAC overt aggression |
| `demand_legal_action` | Calls for FIR, arrest, ban, police or government action | — (new: RQ2 needs the route) |
| `spam_irrelevant` | Ads, self-promotion, off-topic | — |

Sources: Mohammad et al. 2016 (stance); Kumar et al. 2018 (TRAC); Mandl et al. 2019 (HASOC); Bohra et al. 2018.
**Rule:** if a comment both insults and threatens → `threat`; if it both insults and asks for an FIR → `demand_legal_action`.

#### B2. target
`comedian` · `joke_content` · `offended_group` · `platform` · `state` · `other`

#### B3. taboo (taboo the comment invokes)
Same list as A2.

#### B4. sacred_object
`deity` · `icon` (Shivaji, Ambedkar, national heroes) · `nation` (army, martyrs, flag) · `none`. Source: Durkheim 1912.

#### B5. frame
| Code | Rule |
|---|---|
| `play` | Treats it as a joke: "it's just a joke", "it's comedy", "don't watch if you're offended" |
| `serious` | Treats it as a real insult or crime: "this is not comedy", "hurting sentiments", "should be jailed" |
| `none` | Neither |

Sources: Bateson 1972 ("this is play"); Goffman 1974 (keying).

#### B6. stigmatises_comedian
`yes` if the comment attacks the comedian's **identity** (religion, caste, region, gender, sexuality, nationality: "anti-national", slurs) rather than the joke. Otherwise `no`.
Sources: Goffman 1963; Link & Phelan 2001.

#### B7. intensity
1 mild disapproval → 5 violent language. Modelled on the offence rating in Meaney et al. 2021.

#### B8. pushback_type (replies only, when a reply pushes back against a hostile comment; more than one allowed)
`facts` · `hypocrisy` · `consequences` (warns of consequences, without threats) · `affiliation` (appeals to shared identity) · `denouncing` · `humour_sarcasm` · `positive_tone` · `hostile`
Sources: Benesch et al. 2016; Mathew et al. 2019 (YouTube counter-speech).

#### B9. looks_inauthentic
`yes` · `no` · `unsure`. This is human judgement, used to check the automatic flags in `src/spam.py`.

#### B10. norm_invoked
The social norm the comment says the joke broke: `religious_feeling` · `national_honour` · `women_dignity` ·
`family_parents` · `caste_dignity` · `decency_obscenity` · `leader_honour` · `none`.
Sources: Rost, Stahel & Frey 2016 (online firestorms as norm enforcement); Durkheim 1912.

#### B11. intent_attributed
`harm` (says the comedian meant to insult or hurt) · `joke` (says it was meant as a joke) · `not_stated`.
Source: Graefer & Das 2020 (audiences judge offence by inferred intent and context).


### Language
Comments in Hindi, Hinglish, Marathi, Telugu, Tamil and other languages are coded by a team member who reads that
language. Code-mixed text is normal and not a reason to mark `unclear` (Khandelwal et al. 2018).

---

## Part D — Previous work


What researchers have already done on humour, offence and comedy controversies, how they did it, what they
found, and where our project fits. Organised into eleven streams, moving from general humour theory to Indian
stand-up controversies.

**How to use this file.** Each stream lists the key works, *what they did* (method and data), *what they
found*, and *what it means for us*. Items marked ✔ were checked against a publisher, journal or library
record on 2026-11-08; unmarked items are standard works in the field that should still be checked before
citing (page numbers, edition). Read at least the starred (★) works in each stream before the write-up.


### Overview: what has been done, in one table

| Stream | Typical method | Typical data | What it gives us |
|---|---|---|---|
| 1. Theories of humour | Philosophy, psychology experiments | Jokes, lab participants | Why a joke can amuse some and offend others |
| 2. Sociology of humour | Interviews, surveys, historical analysis | Audiences, joke repertoires, social groups | Humour as a marker of group boundaries, class and taste |
| 3. Stand-up comedy studies | Ethnography, performance analysis, interviews with comedians | Live shows, comedians, recordings | Stand-up as a genre with its own norms of licence |
| 4. Offence and the limits of humour | Case studies, audience studies, content analysis | Controversies, TV audiences, press coverage | Offence as social and contextual, not a property of the joke |
| 5. Humour scandals and controversies | Comparative case study, framing analysis | News coverage of controversies | **The closest model for our design** |
| 6. Online outrage and context | Computational analysis, experiments, theory | Social-media comments, petitions | How clips travel and why online anger spikes |
| 7. Humour, the sacred and the state in South Asia | Legal history, political theory, anthropology | Laws (s.295A), court cases, censorship episodes | The Indian legal and political machinery of "hurt sentiments" |
| 8. Indian stand-up comedy | Discourse analysis, content analysis of YouTube videos, interviews | Comedians' videos, audiences | The Indian scene: who performs, for whom, about what |
| 9. Classifying jokes and reactions | Annotation schemes, NLP datasets | Labelled jokes and comments | Our codebook labels (already in Part C) |
| 10. Explaining escalation | Comparative case studies, ethnography, theory | Scandals, moral panics, offence campaigns, courts, online publics | **Our interpretive toolkit**: why a controversy escalates and through which route |
| 11. Detecting spam and coordination | Network analysis, anomaly detection, classifiers | Social-media accounts and comments | How we tell organic outrage from organised campaigns |


### How previous work shapes our methodology

We do not only cite these studies; each part of our method is borrowed from, or adapted from, a specific
earlier study. The table says what we take and where it appears in our own work (Part B and the case
template `cases/_template.md`).

#### Research design

| What we do | Taken from | What exactly we borrow | Where it is in our method |
|---|---|---|---|
| Compare many controversies, each analysed with the same questions | George & Bennett (2005) | Structured, focused comparison | Whole design (Part A §7) |
| Treat each controversy as a "humour scandal" and ask who mobilised, who gained and who lost | Kuipers (2011), Danish cartoons | The scandal lens: humour regimes, power, winners and losers | Template F: *winners and losers*; SQ3 |
| Code how news outlets framed each controversy: problem, blame, remedy; generic frames | Entman (1993), "Framing: toward clarification of a fractured paradigm", *Journal of Communication* 43(4); Semetko & Valkenburg (2000), "Framing European politics", *Journal of Communication* 50(2) | Frame definition and five generic frames (conflict, responsibility, morality, human interest, economic) | News coding sheet `analysis/news_coding.csv`; Part B, News protocol |
| Compare controversies through how the news framed them, and how humour changes meaning when it changes media context | Ödmark (2021), three Swedish humour controversies | Small-n comparison of controversies; framing analysis of coverage; Meyer's (2000) four humour functions | Template E: *dominant media frame*; *humour function before and after travelling*; SQ2 |
| Include controversies that fizzled, not only escalated ones | Lesson from single-case scandal studies (Kuipers 2011; Klausen 2009), which cannot explain why other jokes did *not* explode | Need for contrast cases | Selection rule in Part B, Step 2 (online-only cases are essential) |
| Matched pairs of similar cases | George & Bennett (2005); Mill's method of difference | Hold most things constant, vary one | Part B, Step 6 (paired comparisons) |

#### Variables we record for every case

| Variable (template section) | Taken from | Why |
|---|---|---|
| Topic (B) | Davies (1990, 2011) on joke targets; Allan & Burridge (2006) on taboo | Topics of jokes follow social patterns; taboo domains give our topic list |
| Genre (B) | Willinger et al. (2017); Holbert et al. (2011); Obrdlik (1942) | Definitions of dark comedy, satire types and gallows humour |
| Direction: punching up or down (B) | Krefting (2014), "charged humour"; Shivaprasad (2020) on caste in Indian stand-up | Who is joking about whom matters, judged against local hierarchies |
| Performance setting and intimacy (C) | Mintz (1985); Brodie (2014) | The comic's licence depends on a co-present audience that accepts the comic frame |
| Language and register (C) | Kuipers (2006); Friedman (2014); Bhargava & Singhal (2023) | Humour taste marks class; English and vernacular stand-up reach different publics |
| Collusion or collision; months between performance and controversy (C) | Marwick & boyd (2011); Davis & Jurgenson (2014) | Who moved the clip to a new audience, deliberately or not |
| Distance of the objectors: temporal and social (C) | McGraw & Warren (2010); McGraw et al. (2012) on psychological distance | A violation feels benign when distant and harmful when close: tests why resurfaced clips and directly targeted groups react more |
| Days to peak and to fading (D) | Pfeffer, Zorbach & Carley (2014) | Online firestorms rise and fade quickly; we measure whether legal action outlasts the online storm |
| Norm said to be broken (E) | Rost, Stahel & Frey (2016); Durkheim | Backlash as enforcement of a social norm; tells us *which* norm each group defends |
| Comment frame: play vs serious (E) | Douglas (1968); Bateson (1955); Mulkay (1988) | Whether a remark is accepted as "a joke" is socially decided |
| Intent attributed to the comedian (comment code) | Graefer & Das (2020) | Audiences judge offence by inferred intent and context |
| Attacks on the comedian's identity; label used (E, H) | Goffman (1963); Becker (1963) | Stigma and labelling ("anti-Hindu", "anti-national", "obscene") |
| Highest stigma step; courtesy stigma (F) | Link & Phelan (2001); Goffman (1963) | Our four-step escalation ladder; spread of stigma to venues |
| Sacred object touched (fixed list) (H) | Durkheim (1912) | The sacred is set apart and defended; fixed in advance to avoid circular coding |
| Complainant and whether they claim to speak for a group (F) | Nair (2023) | "Hurt sentiments" complaints as a political tool used mainly by majorities |
| Legal basis: religious offence, enmity, obscenity, defamation, SC/ST Act, contempt (F) | Bhatia (2016) | Different legal categories carry different thresholds and politics |
| Comedian's own narrative (G) | Vásquez (*Narrative Inquiry*); Nicolaï & Maeseele (2024) | Comics' stock responses: contrition, defiance, "humourless audience", blaming social media |

#### Reading comments

| What we do | Taken from |
|---|---|
| Comment labels (reaction, target, frame, stigma, intensity, pushback) | Part C, C2: TRAC, HASOC, SemEval stance, Benesch, Mathew et al. |
| Treat comments as evidence of framing, never as public opinion | Lesson from online-outrage research: firestorms are driven by small, vocal groups (Rost et al. 2016) |
| Spam and coordination audit before reading comments: copy-paste, copied comments, hashtag pushes, co-timing, bursts, batch-created accounts; chance check, sensitivity check, human validation | Stream 11: Pacheco et al. (2021); Giglietto et al. (2020); Jakesch et al. (2021); Cresci (2020, 2023); Alberto et al. (2015) |

#### Interpreting each case and the results

Cases are not read only through stigma, context collapse and Durkheim. Each case gets a verdict for every lens
in the interpretive toolkit (stream 10 and Part A §5), using process tracing and rival explanations.


| Question in the discussion | Taken from |
|---|---|
| Do controversies mark the edges of Indian stand-up as a "comic public sphere"? | Public-sphere studies (*Contemporary South Asia* 2017); Bhargava & Singhal (2023) |
| Is backlash a passionate collective reaction that reaffirms a group, and whose group? | Durkheim (1893, 1912); Erikson (1966) |
| Who is allowed to ridicule whom? | Billig (2005); Krefting (2014); Shivaprasad (2020); Ahmad (2026) on Dalit comedy |
| Is the state a neutral referee or an instrument of offended groups? | Nair (2023); Bhatia (2016); Kaur & Mazzarella (2009) |

#### What we do differently from them

- **More cases.** Scandal studies usually examine 1–3 cases; we compare about 25 with one template.
- **Outcome type as the thing to explain.** Earlier work describes controversies; we explain why they end
  online only, in court, in the street, or in both.
- **India's plural sacred.** European scandal studies deal with one dominant public; we ask *whose* sacred
  was touched and which group claimed to speak for it.
- **Several kinds of evidence per case.** News, legal records, comments and the comedian's statements,
  not news framing alone.


### 1. Theories of humour: why a joke works or offends

| Work | What they did | Key idea |
|---|---|---|
| Hobbes (1651), *Leviathan*; Bergson (1900), *Laughter* | Philosophy | **Superiority**: we laugh at others' inferiority; laughter as social correction |
| Freud (1905), *Jokes and Their Relation to the Unconscious* | Psychoanalysis | **Relief**: jokes release forbidden aggression and sexuality; tendentious jokes |
| McGraw, Warren, Williams & Leonard (2012), "Too close for comfort, or too far to care?", *Psychological Science* 23(10) | Experiments | Psychological distance decides whether a violation feels benign: tragedy is funnier when distant |
| Kant, Schopenhauer; Raskin (1985), *Semantic Mechanisms of Humor*; Attardo & Raskin (1991) | Philosophy; linguistics | **Incongruity**: humour comes from two clashing scripts |
| ★ McGraw & Warren (2010), "Benign violations", *Psychological Science* 21(8) | Lab experiments | Humour needs a **violation** that also seems **benign**; it fails when the violation seems real or harmful |
| Willinger et al. (2017), *Cognitive Processing* 18 | Experiments on black-humour comprehension | Defines dark (black) humour: a grave subject with the laugh coming from that gravity |

**For us:** benign-violation theory explains why the *same* joke is funny in a club and offensive on X: the
"benign" part depends on who is listening. This is the psychological basis for our context analysis.


### 2. Sociology of humour: humour and social groups

| Work | What they did | Key finding |
|---|---|---|
| Radcliffe-Brown (1940), "On joking relationships", *Africa* 13(3) | Anthropology of kinship | Joking is a licensed relationship that manages tension between groups |
| ★ Douglas (1968), "The social control of cognition: some factors in joke perception", *Man* 3(3) | Anthropology | A joke is only perceived as a joke if the **social structure permits it**; the same words can be a joke or an attack |
| Coser (1959), "Some social functions of laughter", *Human Relations* 12 | Observation in a hospital | Humour can include, exclude and reinforce hierarchy |
| Zijderveld (1983), "The sociology of humour and laughter", *Current Sociology* 31(3) | Review | First systematic overview of humour as a sociological object |
| Mulkay (1988), *On Humour* | Discourse analysis | Humour is a separate "mode" of discourse with its own rules; serious and humorous modes can collide |
| Davies (1990), *Ethnic Humor Around the World*; (2011) *Jokes and Targets* | Comparative study of joke repertoires across countries | Ethnic jokes follow patterns (centre vs periphery); jokes are not straightforward evidence of hostility |
| ★ Billig (2005), *Laughter and Ridicule: Towards a Social Critique of Humour* | Theory | Ridicule is a disciplinary force; humour is not innocent and is central to maintaining social order |
| Meyer (2000), "Humor as a double-edged sword: four functions of humor in communication", *Communication Theory* 10(3) | Theory | Humour unites (identification, clarification) and divides (enforcement, differentiation); used by Ödmark (2021) and by us |
| Bateson (1955), "A theory of play and fantasy" | Theory | The "this is play" frame; a message is a joke only if the frame is shared |
| Fine & De Soucey (2005), "Joking cultures", *Humor* 18(1) | Ethnography of small groups | Groups develop shared joking cultures that mark insiders |
| ★ Kuipers (2006), *Good Humor, Bad Taste: A Sociology of the Joke* | Interviews and survey, the Netherlands | Humour styles map onto **class and education**; taste in jokes is used to draw social boundaries (Bourdieu) |
| Kuipers (2008), "The sociology of humor", in Raskin (ed.), *The Primer of Humor Research* | Review chapter | Standard map of the field |
| Friedman (2014), *Comedy and Distinction: The Cultural Currency of a 'Good' Sense of Humour* | Survey and interviews, Edinburgh Festival audiences | Comedy taste signals cultural capital |
| Lockyer & Pickering (2008), "You must be joking: the sociological critique of humour and comic media", *Sociology Compass* 2(3) | Review | Humour can damage people's social standing in some contexts; sociology must take that seriously |

**For us:** Douglas and Kuipers give the core sociological claim that what counts as "a joke" is decided
socially, not by the comedian. Billig supports reading backlash as a fight over **who may ridicule whom**.


### 3. Stand-up comedy as a genre

| Work | What they did | Key finding |
|---|---|---|
| ★ Mintz (1985), "Standup comedy as social and cultural mediation", *American Quarterly* 37(1) | Cultural analysis | The stand-up comic is a licensed "negative exemplar" who can say what others cannot |
| Limon (2000), *Stand-up Comedy in Theory, or, Abjection in America* | Literary theory | Stand-up deals in the abject: what a society expels |
| Double (2014), *Getting the Joke: The Inner Workings of Stand-Up Comedy* | Practice-based analysis | Persona, audience and the comic frame |
| Brodie (2014), *A Vulgar Art: A New Approach to Stand-Up Comedy* | Folklore and performance study | Stand-up depends on **intimacy** with a co-present audience |
| ★ Krefting (2014), *All Joking Aside: American Humor and Its Discontents* | Historical analysis | "Charged humour" by marginalised comics challenges social inequality |
| Quirk (2015), *Why Stand-up Matters* | Interviews and performance analysis | How comics manipulate audiences; the ethics of the stage |
| Smith (2018), *Comedy and Critique: Stand-up Comedy and the Professional Ethos of Laughter* | Sociology of the profession | Comics present themselves as critics; the professional ethos protects licence |
| Pérez (2013), *Discourse & Society* 24(4); (2022) *The Souls of White Jokes* | Ethnography of comedy classes | How racist jokes are taught and justified as "edgy" |
| Reid, Stoughton & Smith (2006), "The humorous construction of disability", *Disability & Society* 21(6) | Analysis of disabled comedians' routines | Disabled comics use humour to challenge stigma |

**For us:** Mintz and Brodie explain the **licence** stand-up gets in the room. Our context-collapse argument
is that this licence is lost when the clip leaves the room. Brodie's "intimacy" is the thing that collapses.


### 4. Offence and the limits of humour

| Work | What they did | Key finding |
|---|---|---|
| ★ Lockyer & Pickering (eds., 2005; 2nd ed. 2009), *Beyond a Joke: The Limits of Humour* ✔ | Edited volume of case studies | Offence is not a property of a joke; the limits of humour are negotiated socially |
| Weaver (2011), *The Rhetoric of Racist Humour* | Rhetorical analysis | How racist humour persuades while claiming "it's just a joke" |
| ★ Graefer & Das (2020), "Towards a contextual approach: audiences, television and 'offensive' humour", *European Journal of Cultural Studies* ✔ | Audience interviews, UK and Germany | People judge offence by **context** (who, where, intent), not by content alone |
| Feinberg (1985), *Offense to Others* | Legal philosophy | When offence (not harm) justifies restricting speech |

**For us:** supports the claim that topic alone cannot explain outcomes; context and who is offended matter.


### 5. Humour scandals and controversies: the closest model for our study

| Work | What they did | Key finding |
|---|---|---|
| ★ Kuipers (2011), "The politics of humour in the public sphere: cartoons, power and modernity in the first transnational humour scandal", *European Journal of Cultural Studies* 14(1), 63–80 ✔ | Case analysis of the Danish Muhammad cartoons (2005–06) | A **humour scandal** reveals clashing "humour regimes" and power relations; asks who won and who lost |
| *Humor* 21(1) (2008), colloquium on the Muhammad cartoons ✔ | Essays by humour scholars | The cartoon crisis read as a case for humour research, not only free speech |
| ★ Ödmark (2021), "De-contextualisation fuels controversy: the double-edged sword of humour in a hybrid media environment", *European Journal of Humour Research* 9(3), 49–64 ✔ | **Three-case comparison** (a radio roast, a TV satire segment, a podcast), framing analysis of Swedish news coverage | When humour changes media context, a uniting function (identification) turns into a dividing one (differentiation) |
| Kuipers & Zijp (2024), "Humour and the public sphere", *European Journal of Humour Research* 12(1) ✔ | Special-issue introduction | Humour is now central to public debate and to fights over it |
| Nicolaï & Maeseele (2024), "Stand-up in the age of outrage", *European Journal of Humour Research* ✔ | Case study of a Flemish comedian | How comics respond to "cancel culture" discourse |
| Andrews & Frame (2026), "Cancel culture: the decline of political comedy on British television in the early 2020s", *Comedy Studies* 17 ✔ | Analysis of UK TV comedy | "Cancel culture" debates and the anti-woke culture war in TV comedy |
| Vásquez, "Stand-up comedians' performed narratives about offended audiences", *Narrative Inquiry* ✔ | Narrative analysis of four comics' routines | Comics portray offended audiences as humourless and blame social media |
| Klausen (2009), *The Cartoons That Shook the World* | Interviews and documents | How the Danish cartoons were mobilised politically across countries |

**For us:** this is the stream we contribute to most directly. **Ödmark (2021) is a small comparative case
study of humour controversies, like ours.** Kuipers gives the "scandal" lens (who mobilises, who wins). These
studies are European and usually examine 1–3 cases through news framing; we compare ~25 cases, add legal and
extra-legal outcomes, and study a plural society with criminal offence laws.


### 6. Online outrage, firestorms and context collapse

| Work | What they did | Key finding |
|---|---|---|
| ★ Marwick & boyd (2011), "I tweet honestly, I tweet passionately", *New Media & Society* 13(1) | Interviews with Twitter users | **Context collapse**: many audiences flatten into one |
| ★ Davis & Jurgenson (2014), "Context collapse: theorizing context collusions and collisions", *Information, Communication & Society* 17(4) | Theory | **Collusion** (deliberate) vs **collision** (unintended) |
| Pfeffer, Zorbach & Carley (2014), "Understanding online firestorms", *Journal of Marketing Communications* 20 | Case analysis | Why online outrage spreads fast and fades fast |
| ★ Rost, Stahel & Frey (2016), "Digital social norm enforcement: online firestorms in social media", *PLoS ONE* 11(6) ✔ | 532,197 comments on 1,612 petitions | Firestorms are **norm enforcement**; named (non-anonymous) users are *more* aggressive |
| Shifman (2014), *Memes in Digital Culture* | Content analysis | How humorous content travels and mutates online |
| Phillips & Milner (2017), *The Ambivalent Internet* | Qualitative | Online humour is ambivalent: play and harm at once |
| Ronson (2015), *So You've Been Publicly Shamed* (journalism) | Interviews | Justine Sacco and others: a joke out of context becomes a public shaming |

**For us:** Rost et al. support reading backlash as Durkheimian norm enforcement (punishment that reaffirms a
group). Davis & Jurgenson give us the collusion/collision variable.


### 7. Humour, the sacred and the state in South Asia

| Work | What they did | Key finding |
|---|---|---|
| ★ Nair (2023), *Hurt Sentiments: Secularism and Belonging in South Asia*, Harvard University Press ✔ | Comparative legal and political history of India, Pakistan, Bangladesh | "Hurt sentiments" claims and s.295A have been **weaponised by majorities**; censorship disputes shape minority belonging |
| Nair (2013), on the making of s.295A (article the book grew from) ✔ | Archival history | Why colonial India criminalised insult to religious feelings |
| Kaur & Mazzarella (eds., 2009), *Censorship in South Asia: Cultural Regulation from Sedition to Seduction* | Edited anthropology volume | Censorship as a productive cultural practice, not only prohibition |
| Bhatia (2016), *Offend, Shock, or Disturb: Free Speech under the Indian Constitution* | Constitutional law analysis | How Indian courts handle offence, hate speech, sedition and obscenity |
| Siegel (1987), *Laughing Matters: Comic Tradition in India* | Literary history | Long tradition of Indian comic forms (Sanskrit drama's *vidūṣaka* etc.) |
| Khanduri (2014), *Caricaturing Culture in India: Cartoons and History of the Modern World* | History of cartoons | Political cartooning and its controversies in India |

**For us:** this is the Indian institutional context. Nair is essential: the legal route (FIR under s.295A or
its BNS successor) is itself a political tool, which our "who mobilises, through which channel" question tests.


### 8. Indian stand-up comedy

| Work | What they did | Key finding |
|---|---|---|
| ★ (2017), "A new public sphere? English-language stand-up comedy in India", *Contemporary South Asia* (DOI 10.1080/09584935.2017.1321618) ✔ | Analysis of Daniel Fernandes's YouTube videos | English stand-up extends the bourgeois public sphere through satire |
| ★ Bhargava & Singhal (2023), "Stand-Up: The 'Comic' Public Sphere in India", *International Journal of Communication* 17, 5852–5869 ✔ | Analysis of performances (Department of Sociology, South Asian University) | Indian stand-up is subversive but shaped by systems of meaning; the scene is overwhelmingly male |
| ★ Chilana & Bhargava (eds., 2024), *Politics of Recognition and Representation in Indian Stand-Up Comedy*, Palgrave Studies in Comedy ✔ | Edited volume | Chapters on caste, gender, language, surveillance, censorship and trolling; Miller's chapter reads stand-up as a "secular ritual" of the young middle class |
| ★ Shivaprasad (2020), "Humour and the Margins: Stand-Up Comedy and Caste in India", *IAFOR Journal of Media, Communication & Film* 7(1) ✔ | Analysis of comedians' online videos | Indian stand-up is largely **upper-caste**; casteist jokes reinforce stereotypes; very little academic work exists |
| Ambade, "'It's the Way I Tell them about Caste': Dalit stand-up comedy as the performance of resistance" ✔ | Performance analysis | Dalit stand-up as resistance |
| Ahmad (2026), "Can Dalit laugh? Humour as resistance and politics of Dalit-comedy in India", *Comedy Studies* 17(1) ✔ | Digital Dalit comedy | Everyday resistance and the obstacles Dalit comics face |
| Poovaragavan (2026), "Shifting Comforts by Laughing Out Caste", *Economic and Political Weekly* (April) ✔ | Commentary | Dalit stand-up specials and urban middle-class audiences |
| Sarkar & Siraj (2022), "Exploring Indian stand-up comedy through the lens of ideology, identity and gender", *Comedy Studies* 13(1) ✔ | Discourse analysis | Language ideology, identity and gender in routines |
| Ahmad, Alam & Kaur (2022), "Performative retrieving of humour for socio-political subversion", *Cogent Arts & Humanities* ✔ | Case studies (e.g. Kunal Kamra, Rahul Dua), Fiske's theory | Stand-up as creative resilience; harsh censorship on TV vs freer online space |
| Content analysis of profanity in 82 YouTube stand-up videos, *Comedy Studies* (2024) ✔ | Content analysis | Online stand-up departs from strict self-censorship |
| "Spaces of Laughter: Stand-up Comedy in Mumbai as a Site of Struggle", MA thesis, Bowling Green State University (2020) ✔ | Ethnography | AIB Roast (2014–15) debated as "un-Indian" obscenity; boosted stand-up's reach |

**For us:** Indian work so far studies **what comedians say** (public sphere, caste, gender, language) and
celebrates stand-up as resistance. **No study we found compares controversies across cases or explains why
some end in FIRs and others in mobs or nothing.** News and commentary cover Faruqui, Kamra and *Latent*, but
we found no peer-reviewed comparative analysis of them.


### 9. Classifying jokes and reactions

Covered in full in Part C: Allan & Burridge (taboo),
Zillmann & Cantor (disparagement), Ford & Ferguson (prejudiced norms), Martin et al. (humour styles),
Holbert et al. (satire types), and NLP schemes (TRAC, HASOC, SemEval stance, HaHackathon, HateXplain).


### 10. Explaining escalation: scandal, panic, mobilisation, law and platforms

These works explain *why* a controversy escalates and through which route. They form most of our interpretive
toolkit (Part A §5).

| Work | What they did | Key idea we use |
|---|---|---|
| ★ Adut (2008), *On Scandal: Moral Disturbances in Society, Politics, and Art*, Cambridge UP ✔ | Comparative historical study of scandals (Oscar Wilde, Watergate, Lewinsky and others) | A scandal is made by **public accusation and publicity**, not by the transgression itself |
| Thompson (2000), *Political Scandal: Power and Visibility in the Media Age* | Theory and historical cases | Scandals are struggles over symbolic power in mediated visibility |
| ★ Cohen (1972), *Folk Devils and Moral Panics* | Case study of the Mods and Rockers | Stages of a moral panic; folk devils; disproportionate reaction; moral entrepreneurs |
| Goode & Ben-Yehuda (1994), *Moral Panics: The Social Construction of Deviance* | Theory and cases | Criteria for a moral panic: concern, hostility, consensus, disproportion, volatility |
| ★ George (2016), *Hate Spin: The Manufacture of Religious Offense and Its Threat to Democracy*, MIT Press ✔ | Comparative study of India, Indonesia and the United States | Offence is often **manufactured** by political entrepreneurs; laws against offence empower the most intolerant |
| Benford & Snow (2000), "Framing processes and social movements", *Annual Review of Sociology* 26 | Review | Diagnostic and prognostic framing of grievances |
| McCarthy & Zald (1977), "Resource mobilization and social movements", *American Journal of Sociology* 82(6) | Theory | Mobilisation depends on organisations and resources, not grievance alone |
| Tarrow (2011), *Power in Movement* | Comparative theory | Political opportunity: allies in power, elections, openings for action |
| ★ Feeley (1979), *The Process Is the Punishment* | Court ethnography | Arrest, bail and repeated court dates punish even when no conviction follows |
| ★ Udupa (2019), "Nationalism in the digital age: fun as a metapractice of extreme speech", *International Journal of Communication* 13 ✔ | Ethnography of Hindu nationalist online volunteers | Organised online publics use "fun" to mobilise and attack, with deniability |
| Udupa & Pohjonen (2019), "Extreme speech and global digital cultures", *International Journal of Communication* 13 | Special-section introduction | Extreme speech as a cultural practice, not only hate speech |
| Crockett (2017), "Moral outrage in the digital age", *Nature Human Behaviour* 1 | Theory and evidence review | Platforms lower the cost and raise the reward of expressing outrage |
| Brady et al. (2017), "Emotion shapes the diffusion of moralized content in social networks", *PNAS* 114(28) | Analysis of 563,312 tweets | Each moral-emotional word raises sharing, mostly within one's own group |
| Gray (2003), "New audiences, new textualities: anti-fans and non-fans", *International Journal of Cultural Studies* 6(1) | Theory | Anti-fans and fan defence as audience behaviour |
| Benoit (1995), *Accounts, Excuses, and Apologies* | Theory of image repair | Denial, evasion, reducing offensiveness, corrective action, mortification |
| Goffman (1971), *Relations in Public* | Theory | Apologies as "remedial work" that splits the self into guilty and repentant parts |
| Crenshaw (1991), "Mapping the margins", *Stanford Law Review* 43(6) | Legal theory | Intersecting identities shape how people are treated |
| Schauer (1978), "Fear, risk and the First Amendment: unraveling the chilling effect", *Boston University Law Review* 58 | Legal theory | Fear of legal process deters lawful speech |

#### How similar projects interpreted their cases

| Method of interpretation | Source | How we use it |
|---|---|---|
| **Process tracing**: reconstruct the sequence and check which mechanism's expected traces appear | George & Bennett (2005); Collier (2011); Beach & Pedersen (2013) | The timeline (template D) is traced step by step in section H |
| **Rival explanations**: test several explanations against each case | Yin (2018), *Case Study Research and Applications* | Each lens gets a verdict (supported, partly, not supported) with evidence |
| **Analytic eclecticism**: combine theories where outcomes have several causes | Sil & Katzenstein (2010), *Beyond Paradigms* | One "best explanation" paragraph per case, combining lenses |
| Stages of a reaction | Cohen (1972) | Moral-panic lens; typology of escalation paths |
| Who makes the accusation public | Adut (2008) | Scandal lens |
| Who manufactures offence and how the state responds, across countries | George (2016) | Strategic-offence and law lenses |
| Winners and losers of a humour scandal | Kuipers (2011) | Template F |
| Change in humour's function across cases | Ödmark (2021) | Template E |


### 11. Detecting spam and coordinated commenting

Why it matters for us: the strategic-offence and online-publics lenses ask whether backlash was organic or
organised. These works give the methods for telling the two apart. Our implementation is `src/spam.py`.

| Work | What they did | What we take |
|---|---|---|
| ★ Pacheco et al. (2021), "Uncovering coordinated networks on social media: methods and case studies", *ICWSM* 15, 455–466 ✔ | Unsupervised network method: link accounts that share unexpectedly similar behaviour (same text, images, hashtags, timing); five case studies | Co-timing network; text-reuse clusters; "unexpectedly similar" = compare with chance |
| ★ Giglietto et al. (2020), coordinated link-sharing behaviour; CooRnet ✔ | Accounts that repeatedly share the same item within a short window | Repetition across several videos, not one coincidence; our `min_videos = 2` |
| ★ Jakesch, Garimella, Eckles & Naaman (2021), "Trend Alert: how a cross-platform organization manipulated Twitter trends in the Indian general election", *Proc. ACM HCI* 5 (CSCW2) ✔ | Joined 600 pro-BJP WhatsApp groups; found 75 campaigns with lists of **pre-written tweets** | Indian campaigns push identical or near-identical text and hashtags; our copy-paste and hashtag signals |
| ★ Cresci (2020), "A decade of social bot detection", *Communications of the ACM* ✔ | Review | Field has moved from single-account to **group-based** detection; bots evolve, so detectors must be validated |
| Cresci et al. (2023), "Demystifying misconceptions in social bots research" ✔ | Critique | Bot research suffers from hype and bias: report precision, test robustness, avoid overclaiming |
| Alberto, Lochter & Almeida (2015), "TubeSpam: comment spam filtering on YouTube", *ICMLA* ✔ | Classifiers on the labelled YouTube Spam Collection (1,956 comments) | Commercial-spam patterns; YouTube spam is short and full of slang, so rules need human checks |
| Kirdemir et al., "Towards characterizing coordinated inauthentic behaviors on YouTube" ✔ | Multi-layer YouTube method: anomaly and peak detection, rolling correlations, rules | Burst detection on YouTube timelines |
| Shajari et al. (2023), commenter behaviour on YouTube channels; Graph2Vec commenter mobs ✔ | Co-commenter networks over 596,982 comments | Accounts that comment together across videos as "mobs" |
| Survey (2024), "Detection and characterization of coordinated online behavior" (arXiv 2408.01257) ✔ | Review of methods across platforms | Overview of the methods above |

**What we do differently.** These methods were built for Twitter and Facebook with full metadata; YouTube's API
gives less (no follower graph, no IP). We therefore combine several weak signals, require two kinds of evidence
before labelling an account, test the timing signal against shuffled data, rerun under other thresholds, and
validate against human coders.


### Where previous work leaves a gap (our contribution)

1. **Indian stand-up research studies texts, not controversies.** It asks what comics say and whether
   comedy is resistance; it does not compare what happens *after* a joke becomes a scandal.
2. **Humour-scandal research is European and small-n.** Kuipers and Ödmark analyse 1–3 cases mainly through
   news framing, in societies without criminal offence laws used this often.
3. **Nobody links topic, context and outcome type.** No study we found asks why the same society sends one
   joke to the police, another to a mob, and lets a third fizzle.
4. **Theory is rarely tested across cases.** Context collapse and Durkheim are invoked in single cases; we
   apply them systematically across ~25 using one template.
5. **India is a plural society with many "sacreds".** Nair shows how hurt-sentiment claims are used
   politically; we bring that legal-political lens to comedy specifically.

**One-sentence positioning for the paper:** *Building on humour-scandal research (Kuipers 2011; Ödmark 2021)
and the study of hurt sentiments in South Asia (Nair 2023), we offer the first structured comparison of Indian
stand-up controversies, asking which topics draw scrutiny and why controversies end online, in court, or in
the street.*


### Key journals and centres (for further searching)

- *HUMOR: International Journal of Humor Research* (International Society for Humor Studies, since 1988)
- *European Journal of Humour Research*
- *Comedy Studies* (Taylor & Francis)
- Palgrave Studies in Comedy (book series)
- Centre for Comedy Studies Research, Brunel University London
- Search terms that work on Google Scholar: "humour scandal", "comedy controversy", "offensive humour",
  "stand-up comedy India", "hurt sentiments", "295A", "context collapse humour", "online firestorm"

---

## Part E — Decisions log


One entry per decision: date, what was decided, why. Newest at the bottom.
Open items come from Part B Section 14 and are settled in the Step 0 team meeting.

### Open (to decide in Step 0)

| # | Question | Options / recommendation | Decision |
|---|---|---|---|
| 1 | Main question and sub-questions (Part B Section 3) | Approve as drafted, or edit | Approved with topic as the focus (see Decided) |
| 2 | Tell the supervisor about the change in method? | Recommended: send the short note in Part B, Step 0 | Not required (see Decided) |
| 3 | Final submission deadline | Unknown; needed for the timeline | Presentation 14–15 Nov 2026; final paper date still to confirm |
| 4 | Number of cases | 20 / 25 / 30 (recommended: 25) | 24 (see Decided) |
| 5 | Sacred-objects list; do family and parents count? | Confirm list in Part A §5 | Yes, family and parents count (see Decided) |
| 6 | Bundled or non-stand-up cases (`disability_sc_2025`, `tangade_dalit`) | Keep / split / drop | Narrowed to `raina_sma_2025`; `tangade_dalit` dropped |
| 7 | Who reads which languages (Hindi, Telugu, Tamil, Marathi, other) | List per member | Everyone reads Hindi and English (see Decided) |
| 8 | Do the optional interviews? Ethics approval needed? | Yes / no | No (see Decided) |
| 9 | Course AI policy and required disclosure | Check | AI use allowed without limit (see Decided) |
| 10 | Which parts of the existing pipeline to keep | As in Part B, Folder structure, or edit | As in Section 12 (see Decided) |
| 11 | Case owners | Assign after the case list is final | Assigned (see Decided; `analysis/assignments.md`) |
| 12 | Final case list | Suggested 25 in `analysis/case_pool_summary.md`. Given team languages, do **not** swap in the Bengali/Kannada reserves; if more regional cases are wanted, prefer Telugu reserves (`rafiq_2026`, `aadi_2021`) | Final 24 in `analysis/final_cases.csv` (see Decided) |
| 13 | Police action against attackers or threateners (not the comedian): counts as "legal"? | Recommended: no; record in the timeline only | No (see Decided) |
| 14 | Administrative action (demolition, permission refused): legal or separate? | Recommended: legal, sub-label `administrative` | Legal, sub-label `administrative` (see Decided) |
| 15 | Forced or pressured apologies: extra-legal? | Recommended: yes | Yes (see Decided) |
| 16 | Tweets and social-media replies: count as comic performances? | Recommended: no, except as reserves | No, except as reserves (see Decided) |
| 17 | Maximum number of comparison (non-stand-up) cases | Suggested 25 have 4 | 4: parithabangal_2025, jain_univ_2023, kapil_2024, bharti_2022 |

### Decided

| Date | Decision | Reason |
|---|---|---|
| 2026-11-03 | Plan proposed: structured comparative case study (Part B) | Revised proposal's computational method did not fit the data and the scope was too large; pending team approval |
| 2026-11-05 | Havish accepts the plan, except the dark comedy focus | The project studies which **topics** bring comedians under scrutiny; topic is the main comparison and genre (incl. dark comedy) is a recorded secondary variable with no case quota. Part A §3–5, Steps 2, 6, 8 and the template updated |
| 2026-11-05 | The original proposal no longer binds the project | Supervisor said the team is free to choose its direction; a note to the supervisor is optional |
| 2026-11-08 | Part B adopted as the project method: structured comparative case study, general comedy (all genres) with topic as the focus | Team agreed; pipeline parts kept or dropped as in Part B, Folder structure |
| 2026-11-08 | Previous work reviewed in Part D; each part of the method is tied to an earlier study, and borrowed fields added to the case template (performance setting, objector distance, norm invoked, humour function, media frame, complainant and legal basis, winners and losers, comedian's narrative) and to the comment codes (norm invoked, intent attributed) | Supervisor asked us to take inspiration from previous work and show how we use it |
| 2026-11-08 | Discussion section led by findings, structure in Part B, Step 8; introduction opens with *India's Got Latent* and the Rs 370 biryani case | These two cases motivated the project; theories are used where they explain findings, not as a fixed list |
| 2026-11-08 | Work moved to branch `project-plan` for the team to review before merging to main | Everyone verifies before the project starts |
| 2026-11-09 | All 24 case files drafted by AI (status `draft`), with `sources.md`, 139 news articles coded in `news_coding.csv`, and one row per case in `comparison.csv` and `mechanisms.csv`; first-draft `findings.md`. Comment collection and spam audit deferred until Havish and the AI have checked the pipeline together | Havish asked for everything except comments; owners and verifiers now check each draft (Step 5.2, 5.5, 5.6) |
| 2026-11-09 | Case owners: Havish, Yogansh, Pranav, Siddanth own 6 cases each, grouped by matched pairs and theme; verifiers rotate (Havish→Pranav→Siddanth→Yogansh→Havish), and the verifier also does the blind second coding before reading the draft. Owner and verifier written into every `case.md`; table in `analysis/assignments.md` | Even workload; pairs stay with one owner |
| 2026-11-09 | `archive/` deleted (both proposals, demo dashboard, thread analysis and test, dashboard exporter); recoverable with `git checkout 32e24f1 -- archive/` | Team decision: keep only what the current plan uses |
| 2026-11-09 | Repository restructured to Part B, Folder structure: one folder per final case with a pre-filled `case.md` and `sources.md`; analysis tables created (comparison, mechanisms, second coding, findings); earlier proposals, the dashboard and unused scripts moved to `archive/`; merged into `main` | Start the project from a clean layout that matches the plan |
| 2026-11-09 | News protocol added (Part B, News protocol): five outlet types including Hindi and Telugu press and outlets on each side; search terms and window recorded; 6–10 articles per case coded for framing in `analysis/news_coding.csv` (Entman 1993; Semetko & Valkenburg 2000); wire copy counts once; GDELT coverage timing optional (`src/news.py` back in use) | News is the main evidence for facts and a source of framing data; it needed a protocol as clear as the comment protocol |
| 2026-11-09 | Spam and coordination audit strengthened and made mandatory before comments are read: copied comments, hashtag pushes and batch-created accounts added; chance (shuffle) check, sensitivity check and human validation added; co-timing time-unit bug fixed (pandas 3 stored microseconds, so the "one minute" window was about 16.7 hours) | Supervisor asked for strong spam detection; methods follow Pacheco et al. 2021, Giglietto et al. 2020, Jakesch et al. 2021, Cresci 2020/2023 |
| 2026-11-09 | **Final case list: 24 cases** (`analysis/final_cases.csv`): the suggested 25 with no reserves added, minus `banerjee_2024`; `disability_sc_2025` narrowed and renamed `raina_sma_2025`; `tangade_dalit` dropped; 4 comparison (non-stand-up) cases | `banerjee_2024` was kept only if Banerjee proved to be a working comedian; every source describes a Latent contestant and no independent stand-up career was found |
| 2026-11-09 | All 24 cases to be analysed before the 14–15 Nov presentation, not only three pilots | Team decision |
| 2026-11-09 | First deliverable: **presentation on 14–15 November 2026** (plan, framework, previous work, early results). Three pilot cases before then: `latent_2025`, `more_2026`, `kamra_2025` | Five days is enough for three fully verified cases, not the whole project; sprint plan in Part B, Timeline |
| 2026-11-09 | AI use is allowed without limit under the course policy | Disclosure statement kept in the paper for transparency |
| 2026-11-09 | Coding rules: (13) police action against attackers or threateners is **not** "legal", recorded in the timeline only; (14) administrative action (permission refused, demolition, venue sealed) **is** legal, sub-label `administrative`; (15) forced or pressured apologies **are** extra-legal; (16) tweets and social-media replies are **not** comic performances, except as reserves | Recommendations accepted |
| 2026-11-09 | Sacred objects include **the family and parents** | Insult to parents was the core of the *India's Got Latent* backlash; Durkheim's sacred covers what a group sets apart and protects |
| 2026-11-09 | Languages: **everyone reads Hindi and English**. English news coverage is enough for every case; Hindi or regional-language press is optional, used only where it adds a frame English outlets miss. Hindi and Hinglish comments are read by the team directly; Tamil, Marathi and Telugu material with AI translation plus English coverage, noted in the case file | Corrected by Havish; replaces the earlier language entries |
| 2026-11-09 | (Superseded by the correction above) Team languages: Telugu, Hindi and English. Hindi, Hinglish, Telugu and English material is checked by a team member; other languages (Tamil, Marathi, Kannada, Bengali) are read with AI translation plus English-language coverage, and the case file says so | The only clearly non-team-language case in the suggested 25 is Parithabangal (Tamil); it stays, with this limitation stated. Bengali/Kannada reserves are not added |
| 2026-11-08 | Cases interpreted with a full toolkit of lenses (scandal, moral panic, strategic offence, mobilisation, law as a weapon, organised online publics, platform outrage, context collapse, stigma, Durkheim, humour theory, identity and power, fandom, apology), using process tracing and rival explanations; template section H becomes "Interpretation" with a verdict per lens | Interpret through whatever helps answer the research question, as earlier comparative case studies do (George & Bennett; Yin; Adut; George; Cohen) |
| 2026-11-09 | **No interviews** (Step 7 dropped); **no Instagram or Reddit** comments: YouTube comments only. Reddit threads may be read for understanding but are not coded | No time; Instagram comments can only be copied by hand; Reddit's API needs an approved app (the public endpoint returned 403) |
| 2026-11-09 | **Every case starts from the full original clip.** The owner watches the whole performance (not only the viral seconds), copies the YouTube transcript into `data/transcripts/` (git-ignored) and writes a first read in `analysis/first_read.csv` **before** opening the AI draft; links per case in `analysis/clips.md` | The drafts were written from news only; the AI cannot watch video but can read transcripts; context is the core of the project |
| 2026-11-09 | **Blind second coding by verifiers dropped** (`second_coding.csv` replaced by `first_read.csv`). The owner's first read is the independent check; the report gives human–AI agreement per judgement. Verifiers only fact-check | A full blind coding of 6 extra cases is not possible in 5 days; the owner's read before the draft keeps an independent human judgement at no extra cost |
| 2026-11-09 | Findings reframed: "nobody with standing acted" is not an explanation of fizzled cases (it is how the outcome is defined); the question is **why** actors with standing took up some jokes and not others | Avoid a circular headline |
