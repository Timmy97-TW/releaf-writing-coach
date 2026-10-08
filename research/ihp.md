# Integrated Human Practices casebook

Six Best Integrated Human Practices winners, 2023 to 2025, read for how they write. Two supplementary pages (UZurich 2024 IHP, SDU-Denmark 2023 education) are used where they add something a plant team needs.

Sources are the rendered text files in `sources/text/`. Word counts are rough and include captions and image alt text. Quoted fragments are verbatim from those files (iGEM wiki content, CC BY 4.0). The excerpt bank is `research/ihp.excerpts.json` (34 excerpts). Six of those are counter-examples; their `why_it_works` starts with "Counter-example:" and says what goes wrong.

## Criteria

The 2026 prompt asks how the project affects society and how society shapes it back, and how that feedback entered the work "throughout the Competition". Standard URL: `/human-practices`. Ballot questions:

1. How well was the Human Practices work integrated throughout the project?
2. How inspiring an example is it to others?
3. To what extent is the work documented so that others can build upon it?
4. How thoughtfully was it implemented? How well did they explain the context, rationale and prior work?
5. How well did it incorporate different stakeholder views?

Where each winner answers each question on the page:

| Question | NYU-Abu-Dhabi 2025 UG | WageningenUR 2025 OG | JU-Krakow 2024 UG | Bielefeld-CeBiTec 2024 OG | HUST-China 2023 UG | SDU-Denmark 2023 OG |
|---|---|---|---|---|---|---|
| 1 Integrated throughout | 22 dated cards (28 Jan to 15 Jul) plus two named pivots in "2.1 A Journey of Pivots" | "Our story" #1 to #8 follows the design stages, problem to regulation; no dates | Month headings per workstream, Spring 2023 to Sep 2024 | Timeline Feb to Oct with 39 interview entries, each with an "Implementation" slot | Sections 1 to 10 follow project phases, topic to market | "Integrating Stakeholders In Our Device Development": four implementation drafts, each dropped for a named reason |
| 2 Inspiring | Personal opening; storybook in 16 languages; physician conference | Farmer and seed-sector co-design; wireworm use case; pilot-plant trade-off | First team from its university; independent tester for the device; panic risk handled | Bias self-check after the Thailand interview; hygiene concept for the university | On-site power-plant measurements that overturn the design | Ethics argument on whether to tell the public; greenwashing guard |
| 3 Documented for others | Regulatory guide (US and UAE), physician directory, replicable conference model | "Why we visited / Main takeaways / Reflection & integration" visits; 16 references | 16 summary cards; protocol changes (IMAC, SUMO step dropped); part documentation | Seven named frameworks, feedback template, 19 full interview links, founder Q&A | Miniature fermentation tank offered to the community | 13 entries in one template; value proposition canvas |
| 4 Context, rationale, prior work | Mechanism-level reasons for each pivot; RARE framework | EU REACH dates, polymer comparison, numbered literature | Government report and source papers cited in text | Mendelow, SWOT, AREA, Gibbs; AMNOG and EMA explained | IPCC, WMO and energy yearbook statistics; CCUS explained | Danish waterworks data; consequentialism and deontology with citations |
| 5 Stakeholder views | Researchers, clinicians, one company, three parents, advocacy group in Mexico; conflicting views on Man-1-P reported | Farmers (incl. anonymous and organic), seed companies, regulators (RIVM, EC), pilot plant; negative impacts | Fishermen, academics, industry (BIOTON), iGEM peers, government expert | Patients, a parent in Thailand, physiotherapist, insurance law, ethics committee, industry; surveys | Academics, government agencies, plant engineers, a foundation, a pharma company | Five waterworks, ethicist, toxicologist, companies, politicians, students; split public opinion |

## NYU-Abu-Dhabi 2025

Project: Revitalyze, enzyme replacement for PMM2-CDG delivered by bacterial extracellular vesicles. About 5,800 words.

### Page anatomy

1. Overview (~400): personal stake, three-month ideation, scattered patient landscape, RARE framework, signpost to the timeline.
2. Stakeholder timeline (~1,550): 22 dated cards. Each card is one summary sentence of 25 to 75 words.
3. R, Reflective Discovery: 1.1 Mapping the CDG landscape (~390: outreach, campus survey, geographic inequity); 1.2 Limited patient data (~170).
4. A, Adaptive Innovation: 2.1 A journey of pivots (~780, labelled Initial Approach / What We Learned / The Pivot, twice); 2.2 bEV-delivered protein approach (~285).
5. R, Responsive Implementation: 3.1 Delivery mechanism (~180); 3.2 Walking-assistance device (~210).
6. E, Ecosystem Empowerment: 4.1 Education, initiatives 1 to 4 (~600); 4.2 Resources for families, initiatives 5 to 7 (~530).
7. Limitations (~165), Future Directions (~90), Conclusion (~275 with thanks).

### Opening

