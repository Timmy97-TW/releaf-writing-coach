# Geospatial Analysis casebook

Research base for the margin feedback on ReLeaf's "Geospatial Analysis" page.
There is no iGEM prize for GIS work, and only one recent team (Marburg 2024)
has a standalone GIS page. The other precedents are GIS sections inside Model
pages. None of the secondary teams was nominated for a special prize, so they
are here for what they show about explaining spatial methods, with their
faults named.

Sources: `sources/text/` files named below; URLs in `sources/pages.txt`.
All quoted text is CC BY 4.0, credited to the team named.

## What the page is judged on

A GIS page has no Standard URL. Judges reach it from Model, Sustainability,
Entrepreneurship or Human Practices, so each of those needs a sentence on
what the maps decided, with a link. The page can answer these ballot
questions (`judging-special-prizes.md`):

| Prize | Ballot question | What the GIS page supplies |
|---|---|---|
| Sustainable Development | Did the team address potential long-term social, environmental and economic impacts of their work? | Where climate stress falls now and how it moves under future scenarios |
| Sustainable Development | Has the team documented their work against their chosen SDG(s) so that other teams can build upon their work? | Named datasets, thresholds, versions and code, reusable by the next team |
| Sustainable Development | Has the team's work measurably and significantly addressed one or more SDGs? | Areas in km² or hectares, farm counts, people affected |
| Entrepreneurship | Has the team identified their first potential customers and their unmet need(s)? | Where the first customers are, and why there first |
| Entrepreneurship | Has the team presented logical product development plans with realistic milestones, timelines, resources and risks? | Rollout order, distribution distances, logistics cost |
| Integrated Human Practices | How well did they explain the context, rationale and prior work? | The spatial context for the problem, with prior suitability models cited |
| Best Model | Did the team use experimental or other relevant data to develop, train, or validate the model? | Validation statistics, agreement between models, ground checks |
| Best Model | Did the model help the team understand, predict, or design a part, device, or system? | Only if the map changed a design or deployment choice |
| Best Software | Can the software be useful to other projects? Is it documented for future groups to extend? | Only if the code is released under an OSI licence in the team's iGEM GitLab repository |

The test for every GIS page is the Best Model question in the second-to-last
row: what did the map change?

## Cases at a glance

| Case | Prize standing | What it is | Why it is here |
|---|---|---|---|
| Marburg 2024 | Best Plant SynBio winner (OG), Best IHP nominee | Standalone page "Geospatial Analysis", about 6,700 words, 12 figures, 5 tables, 3 videos, 48 references | Primary case. Global climate suitability for two rubber crops, now and under three climate scenarios, plus a disease hotspot model |
| IISER-Pune-India 2022 | No special-prize nomination found (the 2022 nominee "IISER-Pune2_India" is a different team) | "Climate Modelling for Waterlogging hotspots in India", a section of the Model page, about 760 words | Plant-growth-promoting bacterium for farmers, satellite indices in QGIS and Google Earth Engine, map tied to a bioreactor rollout plan |
| XJTLU-China 2025 | No special-prize nomination found | MaxEnt species distribution model for *Ulva prolifera*, a section of the Model page, about 1,280 words | Clearest explanation of data cleaning and validation for a suitability model |
| HUBU-China 2024 | No special-prize nomination found | MaxEnt model for an agricultural pest, a section of the Model page, about 860 words | Contrast case. Software output pasted into the page; the conclusion claims more than the map can show |

How the extra teams were found: all 1,062 competition wikis from 2022 to
2025 were listed through the iGEM teams API; slugs such as `gis`,
`geospatial`, `geospatial-analysis` and `mapping` were probed; and the
Model, Human Practices, Sustainability, Description, Implementation,
Entrepreneurship and Safety pages of every team built on the standard
template (about 7,400 pages) were searched for GIS, QGIS, ArcGIS, geospatial,
Landsat, Sentinel-2, Google Earth Engine and MaxEnt. Only four teams did
substantial spatial analysis; the other hits were references or passing
mentions. Teams whose wikis are single-page apps (about 70) were not
searched in full text.

Marburg's abstract calls itself "the first iGEM team to integrate Geospatial
Analysis into our project". IISER-Pune-India built satellite-index maps in
QGIS and Google Earth Engine two years earlier. Marburg may mean the first
dedicated page; as written, the claim does not hold.

---

## Marburg 2024

Files: `mar-2024-gis.md` (rendered page; the site source `gis.txt` holds no
extra content), `mar-2024-hp.md`, `mar-2024-sustainability.md`.

Project: engineered Russian dandelion (*Taraxacum kok-saghyz*, TKS) as a
temperate rubber crop next to the rubber tree (*Hevea brasiliensis*). The GIS
page asks where each crop can grow now, where it will grow under climate
change, and where the rubber tree's worst disease could spread.

