# Engagement writing coach

Research base for a mock of ReLeaf's seven Engagement pages, annotated in the
margin with writing feedback and set beside how past iGEM special-prize winners
wrote the same kind of section. Audience: ReLeaf's Human Practices students,
who will rewrite their own pages from it.

Status (8 Oct 2026): built. `docs/` is the site (GitHub Pages from /docs):
the seven pages from releaf-wiki origin/main 4afd3b8 with 317 margin notes,
135 smaller fixes and 32 cross-page contradictions.

Rebuild after the wiki changes: refresh `releaf-text/` from the new pages,
re-run the reviews whose anchors broke, then
`python3 tools/build_site.py <releaf-wiki checkout at origin/main>`.

## Cases

Winners of the 2023, 2024 and 2025 special prizes, undergrad (UG) and overgrad
(OG). Lists taken from competition.igem.org/results/<year>?tab=special-prizes.

| Prize | 2025 UG | 2025 OG | 2024 UG | 2024 OG | 2023 UG | 2023 OG |
|---|---|---|---|---|---|---|
| Integrated Human Practices | NYU-Abu-Dhabi | WageningenUR | JU-Krakow | Bielefeld-CeBiTec | HUST-China | SDU-Denmark |
| Education | Queens-Canada | Heidelberg | CityU-HongKong | Aachen | IISER-Pune-India | EPFL |
| Entrepreneurship | SUSTech-BIO | UNILausanne, WageningenUR (tie) | Uni-Padua-IT | UToronto | Tec-Chihuahua | Leiden |
| Sustainable Development Impact | EPFL | Aalto-Helsinki | UBC-Vancouver | UZurich | thessaloniki | Heidelberg |

Laws and Regulations, Geospatial Analysis: Marburg 2024 (GIS page, legal and
political HP subpages). Data Physicalization: no prize equivalent; last priority.

## Layout

- `sources/text/` rendered text of each winning page, one file per page,
  named `<prize>-<year>-<track>-<team>.md`. Headings are `#`, list items `-`,
  figure captions `[CAPTION]`, images `[IMG] alt`, folds `[FOLD]`. Marburg
  legal/political come from their own source (`*.src.txt`). Content collapsed
  inside modals may be missing; the visible page text is complete.
- `sources/text/judging-special-prizes.md` iGEM's 2026 prize descriptions and
  ballot questions.
- `sources/pages.txt` file name → URL.
- `research/<prize>.md` casebook per prize; `research/<prize>.excerpts.json`
  the excerpt bank the mock page will draw from.
- `tools/render.sh` headless-Chrome renderer (the 2024–25 wikis are
  client-rendered, so curl returns an empty shell); `tools/totext.py` DOM → text.

## Licence

All iGEM wiki content is CC BY 4.0. Every excerpt carries team, year, track
and source URL; the mock page must show that credit next to each one.

## Excerpt schema (`*.excerpts.json`)

```json
{
  "id": "ihp-2025-og-wur-01",
  "prize": "ihp | education | entrepreneurship | sustainability | laws | gis",
  "team": "WageningenUR", "year": 2025, "track": "OG",
  "url": "https://2025.igem.wiki/wageningenur/human-practices/index.html",
  "section": "the heading the passage sits under, verbatim",
  "function": "page-opening | section-intro | stakeholder-entry | loop-closing | evidence-with-numbers | method | limitation | reflection | transition | conclusion | definition | audience-framing | other",
  "text": "verbatim passage, copied exactly from sources/text",
  "why_it_works": "one or two plain sentences naming the move",
  "teaches": ["feedback categories it models: clarity | structure | concision | consistency | assumed-knowledge | evidence | loop-closing | voice | ..."]
}
```

## ReLeaf pages under review

`releaf-text/<page>.md` is the rendered text of each Engagement page at
origin/main 4afd3b8 (8 Oct 2026, all students' own writing, no `.ai`). One
line = one block element on the page.

## Annotation schema (`annotations/<page>.json`)

```json
{
  "page": "human-practices",
  "summary": {
    "verdict": "2–3 sentences: where the page stands against the winners",
    "strengths": ["3–5 specific things the students did well"],
    "priorities": ["3–5 ordered fixes, biggest payoff first"],
    "ballot": [{"question": "verbatim ballot question", "status": "strong | partial | missing", "where": "ReLeaf section that answers it, or empty", "note": "one sentence"}],
    "skeleton": {"releaf": ["ReLeaf's top-level sections in order"], "winners": ["the shared winner skeleton"], "gap": "one or two sentences"}
  },
  "notes": [{
    "id": "hp-001",
    "type": "praise | restructure | cut | mistake | clarify | suggest",
    "anchor": "exact text from ONE line of releaf-text/<page>.md, 4–30 words, unique in that file",
    "title": "≤ 8 plain words",
    "body": "1–4 sentences to the students, plain English",
    "after": "optional: one way to write it (never invents facts; uses [placeholders])",
    "excerpts": ["0–2 excerpt ids from research/*.excerpts.json"],
    "excerpt_note": "optional: what to look at in the winner passage",
    "ballot": "optional: the ballot question this note serves"
  }]
}
```

Types: **praise** good writing, named precisely; **restructure** sentence or
paragraph order; **cut** words or passages the page does not need;
**mistake** errors, typos, number or name mismatches, contradictions with
other pages; **clarify** unclear writing and knowledge the reader is assumed to
have; **suggest** missing content the criteria ask for.