Paragraph 1 states the stake in short sentences: someone close to the team has the disease and was sometimes in the lab. Paragraph 2 turns that into a method claim with a number (ideation took three months, one third of the time) and names two abandoned ideas with their reasons. Paragraph 3 says no CDG specialist could be reached in the country, so outreach went international. The framework and the timeline come after. A reader knows the stance, the pivots and the frame before any entry.

### Entry template

Timeline card:

```
[Topic]: [Insight type] from [Name]
[Date]
[Name]'s [role or expertise] revealed / provided [issue A, issue B, issue C] that [effect on the project].
```

Pivot block (the strongest part of the page):

```
Initial Approach: what we planned, and the mechanism we relied on.
What We Learned: We consulted [name, role]. She raised [specific concern]. She questioned whether [alternative]. This reframed our thinking: [old view] → [new view].
The Pivot: We abandoned [X] and redirected toward [Y]. [One line on what this taught us.]
```

Initiative block: "[Stakeholder]'s insight that [gap] directly inspired [initiative]. [Initiative] reached [numbers]. [Before/after result]. For detail, see [page]."

### Evidence and numbers

Numbers sit in the outreach: campus survey of 97 (9 had heard of CDG, 9.2%); format preferences 25/35/40%; Man-1-P at $140 per 10 mg; conference with 71 registrants from 19 institutions, basic-knowledge share 50% before and zero after, 94% rated talks useful; 200+ participants and 42,884 social views. The science pivots use mechanisms (PMI sits in several pathways; Man-1-P has a minute-scale half-life in blood) and no lab numbers. One direct stakeholder quote carries the central problem ("the lack of patients").

### Voice

First person plural. Past tense for events, present for the framework. High emotional register in Overview and Conclusion, with verbless fragments ("Between researchers in France, Mexico, and the United States."). Heavy em-dash use (46).

### Folded or hidden

Full interviews sit behind the timeline cards; only the one-sentence summaries render. Event metrics and the storybook process are pushed to the Education page; construct reasoning to Project Design.

### Weak spots

- Timeline cards are single long sentences with stacked nouns. The Duncker card runs about 70 words in one sentence. Stock phrasing repeats across cards: "provided crucial insights" (twice), "provided invaluable insights", "provided critical technical protocols".
- PMM2-CDG appears in paragraph 3 of the Overview and is spelled out only in section 1.1. "bEV" appears in the timeline before it is defined in 2.1.
- Fructose-6-phosphate is abbreviated "Fru-1-P". Duncker is also spelled "Dunker".
- Construct design is called "an elegant, fail-proof solution" with "robust delivery regardless of chassis variations", yet the Limitations section says the validation experiments were not done.
- Framework labels are stamped on afterwards ("exemplifies Reflective Discovery... and Adaptive Innovation"). They add words and no information.

### For a plant or biomanufacturing team

The pivot block fits any team that changed chassis, strain or product mid-season: plan, who objected and why, what replaced it. The delivery logic (milk, because children with feeding problems cannot take pills) is the model for "fits the farmer's existing routine". The Limitations paragraph separates what was designed from what was shown, which a bioreactor page needs.

## WageningenUR 2025

Project: BCoated, modular bacterial-cellulose seed coatings. About 8,000 words. The closest case to ReLeaf: agriculture, microbial production, scale-up and EU regulation.

### Page anatomy

1. Lead (~165): purpose, "over 35 diverse engagements", who the product was co-developed with.
2. Introduction (~680): what HP is (~50); six actor groups and what each contributed (~260); values fold (~210); why Wageningen and the Netherlands (~115).
3. Stakeholder map (~200; the rendered text is the modal template, see source notes).
4. Our story (~4,000): #1 Problem (~460); #2 Key considerations (~260); #3 Platform material and EU regulations (~355); #4 Bacterial cellulose as candidate (~385); #5.1 Bacteria and consortium (~230); #5.2 Feedstock (~290); #6 Refining coatings and use cases (~370); #7.1 Business plan and scale-up (~375); #7.2 Regulatory institutions (~575); #8 Positive impacts (~480) and Negative impacts and risks (~255).
5. Events (~1,050) and Company visits (~920).
6. Conclusion (~330) and 16 references.

### Opening

Two paragraphs. The first gives the purpose, the count of engagements, the kinds of engagement and the four fields the product must fit (arable farmers, sustainable agriculture, biomanufacturing, regulation). The second lists co-developers and ends on a large claim. The Introduction then gives one short paragraph per actor group saying what that group changed, which doubles as a reading guide.

### Entry template

Story chapter, built around a design question:

```
#N [Design question]
[Name, organisation] warned us that [risk]. Instead, [he/she] suggested [alternative].
This led us to [Name], who confirmed [point]. This became [decision or use case].
[Literature check, numbered reference.]
Based on their input, we needed [next requirement].
```

Company visit:

```
Why we visited: [what we needed from this place].
Main takeaways: [facts learned, with numbers].
Reflection & integration: [what we changed or decided].
```

### Evidence and numbers

