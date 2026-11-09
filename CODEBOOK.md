# Codebook — Team K

Every joke and comment label, with decision rules and the earlier work each label comes from. Start from [README.md](README.md) for where everything is.

Labels in C1 go into section B of each case file; labels in C2 are
used when reading comments (PLAN.md, Comment protocol). How each label connects to previous work: LITERATURE.md.

Every label below is adapted from earlier work, so our results can be compared with it. Each label notes
its source and what we changed. Full references are in LITERATURE.md and PROJECT.md.

Rules for all coders:
- Code what the text **does**, not what you think the author meant.
- When unsure, pick `unclear` / `none` and add a note. Do not guess.
- Two coders code independently; disagreements are resolved by discussion, then the codebook is updated.
- Target before scaling up: Cohen's kappa ≥ 0.70 per label (`python -m src.sample kappa ...`).


## C1. Joke-level labels (one row per case in `data/cases.csv`)

The study covers **any topic that brings stand-up comedians under scrutiny**. Topic (A2) is the main variable;
genre (A1) records *how* the joke is told, so we can test whether scrutiny follows the topic or the style.

### A1. Genre (more than one allowed)
| Code | Definition | Source |
|---|---|---|
| `dark` | **Both** (1) a grave subject (death, violence, suffering, disease, disability, the sacred, a stigmatised position in a hierarchy) **and** (2) the laugh comes *from* that gravity, not from merely mentioning it | Willinger et al. 2017 |
| `roast` | Mocks a particular person (a celebrity, a guest, an audience member) | — |
| `gallows` | Dark humour told by or for people who are themselves suffering or oppressed | Obrdlik 1942 |
| `satire_juvenalian` | Biting, contemptuous attack on people or institutions with power | Holbert et al. 2011 |
| `satire_horatian` | Gentle, playful mockery of power or social folly | Holbert et al. 2011 |
| `crude_shock` | Transgression mainly for shock (sex, bodily functions, obscenity) | — |
| `observational` | Everyday-life humour with no taboo subject | — |

### A2. Taboo domain (more than one allowed)
`religion` · `caste` · `gender_sexuality` · `family` · `politics_state` · `regional_national_icon` · `celebrity_public_figure` · `bodies_looks` · `death_violence_tragedy` · `disease_disability` · `none`
Source: Allan & Burridge 2006 (taboo domains). **Added for India:** `caste` and `regional_national_icon`.

### A3. Target and direction
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

### A4. Form and technique
- **form**: `standup_set` · `crowd_work` · `roast` · `sketch` · `song_parody` · `social_reply` · `tv_show` · `college_skit`
- **technique** (main one only): `irony_sarcasm` · `exaggeration` · `parody_impersonation` · `wordplay` · `story`
Sources: Long & Graesser 1988; Buijzen & Valkenburg 2004. We use only 5 techniques so that two coders can apply them reliably.

### A5. Context (see proposal Section 2.3, Table 1)
`collapse_type`: `collusion` (the comedian put it out widely) · `collision` (someone else moved or resurfaced it) · `live_only` (no recording).
Also record: `gap_months`, who first reposted the clip, and whether the most-viewed circulating version has a neutral or accusatory title.
Sources: Marwick & boyd 2011; Davis & Jurgenson 2014.


## C2. Comment-level labels (coding sheet from `src.sample sheet`)

### B1. reaction (exactly one)
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

### B2. target
`comedian` · `joke_content` · `offended_group` · `platform` · `state` · `other`

### B3. taboo (taboo the comment invokes)
Same list as A2.

### B4. sacred_object
`deity` · `icon` (Shivaji, Ambedkar, national heroes) · `nation` (army, martyrs, flag) · `none`. Source: Durkheim 1912.

### B5. frame
| Code | Rule |
|---|---|
| `play` | Treats it as a joke: "it's just a joke", "it's comedy", "don't watch if you're offended" |
| `serious` | Treats it as a real insult or crime: "this is not comedy", "hurting sentiments", "should be jailed" |
| `none` | Neither |

Sources: Bateson 1972 ("this is play"); Goffman 1974 (keying).

### B6. stigmatises_comedian
`yes` if the comment attacks the comedian's **identity** (religion, caste, region, gender, sexuality, nationality: "anti-national", slurs) rather than the joke. Otherwise `no`.
Sources: Goffman 1963; Link & Phelan 2001.

### B7. intensity
1 mild disapproval → 5 violent language. Modelled on the offence rating in Meaney et al. 2021.

### B8. pushback_type (replies only, when a reply pushes back against a hostile comment; more than one allowed)
`facts` · `hypocrisy` · `consequences` (warns of consequences, without threats) · `affiliation` (appeals to shared identity) · `denouncing` · `humour_sarcasm` · `positive_tone` · `hostile`
Sources: Benesch et al. 2016; Mathew et al. 2019 (YouTube counter-speech).

### B9. looks_inauthentic
`yes` · `no` · `unsure`. This is human judgement, used to check the automatic flags in `src/spam.py`.

### B10. norm_invoked
The social norm the comment says the joke broke: `religious_feeling` · `national_honour` · `women_dignity` ·
`family_parents` · `caste_dignity` · `decency_obscenity` · `leader_honour` · `none`.
Sources: Rost, Stahel & Frey 2016 (online firestorms as norm enforcement); Durkheim 1912.

### B11. intent_attributed
`harm` (says the comedian meant to insult or hurt) · `joke` (says it was meant as a joke) · `not_stated`.
Source: Graefer & Das 2020 (audiences judge offence by inferred intent and context).


## Language
Comments in Hindi, Hinglish, Marathi, Telugu, Tamil and other languages are coded by a team member who reads that
language. Code-mixed text is normal and not a reason to mark `unclear` (Khandelwal et al. 2018).
