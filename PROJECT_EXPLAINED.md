# The project explained from the start — Team K

**Who this is for:** everyone on the team (and anyone new to the project). It explains, in simple words, what we
set out to do, what changed and why, what every term means, how the 24 cases were chosen, what we found, how our
work relates to earlier research, and what we can still improve. Read it top to bottom once; after that, use the
section headings to jump around.

**Written:** 14 November 2026, after all 24 cases were checked by their owners and all key facts were verified.

| Step | What it covers |
|---|---|
| [1. The story](#step-1-the-story-of-the-project) | Our first title and questions, the professor's feedback, what changed and why |
| [2. The questions and terms](#step-2-our-research-questions-and-every-term-in-plain-words) | The research questions today, and every confusing word explained |
| [3. Only controversies?](#step-3-we-only-studied-controversies-so-what-are-we-comparing) | Why we compare controversies with each other, what we cannot claim, and the fix |
| [4. The 24 cases](#step-4-how-we-chose-the-24-cases) | Where they came from, the rules, who was left out, the list and the pairs |
| [5. What we found](#step-5-what-we-found) | The findings, one by one, with examples |
| [6. Earlier research](#step-6-earlier-research-what-exists-and-what-we-missed) | What exists, what we add, and what we missed |
| [7. Problems and improvements](#step-7-problems-and-improvements) | Everything to fix or add, ranked, with a plan |

---

# Step 1: The story of the project

## Stage 1: The original proposal

**Title:** *"How Online Outrage Against Indian Dark Comedy Escalates"*

**The idea:** in a comedy club, the audience has an unspoken deal with the comedian: edgy jokes are fine here. When
a clip goes viral, it reaches people who never agreed to that deal, and trouble starts. But the trouble is
different every time:

- **Kapil Sharma's joke about Atlee** → only online criticism.
- **Munawar Faruqui (Indore, 2021)** → jailed for about a month, for jokes he reportedly had not even told.
- **Vir Das's "Two Indias"** → police complaints (FIRs) and an effective ban in one state.

**Why so different?** That puzzle is the heart of the project, and it has never changed.

**The three original research questions:**

| | In simple words |
|---|---|
| RQ1 | When a dark joke goes viral, what range of reactions appears **in the comments** (support, mocking the offended, anger, the comedian's reply)? Do religious, caste, gender and personal taboos get different reactions? |
| RQ2 | When anger leaves the comment section, does it become **legal** (police, court) or **outside the law** (threats, cancelled shows, attacks), both, or neither? Why? |
| RQ3 | Is the anger in the comments **real and widespread**, or a small loud group? Check it with **a survey** of ordinary viewers |

**Method:** mostly computer analysis of thousands of YouTube comments, plus a survey.

## Stage 2: The professor's feedback

> *"What is dark comedy? Read on sociology of stigma. How do you treat context? Think through the idea of context
> collapse. Read on Durkheim."*

In other words: we used the term "dark comedy" without defining it, and we needed real sociological theory, not only
comment counting.

## Stage 3: The revised proposal (Havish, 2 November)

**New title:** *"Laughter Under Scrutiny: Joke Topics, Public Backlash and the Escalation of Comedy Controversies in
India"*. This is still our title (slightly shortened).

What changed, and why:

- **It answered every feedback point:** dark comedy was defined; stigma, context and Durkheim were added.
- **It widened from dark comedy only to all comedy.** Many of the biggest controversies were not dark comedy at all
  (Kunal Kamra's is political satire; Pranit More's is a roast). Keeping only dark comedy would have thrown away the
  most important cases.
- **It put the joke's topic first** (hence "Joke Topics" in the title).
- **It made the method even bigger:** a machine-learning classifier, bot detection, comment-thread statistics, news
  timing, a 150–300-person survey and a dashboard.
- **It planned "control clips":** for each comedian, a similar joke from the same period that did *not* cause
  trouble. (Remember this; Step 3 is about it.)

## Stage 4: The change to the current method (3–8 November)

When we looked at the actual data, the big computational plan did not hold up:

1. **Comments cannot answer the main question.** *Why* was Munawar jailed and Kapil not? That depends on who
   complained, in which state, at what political moment. Those facts are in **news, police and court records**, not
   in YouTube comments.
2. **The data did not fit the design.** Of 78 candidate videos, 51 were news-channel videos, whose commenters are
   news viewers, not the comedian's audience. One case held about 70% of all comments; several had under 100.
3. **Too much at once.** A classifier, bot detection, a survey and a dashboard in a few weeks would have meant doing
   everything halfway.
4. **The professor wanted theory** (stigma, context, Durkheim), which works best by reading each case closely, not by
   counting labels.

**So we switched to a "structured, focused comparison"** (George & Bennett, 2005), a standard method in social
science: study each case in depth, using **the same template for every case**, then compare the cases side by side.

**Dropped:** the survey (so the original RQ3 is gone), the classifier, the dashboard, interviews, and the control
clips. The comment study was kept "for later" and has not been run.

**Two more changes to the question:**
- **5 November:** Havish asked for **topic** to be the main focus instead of dark comedy. Dark comedy became one
  "genre" recorded for every case.
- The professor said the team is free to choose its direction, and that tweaks to the questions are fine.

## What never changed

The core puzzle: **why do some comedy controversies end with online anger only, while others end in police cases,
threats or jail?** Only the method changed, from counting comments to studying cases in depth.

---

# Step 2: Our research questions, and every term in plain words

## The main question, split in two

> *Which topics bring Indian stand-up comedians under public scrutiny, and when a joke becomes a controversy, why
> does it end so differently (online criticism only, legal action, extra-legal action, or both)? How do the joke's
> topic, its target and its context shape that outcome?*

It is really **two questions joined together**:

- **Half 1, "Which topics bring comedians under scrutiny?":** when comedians get into trouble, what were the jokes
  about? ("Scrutiny" simply means being publicly attacked or questioned for a joke.) This half is a **description**.
- **Half 2, "Why does it end so differently?":** once a joke has caused a fuss, why does one end with only angry
  posts and another with police cases or a smashed venue? Does the **topic**, the **target** (who the joke is aimed
  at) or the **context** (where and how the clip spread) explain it? **This half is the real heart of the project.**

### The four possible endings ("outcomes")

| Outcome | Meaning | Example from our cases |
|---|---|---|
| **Online only** | People criticise online; nothing more | Kapil Sharma on Atlee |
| **Legal** | Police complaint, FIR, court case, a commission's summons | Pranit More 2026: NCW summons, FIRs |
| **Extra-legal** | Outside the law: threats, attacks, forced cancellations, forced apologies | Pranit More 2025: attacked in Solapur |
| **Both** | Legal **and** extra-legal | Kunal Kamra 2025: FIRs **and** the venue smashed by party workers |

**"Escalated"** means anything beyond online only.

## The three sub-questions

**SQ1, Topic.** *What were the troublesome jokes about? Were they aimed at the powerful or the weak? Does the style
of comedy matter?*

**SQ2, Context.** *Does it matter how the clip got out: did the comedian post it, or did someone else dig it up and
spread it?* (Agrima Joshua's Shivaji joke was performed in 2019 and blew up in 2020, when someone resurfaced it.)

**SQ3, Who reacts, and what happens to the comedian.** *Who pushed the anger forward (a party, a religious group, a
government commission, ordinary people)? Through which channel (police complaint, street, social media)? Was the
comedian treated as a bad person, not just as someone who told a bad joke ("stigma")? Did people say the joke
insulted something "sacred", and sacred to whom?*

## Every term, explained

### Topic and genre are different things

**Topic = WHAT the joke is about. Genre = HOW it is told (its style).**

Like films: the topic can be "war", but the genre can be a drama, a comedy or an action film. In the same way, the
topic "politics" can be told as:
- a sharp, mocking attack on a minister → **satire**;
- making fun of a politician's face → **roast**;
- a joke about killings in a riot → **dark comedy**.

### The genres

| Genre | Simple meaning | Example |
|---|---|---|
| **Dark comedy** | Jokes about something **painful or grave** (death, rape, disease, disability, tragedy), where the laugh comes **from** the pain itself, not from merely mentioning it (definition from Willinger et al., 2017) | Neville Shah's caste and disability joke; Madhur Virli's rape joke |
| **Satire** | Mocking **people or institutions with power**, to criticise them | Kunal Kamra's song about Eknath Shinde |
| **Roast** | Mocking **one particular person** (a celebrity, a guest, an audience member) | Pranit More on Veer Pahariya; Kapil Sharma on Atlee |
| **Crude / shock** | Mainly sex, bodily functions or vulgarity, meant to shock | The parents question on *India's Got Latent* |
| **Observational** | Everyday-life humour with nothing taboo | Rare in our cases, because ordinary jokes rarely cause controversies |

**Dark is not the same as offensive.** Dark comedy is about pain or tragedy; a political insult can be offensive
without being dark.

### Punching up and punching down ("direction")

Who does the joke hit, compared with the comedian?

- **Punching up:** mocking someone **more powerful** (a minister, the government, a big celebrity). Usually seen as
  fair ("speaking truth to power"). Example: Kamra mocking Deputy Chief Minister Eknath Shinde.
- **Punching down:** mocking someone **weaker or already disadvantaged** (Dalits, disabled people, victims). Usually
  seen as bullying. Example: Neville Shah's caste and disability joke.
- **Lateral:** mocking someone at the **same level**.
- **Self / own group:** mocking **yourself, your family or your own community**.

Direction is judged against the **local** hierarchy (caste, majority and minority religion, state power), not a
universal one.

### "Sacred"

This comes from **Durkheim**, one of the founders of sociology. Every group has things it treats as **untouchable**,
set apart and protected; insulting them feels like an attack on the whole group, not just an opinion. They are not
only gods.

**Our fixed list:** gods and religious symbols; regional heroes (Shivaji); Ambedkar; the nation; the family and
parents (which is why the *Latent* parents question exploded); and **collective trauma**, added by the team on
12 November: a specific, widely remembered event of mass violence or displacement against a group, and its victims
(for example, the Kashmiri Pandit exodus, the Pahalgam attack, communal riots).

**"Whose sacred?"** asks whether it was sacred to **another group** or to the **comedian's own group**.

### Context collapse

At a comedy club, the audience **chose** to be there and knows it is a joke: that is the context. Online, the clip
reaches **everyone** (family members, political parties, religious groups) who never signed up for edgy jokes. The
context "collapses", and the joke is judged by people it was never meant for (Marwick & boyd, 2011).

### Collusion and collision

The **two ways** a clip escapes the room (Davis & Jurgenson, 2014):
- **Collusion:** the **comedian** put it out widely (uploaded it, posted the reel). Example: Pranit More posted the
  2026 clip himself.
- **Collision:** **someone else** dug it up, cut it or spread it, often much later and often with an angry caption.
  Examples: Agrima's joke resurfaced a year later; Bharti Singh's clip was re-titled "Sikh beard" by re-uploaders.

### Mobilising actor

**Whoever turns anger into action.** Thousands of people can be angry online and nothing happens; someone has to
file the police complaint or lead the protest: a party worker, a religious organisation, a commission such as the
National Commission for Women (NCW).

### Stigma and courtesy stigma

From **Goffman**: a person becomes **"tainted"** in society's eyes: not "they told a bad joke" but "they are a bad
person" (shows cancelled, banned from a state, called "anti-national"). We measure it on a ladder of steps 0–4:
online criticism at the bottom; an FIR or summons is step 3; arrest, ban, assault or venue vandalism is step 4.

**Courtesy stigma:** people **connected** to the comedian are punished too: the venue, the organiser, the audience.
Kamra's venue was demolished in part; after More's 2026 show, an audience member lost his job.

### Labelling

From **Becker**: something becomes "deviant" because people **successfully label** it so, not because of the act
itself. The same joke can be "just a joke" or "an insult to the nation", depending on whose label sticks.

### Benign-violation theory

A theory of why jokes are funny (McGraw & Warren, 2010): something feels **wrong** (a violation) but at the same
time **safe** (benign). In a club, the setting makes edgy jokes feel safe. When the clip goes viral, the "safe" part
disappears and only the "wrong" part remains.

## The whole project in one picture

```
A JOKE (topic, genre, direction, sacred?)
   ↓  told in a room (context)
   ↓  escapes: the comedian posts it (collusion) or someone digs it up (collision)
   ↓  people get angry
   ↓  someone MOBILISES (party, religious group, commission) ... or nobody does
   ↓
OUTCOME: online only / legal / extra-legal / both
   +  STIGMA for the comedian (and the venue, organisers, audience)
```

**Our job:** fill in every box of this chain for 24 real cases, then compare the cases to see which boxes explain
the different outcomes.

---

# Step 3: "We only studied controversies, so what are we comparing?"

This is the most important idea for defending the project.

## Two very different questions

- **Question X:** *"Which topics are risky?"* If a comedian jokes about religion, how likely is trouble?
- **Question Y:** *"Once a joke has already caused a fuss, why does one end with angry posts and another with
  jail?"*

They need **completely different data**.

**An analogy: road accidents.**
- *"Is driving at night dangerous?"* (an X-type question) cannot be answered by looking **only at accidents**.
  Maybe 60% of accidents happen at night, but if 80% of all driving happens at night, night driving is actually
  safer. You need **all trips**, including the millions with no accident.
- *"Among accidents, why do some end with a scratch and others with a death?"* (a Y-type question) can be answered
  by looking **only at accidents**: compare speed, seatbelts, ambulance time.

**Our project mainly answers question Y.** We compare controversies with other controversies.

## What exactly we compare

All 24 cases are controversies, but they **ended very differently**: 5 online only, 8 legal, 4 extra-legal,
7 both. **That difference is what we explain.** Kapil Sharma (a joke on Atlee's looks) ended with online criticism;
Kunal Kamra (a song about Eknath Shinde) ended with FIRs and a smashed venue. Why? That is a real, answerable
question, and it does **not** need ordinary stand-up shows.

**Our sharpest comparisons are the same comedian with different outcomes.** The comedian stays the same, so the
difference must come from the joke or the situation: Kunal Kamra 2018 and 2025; Pranit More 2025 (Solapur) and 2026;
Samay Raina 2025 and 2026; Daniel Fernandes 2024 and 2025.

## What we cannot answer

**Half 1 of the question ("which topics bring comedians under scrutiny") is weak with our data**, for two reasons:

1. **We do not know how many jokes on each topic caused no trouble.** Comedians tell thousands of political,
   religious and family jokes every year, and most cause nothing. Without those, we **cannot** say "religion jokes
   are risky".
2. **We chose the 24 cases to include a mix of topics.** If politics appears often among our cases, that is partly
   because we picked it, not because politics causes the most controversies in real life.

So for half 1 we can honestly say only: *these are the kinds of topics involved when comedy controversies happen in
India* (politics, religion, caste, gender, family, regional icons, disability, collective tragedy). That is a
**description, not a risk ranking**. Our project documents have said this from the start (PROJECT.md: "we cannot
say that a topic is risky in general"), but the title and the first half of the question can make it sound as if we
do. Step 7 suggests a small tweak to the wording.

## Why we did not study ordinary stand-up as well

1. **It is huge.** To say "religion jokes cause trouble X% of the time", we would have to find and label every
   religion joke in a large sample of shows: months of work.
2. **Ordinary jokes leave no trail.** Controversies have news reports, FIRs and court records; a joke that caused
   nothing has none, so we would have to watch everything ourselves.
3. **It was planned and then dropped.** The revised proposal's "control clips" were cut when the method was
   simplified, to save time.

This was a **trade-off, not a mistake**, but it is the **biggest weakness** of the project.

## The fix (doable)

We do not need all of stand-up. A small, targeted version works: **6–8 "same risk, no trouble" cases**, i.e. jokes
with the same ingredients as our troubled cases where nothing happened (for example, viral jokes mocking a
ruling-party politician with no FIR, or popular jokes on religion or caste with no police action). If our main
finding is right, most of these should have escalated too; if many did not, the finding is weaker than we think.
Choosing such "negative cases" is an established method (Mahoney & Goertz, 2004). It is the number one upgrade for
the final paper.

## If we are asked about this

> *"All 24 cases are controversies, so we cannot say which topics are risky in general; that would need jokes that
> caused no trouble. Our question is a different one: among jokes that did become controversies, why did some end in
> online criticism and others in FIRs, threats or arrests? Comparing controversies with each other answers that, and
> comedians who appear twice with different outcomes, like Kamra or More, give the cleanest comparisons. For the
> final paper we plan to add cases with the same risky ingredients where nothing happened."*

---

# Step 4: How we chose the 24 cases

## Chosen on purpose, not at random

- **Random selection** (a lottery) represents everything and suits "how often" questions.
- **Purposive selection** (picking on purpose for variety) suits "why different outcomes" questions.

We chose **purposively**, to get cases that differ in topic, outcome, style, region and year.

## Where the cases came from

1. **Havish's list:** 23 cases collected for the revised proposal (`data/cases.csv`), each fact-checked against news.
2. **Filling the gaps:** an AI search for what the list lacked: dark comedy; cases that **fizzled out online** (so
   that not every case is a big escalation); crude and roast cases; **regional-language** cases (Telugu, Tamil,
   Marathi); and older cases (2018–2019). Total: **45 candidates**.
3. **The rules:** each candidate was checked and marked include (24), reserve (13) or exclude (8). The team fixed
   the final **24** on 9 November (`independent_analysis/case_selection/`).

## The four rules (a case must pass all)

| Rule | Meaning | Why |
|---|---|---|
| (a) | A joke by an **Indian comedian**, or a clearly marked comparison case (TV show, sketch, college skit) | It is a project on Indian comedy |
| (b) | Covered by **at least two independent news sources** (a PTI or ANI story reprinted by ten papers counts once) | So the facts can be checked |
| (c) | Happened **between 2018 and 2026** | Recent, social-media era |
| (d) | **Enough material:** what the joke was, a dated timeline, the outcome | Otherwise the template cannot be filled |

## Who was left out, and why

| Reason | Examples |
|---|---|
| Tweets, not a performance | Several old tweet controversies; a contempt-of-court case over tweets |
| Not a working comedian | `banerjee_2024`: every source describes a contestant on *India's Got Latent*, with no stand-up career |
| The joke was never reported | A 2018 religion case where nobody quoted what was said |
| Too few sources, or outcome unknown | A few thin cases; one with an unnamed performer |
| Languages the team cannot read | Bengali and Kannada cases kept as reserves |
| Adds nothing new | A third Andhra case too close to Katikala and Sarat |

One case was narrowed: Samay Raina's disability case originally bundled jokes by five comedians; it was reduced to
Raina's joke alone (`raina_sma_2025`), because the others were not documented well enough.

## The 24 cases, grouped

(A case can belong to more than one group.)

**Politics: jokes about people in power**

| Case | What happened | Ended |
|---|---|---|
| kamra_2018 | Kunal Kamra's early political satire; a state university cancelled his show | legal |
| kamra_2025 | Kamra's song mocking Deputy CM Eknath Shinde; Shiv Sena workers smashed the venue | both |
| virdas_2021 | Vir Das's "Two Indias" monologue in the US | both |
| rangeela_2021 | Shyam Rangeela imitating PM Modi | legal |
| katikala_2026 | Anudeep Katikala (Telugu) joking about Pawan Kalyan | both |
| sarat_2026 | Sarat Uday (Telugu) joking about Naidu and Lokesh, the same weeks as Katikala | extra-legal |

**Religion and community**

| Case | What happened | Ended |
|---|---|---|
| munawar_2021 | Munawar Faruqui arrested in Indore over jokes on Hindu deities he reportedly had not told | both |
| faruqui_2024 | Munawar's crowd work about Konkani people; threats from BJP MLA Nitesh Rane; forced apology | extra-legal |
| fernandes_2024 | Daniel Fernandes's joke on a Jain practice | extra-legal |
| fernandes_2025 | Fernandes's set touching the Pahalgam terror attack | legal (legal notice) |
| bharti_2022 | Bharti Singh's beard joke on TV, re-titled "Sikh beard" by re-uploaders | legal |
| agrima_2020 | Agrima Joshua's 2019 joke about the Shivaji statue, resurfaced a year later | both |

**Family, sex and crude humour**

| Case | What happened | Ended |
|---|---|---|
| latent_2025 | *India's Got Latent*: Ranveer Allahbadia's question about parents | both |
| sachdeva_2025 | Swati Sachdeva's crude joke involving her own mother | online only |
| more_2026 | Pranit More's crowd work with an audience member (the Rs 370 case) | legal |

**Dark comedy: tragedy, rape, disability, caste**

| Case | What happened | Ended |
|---|---|---|
| virli_2026 | Madhur Virli's rape joke | legal |
| mohanraj_2026 | Aishwarya Mohanraj's dark joke on gender and family | online only |
| raina_sma_2025 | Samay Raina's joke about a baby with a serious disease (SMA) | legal (reached the Supreme Court) |
| shah_2021 | Neville Shah's old joke on caste and disability, resurfaced | online only |
| raina_2026 | A roast with jokes on Biharis and the Kashmiri Pandit exodus | online only |

**Celebrity roasts**

| Case | What happened | Ended |
|---|---|---|
| more_2025 | Pranit More roasted actor Veer Pahariya, then was attacked in Solapur | extra-legal |
| kapil_2024 | Kapil Sharma's joke about Atlee's looks, on TV | online only |

**Comparison cases (not stand-up).** These check whether the same kind of topic draws the same response when the
performer is not a stand-up comedian: kapil_2024 (TV show), bharti_2022 (TV banter), parithabangal_2025 (a Tamil
YouTube sketch on caste → legal), jain_univ_2023 (a college skit mocking Dalits and Ambedkar → both).

## The pairs

Many cases were picked in pairs, so that one thing differs while the rest stays similar:

| Pair | What is similar | What differs |
|---|---|---|
| Kamra 2018 ↔ 2025 | Same comedian, both political | legal vs both |
| More 2025 ↔ 2026 | Same comedian | fans attacked him vs the NCW and police |
| Fernandes 2024 ↔ 2025 | Same comedian | religion vs a national tragedy |
| Katikala ↔ Sarat | Same state's politics, same weeks | both routes vs street only |
| Virli ↔ Mohanraj | Dark jokes on gender | legal vs online only |
| Latent ↔ Raina 2026 | Same show | exploded vs stayed online |
| Munawar 2021 ↔ 2024 | Same comedian | religion vs a regional community |

## Strengths and weaknesses of the selection

**Strengths:** written rules (so nobody can say we picked cases to fit a theory); a lot of variety (topics,
outcomes, 2018–2026, Hindi, Marathi, Telugu, Tamil); built-in pairs; fizzled "online only" cases included on
purpose.

**Weaknesses:**
1. Every case is a controversy (Step 3).
2. The "two news sources" rule favours **famous comedians and big controversies**; a small local case with little
   coverage cannot get in.
3. Topic counts are **designed, not natural**.
4. Only 5 of 24 cases stayed online; more would make the comparisons fairer.

---

# Step 5: What we found

Source files: `independent_analysis/conditions.md` (the main finding) and `independent_analysis/findings.md`
(everything else).

## Finding 1: The topic alone does not decide how a controversy ends

**The same topic ended in opposite ways:**

| Same topic | Escalated | Stayed online |
|---|---|---|
| Sex and parents | latent_2025: FIRs in several states | sachdeva_2025 |
| Violence against women and children (same weeks) | virli_2026: NCW, FIRs | mohanraj_2026 |
| Caste | jain_univ_2023: FIRs, arrests | shah_2021 |

**One exception: politics.** All 10 cases involving politics escalated; none stayed online (Finding 3 explains
why).

**Sometimes the topic was given to the joke by others.** Bharti Singh never mentioned Sikhs (re-uploaders added
"Sikh beard"); Agrima mocked the statue hype and "masterstroke by Modi ji", not Shivaji himself; Munawar's 2024 joke
was about Konkani people, and a BJP MLA turned it into a religious issue. **What a joke is "about" is partly decided
by whoever gets angry about it.**

## Finding 2: Punching up is riskier than punching down

| Direction | Cases | Stayed online only |
|---|---|---|
| Up (mocking the powerful) | 10 | **0** |
| Down (mocking the weak) | 5 | 1 |

In India, a powerful target has people who act for them (party workers, fans, friendly police, state institutions).
A weak group can fight back only if it has an **official protector** (see Finding 3).

## Finding 3 (the main finding): Three "danger signs" in the joke

We looked only at things that can be judged **from the joke itself, before anyone reacts**, so the explanation is
not circular (we do not explain "a complaint was filed" by "someone complained").

| Danger sign | Meaning | Escalated |
|---|---|---|
| **1. Mocks a ruler** | Mocks a leader whose party holds power (in that state or at the centre) | **7 of 7** |
| **2. Targets a defended group** | The group has an official protector in law: women (NCW), Dalits (SC/ST Act), disabled people, notified religious minorities | **5 of 6** |
| **3. Touches someone else's sacred** | Gods, Shivaji, Ambedkar, the nation, the family, a collective tragedy, of a group the comedian does not belong to | **4 of 5** |
| (Touches the comedian's own group's sacred) | Joking about one's own family or community | 0 of 2 |

**Why it makes sense:** anger alone does nothing; someone has to act. The three signs guarantee that someone can:
a ruling party has workers, police and power; a protective law gives a commission or group a ready tool; religious
and community groups can use "hurt sentiments" laws.

**How to state it honestly.** Nineteen of our 24 cases escalated, so a lazy rule ("everything escalates") would also
be right 19 times out of 24. The fair statement is: **when a danger sign is present, escalation followed in 16 of
18 cases, so the signs are almost always enough for escalation; but they are not the only path, since 3 of the 4
cases with no sign also escalated.** In research terms, the signs are close to **sufficient but not necessary**.

**The five cases where the rule fails, and what they teach:**

| Case | Rule said | Actually | Lesson |
|---|---|---|---|
| shah_2021 | escalate (Dalits, disabled people) | online only | A legal tool exists, but **someone must choose to use it**; nobody did |
| bharti_2022 | stay online | FIR | Re-uploaders **added** the Sikh angle |
| faruqui_2024 | stay online | threats | **Who the comedian is** (a Muslim comic jailed in 2021) mattered more than the joke |
| more_2025 | stay online | assault | **Fans** of a film star, a route the rule does not cover |
| raina_2026 | escalate | online only | Mutual roasting on a show whose host is himself a Kashmiri Pandit; the "own group" licence may have covered both comics |

## Finding 4: Who picks it up decides the route

| Who acted | What happened | Cases |
|---|---|---|
| The party ruling the comedian's state | Police and street together → both | kamra_2025, katikala_2026, agrima_2020, munawar_2021 |
| A party with no power in that state | Street only: threats, stage invasion, forced apology | sarat_2026, fernandes_2024, faruqui_2024 |
| An official commission (NCW) | Summons and FIRs → legal | more_2026, virli_2026, latent_2025 |
| Fans | Assault | more_2025 |
| Nobody with standing | Fades within about a week | kapil_2024, mohanraj_2026, raina_2026, sachdeva_2025, shah_2021 |

**The clearest example: Katikala vs Sarat.** Same weeks, both Telugu comics, both mocking Andhra politicians.
Katikala mocked a leader whose party governs Andhra Pradesh: police complaint and a cross-state arrest. Sarat
performed in Bengaluru, outside that party's state: a stage invasion and a forced apology, but no police case.
**Where the joke happens, and who rules there, matters as much as the joke.**

## Finding 5: The sacred opens the legal route; without it, the street

- **All four street-only cases touched nothing sacred.** With nothing to file a "hurt sentiments" case about, angry
  groups used threats and violence instead.
- **Six of the seven "both" cases touched something sacred.** Indian law protects the sacred (hurting religious
  sentiments, national honour, obscenity), so touching it gives people a legal weapon on top of the street.

Durkheim's sacred works in India as a **tool that people use**, not only as a feeling.

## Finding 6: Viral clips strip the context, but that does not decide the outcome

We watched the full performances. In most cases **the viral version had lost the joke's meaning**:
- **virdas_2021:** the negative lines were paired with positive ones, and the piece ended by asking the room to
  applaud India.
- **latent_2025:** the panel immediately mocked the question; the most-viewed clip cuts that reaction.
- **sarat_2026:** the line the hecklers objected to actually praised Naidu.
- **more_2026 is the opposite:** the full version was **worse** than the clip.

**But restoring the full context would not have changed most outcomes** (bharti_2022 led to an FIR although no
community was named). **Context collapse explains why anger starts, not how far it goes.**

**Timing ("waves") matters.** Virli's clip had circulated for about a year with little reaction; it blew up only
during the Pranit More controversy, when people were already looking for similar jokes.

## Finding 7: Who posted the clip matters little

| How it got out | Escalated |
|---|---|
| The comedian posted it (collusion) | 12 of 15 |
| Someone else dug it up (collision) | 6 of 8 |

About the same. What collision changes is **who frames the joke**: re-uploaders add titles like "insults Shivaji
Maharaj" or "Sikh beard" before any objector speaks.

## Finding 8: The punishment is the process, not a verdict

- **No case ended in a conviction.**
- The punishment was **the process itself:** FIRs in several states, summons, police-station visits, jail before bail
  (Munawar spent about a month inside), cancelled shows. Courts often stopped or limited it later. This matches
  Feeley's (1979) idea that "the process is the punishment".
- **Stigma reached step 4** (arrest, ban, assault, venue vandalism) in 8 cases: all 7 "both" cases and more_2025.
- **Courtesy stigma** reached venues, organisers, co-performers or audience members in 11 cases.

## Finding 9: Apologies stop the street, never the police

- **Forced apologies ended street episodes quickly** (faruqui_2024 within a day; sarat_2026 on stage).
- **Once a legal process had started, apologising never stopped it** (more_2026, virli_2026, bharti_2022,
  katikala_2026).
- **Refusing to apologise** ended the matter when no organised group was involved (fernandes_2025) and prolonged it
  when one was (virdas_2021, kamra_2025).

## Finding 10: Genre adds little on its own

- **Dark comedy is not automatically riskier:** of 9 dark jokes, 3 stayed online.
- **Satire ends in "both" more often**, but only because satire targets leaders, and leaders have workers.
- **Dark jokes never led to street action alone;** they went to commissions and courts, or nowhere.

Genre matters **through whom the joke targets**, not by itself.

## The whole answer in one paragraph

> Among these 24 comedy controversies, **the topic alone does not decide how they end**: the same topic ends in
> opposite ways. What matters is **whether someone with power has a reason and a tool to act**, which is almost
> guaranteed when the joke **mocks a ruling-party leader, targets a group the law protects, or touches the sacred of
> a group the comedian does not belong to**. **Who** then acts decides the **route**: ruling parties bring police and
> street together, commissions bring legal cases, groups without state power use the street, and with nobody the
> controversy fades within a week. Viral clips usually strip the joke's context, which explains **why anger starts**
> but not **how far it goes**. And the real punishment is **the process** (FIRs, summons, cancellations): nobody was
> convicted.

## Answers to the research questions, in short

| Question | Short answer |
|---|---|
| **Main** | Topics are varied and do not decide the ending alone; power and protection do (the three danger signs, plus who acts) |
| **SQ1 Topic** | Same topic, opposite endings; only politics always escalated. Punching up is riskier than punching down. Genre adds little |
| **SQ2 Context** | Clips usually lose the context, but that explains the start, not the outcome. Who posted it matters little; waves and re-uploaders' titles matter |
| **SQ3 Who and stigma** | Who acts decides the route. The sacred gives a legal weapon. The punishment is the process. Venues and audiences are punished too |

---

# Step 6: Earlier research: what exists, and what we missed

Full list with references: [LITERATURE.md](LITERATURE.md).

## Why it matters

Every project must answer: *what do we already know, and what are you adding?* If someone already did the same
study, ours adds nothing; if we ignore important earlier work, it shows.

## What we use, in five buckets

**1. Why jokes are funny and why they offend**

| Work | What it says | How we use it |
|---|---|---|
| McGraw & Warren (benign violation) | A joke is funny when something is wrong but feels safe | Why a joke fine in a club offends online |
| Lockyer & Pickering; Graefer & Das | Offence depends on who tells the joke, to whom and where, not only on the joke | Finding 1: same topic, different endings |
| Billig; Kuipers | Humour draws group boundaries: "us" who laugh, "them" who are mocked | Why "whose sacred" and "own group" matter |

**2. Dark comedy specifically.** There is **very little research on dark comedy controversies**. Most research on
dark humour is psychology about **who enjoys it**:
- **Willinger et al. (2017):** experiments; define dark humour (a grave subject, with the laugh coming from that
  gravity) and find that people who enjoy it tend to score higher on intelligence and lower on aggression. We use
  their definition.
- **UK and German audience studies** (Graefer & Das; Birmingham City University and Leicester): most people think
  blasphemy, disability and the Holocaust are off-limits on TV, but who tells the joke and where changes the
  judgement; offence is more likely when a majority mocks a minority.
- **A 2026 study of YouTube Shorts:** dark humour draws more mixed and more toxic comments than other humour.
- **Goswami & Shruthi (2024):** dark humour in Bollywood films (not stand-up); cited in our original proposal.

**Nobody has studied why dark comedy controversies end differently.** This is one reason the project moved from
"dark comedy" to "all comedy, with genre recorded".

**3. Comedy controversies and scandals (closest to us)**

| Work | What they did | How we differ |
|---|---|---|
| Kuipers (2011) | The Danish Muhammad cartoons: a humour scandal reveals clashing groups and power | One case, Europe |
| Ödmark (2021) | Three Swedish cases: humour moved to a new media context fuels controversy | Closest model to our design, but 3 cases and news framing only |
| Marwick & boyd; Davis & Jurgenson | Context collapse; collusion and collision | Our SQ2 comes from this |
| Rost et al. (2016) | Online outrage as enforcement of social norms | Fits Durkheim: punishment unites the group |

**4. India: the law, the sacred and the state**

| Work | What it says | How we use it |
|---|---|---|
| Nair (2023), *Hurt Sentiments* | India's "hurting religious sentiments" law (s.295A) has been used as a political weapon, often by majorities | Finding 5: the sacred as a tool |
| Bhatia (2016) | How Indian courts handle offence, obscenity and sedition | Legal background |
| Feeley (1979) | "The process is the punishment" | Finding 8 |

**5. Indian stand-up comedy:** Bhargava & Singhal (2023): stand-up as a "comic public sphere" for criticising
power; Chilana & Bhargava (eds., 2024): caste, gender, censorship and trolling; Shivaprasad (2020): Indian stand-up
is largely upper-caste; Ahmad, Ambade: Dalit comedy as resistance; Sarkar & Siraj (2022): ideology, identity and
gender.

**The pattern:** Indian research studies **what comedians say** and often celebrates comedy as resistance. **Nobody
compares what happens after a joke becomes a controversy.** A fresh search on 14 November found single-case papers
(for example on Vir Das), legal commentary (Vidhi Legal Policy's "Laughing Under Law") and journalism (ThePrint's list
of comedians in trouble), but **no peer-reviewed comparison of Indian comedy controversies**.

## What we add

> **The first structured comparison of Indian comedy controversies: across 24 cases, it asks why some end with
> angry posts, some in police cases and some in the street.**

Compared with earlier work: 24 cases instead of 1–3; the **outcome** is what we explain; India's many "sacreds"
(we ask *whose* sacred); and we watched the **actual clips**, not just news reports.

## What we missed (none of it on purpose)

**1. Three works from our own original proposal are no longer cited** (the professor has seen them):
- **Kodavanti (2024)**, "Sedition and Comedy: The Weaponization of the State against Humor": directly about the
  state using law against comedians.
- **James (2022)**, on caste and media in Mumbai's comedy circuit, in ***Punching Up in Stand-Up Comedy***
  (Bhargava & Chilana, eds., Routledge, 2022), the book behind our "punching up" idea, which is not cited either.
- **Goswami & Shruthi (2024)**, dark humour in Bollywood black comedies.

**2. Methods works on our biggest weakness (Step 3):**
- **Geddes (1990)**, "How the cases you choose affect the answers you get": studying only cases where something
  happened can give wrong answers. Lets us name and cite our limitation.
- **Mahoney & Goertz (2004)**, the "possibility principle": how to choose "nothing happened" cases properly, by
  picking ones where trouble *could* have happened.
- **Ragin (QCA)**: comparing cases by **combinations of conditions**, in terms of "sufficient" and "necessary". Our
  danger-signs analysis is essentially this without the name.

**3. Political science on why ruling parties make the police act** (used as analogies, since they study riots, not
comedy):
- **Wilkinson (2004)**, *Votes and Violence*: whether police act in communal conflict depends on the state
  government's political interests (fits Katikala vs Sarat).
- **Brass (2003)**: organised networks that can produce outrage when it is politically useful.
- **Jaffrelot (2021)**, *Modi's India*: the rise of vigilante groups acting alongside the state (fits the
  extra-legal route).

**4. Indian free-speech data:** the Free Speech Collective's tracker and yearly reports (its 2025 report counts 14,875
free-speech violations that year; not confirmed whether comedians are listed separately), and Vidhi Legal Policy's
analysis of the laws used against comedians.

**5. Dropped on purpose (fine):** the original proposal also cited Noelle-Neumann (spiral of silence), Inglehart and
Mannheim (generations and values), and Hox and Bonikowski & Nelson (computational text analysis). They supported the
survey and the large-scale comment analysis, which were dropped, so these works went with them.

---

# Step 7: Problems and improvements

## Before the presentation

| # | What | Why | Effort |
|---|---|---|---|
| 1 | **Restate the main finding:** "the danger signs are almost always enough for escalation (16 of 18), but not the only path (3 of 4 cases without them also escalated)"; add a **truth table** (each row a combination of signs, with how many cases escalated) | "19 of 24" alone is no better than "everything escalates" | 30 min |
| 2 | **Tweak the main question** to match what we answer, e.g. "*What topics are involved when* Indian stand-up comedians come under public scrutiny, and why do these controversies end so differently…", and say on a slide that we compare controversies, so we cannot rank topics by risk | The current wording sounds like "which topics are risky" | 10 min, team decision |
| 3 | **Update the status line of `findings.md`** (it still says "awaiting human verification" and points to the deleted drafts) | Out of date | 5 min |
| 4 | **Add the missing works** from Step 6 (Kodavanti, James, the *Punching Up* book, Goswami & Shruthi, Geddes, Mahoney & Goertz, Ragin, Wilkinson) | The professor knows the first ones; the rest strengthen the method and the findings | 20 min |
| 5 | **Do not oversell:** call "own group never escalates" (2 cases, noticed after looking) a possible pattern; make no strong claims from the news-framing table, which the AI coded from headlines only | Honesty | none |
| 6 | **Slides** | See the outline below | |

**Suggested slides:** (1) the puzzle: Kapil vs Munawar vs Kamra; (2) what changed and why; (3) how the 24 were
chosen, and the pairs; (4) same topic, opposite endings; (5) punching up is riskier; (6) the three danger signs, with
the truth table; (7) who acts decides the route: Katikala vs Sarat; (8) viral clips strip the context, but that does
not decide the outcome; (9) the process is the punishment; (10) limitations and next steps.

## For the final paper

| # | What | Why | Effort |
|---|---|---|---|
| 7 | **Add 6–8 "nothing happened" cases** with the same danger signs, chosen by the possibility principle | Fixes the biggest weakness; tests whether the signs really predict trouble | 1–2 days |
| 8 | **Blind check of the danger signs:** two members label the signs for all 24 jokes from the joke only, without the outcome; compare with Cohen's kappa (`src/sample.py`) | The signs were labelled by AI knowing the outcomes (hindsight risk) | half a day |
| 9 | **Test the "wave":** did similar jokes escalate more after *India's Got Latent* (February 2025)? | A rival explanation: the climate got stricter | a few hours |
| 10 | **Read 20–30 news articles in full** and check the headline-only coding | Makes the media findings usable | half a day |
| 11 | **Decide on the comment study:** run it on 3–4 cases (the code works; tests pass) or drop it formally | It is promised but not done | 1 day, or none |
| 12 | **Follow up the court cases:** quashed, stayed or pending? | Turns "the process is the punishment" into numbers | half a day |

## Optional

- Add 2–3 more cases that stayed online only (only 5 of 24 did).
- Background numbers from the Free Speech Collective.
- A timeline chart of all 24 cases (shows the 2025–26 cluster).
- A practical section: what comedians, venues and platforms can learn (promised in the original proposal).

---

## Sources consulted for Step 6 (14 November 2026)

- [Chilana & Bhargava (eds., 2024), introduction (Springer)](https://link.springer.com/chapter/10.1007/978-3-031-39427-0_1)
- [IIS University Journal of Arts (2024), paper on the Vir Das case](https://iisjoa.org/sites/default/files/iisjoa/April%202024/7th%20Paper.pdf)
- [Shivaprasad (2020), "Humour and the Margins", IAFOR](https://iafor.org/journal/iafor-journal-of-media-communication-and-film/volume-7-issue-1/article-2/)
- [Vidhi Legal Policy, "Laughing Under Law"](https://vidhilegalpolicy.in/blog/laughing-under-law-free-speech-stand-up-comedy-and-the-limits-of-criminal-regulation-in-india/)
- [ThePrint, comedians who got into trouble](https://theprint.in/india/no-laughing-matter-all-the-comedians-who-got-into-trouble-for-trying-to-be-funny/580663)
- [Free Speech Collective, "Free Speech in the States" (2023)](https://sabrangindia.in/wp-content/uploads/2023/11/Free-Speech-In-The-States-6Nov23-A-Free-Speech-Collective-Report.pdf)
- [Graefer & Das (2020), "Towards a contextual approach"](https://openresearch.surrey.ac.uk/esploro/outputs/journalArticle/Towards-a-contextual-approach-Audiences-television/99512495502346)
- [Birmingham City University, "Only joking! Offensive humour on television"](https://www.bcu.ac.uk/news-events/news/humour-offence-television)
- [Levinson, "Taking offense seriously"](https://www.israeli-humor-studies.org/media/2-taking_offense_seriously-a_v_levinson.pdf)
- [arXiv (2026), dark humour on YouTube Shorts](https://arxiv.org/abs/2606.00046)
- [Human Rights Watch (2016), India's speech laws](https://www.hrw.org/news/2016/05/24/how-indias-archaic-laws-have-chilling-effect-dissent)