Regulation as dated bullets (microplastics restrictions by 2028 and 2031). Market and agronomy figures with references (coatings raise yields 20 to 50%; over 55% synthetic; about 10% of microplastics). Regulator answers with consequences (0.9% GMO DNA threshold in the final product, "regardless of whether the cells are dead or alive"; EU active-substance approval 2.5 to 3.5 years). Pilot plant figures (about 5 million to build a bespoke pilot; seven stirred-tank cellulose processes already scaled at Bio Base). Four numbered figures, three of them photos of their own cellulose samples.

### Voice

We, past tense for the story, present for the product. Calm register. Farmers appear through paraphrase and one long quote; the anonymous farmer is kept anonymous throughout.

### Folded or hidden

Stakeholder bios and quotes are in the map modal. Values open on click. Cost analysis is on the Entrepreneurship page.

### Weak spots

- No dates anywhere. Integration "throughout" is shown by sequence of decisions only; a reader cannot tell what came before the lab work.
- Events read as a diary. The intro is general feeling ("All of these experiences were inspiring"). The summer-school paragraph is about how to win the Entrepreneurship prize.
- Unsupported claims in the lead and introduction: "redefines the role of synthetic biology", "sets new standards", and "CRISPR was discovered here!" with no source.
- The wireworm result is "significantly reduced" with no number or figure on this page.
- Figures repeat: about 10% of microplastics and 20 to 50% yield each appear twice.
- "What is Human Practices in iGEM" explains the competition's own definition to the judges.

### For a plant or biomanufacturing team

Copy the #7.1 paragraph shape for the bioreactor: what the plan was, who showed it had no existing infrastructure, what replaced it, and what that costs ("This might slightly decrease the yields, but..."). Copy #7.2 for any GMO-derived product: the question asked, the regulator's answer, and the part of the process it changes. Farmers are named as end users even though they are not the customer. Negative impacts get one paragraph each with a mitigation (soil microbiome, price for small farms, jobs in the old industry).

## JU-Krakow 2024

Project: PrymDetect, a SHERLOCK field test and 3D-printed reader for golden algae (Prymnesium parvum). About 8,200 words.

### Page anatomy

1. Overview (~250): first team from the university; why golden algae; the tool and four design goals.
2. "Whom did we contact?" counters (render as 0, see source notes).
3. "Our human practices in a nutshell" (~1,820): 16 cards, each Who we contacted / Why / What we learned / What we adapted.
4. Narrative by workstream with month headings: How did it all start (~560); Protein production and purification (~1,100, including genome troubleshooting); 3D printing, the PrymChip (~640); Consultations at conferences (~1,050); PCR troubles (~90); Alga Lab (~450); Social acceptance (~150); Expert evaluation (~420); Progress meetings (~260); Part design (~350); Presentation (~130); IP (~60); Further development (~170); Gratitude (~130); References.

### Opening

Paragraph 1 is about the team (first from the Jagiellonian University, only Polish team) and an unnamed "ecological problem". Paragraph 2 says conversations mattered more than literature. The concrete problem (1,650 tons of dead fish, a 60% drop) only arrives in "Spring 2023". Weak start; the cards then carry the page.

### Entry template

Card:

```
Who we contacted: [Name(s)]
Why: [the problem we had]
What we learned: [1–3 specific points]
What we adapted to our project: [the change, ideally with a number]
```

Narrative entry: "[Month Year]. [Problem]. We consulted [Name, department, why them]. [Advice]. [What we tested or decided], [result]."

### Evidence and numbers

Lab and field numbers tied to advice: pH 5.5 to 7.3; 14/10 light cycle; fluorescein 0.78 to 100 µM for the independent test; 100% BLAST identity; strain KAC39. Context numbers from cited sources (1,650 tons, 60%; blooms in at least 13 countries). Photos with captions, including a translated warning sign at the reservoir.

### Voice

We, past tense, lively. Story headings ("An Endless Tale of PCR Troubles", "A light at the end of the tunnel appeared"). Honest about being new ("None of our team members had any prior experience working with algae").

### Folded or hidden

Cards end in "Find out more!", which jumps to the narrative. Counters are animated.

### Weak spots

- Every consultation is told twice: once as a card, once in the narrative.
- Several "What we adapted" slots hold no change: the ValleyDAO card ("We will try to incorporate all of this advice into our presentation"), the Symbioza card ("We deepened our understanding"), the Dziga card (he "will consider forming a dedicated team").
- "To Protect or Not to Protect: That is the Question" asks whether to patent and never gives the answer.
- Lab troubleshooting with instructors fills much of the page. Social and end-user voices are few: one site visit to fishermen and the panic concern.
- Small slips: "lightning" for lighting; "5,5 to 7,3" in one place and "5.5 to 7.3" in another.
- The Gratitude section praises the team ("remarkable creativity").

### For a plant or biomanufacturing team

The card is the best short summary format in the set. The independent-tester section (someone outside the team uses the device and lists problems: drawer, phone support, camera) maps directly to a farmer or operator trying the bioreactor. The social-acceptance entry shows how to handle a perception risk with a named source, a second opinion and two concrete actions.

## Bielefeld-CeBiTec 2024

