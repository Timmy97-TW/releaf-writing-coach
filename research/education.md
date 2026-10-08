# Best Education casebook

Six winning Education pages, 2023 to 2025, read for how they are written. The
excerpt bank is `education.excerpts.json` (35 passages). Line numbers below
refer to the files in `sources/text/`.

| Year | UG | OG |
|---|---|---|
| 2025 | Queens-Canada (`edu-2025-UG-queens-canada.md`) | Heidelberg (`edu-2025-OG-heidelberg.md`) |
| 2024 | CityU-HongKong (`edu-2024-UG-cityu-hongkong.md`) | Aachen (`edu-2024-OG-aachen.md`) |
| 2023 | IISER-Pune-India (`edu-2023-UG-iiser-pune-india.md`) | EPFL (`edu-2023-OG-epfl.md`) |

Excerpt convention: most excerpts are models. Some show a mistake that even a
winner made. Their `why_it_works` starts with "Counter-example:" so the mock
page can file them as mistake tips. The schema is unchanged.

ReLeaf context, from the 4 Oct draft (`1008 Engagement/Education /Education Wiki.docx`):
the page is organised by audience (elementary, junior high, high school), with
lesson plans and slides as downloads, pre- and post-surveys per trial, and a
table of issues raised by students and teachers with the change made for each.
That table is already closer to what judges want than most of these winners.
The comparisons below say where.

## Criteria

The 2026 ballot (`judging-special-prizes.md`, "Best Education") asks four
questions. The prize text adds two conditions: the activity must promote
scientific learning and must not market iGEM or synthetic biology, and the page must
"Document your approach and what everyone involved learned."

1. Mutual learning: how well did the work promote mutual learning or a dialogue?
2. Build-on: is it documented in a way that others can build upon?
3. Implementation: was it thoughtfully implemented?
4. Participation: will the activities enable more people to shape, contribute to, or participate in synthetic biology?

### Where each winner answers the ballot

| Team | Mutual learning | Build-on | Implementation | Participation |
|---|---|---|---|---|
| Queens 2025 UG | A labelled "Learning & Dialogue" field in all 17 entries. Mostly asserted. Real cases: WiSE (assumption about young children overturned, l.58), APSC 103 (informal student feedback, l.157) | A "Future Directions" field in every entry; lesson plans, slides and kits donated to Let's Talk Science (l.19); four transition manuals; two YouTube tutorials | Age ranges, station timings (l.92), a mid-activity rule change and rotating mentors (WiSE, l.51); credits the 2022 UBCO workshop it adapted (l.12) | "over 22,000 people" (l.6); low-cost DIY kits; workshops for Girl Guides; engineering students via a first-year course |
| Heidelberg 2025 OG | Three student quotes (l.243–247); the mRNA misconception at the booth (l.315); the pub quiz missed its audience (l.302); an industry workshop changed the team's project page (l.335) | Learning platform on its own wiki page; Regional Guide PDF; game materials PDF (l.320); panel on YouTube; lecture series and summer school handed to next year's team | Each activity traced to an expert insight; summer school written day by day (l.363–374); before/after measurement (l.316) | Free online platform; regional guide to support networks; English-language pub quiz for international students; street booth |
| CityU 2024 UG | Opening questions put to 4–6 year olds (l.32); parents' questions (l.33); Kahoot quizzes (l.70, l.85); 70% top rating, 85% "gained new insights" (l.71) | Activity handbook in six languages with materials list (l.38); comic and board game downloads; three handbooks for undergraduates | "Why did we reach out to them?" per audience (l.27, 54, 99); trilingual sessions (l.31); content tied to the local DSE exam (l.85) | 179 students in Kazakhstan (l.59); participants from eleven countries (l.71); translations |
| Aachen 2024 OG | Feedback changed the format twice: hybrid, then asynchronous video (l.81); a professor's suggestion became Colab support (l.70); eleven viewer comments and an expert statement (l.162–189) | Full GitLab repo with tutorials, solutions, build logic and scripts (l.191); step-by-step "Try It Out Yourself" (l.73–74) | Prerequisite analysis (l.37–41); a teaching version cut to 1,411 lines from 5,287 (l.43); skeleton code with automatic error checks (l.63–67) | Colab removes the hardware barrier (l.70); self-paced video for learners worldwide (l.81); entry level stated as basic Python (l.41) |
| IISER Pune 2023 UG | One sentence naming "a bidirectional learning process" (l.59); a debate that showed students' view of aviation fuel (l.111); a public survey (l.135) | Activity book link; YouTube video; dictionary in Indian languages; survey editions on another page | Audience categories tied to SDGs; partner clubs for underprivileged children (l.65); judged competitions | Survey in five Indian languages (l.135); 250+ art entries; 100+ students in biomimetics; ~30 teams at a wiki workshop |
| EPFL 2023 OG | A quiz after the school visit, result not given (l.62); open discussion; BioQuest feedback "positive" (l.76) | BSGV page with video courses and competition documents (l.28); BioQuest GitLab repo with README (l.44–45) | A six-week mini-iGEM for high schools with videos and online support (l.22–24); a simplified wiki with dictionary (l.50) | A regional high-school competition meant to run yearly (l.26); open-source game; a high school helped toward iGEM 2024 (l.76) |