### Page anatomy

| Section | Words | Figures and tables |
|---|---|---|
| Abstract | 150 | |
| Introduction | 450 | |
| Motivation | 410 | |
| Data & Technical Background | 480 | |
| Climatic Suitability Criteria | 400 | Figure 1 (workflow) |
| H. brasiliensis Cultivation Zones | 570 | Table 1 (thresholds), Figure 2 (2018 map), Video 1 (1980 to 2018 timelapse) |
| Habitat Suitability Model for T. kok-saghyz | 1,130 | Figure 3 (native sites), Table 2 (17 field-trial sites), Figures 4 and 5, Table 3 (new thresholds), Figure 6 (both crops) |
| Natural Rubber in the Age of Climate Change | 940 | Figure 7 (scenarios) |
| Modelling the Effects of Climate Change | 370 | Table 4 (five climate models), Figure 8 (ensemble and confidence) |
| Effects on Natural Rubber Production | 560 | Figure 9 (maps by scenario and period), Figure 10 (km²), Figure 11 (Sankey) |
| Disease | 940 | Figure 12, Table 5, Videos 2 and 3 |
| Conclusion & Outlook | 260 | |
| Materials and Methods | 50 | |
| References | 48 entries | |

The page reads like a paper: abstract, background, methods woven into
results, conclusion, short methods block, references. A sticky contents list
sits beside it.

### How it opens