Project: PreCyse, prime editing for cystic fibrosis with lung-targeted LNPs. About 45,400 words, six times the next longest. Mapped in full; read selectively.

### Page anatomy

1. Abstract (~765): framework claim, stakeholder counts, the HP definition quote, seven stakeholder categories.
2. Introduction (~725): HP questions, strategy list, goals, target groups.
3. Framework (~3,760): list of seven tools; stakeholder management framework; Mendelow power-interest matrix; SWOT tables for 13 stakeholder groups; Third-Party Feedback Template; AREA; feedback cycle; Gibbs reflection cycle.
4. Timeline (~30,700): about 64 cards by type (Milestone, Patient, Academia, Industry, Medical Professional) from February to October, then 64 entries. 39 are stakeholder entries with Summary / Aim of contact / Insights / Implementation and a pull quote; the rest are milestones with a summary, a bullet recap and a team-member quote. Ends with the Jamboree, prizes, a paper and "Carry It Forward".
5. Implementation & Feedback (~420): survey results; "Stakeholder Analyses" (18 headings, content folded).
6. Conclusion (~820): seven sub-heads and Next Steps.
7. Further Engagement (~8,200): Education, Public Engagement, Entrepreneurship (ten founder questions), Collaborations, Partnerships.

### Opening

The abstract leads with method size: "seven reglementations", "seven frameworks", "over 80 interviews", "33 key interviews", "five iterative feedback loops". Then the HP definition quote and a list of seven stakeholder categories with one generic sentence each. The cystic fibrosis problem is barely stated in the first screen. The reader learns how big the method was before learning what it was for.

### Entry template

```
[Name]
[Role] - [Institution]
Original language: [language]
Summary: [whole entry in 80–150 words]
Aim of contact: [why this person; the question we brought]
Insights: [what they told us]
Implementation: [what we changed]
"[Pull quote]" — [Name]
Read full interview
```

Founder interviews use a second template: What we asked the founders / What the founders had to say / Learnings and implications for our project.

### Evidence and numbers

Best where a single entry carries protocol numbers: lipid-to-nucleic-acid ratio 22:1 to 10:1, storage at 4 °C, named QC methods (Radukic). The Bauder entry cites four papers to test its own target choice. The physiotherapy visit gives session length (30 to 60 minutes), four observed sessions and short anonymised patient vignettes. Stakeholder counts in the abstract are undefined and do not match each other.

### Voice

"We" in Aim, Insights and Implementation. Several Summaries switch to third person ("This team is an excellent example", "prompted the team to reflect on their focus"). Formal and repetitive: "valuable" or "invaluable" 85 times, "crucial" about 50.

### Folded or hidden

Stakeholder analyses, full interviews (19 links), Mendelow quadrant details, survey results and a handbook download.

### Weak spots

- Each interview is told three times (Summary, Insights, Implementation), which explains much of the length.
- An unfilled placeholder in the Gibbs section: "conducted with X groups of stakeholders".
- The Conclusion says "we ensured our therapy addressed a wider range of CF mutations". The Bauder entry says a change of target was "not being feasible anymore" and F508del stayed.
- The Mendelow matrix puts patients and patient organisations at "Low Power, High Interest - Priority Level 2", while the page calls patients "At the heart" and credits patient Max with moving the target from pancreas to lung.
- The Berens entry asks whether the project needs an ethics vote and never states the answer.
- Seven frameworks are described in general terms. The entries do not show which AREA or Gibbs step they are.
- Some Implementation slots are attitudes ("a more empathetic understanding", Olariu). Trade-fair milestones (Hannover Messe, LabSupply) carry no HP content.
- "Our Entrepreneurship" opens with "In conclusion,".

### For a plant or biomanufacturing team

Take the "Aim of contact" slot: it forces the writer to state the question before the answer. Take the Bauder move: ask whether a core choice (crop, region, peptide, chassis) came from bias, check it, and report the answer even when the choice stands. Take the Radukic Implementation as the standard for protocol changes. Avoid the scale: length here hides the best entries.

## HUST-China 2023

Project: engineered Synechocystis and Shewanella that fix CO2 and generate electricity at coal-fired power plants, with hardware. About 4,200 words.

### Page anatomy

1. Section 1 Topic selection (~370): global warming statistics, China's coal share, focus on coal plants.
2. Section 2 Background investigation (~775): Prof. Luo, CCUS explained, government agencies, iCarbonMap emissions data.
3. Section 3 Initial design (~380): strains, inserted genes, two experts' advice.
4. Section 4 Design refinement (~540): resistance genes, Prof. Zhang, TIB visit.
5. Section 5 Hardware (~755): 5.1 waste heat with Prof. Li; 5.2 refinement; 5.3 miniature fermentation tank after a pharma company visit.
6. Section 6 On-site research (~510): power-plant measurements, relocation, SO2 data, engineers' concerns, foundation feedback.
7. Section 7 Market research (~230); Section 8 Positive feedback (~170); Section 9 Alternative application (~80); Section 10 Education links (~260).

### Opening