### How they show what participants learned

| Team | Participant learning | Team learning | Measurement |
|---|---|---|---|
| Queens | Asserted in every entry; "Teachers reported increased curiosity" (l.17) without data | Explicit in WiSE (l.58), QUEMA (l.139), Pipetting video (l.184) | None reported. Two entries propose pre/post assessment as future work (l.39, l.98). Numbers are reach: 22,000 people, ~6,000 and ~10,000 impressions, 200 views |
| Heidelberg | Student quotes with a before and after in them; booth self-assessment | Pub quiz audience, mRNA misconception, pitch simplification (l.323), ATMP workshop (l.335) | Before/after self-rating: interest +20%, knowledge +56.3%, p < 0.01 (l.316, caption l.318). No n. Summer school, lectures and platform have no counts |
| CityU | One participant quote naming what she learned (l.72); one teacher quote (l.85) | Little. The handbook came from noticing local workshops are rare (l.36) | 70% and 85% from the online talk, no n. Kahoot results never given |
| Aachen | Viewer comments; one expert statement | Format changes driven by feedback (l.81) | View counts only, and two different ones (1,567 in the header, 2,920 at l.162) |
| IISER Pune | "they enjoyed the session and learned a lot" (l.116) | One sentence (l.59), the debate (l.111) | Entry counts for competitions. Survey results described as "really great" (l.136) |
| EPFL | "The feedback from the students was positive" (l.62) | Not stated | A quiz without a reported score |

Only Heidelberg measured learning and reported it with numbers. Only Aachen
and Heidelberg show feedback changing what the team built. Every other "we
learned from them" claim on these pages is a sentence without an example.

## Queens-Canada 2025 UG

### Page anatomy

About 5,600 words, nothing folded. Organised by learning style.

1. Education: tagline and three opening paragraphs (~205)
2. Kinesthetic Learning (~2,820): Let's Talk Science kits, three workshops (~690); QSEA (~285); WiSE Workshop (~635); KCHC Workshop (~310); Mini Q (~245); DIY Lab Handbook (~355); Lab Workshop (~300)
3. Auditory Learning (~1,520): Genes to Genius (~265); Science Fair (~260); Healthcare & Business Conference (~380); Exploring Medicine Association (~310); Applied Biotechnology Club Conference (~305)
4. Reading/Writing Learning (~380): APSC 103 (~280); Transition Manual Handbooks (~100)
5. Visual Learning (~570): Protein Modelling tutorial (~275); Pipetting tutorial (~295)

### How it opens

Three paragraphs. The first argues that synthetic biology needs input from
everyone it affects (excerpt queens-01). The second gives the organising idea:
people learn differently, so the page is sorted by kinesthetic, auditory,
reading/writing and visual. The third gives one reach number, 22,000 people.
The reader knows the purpose, the structure and the scale in about 200 words.

### Entry template

Every entry uses four labelled fields, always in this order:

```
### [Activity name]
Description: [Partner] + [audience with age range] + [what they did, with materials, timings, numbers].
Knowledge Gap: [What this group lacks or misbelieves] + [why it matters] + [how this activity addresses it].
Learning & Dialogue: [What participants did that shows learning] + [questions they asked] + [what the team learned].
Future Directions: [What is documented and where] + [how another team can reuse it] + [what we would change].
```

The template is the page's main strength. A judge can find "dialogue" and
"build on" in the same place in every entry.

### Evidence and numbers

