# Laws and Regulations casebook

Research base for the margin feedback on ReLeaf's "Laws and Regulations" page.
No iGEM prize exists for this page type, and few teams write a dedicated one.
The strongest precedents are sections inside prize-winning Human Practices
pages, plus one hub-and-subpage structure (Marburg 2024).

Sources: `sources/text/` files named below; URLs in `sources/pages.txt`.
All quoted text is CC BY 4.0, credited to the team named.

## What the page is judged on

There is no Standard URL for a laws page. Judges reach it only through links
from pages that do have one: Human Practices, Entrepreneurship,
Safety and Security, Sustainability. So the page must be summarised, in a
sentence or two with a link, on each of those pages. A laws page nobody links
to scores nothing.

Ballot questions it can help answer (`judging-special-prizes.md`):

| Prize | Ballot question | What the laws page supplies |
|---|---|---|
| Integrated Human Practices | How thoughtfully was it implemented? How well did they explain the context, rationale and prior work? | The legal context for design choices, with the rule cited |
| Integrated Human Practices | How well did it incorporate different stakeholder views? | Regulators, lawyers, patent offices and critics as named stakeholders |
| Integrated Human Practices | To what extent is the work documented so that others can build upon it? | A reusable map of which rule applies to which part of the system |
| Entrepreneurship | Has the team presented logical product development plans with realistic milestones, timelines, resources and risks? | Approval routes, durations and costs that the business plan must carry |
| Entrepreneurship | Has the team considered the positive and negative long-term impacts? | Market access limits, labelling, organic-farming eligibility |
| Safety and Security | In addition to broader safety work, has the team managed risks from their project appropriately? | Containment class, release rules, residual-DNA thresholds |
| Safety and Security | Has the team addressed the use of synthetic biology in the real world? | Whether the product could legally be used at all, and where |
| Sustainable Development | Did the team address potential long-term social, environmental and economic impacts? | Rules that push the market (bans, restrictions) or block it |

It also feeds Best Wiki's question on whether content is "properly referenced
and cited". Legal claims are the easiest place on a wiki to be wrong.

## Cases at a glance

