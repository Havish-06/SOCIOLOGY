# Previous work — Team K

The literature review, and how each study shapes our method. Start from [README.md](README.md) for where everything is.

What researchers have already done on humour, offence and comedy controversies, how they did it, what they
found, and where our project fits. Organised into eleven streams, moving from general humour theory to Indian
stand-up controversies.

**How to use this file.** Each stream lists the key works, *what they did* (method and data), *what they
found*, and *what it means for us*. Items marked ✔ were checked against a publisher, journal or library
record on 2026-11-08; unmarked items are standard works in the field that should still be checked before
citing (page numbers, edition). Read at least the starred (★) works in each stream before the write-up.


## Overview: what has been done, in one table

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
| 9. Classifying jokes and reactions | Annotation schemes, NLP datasets | Labelled jokes and comments | Our codebook labels (already in CODEBOOK.md) |
| 10. Explaining escalation | Comparative case studies, ethnography, theory | Scandals, moral panics, offence campaigns, courts, online publics | **Our interpretive toolkit**: why a controversy escalates and through which route |
| 11. Detecting spam and coordination | Network analysis, anomaly detection, classifiers | Social-media accounts and comments | How we tell organic outrage from organised campaigns |


## How previous work shapes our methodology

We do not only cite these studies; each part of our method is borrowed from, or adapted from, a specific
earlier study. The table says what we take and where it appears in our own work (PLAN.md and the case
template `cases/_template.md`).

### Research design

| What we do | Taken from | What exactly we borrow | Where it is in our method |
|---|---|---|---|
| Compare many controversies, each analysed with the same questions | George & Bennett (2005) | Structured, focused comparison | Whole design (PROJECT.md §7) |
| Treat each controversy as a "humour scandal" and ask who mobilised, who gained and who lost | Kuipers (2011), Danish cartoons | The scandal lens: humour regimes, power, winners and losers | Template F: *winners and losers*; SQ3 |
| Code how news outlets framed each controversy: problem, blame, remedy; generic frames | Entman (1993), "Framing: toward clarification of a fractured paradigm", *Journal of Communication* 43(4); Semetko & Valkenburg (2000), "Framing European politics", *Journal of Communication* 50(2) | Frame definition and five generic frames (conflict, responsibility, morality, human interest, economic) | News coding sheet `independent_analysis/news_coding.csv`; PLAN.md, News protocol |
| Compare controversies through how the news framed them, and how humour changes meaning when it changes media context | Ödmark (2021), three Swedish humour controversies | Small-n comparison of controversies; framing analysis of coverage; Meyer's (2000) four humour functions | Template E: *dominant media frame*; *humour function before and after travelling*; SQ2 |
| Include controversies that fizzled, not only escalated ones | Lesson from single-case scandal studies (Kuipers 2011; Klausen 2009), which cannot explain why other jokes did *not* explode | Need for contrast cases | Selection rule in PLAN.md, Step 2 (online-only cases are essential) |
| Matched pairs of similar cases | George & Bennett (2005); Mill's method of difference | Hold most things constant, vary one | PLAN.md, Step 6 (paired comparisons) |

### Variables we record for every case

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

### Reading comments

| What we do | Taken from |
|---|---|
| Comment labels (reaction, target, frame, stigma, intensity, pushback) | CODEBOOK.md, C2: TRAC, HASOC, SemEval stance, Benesch, Mathew et al. |
| Treat comments as evidence of framing, never as public opinion | Lesson from online-outrage research: firestorms are driven by small, vocal groups (Rost et al. 2016) |
| Spam and coordination audit before reading comments: copy-paste, copied comments, hashtag pushes, co-timing, bursts, batch-created accounts; chance check, sensitivity check, human validation | Stream 11: Pacheco et al. (2021); Giglietto et al. (2020); Jakesch et al. (2021); Cresci (2020, 2023); Alberto et al. (2015) |