Numbers describe reach and logistics: 22,000 people, 50 Girl Guides, 70
conference attendees, 200 views, 6,000 and 10,000 impressions, station times
of 20 to 25 minutes. The one statistic about people is about the team itself:
61% of members identify as women (l.53). No entry reports what participants
knew before and after. The Learning & Dialogue fields describe what the
activity was designed to produce ("Students develop technical competencies",
l.96) and present it as an outcome.

### Reuse

Strong on paper. Lesson plans, slide decks, templates and kits donated to Let's
Talk Science (l.19). A DIY lab handbook. Four transition manuals named by role
(l.164–167). Every entry ends with how another team could run it again. Some of
this is still planned: Workshop 2 materials "are documented for upload" (l.30).

### Voice, person, tense

"We", "our team" and "QGEM" mixed in the same entry. Descriptions in present
tense ("introduces", "guides"), events in past tense, APSC 103 in future tense
because it runs in Winter 2026. Register is earnest and even.

### What it folds

Nothing. Every entry is flat and full length, so the page is long and the
template's repetition is visible.

### Where it is weak

- Learning & Dialogue is asserted. "Teachers reported increased curiosity and clearer student language" (l.17) has no number and no quote.
- Reach is offered as dialogue. Genes to Genius claims "genuine dialogue" and "mutual learning" from 6,000 impressions (excerpt queens-07).
- One paragraph says everything twice. The QHBC Knowledge Gap (l.126) repeats its two points in the second half (excerpt queens-05).
- The 22,000 figure has no breakdown. The page's own numbers add up to about 16,000, most of them social media impressions.
- The four learning-style headings carry little. A science fair sits under "Auditory", and internal team manuals sit under "Reading/Writing". Learning-styles theory also has weak research support, which an education judge may know.
- Future Directions often lists what future teams "could" do. None of these has an owner or a date.
- Typos a proofread would catch: "Lets Talk Science" (l.9), "demonstrate that broaden" (l.15), "the basics DNA" (l.12), "brake down" (l.102), "is has been" (l.151).

### What ReLeaf could take

- The fixed four-field entry. ReLeaf's audience sections could use the same four labels inside elementary, junior high and high school.
- Knowledge Gap written per audience, naming what that age group lacks.
- Future Directions that lists file names and where they live.
- The WiSE reflection pattern (excerpt queens-04): we assumed X, other events showed Y, so next time Z.
- Avoid: reach numbers in the Learning field, and any claim of learning without a survey number or a quote. ReLeaf has pre/post data, so it can do better here.

## Heidelberg 2025 OG

### Page anatomy

About 7,500 words of body text. Two subgoals, eight activities.

1. Two-paragraph abstract, one per subgoal (~200)
2. Our Motivation: why translation needs young scientists; folded expert quotes (~330)
3. Overview of our Projects: tile navigation (~30)
4. Subgoal 1, Empowering Today's Researchers to Think Translational (~75 intro, network map)
   - Panel Discussion: result bullets; events leading up (~390); the event (~85); content and impact (~120); panelists' points, folded (~325); feedback from the audiences, folded (~325)
   - Regional Guide to Scientific Translation: bullets; journey (~280); what we made (~100); why it matters (~80); contents (~440); outlook (~145)
   - Social Dialog: bullets and intro (~170); Science Pub Quiz (~215); Workshop Booth with before/after figure (~380); Ideas Competition (~190)
   - Industry x Academia: intro (~135); ATMP workshop and folded case study (~380)
5. Subgoal 2, Where Tomorrow's Scientists Begin (~70 intro)
   - Summer School (~270, then Day 1–3 ~200)
   - Interactive Learning Platform (~380, then two educator statements ~155)
   - Friday Lecture Series (~215, then six speaker cards ~790)
   - High School Workshops (~375, then educator statement ~100)
6. Closing motto (~45)

### How it opens

With an abstract. Two short paragraphs, one per subgoal, each naming every
activity in it (excerpt heidelberg-01). Then a motivation section built on
quotes from senior figures. A reader who stops after the first screen knows
all eight activities.

### Entry template

```
## [Activity]
- We [did X], reaching [number]
- We created [artefact or format]
- We [intended learning outcome]
[Stakeholders who contributed]
Why: [the expert or interview that raised the need] + [our own experience of the gap]
What we did: [format, venue, date, partners]
What happened: [number] + [a specific moment, question or misconception]
What participants learned: [quotes, or a before/after measure]
What we learned / what changed: [one sentence]
Materials: [PDF or link, in a dropdown]
Next: [who continues it, and when]
```

The three bullets at the top of each section are the most copyable device on
any of these pages (excerpt heidelberg-02). Each section can be skimmed in
three lines.