| Case | Prize standing | What it is | Why it is here |
|---|---|---|---|
| Marburg 2024 | Best Plant SynBio winner (OG), Best IHP nominee | Hub page, two subpages (Legal Framework, Political Dimension), eight interview subpages | Primary case. The only full page structure for law and politics among recent winners; closes the loop on two lab pages |
| WageningenUR 2025 | Best IHP winner (OG), Best Entrepreneurship winner (OG, tie) | Two numbered sections inside the IHP page (#3 and #7.2), plus one sentence in the Entrepreneurship timeline | Best single example of the full entry template, with named regulators and a cited regulation. Agricultural, microbial product, EU |
| UZurich 2024 | Best Sustainable Development winner (OG) | Chapter 3 of the IHP page, "Ethics, Politics, Law and Consumer Perception" | Engineered soil bacteria for crops. States plainly that the product could not legally be used in Switzerland |
| Waterloo 2024 | No special-prize nomination found | Dedicated "Policy Research" page, about 920 words | Short dedicated page on a GM agricultural input (feed additive). Shows how to write an unresolved classification |
| CSU-China 2024 | No special-prize nomination found | Dedicated "Laws and Regulations" page, about 4,500 words | Contrast case. Recites a statute article by article and barely mentions the project |

How the extra teams were found: a scan of all 1,062 competition wikis for
2022 to 2025 (iGEM teams API, then homepage navigation links and probes for
`laws`, `regulations`, `policy`, `legal`, `legislation` slugs), plus a grep of
the prize-winner texts already in `sources/text/`. Dedicated law pages turned
up at CSU-China 2024 and Waterloo 2024 (both used here), UAlberta 2023 (a
policy review of agricultural sprays, rendered text about 100 words, the rest
apparently an embedded paper), Guangxi-U-China 2023 and UAM 2025 (lists of
statutes, one line each). CSU-China's 2023 "ethicsandlaw" page did not
render. No prize winner or nominee from 2022 to 2025 has a dedicated laws
page that the scan could find, so the prize-level precedent lives inside IHP
pages. The scan could not read about 70 wikis built as single-page apps, so
it is not complete.

---

## Marburg 2024

Files: `mar-2024-legal-political.md` (hub, rendered), `mar-2024-legal.src.txt`,
`mar-2024-political.src.txt`, `mar-2024-legal-<name>.src.txt` (eight
interview subpages), `mar-2024-hp.md` (section "(5+6)"),
`mar-2024-part-collection.src.txt`, `mar-2024-non-amt.src.txt`,
`mar-2024-safety-security.md`, `mar-2024-economic.md`.

Project: engineered Russian dandelion (*Taraxacum kok-saghyz*) as a European
rubber crop. The legal questions were the EU proposal on New Genomic
Techniques (NGTs) and the patents around *Agrobacterium* transformation.

### Page anatomy

The legal thread is spread over three layers.

1. Hub, "Legal Framework & Political Dimension" (about 580 words). An
   engagement-network image, one framing paragraph, then one paragraph per
   contact in the order they were met, then two tiles leading to the
   subpages.
2. Two subpages, prose only, no internal headings.
   - Legal Framework, "Deciphering the Patent Landscape" (about 760 words):
     why patents matter once work leaves the university; the NGT law and
     existing *Agrobacterium* patents; the GASB webinar and Prof. Dederer;
     the university contracts office; a patent attorney; three "pioneers"
     (Jefferson, Potrykus, Rathore); a closing reflection; a card grid of
     seven contacts.
   - Political Dimension, "GMO & NGT Legislation" (about 800 words): three
     framing questions; the July 2023 NGT proposal; an NGT graphic; the
     consultations; the same three pioneers; a summary that names the one
     design change; a turn to public engagement; a card grid.
3. Eight interview subpages (280 to 1,470 words each), all on one template:
   name and affiliation as header, photo, "Reason for Contact", "Most
   Significant Points" (four to eight subsections), "Inclusion in Our
   Project". One of them (EcoProg) ends with a three-row table: Initial
   Thought, Learning through Interview, Revisioned Thought.

Outside the subpages the thread reappears four times: the IHP hub section
"(5+6) Political Dimension and Legal Framework" (about 250 words), the Part
Collection page (why only endogenous elements), the non-AMT page (why avoid
*Agrobacterium* patents) and the Safety page (buffer-zone rules in the US, EU
and Germany). The Economic Stakeholders page adds EU supply-chain rules.

### How it opens

The hub opens with one claim and one purpose sentence: law and politics are
"closely intertwined", and the page gives "an overview of the entirety of
interviews". The Political Dimension subpage opens better, with three
questions a reader can hold the page against: what regulations apply, what
restrictions exist on the organisms, what is the current stance on GMOs.
Both openings frame the page as a record of conversations. Neither states the
project's legal position in the first paragraph.

### Entry template

The interview subpage is the unit. Mapped onto the five-slot template:

| Slot | Where Marburg puts it | Example |
|---|---|---|
| Regulation | "Most Significant Points", in the expert's voice | NGT1 and NGT2 categories, explained by Prof. Dederer |
| What it requires | Same section | NGT1 plants are exempt from GMO rules; NGT2 stay under them |
| What it means for us | "Relevance for Our Approach", "Inclusion in Our Project" | A Cre-lox scar of 34 bp might push the dandelion into Category 2 |
| Who confirmed it | The subpage itself (named expert, title, affiliation) | EcoProg board members; a constitutional-law chair; a patent attorney |
| What we changed | IHP hub and two lab pages | Only endogenous regulatory elements in the part collection; a non-*Agrobacterium* transformation route |

The EcoProg subpage is the best single entry: it names the rule, places the
project in a category, finds the detail that could move it to the other
category (the loxP scar), and records the revised belief in a table. The
change itself is written up where a judge reading the lab work will meet it.
The Part Collection page says the choice of endogenous parts followed
"extensive consultations with experts" and the expected NGT1 exemption.

### How legal claims are sourced

Almost entirely through people. The law is described in the words of a law
professor, a patent attorney, an NGO and a university contracts office. That
makes the claims easy to trust and hard to check. The pages name the
proposal's date (July 2023), the 2001 GMO framework, the Biopatent Directive
and the European Patent Convention, but give no document numbers, article
numbers or links to EUR-Lex. The Safety page's buffer-zone figures (20 m in
the EU, 150 m in Germany before 2009) carry no reference, though the
paragraphs around them do. The claim that EFSA "requires" a 20 m zone is
doubtful: EFSA gives scientific opinions, and coexistence distances are set by
member states.