Three paragraphs of global statistics (IPCC, WRI, WMO, China Energy Statistical Yearbook) before any stakeholder. The first sentence carries a doubtful, unsourced figure (Arctic summer average of "an astonishing 30°C"). The fourth paragraph narrows to coal-fired plants. This is the weakest opening of the six.

### Entry template

```
[Need or phase]. We consulted [Name], [institution], who [credentials].
[Fig. N: photo of the expert or meeting]
During our discussion, [Name] explained / recommended [advice].
After [literature review / careful consideration], we [decision].
[Name] acknowledged the feasibility of / expressed confidence in our project.
```

### Evidence and numbers

The site section is the model: cooling-tower water about 18 °C in winter against the 30 °C culture needs, so the first site was dropped; the exhaust spot holds about 45 °C year round, so the hardware moved there; desulfurized flue gas below 30 mg/m³ SO2, so the resistance genes were dropped. Context numbers are from cited reports. 23 figures; most show people at meetings or visits.

### Voice

We, past tense, formal. Adjective-heavy ("astonishing", "valuable" 11 times in 4,200 words). Long expert credentials.

### Folded or hidden

Little. Detail is linked to Design, Hardware, Implementation and Education sections.

### Weak spots

- Long generic opening; literature review inside HP (Section 2 compares physical and chemical capture methods).
- Praise as evidence: Section 8 is titled "Positive Feedback"; experts "acknowledged the feasibility", a foundation "expressed confidence".
- Market section is speculative ("prices... are expected to soar") with no figures.
- Gene names listed without explanation (ycel, pncB, nadM, nadD*, nadE*).
- Section 9 (road lighting) has no follow-up. No dates on the page.
- Self-assessment as a transition: "After recognizing the importance and viability of our project".

### For a plant or biomanufacturing team

Go to the deployment site and measure before fixing the reactor design: temperature, power, water, space. Report the number that changed the plan, and the new number that justified the new plan. Section 5.3 (lab flasks do not behave like industrial fermentation, so a scale-down tank was built) is the argument a farm-scale bioreactor page needs.

## SDU-Denmark 2023

Project: vitroFAS, enzymes (vitroZymes) that degrade PFOA, placed in Danish water treatment. About 7,900 words.

### Page anatomy

1. Overview (~250): HP as a pillar; the two HP questions; goal and product; scope of engagement; a toggle between two halves.
2. Working With People (~3,380): intro (~175) and 13 entries (180 to 420 words each).
3. Concern for PFAS (~370); The Fear of GMOs (~320, cognitive bias); Ethics (~795, whether to inform the public); Demystifying GMOs and PFAS (~440).
4. Integrating Stakeholders In Our Device Development (~1,290): household or state; four implementation drafts (submarine with live cells, bacteria in sand filters, vitroFilter, cleaning resin beads) and the final design; Final thoughts.
5. Value Proposition Canvas (~425) and Avoid greenwashing (~115).
6. Conclusion (~150).

### Opening

The Overview restates the two iGEM HP questions, gives the goal and the product in one sentence each, and lists who was engaged (citizens, politicians, PFAS experts, water companies). Then a navigation instruction. Plain and short; no hook.

### Entry template

```
### [Name] – [role / organisation]
Why did we establish contact? [Who they are; what we wanted from them.]
What we learned
- [fact, often with a number]
- [fact]
Reflection
[What this means for us; what we decided.]
```

### Evidence and numbers

Stakeholder-sourced figures in the bullets: a new borehole costs 1.2 million DKK; resin filter at 250 L/h, 4,500 L of resin for about 900,000 DKK, 2 to 3 year life; 22 PFAS types measured in wastewater; 67 of 224 waterworks above the limit; 67% of surveyed Coop customers worried; one of 30 students had heard of PFAS. Each number is attributed to the person or document it came from.

### Voice

We, past tense, plain, sometimes conversational ("We got blown away by the extortionate cost"). The Ethics section switches to an academic register with encyclopedia citations.

### Folded or hidden

The two halves toggle. The ethics argument sits in a dropdown. Implementation and Model pages hold the detail.

### Weak spots

- The "Reflection" label invites feelings. Grandjean's reflection ("we contemplated", "began to brainstorm") and the SDU RIO reflection change nothing.
- The Conclusion says the solution "has developed into a product that can be implemented in the real world". The Bioomix entry says the vitroZymes "were not ready to be tested before the deadline".
- The "Concern for PFAS" paragraph says relevance was confirmed at the People's Climate Meeting in Middelfart, then describes the People's Meeting on Bornholm in the next sentence.
- Ethics definitions are garbled (cognitive bias; "pro-science deniers... deceit themselves").
- The value proposition canvas was built with one engineering student and reads as theory.
- "access the impact" for assess; generic "Final thoughts".

### For a plant or biomanufacturing team