### Evidence and numbers

The best measurement in the set. At the booth, visitors marked interest and
self-assessed knowledge on a graph before and after the game; interest rose
20% and knowledge 56.3% (excerpt heidelberg-05). The figure caption names the
test. Three student quotes each contain a before and after ("I hadn't focused
much on regulation... but I realized", excerpt heidelberg-03). The page also
introduces its quotes with a line worth stealing: "Rather than describing how
great it was, we would like to share how our audience described its impact"
(l.240).

Weak points in the evidence: no number of booth participants; the figure
caption says the points were extracted from a photo of the paper graph and
tested with an unpaired test, though the same people rated before and after;
"self-assessed" knowledge is not tested knowledge. The summer school, lecture
series and learning platform give no attendance or usage counts, only "all
spots filling up instantly" and students who "traveled over an hour by train".

### Reuse

The learning platform has its own wiki page. The Regional Guide and the booth
game are PDFs. The panel is on YouTube. The summer school and lecture series
are partnerships already booked for next year's team (l.362, l.437). Two
educators are quoted on using the platform in teaching (l.425, l.429).

### Voice, person, tense

"We" throughout, past tense for events, present for the platform and guide.
Confident and warm. Many sentences open with "We".

### What it folds

Expert quotes, the panelists' main points, the student quotes, the industry
case study, and the PDFs. The argument for each activity stays flat; the
supporting quotes open on demand.

### Where it is weak

- Long. Subgoal 1 carries an industry workshop and a pitch competition win that read as entrepreneurship or IHP. A judge may ask what was taught.
- Stock words: "inspir-" appears 20 times and "next generation" 9 times.
- Paragraph order in the High School Workshops entry: verdict first, outcome second, then the Q&A that came before both (excerpt heidelberg-09).
- Mr. Schonert's platform feedback is paraphrased (l.429). A quote would carry more weight. He also appears twice, for two different activities.
- Small inconsistencies: "realised" (l.111) and "realized" (l.210); "dialog" and "dialogue"; "we are planning to organizing" (l.288).

### What ReLeaf could take

- The three result bullets at the top of each audience section.
- The before/after method sentence followed by the result sentence. ReLeaf already has pre/post surveys; it should copy the clarity and avoid the gaps: give n for pre and for post, and say whether the comparison is paired.
- The "Rather than describing how great it was" line, followed by student quotes.
- The misconception paragraph (excerpt heidelberg-04): one specific thing the audience believed, what was shown, what the team concluded.
- The limitation sentence (excerpt heidelberg-06).

## CityU-HongKong 2024 UG

### Page anatomy

About 3,540 words. Organised by audience, which makes it the closest match
to ReLeaf's page.

1. Title, tagline "Spot the Fake. Safeguard the Cure.", contents list (~120)
2. GOAL (~115)
3. Children: Why did we reach out to them? (~70); What did we do? Four entries: charity workshop (~215), activity handbook (~180), comic book (~110), board game (~155)
4. High School Students: Why (~90); six entries: summer camp (~120), online talk (~410), biosensor video (~315), Cognitio workshop (~235), UCCKE workshop (~205), postcard exchange (~240)
5. University Students & General Public: Why (~95); three handbooks (~235, ~210, ~170)

### How it opens

A tagline from the project, then a GOAL paragraph in general terms ("we invite
you to join us on an exciting journey", l.24). The page only becomes specific
at the first audience section.

### Entry template

```
# [Audience]
## Why did we reach out to them?
[What this group lacks] + [our goal for them]
## What did we do?
## [n]. [Activity name] ([partner])
[Date] + [partner] + [participants, ages, language]
[What we taught, with the actual questions or curriculum topics]
[The hands-on activity]
[How they engaged: questions asked, quiz, rating]
[Download or link]
```

The two fixed sub-headings per audience ("Why did we reach out to them?",
"What did we do?") are simple and easy to copy (excerpt cityu-01).

### Evidence and numbers

Specific where it is good: 179 students online, eleven countries, 70% gave the
top rating and 85% reported new insights, a named student's quote (excerpt
cityu-03). The children's workshop quotes the actual opening questions (excerpt
cityu-02). Missing elsewhere: no headcount for most workshops, no base for the
percentages, and Kahoot quizzes run "for students to know how much they
learned" without results (excerpt cityu-06).

### Reuse

The activity handbook is the model: written for event organisers, in six
languages, with a materials list and procedures (excerpt cityu-04). The comic
and board game are downloads.