### Voice and tense

First person plural, past tense for what happened ("we consulted", "we
learned"), present for the law ("NGT1 plants are equated with conventionally
produced plants"). The interview subpages report expert views as plain
statements without "he said", which blurs the line between the expert's
opinion and the law itself. Gratitude sentences open most "Inclusion"
sections.

### Weaknesses

- One finding, told five times. The hub, both subpages and the IHP section
  repeat the same contacts in near-identical paragraphs. The sentence "In
  academia, patents often seem distant..." appears on at least five pages.
- Contradiction inside one entry. The EcoProg subpage says "We now know that
  our CRISPR approach falls under category 1" and, a paragraph later, that
  the project "might fall under category 2".
- Names swapped. The Dederer subpage links to "Vanessa Nitsch and Dr. Claudia
  Kuhl"; the people are Vanessa Kuhl and Dr. Claudia Nitsch.
- No primary legal citations, and no "as of" date for a law still in
  negotiation. The European Parliament's patent amendment is reported without
  a date.
- The patent thread changed the team's understanding more than its design.
  The Legal Framework page ends on "the complexity of the patent landscape",
  a reflection with no outcome attached. The outcome (the non-AMT route)
  lives on another page and is not named here.
- The Political Dimension page ends by drifting into science communication
  (Science Slam, plant market), with a broken link label ("engaged with the
  public" used twice).
- Translation slips: "Leaderboard" for the NGO's board, "underwood" for
  "understood".

### What ReLeaf could take

- The three-row table (initial thought, what we learned, revised thought) for
  any rule where ReLeaf's classification moved during the season.
- The specific-detail move: find the one design feature that decides the
  category (Marburg's 34 bp loxP scar). For ReLeaf this could be whether any
  engineered cells or DNA leave the bioreactor with the output.
- Write the change where the judge will see it. Each legal decision should
  appear on the lab or engineering page it changed, with a link back.
- Avoid the hub-plus-subpage repetition. One page, one paragraph per rule,
  with the interview detail folded.

---

## WageningenUR 2025

Files: `ihp-2025-OG-wageningenur.md` (sections "#3 Choice of the platform
material for the coating and EU regulations", "#7.2 Insights from regulatory
institutions", and the Bigger Better Biotech event),
`ent-2025-OG-wageningenur.md` (timeline paragraph).

Project: BCoated, a bacterial-cellulose seed coating carrying a
bioinsecticide protein. Same sector as ReLeaf: a microbially made product
for farmers, sold into EU agriculture.

### Page anatomy

Law is not a page here. It is two numbered steps in the IHP "Our story".

- #3, "Choice of the platform material for the coating and EU regulations"
  (about 370 words): the REACH microplastics restriction with two dated
  bullets; a farmer on the neonicotinoid ban; a one-sentence realisation;
  advice from a biopolymer company; the seed sector's non-negotiables; the
  search for a matrix that follows.
- #7.2, "Insights from regulatory institutions" (about 580 words): the
  Dutch RIVM on grouped approval, protein modules and the 0.9% GMO DNA
  threshold; the European Commission (DG SANTE, unit E4) on active-substance
  approval and its 2.5 to 3.5 years; what that did to the business plan;
  organic-farming rules via SKAL; EU eco-premiums.
- An events entry: a panel with a Commission policy director, the Dutch
  GMO commission and a life-sciences lawyer, listing five approval standards.

### How it opens

Section #3 opens on a practice that is about to become illegal: "This is a
practice soon to be outlawed, as we found out from our stakeholders in the
seed sector." The law enters as a pressure on the design, in the first
sentence, through a named source.

### Entry template

The RIVM and DG SANTE paragraphs hit all five slots in under 150 words each:
the rule (Regulation (EC) No 283/2013; the 0.9% threshold), the requirement
(EU active-substance approval, then member-state authorisation; each toxic
protein module assessed separately), the consequence (downstream processing
must remove GMO DNA; some functionalisations need their own assessment),
who confirmed it (named RIVM staff; the Commission unit), and the change
("This shaped our business plan: we included regulatory timelines and
emphasised partnerships with established seed companies"). The same
three-year figure reappears in the Entrepreneurship timeline, attributed to
the same two bodies.

### How legal claims are sourced

Through regulators by name, with the regulation number given once. The
Entrepreneurship page lists Commission Regulation (EU) 2023/2055 (the REACH
microplastics restriction) in its references. The IHP page itself has no
legal reference at the point of the claim.

### Voice and tense

First person plural, past tense for meetings, present for rules. Inference is
marked: "We therefore think that our microbially produced BC could also fall
under biological regulations." The reader can tell what the regulator said
and what the team concluded.

### Weaknesses

- Regulation (EC) No 283/2013 sets the data requirements for active
  substances; the approval itself runs under Regulation (EC) No 1107/2009.
  The page names only the first.
- The REACH dates in the two bullets are given without the regulation number
  on the IHP page; they should be checked against the regulation text.
- The section is buried in step 7 of an eight-step story. A judge looking
  for regulation has to know to look there.
- Template residue in the rendered page: "NAME OF STAKEHOLDER", "Lorem ipsum"
  and image placeholders ("brochure placeholder") were left in.

### What ReLeaf could take

- Ask a regulator the questions WUR asked: does each variant need its own
  approval, and what residual DNA or cell threshold applies to the final
  product. For a cell-free output from an engineered *B. subtilis* culture,
  the second question is the one that decides the downstream process.
- Carry every duration and cost a regulator gives into the business plan,
  with the same number and the same attribution on both pages.
- Mark inference as inference ("we therefore think").
- Check the organic-farming route: WUR found a list of permitted inputs
  (SKAL) and a premium scheme, which turned a constraint into a market.

---

## UZurich 2024

Files: `xtra-2024-uzurich-ihp.md` (chapter "3. Ethics, Politics, Law and
Consumer Perception"; framing paragraphs at the top), `sus-2024-OG-uzurich.md`.

Project: RhyzUp, an engineered *Pseudomonas* root-biofilm bacterium for crops,
with a sensing mechanism and kill switch. The closest of all the cases to
ReLeaf's biology: engineered soil-associated bacteria helping plants.

### Page anatomy

The IHP page opens with four groups of questions, one per chapter. The third
group is legal and political. Chapter 3 (about 1,170 words) holds four
entries: a bioethicist, the director of the Swiss Alliance for GMO-free
agriculture, a lawyer for an association that wants differentiated GMO rules,
and a consumer-perception researcher. Each entry runs: name and organisation
as heading, photo, a short biography, "We learned that:" or "During our
conversation we discussed:" with four to nine bullets, a reflection paragraph,
a note on the recorded interview.

### How it opens

With the questions: "How is gene technology regulated in Switzerland? What
criticism is there regarding the use of GMOs in agriculture? Are there
ecological risks to our project? How do consumers perceive our project?"
Then one sentence saying who they asked.

### Entry template

The lawyer's entry covers four slots: the rule (the Swiss moratorium on GMO
cultivation), the pending change (a Federal Council decree on non-transgenic
plants, requested by mid-2024 and not yet drafted), what it means ("currently
our project could not be legally implemented in Switzerland due to the
moratorium"), and who said it (named lawyer, named association). The
"what we changed" slot is weak: the critic's entry ends with "We were
vindicated in our decision to incorporate a sensing mechanism and kill
switch", which confirms an existing design choice.

Pairing an opponent (the GMO-free alliance) with a reform advocate (the
lawyer) gives the reader both sides of the legal debate from people who hold
them.

### How legal claims are sourced

Interviewees only. The moratorium is not cited to the Swiss Gene Technology
Act, and the decree request is not cited to the parliamentary decision.

### Voice and tense

First person plural, past tense. Bullets in the expert's voice, reflections
in the team's. Short, plain sentences.

### Weaknesses

- The biggest legal finding (the product cannot be used in Switzerland) gets
  one sentence and does not reach the Sustainability page in the source set.
- No statute or article numbers.
- Bullet lists of topics discussed ("Biocentric views on the synthesis of
  life") list the topics discussed and leave out what was learned.

### What ReLeaf could take

- State the hard result in one plain sentence, even when it is bad news. If
  the engineered culture cannot be run on a farm under current Taiwanese rules
  without a permit that does not yet exist, say so.
- Put a pending legal change on the page with its date and its status ("was
  requested by mid-2024. This has not yet happened").
- Interview one critic of GM agriculture on the legal question, alongside
  regulators and supporters.

---

## Waterloo 2024

File: `law-2024-waterloo.md`.

Project: BovEco, a genetically modified feed additive or plant that reduces
methane from cattle. An agricultural GM input facing a regulator who may not
have a category for it.

### Page anatomy

About 920 words with references. Headings: Challenges & Solutions; Climate
Policies; Canadian Food Inspection Agency (CFIA) Regulations; Antibiotic
Policy; Global Policy Perspective; References (nine numbered entries,
mostly government pages with access dates).

### How it opens

With the sector's problem, then the product and its exposure in one sentence:
it "would, like other feed additives and GMOs, be subject to regulatory
scrutiny before implementation could occur".

### Entry template

The Antibiotic Policy section is the useful one. It explains Canada's 1 to 4
antibiotic classes, places a comparable product (ionophores) in class 4, then
writes the open question as a conditional: it is unclear whether agencies
would classify the enzyme as an antibiotic; if they did, it would fall into
class 4 for a stated reason. That is the shape ReLeaf needs for any
classification no regulator has confirmed. The "who confirmed it" and
"what we changed" slots are empty.

### How legal claims are sourced

Numbered references to government web pages (CFIA, Health Canada), dated.
Industry experts are mentioned ("a recurring theme of discussion") but not
named.

### Voice and tense

Mostly impersonal and present tense, like a policy brief. Little "we".

### Weaknesses

- The Global Methane Pledge is misdescribed. The pledge is a collective cut
  of at least 30% from 2020 levels by 2030; the page describes a 50% cut and
  climate neutrality by 2050.
- "Methane is 34 times more potent than carbon dioxide" with no time horizon.
- Typo that changes meaning: "class a lytic enzyme and an antibiotic".
- No named stakeholder, no design consequence.

### What ReLeaf could take

- The conditional sentence for unconfirmed classifications: "It is unclear
  whether X would be classed as A. If it were, it would fall under B,
  because C."
- Use a comparable product already on the market as the anchor for the
  argument (ionophores here; Kelpak and Sagarika on ReLeaf's page).

---

## CSU-China 2024 (contrast)

File: `law-2024-csu-china.md`.

A dedicated "Laws and Regulations" page of about 4,500 words for a diabetes
project. Anatomy: overview; the Biosafety Law of the PRC with its legal
hierarchy, chapter catalogue and articles 1, 2, 3, 7, 34, 35 to 41 and 55,
each followed by the legislature's commentary; international conventions; an
ethics section (questionnaire, patient interviews); lab safety; an IP guide
and a list of patent databases.

The project's own system appears once, in the IP section. Paragraphs such as
"We obey the law strictly and all actions are required by law" make a claim
nobody can check. A reader finishes knowing the statute and not knowing which
article touched the project or what it changed. It is the clearest example of
the failure the five-slot template prevents: law recital with no
"what it means for us".

---

## Synthesis

1. The strong cases treat law as a design input. WUR's coating material,
   Marburg's endogenous parts and non-AMT route, and the business timelines
   all exist because of a rule. The weak cases treat law as a compliance
   statement.
2. The unit that works is the entry: one rule, one consequence
   for a named part of the project, one named confirmer, one change. WUR does
   it in a paragraph; Marburg spreads it across a subpage and a lab page.
3. Regulators and lawyers make stronger stakeholders than literature, but
   none of the winners cites the legal text itself at the point of the
   claim. ReLeaf can do better than every precedent here by citing the
   instrument and article next to the claim, with a link and a date.
4. Honest bad news reads as strength. UZurich's "could not be legally
   implemented" and ReLeaf's own "What is still unconfirmed" list are more
   persuasive than a page that claims full compliance.
5. Repetition is the main writing fault. Marburg tells one story on five
   pages. One page, linked from the Standard URL pages with a one-line
   summary, is enough.

## Rewrite checklist

1. Every rule is cited by instrument, number and article, with a link to the
   official text. Reason: no precedent does this, so it is the easiest way to
   stand out, and it lets a judge check the claim.
2. Any rule still being drafted or negotiated carries an "as of" date and its
   current stage. Reason: Marburg and UZurich describe pending law without
   dates, so the reader cannot tell if it is still true.
3. Each entry fills five slots: rule, requirement, consequence for a named
   component, who confirmed it, what changed. Test: point to each slot in the
   paragraph. Reason: WUR's #7.2 does this and is the strongest passage in
   the casebook.
4. "Consequence" names the component (culture, bioreactor, output, claim), not
   "our project". Reason: ReLeaf already splits the system this way; vague
   consequences undo that work.
5. Unconfirmed classifications are written as conditionals: "If X is classed
   as A, then B, because C." Reason: Waterloo and Marburg's loxP example show
   the shape; a hedge without the "then" is not useful.
6. What a regulator or lawyer said is attributed to them; what the team
   concluded is marked as the team's inference. Test: every "we think" or
   "we conclude" follows a named source. Reason: WUR keeps these apart;
   Marburg's subpages blur them.
7. Every duration, cost or threshold from a regulator appears with the same
   number and attribution on the Entrepreneurship page. Reason: WUR's
   three-year approval figure appears on both pages and ties them together.
8. Every "what we changed" links to the page where the change is visible
   (Engineering, Hardware, Business plan). Reason: Marburg's endogenous-parts
   decision is credible because the Part Collection page repeats it.
9. No statute recital. Quote an article only if the next sentence says what
   it means for ReLeaf. Test: every paragraph names a ReLeaf component or
   decision. Reason: CSU-China's page fails exactly here.
10. State a negative result plainly, in one sentence, near the top of its
    section. Reason: UZurich's moratorium sentence is the most honest line in
    the casebook and costs nothing.
11. No sentence appears twice across the laws page and the pages that link to
    it; the linking pages carry a one-line summary and the link. Reason:
    Marburg's repeated paragraphs make five pages read like one.
12. Names, titles and category labels match across every page. Test: search
    the wiki for each person's name and each category label. Reason: Marburg
    swapped two names and gave two categories for the same plant.
13. At least one legal stakeholder disagrees with the project. Reason:
    UZurich's GMO-free alliance entry answers the IHP question on different
    stakeholder views better than any regulator could.
14. The "What is still unconfirmed" list names an owner or next step for each
    item. Reason: an open question with a plan reads as work in progress, one
    without reads as a gap.

## Note for the mock (from ReLeaf's local wiki checkout)

The local `wiki/` checkout may be stale, so treat this as a lead to verify.
The Geospatial Analysis page describes ReLeaf as "a field-deployed bioreactor:
engineered Bacillus subtilis that senses stress in the soil and releases a
protectant". The Laws and Regulations page treats the culture as contained
and the output as cell-free. A regulator would read those as two different
products (contained use versus release). The two pages need the same
sentence.