The household-or-state paragraph is the model for "who is the customer and why": a value (clean water is the state's job) changes the business model. For ReLeaf the same question is farmer, cooperative or distributor. The greenwashing guard is the model for biostimulant claims: limit the claim to what was tested and say what partners may not claim. Rename "Reflection" to "What we changed" before reusing the template.

## Supplementary cases

UZurich 2024 IHP (the team won Sustainable Development, not IHP). Opens with four sets of questions, each answered by one stakeholder group: lab experts, farmers and agricultural experts, ethics/politics/law/consumers, industry. Entry: short bio, a bullet list of topics ("We talked about:"), then a paragraph of consequences. Strong entries: Emmenegger (wet years and pathogens reframe the product; xylose sensing confirmed), Vaderna (a GMO critic's points become testing obligations), Niklaus ("currently our project could not be legally implemented in Switzerland"). Weak: topic bullets list subjects and no findings; lab-expert entries are thin; no dates. The plant-microbe setting and the regulatory blocker stated plainly make it useful to ReLeaf.

SDU-Denmark 2023 education subpage. A before-and-after questionnaire with counts (13 thought exposure was limited before, 6 after; 8 thought it frequent before, 16 after), post-it feedback, and the changes made to the material. Short proof that outreach can report an outcome.

## Cross-case synthesis

### Shared skeleton

1. An opening that states the problem and the team's HP stance (three of six also restate the iGEM HP definition).
2. A stakeholder index: timeline cards, a map or summary cards, each a few lines.
3. An argued narrative where stakeholders appear as causes of design decisions, ordered by phase (HUST, JU), by design question (WUR), by pivot (NYU) or by implementation draft (SDU). Bielefeld is the exception: its narrative is the people timeline itself.
4. Outputs beyond the lab: guides, directories, education, hygiene concept, community tools.
5. Limits, next steps and a conclusion.

The argued part is organised around decisions. The people list is an index. Bielefeld, organised by person, has to rebuild the decisions in its Conclusion, and that is where it contradicts its own entries.

### UG and OG

- UG pages (NYU, JU, HUST) are 4,000 to 8,000 words, mostly chronological, and lean on academic advisers for feasibility and lab troubleshooting. They tell persistence stories ("Many attempts went unanswered", "The only person who responded").
- OG pages (WUR, Bielefeld, SDU) add business, regulation and ethics layers: pilot plants and regulators (WUR), formal frameworks (Bielefeld), ethics theory and a value proposition canvas (SDU). They reach more of the supply chain.
- Loop-closing quality does not track track or length. HUST at 4,200 words has cleaner evidence-to-change chains than Bielefeld at 45,000.

### 2023 to 2025

- 2023 (HUST, SDU): organised by phase or by person; photos as figures; endorsements as endings; ethics as an essay.
- 2024 (JU, Bielefeld): volume and apparatus peak. Card UIs and modals arrive; JU tells everything twice; Bielefeld adds seven frameworks the entries do not visibly use.
- 2025 (NYU, WUR): the argued text is shorter and built as a decision chain (numbered story, named pivots). Stakeholder detail moves into cards and modals. Both have their own section for limitations or negative impacts. Outreach is reported with before/after numbers, regulation with dates and standards.

### Loop-closing sentence patterns

Short fragments from the winners, each closing the loop between input and change:

- Warning plus alternative: "warned us that microbial inoculants can disrupt soil communities ... Instead, he suggested" (WUR)
- Hand-off to the next step: "This led us to" ... "This became our first proof-of-concept use case" (WUR)
- Measurement kills a plan: "As a result, our initial plan ... proved unfeasible." (HUST)
- Before and after with units: "we adjusted the lipid-to-nucleic acid ratio from 22:1 to 10:1" (Bielefeld); "changed it from 5,5 to 7,3 (as he recommended)" (JU)
- Dropped with reason: "Considering the safety and practical aspects, we decided to abandon this idea." (JU)
- Trade-off stated: "This might slightly decrease the yields, but the capital expenditures are not worth the increase in yield." (WUR)
- Back to the start: "so we went back to the drawing board." (SDU)
- Shaped a plan: "This shaped our business plan: we included regulatory timelines" (WUR)
- Confirmation, stated as such: "We were also confirmed in our decision of choosing to focus on PFOA" (SDU)
- Checked though unchanged: "Despite a change of target not being feasible anymore, we looked into it" (Bielefeld)
- Insight to design: "This insight fundamentally shaped our delivery approach. We developed" (NYU)

The verbs that close a loop are adjusted, changed, dropped, abandoned, moved, selected, built, added. The verbs that leave it open are learned, understood, contemplated, reflected, appreciated, will try.

### Anti-patterns seen in winners

1. Praise as evidence: endorsement endings and praise pull quotes (HUST Section 8; Bielefeld quotes such as "Wow, you’re already further along than I was!").
2. Intentions in the change slot: "We will try to incorporate" (JU); "we contemplated" (SDU); "a more empathetic understanding" (Bielefeld).
3. Undefined or clashing counts: Bielefeld abstract; the "X groups" placeholder.
4. Conclusions that outrun the entries: Bielefeld on mutations; SDU on real-world readiness; WUR "sets new standards".
5. Framework theatre: named methods the entries never use (Bielefeld AREA and Gibbs); labels stamped after the fact (NYU RARE).
6. Assumed knowledge: disease and vector abbreviations before definition (NYU); gene lists (HUST).
7. Telling it twice or three times: JU cards plus narrative; Bielefeld Summary plus Insights plus Implementation; WUR repeated statistics.
8. Generic openings: global statistics (HUST); stakeholder-category lists (Bielefeld); explaining HP to the judges (WUR).
9. Diary entries: events and fairs with no change (WUR Events; Bielefeld trade fairs).
10. Voice slips: third-person summaries inside a "we" page (Bielefeld).
11. Questions raised and not answered: patenting (JU); ethics vote (Bielefeld).
12. Name and unit slips: Duncker/Dunker, Fru-1-P (NYU); Kristiann, Bielfeld (Bielefeld); 5,5 and 5.5 (JU).

## Rewrite checklist

Each rule can be checked by reading the page.

1. Every stakeholder entry ends with a change you can point to: a number, a dropped option, a new part or a decision. Check: underline the last sentence of each entry; if its main verb is learned, understood, reflected or will, rewrite it. Reason: this is the integration judges score. Shown by JU (pH card), Bielefeld (Radukic), HUST (cooling tower).
2. State each change as before and after, with units. Reason: a number can be checked; "optimised" cannot. Bielefeld, JU, WUR.
3. Report at least one option you dropped, who caused it and why. Reason: a dropped option is the clearest proof that input changed the project. All six; strongest in NYU, SDU, HUST.
4. Organise the argued text by decisions or design questions; put the list of people in an index. Reason: readers follow a decision chain; a list of names has no thread. WUR, NYU.
5. Use one fixed entry template and name the last slot after action ("What we changed"). Reason: the label decides what gets written there. WUR, JU, Bielefeld; SDU's "Reflection" shows the risk.
6. Open each entry with who, their role, the date and the question you brought. Reason: the reader needs to know why this person before what they said. Bielefeld "Aim of contact", SDU "Why did we establish contact?", NYU dated cards.
7. Define every abbreviation and trade term at first use on the page, in the same sentence. Check: search the page for capitalised abbreviations and confirm each is expanded at its first appearance. Reason: judges come from other fields. WUR ("seed stickers"), HUST (low-quality heat); counter NYU (PMM2-CDG, bEV).
8. Give every number a source and a consequence in the same or next sentence. Reason: a number with no "so what" is decoration. NYU survey, WUR regulators.
9. Remove praise used as evidence; move thanks to acknowledgements. Reason: an expert liking the project is not a change to it. Counter HUST Section 8.
10. When stakeholders disagree, put both views side by side and say what you did. Reason: hiding a conflict reads as cherry-picking. Bielefeld (Max and Joshua), NYU (Alaoui and Andreotti).
11. Check the conclusion line by line: each claim must point to an entry that supports it. Reason: winners lose credibility exactly here. Counter Bielefeld, SDU.
12. Limit product claims to what was tested and write a limitations paragraph. Reason: overclaiming is easy to spot against the Results page. SDU greenwashing, NYU limitations.
13. Name negative impacts and give each a mitigation. Reason: the prize asks how the project affects society, which includes harm. WUR.
14. Count once, name the unit (people, organisations, interviews) and use the same number everywhere on the wiki. Reason: clashing counts read as inflation. NYU's 22 is consistent; counter Bielefeld.
15. Include an event only if it changed something; otherwise cut it or move it to a list. Reason: diaries bury the loops. WUR company visits pass; WUR Events fail.
16. Open with your own problem and stake in two or three paragraphs. No restated HP definition, no global statistics wind-up. Reason: the first screen decides whether a judge reads on. NYU, WUR; counter HUST, Bielefeld.
17. Keep "we" and past tense for what happened, present tense for what the product does. Reason: switching person or tense makes it look pasted. Counter Bielefeld summaries.
18. One paragraph covers one interaction or one decision, in about 150 words or fewer. Reason: long multi-topic paragraphs hide the change. JU cards, WUR brewery visit.
19. If you raise a question, answer it on the page. Reason: an open question reads as unfinished work. Counter JU (patenting), Bielefeld (ethics vote).
20. Link to the Engineering, Implementation or Education page for detail instead of repeating it. Reason: repetition doubles length and risks contradiction. NYU, HUST.

## Source notes

- WageningenUR: the stakeholder map renders as its modal template ("NAME OF STAKEHOLDER", "Lorem ipsum", "Quotes from them") followed by image labels only. Per-stakeholder bios and quotes are missing from the text file; check the live page before judging the map. Several event images have alt text ending in "placeholder", which may be alt text only.
- NYU-Abu-Dhabi: each timeline card heading appears twice (card and modal title). Only the one-sentence summaries render; any longer interview text behind the cards is missing.
- JU-Krakow: the "Whom did we contact?" counters render as "0 individuals", "0 institutions", "0 iGEM teams" (animated counters captured before they ran). Card titles are missing; each card starts at "Who we contacted:". The subsection "Prymnesium parvum genome – creative troubleshooting" renders as plain text.
- Bielefeld-CeBiTec: "Stakeholder Analyses" (18 items) renders as headings only; 19 "Read full Interview here" transcripts and "Full results of our surveys" are not captured; Mendelow quadrant images say "Click on the images". The "X groups" placeholder is in the rendered text, so it was on the live page.
- SDU-Denmark: both halves of the toggle are captured. The value proposition canvas is an image only.
- SDU education subpage: one PDF failed to render ("Unable to display PDF file").
- HUST-China: figures are images with captions only; text is complete.

## Hidden text recovered

On 8 Oct the text behind both pages' clicks was recovered in full: sources/text/ihp-2025-UG-nyu-abu-dhabi.cards.md (22 cards, from the site's JS bundle) and sources/text/ihp-2025-OG-wageningenur.map.md (30 map nodes, from data attributes in the page HTML). The two source-note bullets above about missing modal text no longer apply. New excerpts are in research/ihp-hidden.excerpts.json.

### NYU-Abu-Dhabi cards

- Every card opens to the same three slots: Rationale, Interview Summary, Integration. The one-sentence card text is only the front.
- The full entries add about 5,800 words, as much as the visible page. A typical entry is 250 words: a 40-word rationale, a 100-word interview summary and a 100-word integration.
- Rationale says who the person is and what the team asked them. Interview Summary reports what they said, with no team reaction. Integration says what changed. Talk and response never mix inside one slot.
- The loop closes best when Integration names a dropped plan (Montclare: PMI inhibition abandoned; Afzal: desalination dropped) or a thing built (Lisa: walking-assistance prototype; Kara: Milo the Monkey; Duncker: physician directory).
- The cards argue with each other. Rabeh's Integration corrects Gyorgy's advice. Alaoui's answers part of Andreotti's doubt. Palanikumar's adds up Rabeh and Andreotti. The visible page hides this chain.
- Many Integrations end on a moral line ("taught us to prioritize patient safety over technical novelty"). The decision sentence before it does the work.
- Weak entries: Karen's Integration is 41 words with no change. Gonzalez-Kozlova's says his method made EVs look easier, then that simpler delivery "might be more appropriate". Stanley's ends on a future step, and Kozicz's on the partner's interest.
- Slips: the Nuha card title says "Nuha Salem", and its Rationale says "Nuha Mehdi". "Malcom" sits next to "Malcolm". "Dr. Eva Morav’s" appears in the Stanley entry. One Rationale starts with the word "Rationale" twice. Each parent interview ends "Read more about ... story here." and none of them links anywhere.

### WageningenUR map

- 30 nodes in four groups: Industry 13, Farmers 3, Academia 9, Regulatory institutions 5. Six nodes share text: the three SUMATRIX people have one entry between them, and so do the three RIVM people. That leaves 26 distinct entries and about 5,500 words.
- The template is fixed: Why we reached out (or Why we visited), Main takeaways, Reflection & integration. 28 of 30 nodes use it. The Centre for Living Technologies node is an event report. Robin Reijnen has no reflection slot.
- Takeaways are numbered lists of up to 12 points. Reflections are short, often 20 to 60 words. A long list followed by one sentence is common (Foamlab: 12 takeaways, 1 reflection sentence).
- Seven nodes carry a pull quote. No node has a date, so the map cannot show when advice reached the lab. This matches the weak spot noted above for the story section.
- The loop closes by links. Foamlab's warning about sticky cellulose sends the team to Hussain. Hussain's beer-waste tip sends them to the brewery. Singh's tray bioreactor is dropped after Bio Base Europe. Van den Ende connects them to Carapace. Etalo points to Rodenburg. Several reflections link to the Proof of Concept and Seed Coating pages for the result.
- Best entries tie one fact to one lab or business change: Thiyagajaran (hydroxyl groups become an enzymatic-modification project), Kafka (the value proposition moves to how easily active compounds go in), Carapace (seeds coloured with natural dyes).
- Weak entries: the RIVM and DG SANTE reflections say "We have adjusted our timeline" and do not say how. Bert Smit's six takeaways name two approval bodies, and his reflection uses none of them. The organic-farmer entry ends "We have not received a response yet". That is an honest open loop and a fair model for one.
- Slips: "doesn not", "assesments", "Striga hermontica", a stray "}" inside the NanoCell quote, and a literal "\&" in Bert Smit's title.

### What this changes for the coaching

- Both winners keep the argued text short and put about 5,500 to 5,800 words of per-person detail behind clicks. Judges who click get a fixed template every time.
- Both templates give the change its own labelled slot (Integration; Reflection & integration). The label works only when the slot names a decision. Karen, RIVM and Bert Smit show what happens when it does not.
- NYU writes the slot as prose and cross-references other experts. WUR writes it as a list plus one short paragraph and cross-links other nodes. Either works. Pick one and keep it for every entry.
- For ReLeaf: a stakeholder card can follow WUR's three labels. Add a date, which neither winner's map has. End the last slot on what was dropped, built or changed.