### Voice, person, tense

"We" and "CityU iGEM team 2024", plus the project name "Bevatech" or
"BevaTech". Past tense for events. The why-paragraphs read well; the handbook
and postcard paragraphs switch into promotional register.

### What it folds

Nothing. Handbooks are links.

### Where it is weak

- Inflated impact paragraphs with no evidence behind them. The postcard exchange is called "a cultural exchange platform" that fosters "global citizenship" (excerpt cityu-05). The handbooks have "far-reaching implications" and "tremendous impact" (l.104, l.109).
- Measured but not reported (Kahoot, l.70 and l.85).
- Little on what the team learned.
- Shared handbooks do not say what CityU wrote (l.105 lists three teams).
- A mascot toy given out "to promote our project in their community" (l.86). The prize text excludes marketing.
- Inconsistent names: "Snake and Ladders" in the contents, "Snakes and Ladders" in the heading; "Bevatech" and "BevaTech"; "Kazahkstan" (l.66).

### What ReLeaf could take

- The two fixed questions per audience. ReLeaf's elementary, junior high and high school sections could open with "Why this group?" in two to four sentences.
- Quote the actual questions you asked children (excerpt cityu-02).
- Percentages plus one named quote, and add the n they left out.
- A handbook written for the next organiser: materials list, steps, languages.

## Aachen 2024 OG

### Page anatomy

About 5,800 words of prose plus about 1,000 words of code. One program,
AlphaFold Decoded, a course on rebuilding AlphaFold.

1. Stat strip: 39 minutes of content, 2 chapters, 1,567 views
2. Introduction (~80)
3. Why AlphaFold Decoded Matters: three cards (~130)
4. Challenges to Overcome: missing prerequisites, the size of the codebase (~220)
5. Implementation Code: line counts, licence note, code comparison tabs, prediction comparison (~300 prose)
6. Guided Learning with Jupyter Notebooks: skeleton code, error checking, Colab, Try It Out Yourself (~440)
7. Rolling Out AlphaFold Decoded: workshops to hybrid to video; who it is for (~345)
8. Course Content Overview: nine lessons, ~75 words visible each, ~2,700 words folded
9. Reception and Impact: views, eleven comments, expert statement (~530)
10. Outlook (~140); References, folded (~110)

### How it opens

Five sentences: AI changed biology, biologists use these tools but cannot
build them, so this course teaches building AlphaFold from scratch (excerpt
aachen-01). Gap and response before any detail.

### Entry template

A single-program page, so the template is the page:

```
Gap: [what learners cannot yet do]
Why it matters: [two or three reasons, one per audience]
Barriers: [prerequisites and difficulty], then "We assume only [entry level]"
Design response: [how the material removes each barrier]
Try it yourself: [steps to start]
Roll-out: [first format] → [feedback] → [changed format] → [result]
Content: [one short summary per unit, details folded]
Reception: [numbers] + [comments] + [expert view]
Outlook: [what is published, where, for whom to build on]
```

### Evidence and numbers

Strong on the design: 1,411 lines in the teaching version against 5,287 in
AlphaFold's key files (l.43); a side-by-side prediction with stated limits
(excerpt aachen-05). Weak on learners: there is no workshop attendance, no
completion rate, no test of what learners could do. Reception is views and
comments. The two view counts disagree (excerpt aachen-06), and the stat strip
says "2 Chapters" and "39 Minutes" for what the text calls a nine-part series.

### Reuse

The strongest of the six. The repo holds tutorials, solutions, build logic and
chapter scripts (l.191). Getting started is a step-by-step procedure down to
"select a GPU under Runtime > Change runtime type" (l.74).

### Voice, person, tense

"We" for the team and "you" for the learner. The lesson summaries say "we
learned" and "we explored", in the voice of a lecture. Some hype: "this AI
marvel", "game-changer".

### What it folds

The lesson details (about half the page) and references. Visible text gives
each lesson in one paragraph.

### Where it is weak

- Numbers that contradict each other (header and body).
- The comment list is unfiltered and includes a joke about drugs and gunpoint (l.165).
- One commenter asks for a different course structure (l.177). The page never says whether the team acted on it. Showing feedback without a response leaves the loop open.
- "Bridging Fields" (l.86) predicts benefits for four audiences without evidence.
- Long technical summaries that a non-specialist judge will skip.

### What ReLeaf could take