The abstract states the result in its second sentence ("we mapped the global
distribution of Hevea brasiliensis ... under current and future climate
scenarios"), then the second finding (the first suitability parameters for
TKS), then what it is for ("data-driven recommendations for diversifying the
natural rubber supply chain"). It leans on superlatives ("the most detailed
model to date", "the first iGEM team") that the page cannot back up.

### How methods, data and limits are explained

This is the page's strength, and the part most worth copying.

- Data choice is argued. The page sets the requirement first (monthly
  temperature and precipitation, decades of history, future projections, fine
  resolution), names four candidate datasets, and says why CHELSA won.
- Units are translated. "0.25° to 1°, equivalent to about 25 to 100 km at the
  equator"; "30 arc-seconds, approximately 1 km² at the equator".
- Thresholds sit in tables with their source (Table 1 from Rivano et al.
  2015; Table 5 from Roy et al. 2017), and a workflow figure shows the
  classification steps.
- The direction of error is stated before the results: suitability models
  "often tend to overestimate", because they ignore topography, population,
  soil and pests. The overestimate is then named on the map (South America,
  where leaf blight blocks cultivation).
- Uncertainty is shown. Five climate models are run separately; the page maps
  the majority result and, beside it, how many models agree. The text says
  where agreement drops (far future, high-emission scenarios, edges of the
  zone).
- Maps become numbers. Areas are recomputed on the Earth's ellipsoid before
  being reported in km², with a sentence on why a flat map distorts area.
- Figure choice is justified: a Sankey diagram, because cross-tabulation
  tables are "difficult to interpret at a glance", with a citation.
- Field knowledge enters the model. Native-site climate data suggested a
  narrow niche; interviews with TKS farmers said the crop is adaptable; the
  team then added 17 field-trial sites (two from its own interviews) and built
  wider thresholds.

### Voice and tense

First person plural, past tense for what was done, present for what the maps
show. Long sentences with stacked clauses. Heavy use of "crucial" (8),
"essential" (10) and "robust" (3).

### Weaknesses

- The map does not visibly change the project. The page ends on
  recommendations for "policymakers and stakeholders". It never says what
  the team did differently because of it (which TKS traits to engineer,
  where field trials should go). Only the Description and Climate pages link
  to it, in passing.
- Class names change. The same four classes are "AllOpt / SubOpt / SingProh /
  MultProh", then "Optimal / Suboptimal / Single prohibitive / Prohibitive"
  in a caption, then "optimal, suboptimal, marginal, and prohibitive" in the
  climate section.
- No validation against where rubber is actually grown. The 2018 map is never
  compared with known plantation maps, and the TKS thresholds rest on four
  native sites and 17 trials whose outcomes are not reported.
- The scenario bullet lists (SSP1, SSP3, SSP5) follow the published scenario
  narratives very closely, without quotation marks.
- One factual slip in the introduction: zones shifting to "higher latitudes
  and longitudes" (later corrected to altitudes and latitudes).
- Not reproducible from the page. Software versions are listed, but there is
  no code or processed data link.
- The 940-word climate-change background section could be a paragraph.

### What ReLeaf could take

- The uncertainty map beside every forecast map, and one sentence on where
  agreement is weakest.
- State which way each map errs (over or under) and the reason, before the
  reader sees the map.
- "Why this dataset": name the alternatives considered and the one property
  that decided it.
- The interview-to-model move: a farmer or agronomist contradicts the
  literature, and the thresholds change. If any ReLeaf interview changed a
  threshold or a layer, say so on the GIS page.
- One class vocabulary, used identically in text, legend and table.

---

## IISER-Pune-India 2022

Files: `gis-2022-iiser-pune-india.md` (Model page; section "Climate
Modelling for Waterlogging hotspots in India"),
`gis-2022-iiser-pune-india-hp.md`, `-entrepreneurship.md`,
`-implementation.md`.

Project: an engineered *Azospirillum* biofertiliser carrying ACC deaminase, to
help crops survive waterlogging. Close to ReLeaf: a beneficial bacterium for
crop stress, a bioreactor in the production plan, and a map to decide where
to sell first.

### Page anatomy

About 760 words inside a long Model page: why (people confused waterlogging
with flooding; the start-up needed priority regions); a failed first method
(k-means segmentation, pixel masking); four satellite indices defined in one
line each; the workflow (thresholds, then SNAP and QGIS on Sentinel-2 for one
area in Punjab, then Google Earth Engine on Landsat 8 for India); three national
maps, each with its thresholds, a legend reading and a list of states; a
conclusion in the "Results of Optimisation" section.

### How it opens

With the reason for the map, from the team's own fieldwork: most people they
spoke to did not know the term or confused it with flooding. The next
paragraph ties the map to the start-up: find the hotspots first to "prioritise
and focus on the areas which would be greatly benefitted". The map has a job
before it has a method.

### How methods, data and limits are explained

- Each index gets a one-line plain definition ("NDVI ... is the measure of
  the greenness of an area").
- The failed first attempt is kept in, with its figures: "the results were
  not good, and we shifted our approach".
- Thresholds are printed under each map, and the legend is read aloud in
  words ("The dark green parts are the NDVI masking layer ...").
- Expert input on method is credited on the HP page (two earth-science
  professors suggested SNAP, QGIS and Google Earth Engine).
- The result reaches the business plan: the Entrepreneurship page says the
  bioreactor rollout will "prioritise waterlogging and drought hotspots".

### Voice and tense

First person plural, past tense, conversational ("Basically, this masking was
done to ..."). Short paragraphs.

### Weaknesses

- No validation. The thresholds have no source, the three maps disagree on
  which states are hotspots, and nothing reconciles them or checks them
  against known waterlogged districts.
- No dates. The page does not say which season or year of imagery was used,
  which matters for a seasonal problem.
- Contradiction across pages. The Model page shows national maps; the
  Implementation page plans to "extend our waterlogging hotspot map from one
  state to the rest of the Indian subcontinent".
- Index formulas and band tables are images, so they cannot be searched or
  copied.

### What ReLeaf could take

- Give the map its job in the first paragraph, in business terms: where the
  first reactors go.
- Read the legend in words under each map.
- Keep the failed method, briefly, with the reason it failed.
- Make the Entrepreneurship page quote the GIS result, and make both pages
  agree on its scope.

---

## XJTLU-China 2025

File: `gis-2025-xjtlu-china.md` (Model page; section "MaxEnt (Maximum
Entropy) Model for the Distribution of Ulva prolifera").

Project: a response to green-tide algae blooms. The species distribution
model predicts where blooms could occur.

### Page anatomy

About 1,280 words under five fixed subheadings: Description, Materials and
Method, Results, discussion and analysis (model validation, variable
contribution), Limitations. One variable table, a workflow figure, a ROC
curve, a contribution table.

### How it opens

"To predict the potential distribution of Ulva prolifera under different
environmental conditions and identify high-risk outbreak zones, we developed
a species distribution model based on MaxEnt." Purpose, output and method in
one sentence.

### How methods, data and limits are explained

- Data cleaning is listed step by step (bad coordinates, points on land,
  duplicates), with the reason for spatial thinning (spatial
  autocorrelation) and the final count (272 points).
- Variables are named with their database and version (Bio-ORACLE V3.0), and
  correlated variables were removed first.
- The validation number is given a baseline a lay reader can use: AUC 0.952
  "significantly higher than the random prediction value of 0.5".
- Limitations state the direction of error: ignoring storms and heat waves
  "could lead to an underestimation of actual bloom risks".

### Weaknesses

- Validation is on training data only; no held-out test AUC is reported.
- The results paragraph ends with "it is evident that our project has
  long-term applicability and potential", which the map does not show.
- Software output terms ("regularized training gain is 2.564") are reported
  without saying what they mean for the reader.

### What ReLeaf could take

- Give every validation or agreement number a baseline in the same sentence.
- A fixed five-part structure per map (purpose, data and method, result,
  check, limits) is easy to skim and easy for judges to score.

---

## HUBU-China 2024 (contrast)

File: `gis-2024-hubu-china.md` (Model page, section "1 Distribution of
Spodoptera litura").

A MaxEnt model of a crop pest in China, about 860 words. It names its data
(GBIF, WorldClim) and reports an AUC of 0.98. Two faults make it a useful
warning. A long passage is pasted from the software's own report ("These are
1-sided p-values for the null hypothesis ..."), so the explanation of
thresholds is the tool's own boilerplate. And the conclusion says the pest
"has an obvious tendency to spread to the surrounding areas", which a single
suitability map cannot show. The map is not tied to any decision in the
project.

---

## Synthesis

1. A GIS page earns its place by changing a decision. IISER-Pune-India's map
   decides where the start-up sells first; Marburg's decides an argument
   (diversify into dandelion) but not an experiment. The page should say
   which decision it informs in the first paragraph and close by saying what
   was decided.
2. The non-specialist reader needs four things for each map: what the colours
   mean, where the numbers came from, how sure the team is, and which way the
   map is wrong. Marburg supplies all four; the weaker cases supply one or two.
3. Uncertainty is shown best as a second map or a number with a baseline
   (Marburg's model agreement, XJTLU's AUC against 0.5).
4. Field knowledge belongs in the model. Marburg's TKS thresholds widened
   after farmers said the crop was adaptable; that is the most
   "integrated" moment in any of these pages.
5. Reproducibility is the common gap. No case links code and processed data.
   ReLeaf's "Reproducing this" section can beat every precedent if it
   actually links them.

## Rewrite checklist

1. The first paragraph names the decision the maps inform and who makes it.
   Reason: IISER-Pune-India's map has a job before it has a method; Marburg's
   does not, and its conclusion drifts to "policymakers".
2. The last section says what ReLeaf decided because of the maps (rollout
   order, partner, site), with a link to the page where that decision lives.
   Reason: the Best Model question asks whether the model helped design
   something; none of the precedents answers it on the page.
3. Every dataset has publisher, resolution, period and edition in one table,
   and the text says why it was chosen over a named alternative. Test: no
   "edition" or "year" cell is blank. Reason: Marburg's CHELSA paragraph.
4. Every threshold is in a table with its source. Test: no threshold appears
   only in prose or only in an image. Reason: IISER-Pune-India's thresholds
   are unsourced.
5. Units are translated once for a lay reader (degrees or arc-seconds to km,
   index values to what they mean on the ground). Reason: Marburg's "about 25
   to 100 km at the equator".
6. Each map states the direction of its error and the reason, before the
   results. Reason: Marburg and XJTLU both do this; it disarms the obvious
   judge question.
7. Every forecast map has an uncertainty companion, or its key number has a
   baseline in the same sentence. Reason: Marburg's agreement map; XJTLU's AUC
   against 0.5.
8. Each legend is read in words in the caption or the paragraph below.
   Reason: IISER-Pune-India's "The dark green parts are ...".
9. Class names, colours and units are identical across text, legends and
   tables. Test: search for each class name. Reason: Marburg uses three naming
   schemes for one set of classes.
10. Areas and distances are computed in a projected coordinate system or on
    the ellipsoid, and the page says which. Reason: Marburg's km² step;
    ReLeaf already uses EPSG:3826 and should keep the sentence.
11. Any interview that changed a layer, threshold or weight is named on the
    GIS page. Reason: Marburg's farmer interviews widened the TKS niche; that
    is the IHP link judges look for.
12. No pasted software output. Every statistic is followed by what it means
    for ReLeaf. Reason: HUBU-China.
13. No unverifiable firsts or superlatives. Reason: Marburg's "first iGEM
    team" claim is contradicted by IISER-Pune-India 2022.
14. Code and processed layers are linked from "Reproducing this", from the
    team's iGEM GitLab. Reason: no precedent does it, and Best Software
    requires the code there under an OSI licence.
15. The Entrepreneurship and Sustainability pages quote the GIS result with
    the same numbers and scope. Reason: IISER-Pune-India's Implementation
    page contradicts its Model page.

## Note for the mock (from ReLeaf's local wiki checkout)

The local `wiki/` checkout may be stale; verify against the live page. The
Method section still carries a "to document" marker: the weighting of the
three components of the climate volatility index and the climate surface they
come from are not written up. Rule 4 above applies. The opening also
describes ReLeaf as releasing engineered *B. subtilis* into soil, which
conflicts with the Laws page (see `laws.md`).