### Interpreting each case and the results

Cases are not read only through stigma, context collapse and Durkheim. Each case gets a verdict for every lens
in the interpretive toolkit (stream 10 and PROJECT.md §5), using process tracing and rival explanations.


| Question in the discussion | Taken from |
|---|---|
| Do controversies mark the edges of Indian stand-up as a "comic public sphere"? | Public-sphere studies (*Contemporary South Asia* 2017); Bhargava & Singhal (2023) |
| Is backlash a passionate collective reaction that reaffirms a group, and whose group? | Durkheim (1893, 1912); Erikson (1966) |
| Who is allowed to ridicule whom? | Billig (2005); Krefting (2014); Shivaprasad (2020); Ahmad (2026) on Dalit comedy |
| Is the state a neutral referee or an instrument of offended groups? | Nair (2023); Bhatia (2016); Kaur & Mazzarella (2009) |

### What we do differently from them

- **More cases.** Scandal studies usually examine 1–3 cases; we compare about 25 with one template.
- **Outcome type as the thing to explain.** Earlier work describes controversies; we explain why they end
  online only, in court, in the street, or in both.
- **India's plural sacred.** European scandal studies deal with one dominant public; we ask *whose* sacred
  was touched and which group claimed to speak for it.
- **Several kinds of evidence per case.** News, legal records, comments and the comedian's statements,
  not news framing alone.


## 1. Theories of humour: why a joke works or offends

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


## 2. Sociology of humour: humour and social groups

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


## 3. Stand-up comedy as a genre

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


## 4. Offence and the limits of humour

| Work | What they did | Key finding |
|---|---|---|
| ★ Lockyer & Pickering (eds., 2005; 2nd ed. 2009), *Beyond a Joke: The Limits of Humour* ✔ | Edited volume of case studies | Offence is not a property of a joke; the limits of humour are negotiated socially |
| Weaver (2011), *The Rhetoric of Racist Humour* | Rhetorical analysis | How racist humour persuades while claiming "it's just a joke" |
| ★ Graefer & Das (2020), "Towards a contextual approach: audiences, television and 'offensive' humour", *European Journal of Cultural Studies* ✔ | Audience interviews, UK and Germany | People judge offence by **context** (who, where, intent), not by content alone |
| Feinberg (1985), *Offense to Others* | Legal philosophy | When offence (not harm) justifies restricting speech |

**For us:** supports the claim that topic alone cannot explain outcomes; context and who is offended matter.


## 5. Humour scandals and controversies: the closest model for our study

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


## 6. Online outrage, firestorms and context collapse

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


## 7. Humour, the sacred and the state in South Asia

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


## 8. Indian stand-up comedy

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


## 9. Classifying jokes and reactions

Covered in full in CODEBOOK.md: Allan & Burridge (taboo),
Zillmann & Cantor (disparagement), Ford & Ferguson (prejudiced norms), Martin et al. (humour styles),
Holbert et al. (satire types), and NLP schemes (TRAC, HASOC, SemEval stance, HaHackathon, HateXplain).


## 10. Explaining escalation: scandal, panic, mobilisation, law and platforms

These works explain *why* a controversy escalates and through which route. They form most of our interpretive
toolkit (PROJECT.md §5).

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

### How similar projects interpreted their cases

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


## 11. Detecting spam and coordinated commenting

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


## Where previous work leaves a gap (our contribution)

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


## Key journals and centres (for further searching)

- *HUMOR: International Journal of Humor Research* (International Society for Humor Studies, since 1988)
- *European Journal of Humour Research*
- *Comedy Studies* (Taylor & Francis)
- Palgrave Studies in Comedy (book series)
- Centre for Comedy Studies Research, Brunel University London
- Search terms that work on Google Scholar: "humour scandal", "comedy controversy", "offensive humour",
  "stand-up comedy India", "hurt sentiments", "295A", "context collapse humour", "online firestorm"