- The roll-out paragraph (excerpt aachen-02) as the pattern for ReLeaf's trial-by-trial changes: format, feedback, change, reason.
- Credit the person behind a suggestion (excerpt aachen-03).
- State the entry level for each audience in one sentence (excerpt aachen-04).
- Check every number on the page against every other.

## IISER-Pune-India 2023 UG

### Page anatomy

About 4,100 words. Organised by audience, with 20 entries.

1. Our View: quote, mission, SDG figure (~180)
2. Outreach and Engagement Events (~30)
3. Students Till Middle-School (~900): activity book, school visit, educational video, hands-on session
4. High School and University Students (~1,565): science exhibit, art competition, biomimetics competition, DNA fingerprinting workshop, debate, awareness session
5. The iGEM Community (~450): All India iGEM Meet, wiki workshop, biosafety webinar, collaborations
6. General Public (~885): survey, dictionary, biofuel symposium, social media, river cleaning, plantation drive

### How it opens

A Helen Keller quote (spelled "Hellen", l.37), then the UN SDGs, then a
general mission statement. The first activity starts after about 200 words.

### Entry template

```
### [Activity]
We wanted to [goal] and that's why we [did X] with [partner].
We explained/showed [content list].
[Highlight: winners, a vivid moment, a number of entries]
We hope that [future effect].
```

"We hope" appears seven times on the page.

### Evidence and numbers

Counts of participation: 250+ art entries, 100+ biomimetics students, about
30 teams at the wiki workshop, 15 teams at the national meet, five survey
languages. No measure of learning. The survey section says the results "were
really great" and moves the numbers to another page (excerpt iiser-03).

### Reuse

Links to an activity book, a YouTube video and a dictionary. The survey's
language versions sit on the inclusivity page.

### Voice, person, tense

"We", past tense, warm and informal ("Which kid doesn't love to solve fun
puzzles", l.48; "stole our hearts", l.81).

### What it folds

Nothing. Survey charts live on another page.

### Where it is weak

- Breadth over depth. River cleaning, tree planting and social media posts sit on the Education page with no learning content.
- Mutual learning is one sentence without an example (excerpt iiser-01).
- Impact claims without evidence: the session "left a meaningful impact on the young participants" (l.71).
- Unclear sentences: "We had our outreach events categorised, in our minds (to keep in line with the SDGs) and for the sake of ease of navigation" (l.44).

### What ReLeaf could take

- Audience categories as top-level headings, which ReLeaf already uses.
- Translation as a concrete inclusion step, named language by language (excerpt iiser-02).
- Avoid: "we hope" endings, and activities that teach nothing.

## EPFL 2023 OG

### Page anatomy

About 2,400 words. Two flagship tools and four events.

1. Contents and introduction, four paragraphs (~255)
2. BSGV, a mini-iGEM for high schools (~550)
3. BioQuest, an educational game (~450, README PDF folded)
4. Wiki, an adapted version with dictionary (~125)
5. Events: open days booth (~295), high school visit (~185), summer school (~265)
6. Helping and encouraging the future of iGEM (~185)

### How it opens

Generally. "The magnitude of change achieved by scientists and engineers has
always been related to its support in society" (l.12). The useful sentence
comes third: the team chose to focus on younger students, and says why (l.14).

### Entry template

```
## [Initiative]
[Rationale tied to "learning by doing"]
Objectives: [three bullets]
Support we provided: [bullets]
Outcome / next: [planned event, interest from teachers]
Links: [page, repo, drive]
```

Events follow a shorter pattern: size of the event, activities by age, aim,
"positive response".

### Evidence and numbers

Event sizes (25,000 open-day visitors, two groups of 12 students, 16 summer
school students). No learning results. The school visit gave a quiz and
reports only that feedback "was positive" (excerpt epfl-03).

### Reuse

Good for a 2023 page. The game's repo includes build files and a README that
explains how to modify it (excerpt epfl-02). BSGV materials are on a separate
page.

### Voice, person, tense

"We", formal, some passive. BSGV's award ceremony is described in future
tense because it had not happened at wiki freeze (l.25).

### What it folds

The BioQuest README PDF.

### Where it is weak

- Generic opening.
- "delve" four times.
- Typos: "this our problem" (l.13), "were and carried out" (l.15), "feeback" (l.76), "More informations" (l.28).
- The open-day booth set out to "promote the iGEM competition" (l.59). The prize text rules out marketing iGEM.
- The flagship competition's results are not on the page.

### What ReLeaf could take

- A jargon fix built into the page: a glossary or simplified version for younger readers (excerpt epfl-01).
- A README-style list of what is inside each download.
- Avoid: quiz without results, and a closing line about "positive response" (excerpt epfl-04).

## Cross-case synthesis

### Shared skeleton

All six pages, under different labels, follow the same order:

1. Purpose: why public learning matters for synthetic biology, in one or two paragraphs.
2. Structure statement: how the page is organised (by audience, by learning style, by subgoal, or by course unit).
3. Groups of activities, each group opening with why that audience.
4. Per activity: setting and participants, what was taught, the hands-on part, how participants engaged, materials to reuse.
5. A forward look: who continues it and where the materials live.

The stronger pages add two things to step 4: a measured or quoted learning
outcome, and a sentence on what the team changed.

### UG and OG

- UG pages (Queens, CityU, IISER) are wide: 13 to 20 activities, each 150 to 400 words, organised by audience or learning style. They make more unsupported claims and use more stock adjectives.
- OG pages (Heidelberg, Aachen, EPFL) build fewer, larger things (a course, a platform, a competition, a guide) and explain the design reasoning. They tie education to one theme: translation for Heidelberg, AI literacy for Aachen, learning by doing for EPFL.
- Both tracks are weak at measuring learning. The one exception is Heidelberg.

### Changes from 2023 to 2025

- 2023 pages are event lists. Entries end with hopes. Evidence is participation counts.
- 2024 adds structure. CityU fixes two questions per audience. Aachen shows feedback changing the product.
- 2025 adds labelled fields that echo the ballot (Queens' "Learning & Dialogue"), summary bullets per section, participant quotes, and a before/after measure (Heidelberg). On these six pages the phrase "mutual learning" first appears in 2025.

### Sentence patterns for reflection and impact

Copied from the winners, with slots:

- "While we initially [avoided/assumed X] out of concern [Y], our experiences with [Z] showed that [finding]. Future workshops may [change]." (Queens, l.58)
- "While the event aimed to reach [X], we noticed [Y]. This made us realize [Z]." (Heidelberg, l.302)
- "[Participants] expressed a desire for [X], as [reason]. This feedback pushed us to develop [Y]." (Aachen, l.81)
- "We acquired feedback from [who] to [purpose]. As a result, we decided to [change]." (Heidelberg, l.415)
- "[Feature] was proposed by [person], who highlighted [problem]." (Aachen, l.70)
- "To measure our impact, we asked participants to [method] before and after [activity]. [Result with numbers]." (Heidelberg, l.316)
- "[N]% of the participants [rated X], with [M]% responding that [they learned Y]." (CityU, l.71; add n)
- "An example of a particularly hotly debated topic was [X]. [Who] believed [Y]. When we showed [Z], [reaction]. [What we concluded]." (Heidelberg, l.315)
- "We assume only [entry level] and aim to guide you through the rest." (Aachen, l.41)

### Anti-patterns seen even in winners

| Anti-pattern | Where | Fix |
|---|---|---|
| Reach offered as proof of learning or dialogue | Queens l.106, l.175; Aachen l.162 | Put views and impressions under reach. Use quotes, questions or scores for learning |
| Measured but never reported | EPFL l.62; CityU l.70, l.85 | Give the score or cut the mention |
| Percentages with no base | CityU l.71; Heidelberg l.316 | Add n for every percentage |
| Inflated impact paragraphs | CityU l.95, l.104, l.109 | Replace with what happened and who saw it |
| Closing on "we hope" or "inspire the next generation" | IISER (7 × "we hope"); Heidelberg (20 × "inspir-") | End on a result or a next step with a date |
| Same point twice in a paragraph | Queens l.126 | Keep the clearer half |
| Numbers that disagree | Aachen header and l.162 | Check every repeated number |
| Planned work written as done | EPFL l.25; Queens l.30, l.155 | Past tense for done, future with a date for planned |
| Promotion of iGEM or the project | EPFL l.59; CityU l.86 | Cut, or rewrite as what people learned |
| Feedback shown without a response | Aachen l.177 | Say what you did with it, or why not |
| Paragraph out of time order | Heidelberg l.513 | Events in order, result last |
| Generic opening | EPFL l.12; CityU l.24 | Open with your audience and your focus |
| Non-education activities on the page | IISER l.148–157 | Move them or cut them |
| Stock words | `delve` (EPFL 4, Aachen 3), `crucial` (Heidelberg 7, Aachen 6), `foster` (Queens 8) | Use the plain verb |
| Typos in published text | EPFL, Queens, IISER | Read it aloud before freeze |

## Rewrite checklist

Each rule can be checked by reading the page. Team names show who
demonstrates it (or, marked "counter", who breaks it).

1. Each audience section opens with two to four sentences on why this group, naming a gap specific to that age or grade. Reason: judges need the rationale before the activity. CityU, Queens.
2. Every activity entry uses the same labelled parts in the same order. Reason: a judge finds dialogue and reuse in the same place every time. Queens, CityU.
3. The first two sentences of an entry give date, place, partner, age or grade, and headcount. Reason: these are the facts judges check first. CityU (l.31), Queens (l.92); counter: most CityU and Heidelberg school entries lack a headcount.
4. If you ran a quiz or survey, the result is in the same paragraph. Reason: a measure without a result reads as a gap. Heidelberg; counter: EPFL, CityU.
5. Every percentage has its n, and pre/post comparisons say whether the same students answered both. Reason: 70% of 10 and 70% of 200 are different claims. Counter: CityU, Heidelberg.
6. Views, impressions and attendance go under reach, never under learning or dialogue. Reason: reach shows who saw it. It says nothing about what they learned. Counter: Queens, Aachen.
7. Each entry gives one specific thing participants said, asked or got wrong. Reason: a concrete example is the proof of dialogue that judges can check. Heidelberg (l.315), CityU (l.32–33).
8. Each entry gives one thing the team changed, written as "we changed X because Y". Reason: this is the ballot's mutual learning question. Aachen (l.81), Heidelberg (l.415), Queens (l.58).
9. Any feedback you show is followed by your response to it. Reason: unanswered feedback leaves the loop open. Counter: Aachen (l.177).
10. Each download is named, with what is inside it (file, language, materials list). Reason: other teams build on what they can find. CityU (l.38), EPFL (l.44–45), Queens (l.19).
11. Each audience section states the entry level, and each technical term is explained the first time it appears. Reason: judges and teachers may not share your vocabulary. Aachen (l.41), EPFL (l.49–50).
12. Every number that appears twice on the page is the same both times. Reason: one mismatch makes every number doubtful. Counter: Aachen.
13. Past tense for what happened; future tense only with a date. Reason: planned work written as done misleads the reader. Counter: EPFL (l.25), Queens (l.30).
14. No paragraph makes the same point twice. Reason: repetition looks like padding. Counter: Queens (l.126).
15. No paragraph ends on "we hope", "inspire" or "next generation" unless the next sentence gives evidence. Reason: these endings carry no information. Counter: IISER, Heidelberg, CityU.
16. Each audience section names one limitation or thing that did not work. Reason: honesty makes the positive results believable. Heidelberg (l.302), Aachen (l.57).
17. Cut sentences whose purpose is promoting iGEM or the team. Reason: the prize text excludes marketing. Counter: EPFL (l.59), CityU (l.86).
18. Events within a paragraph are in time order, and the paragraph ends on the result. Reason: readers follow time order without effort. Counter: Heidelberg (l.513).
19. If you adapted another team's activity, name the team and say what you changed. Reason: judges reward building on prior work and see the difference. Queens (l.12), Heidelberg (l.362).
20. Read the page aloud once before freeze. Reason: every page here has typos a read-aloud catches. Counter: EPFL, Queens, IISER.

## Source-quality notes

- Aachen: the stat strip (1,567 views, 2 chapters, 39 minutes) disagrees with the body (2,920 views, nine videos). The strip may be an older snapshot; the text cannot tell which is current. Code comparison tabs render as one long line each (l.54–55).
- Heidelberg: the first ~100 lines are site navigation. Galleries render as repeated "Image 1–16" lines. Some prose sits under widget headings ("Click on the images to enlarge them!", "Click on the stakeholders..."), so the excerpt `section` field uses the nearest real heading. The pillar content (l.224–226) is clickable and only one pillar's text was captured.
- IISER Pune: the top ~35 lines are the site menu. Images carry no alt text, and the survey pie charts are images, so their numbers are not in the text.
- CityU: images carry no alt text; the handbooks are links, so their content is absent.
- Queens: field labels (Description, Knowledge Gap, Learning & Dialogue, Future Directions) are plain lines without heading markup, so the counts above treat each entry as one section.
- EPFL: BSGV team posters and the adapted wiki appear only as image labels.
