#!/usr/bin/env python3
"""Build the writing-coach site into docs/.

    python3 tools/build_site.py <path to a releaf-wiki checkout at origin/main>

Copies the seven Engagement pages and the assets they use from the wiki
checkout unchanged, then adds the coach layer: coach.css in <head>, and before
</body> a data file (annotations + the winner excerpts they cite) and coach.js.
Pages without annotations/<page>.json are left out. Writes docs/index.html.
"""
import html, json, re, shutil, sys, time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"

PAGES = [  # slug, title, prize the page is judged against, short label
    ("human-practices", "Integrated Human Practices", "Best Integrated Human Practices", "IHP"),
    ("education", "Education", "Best Education", "Education"),
    ("entrepreneurship", "Entrepreneurship", "Best Entrepreneurship", "Entrepreneurship"),
    ("sustainability", "Sustainability", "Best Sustainable Development Impact", "Sustainability"),
    ("laws-and-regulations", "Laws and Regulations", "Integrated Human Practices, Safety and Security", "Laws"),
    ("geospatial-analysis", "Geospatial Analysis", "Integrated Human Practices, Sustainable Development", "GIS"),
    ("data-physicalization", "Data Physicalization", "Education, Integrated Human Practices", "Data physicalization"),
]
PRIZE_SHORT = {"ihp": "IHP", "education": "Education", "entrepreneurship": "Entrepreneurship",
               "sustainability": "Sustainability", "laws": "Law page", "gis": "GIS page",
               "data-physicalization": "Data physicalization"}
IMG_DIRS = ["human-practices", "education", "entrepreneurship", "sustainability",
            "laws-and-regulations", "geospatial", "data-physicalization"]
SKIP_IN_PAGE = {"education": ["materials"]}  # 33 MB of lesson PDFs; links go to the live wiki
LIVE = "https://2026.igem.wiki/gems-taiwan/"
VER = time.strftime("%m%d%H%M%S")
TYPES = [("praise", "Praise"), ("restructure", "Restructure"), ("cut", "Cut"),
         ("clarify", "Clarify"), ("mistake", "Mistake"), ("suggest", "Add")]


def excerpts():
    bank = {}
    for f in sorted((ROOT / "research").glob("*.excerpts.json")):
        for x in json.loads(f.read_text()):
            x["prizeName"] = PRIZE_SHORT.get(x.get("prize"), x.get("prize", ""))
            bank[x["id"]] = x
    return bank


def main(src):
    src = Path(src)
    bank = excerpts()
    if DOCS.exists():
        shutil.rmtree(DOCS)
    (DOCS / "assets").mkdir(parents=True)
    for d in ["css", "js", "data", "fonts", "vendor"]:
        shutil.copytree(src / "assets" / d, DOCS / "assets" / d)
    (DOCS / "assets/img").mkdir()
    for f in (src / "assets/img").iterdir():
        if f.is_file():
            shutil.copy2(f, DOCS / "assets/img" / f.name)
    for d in IMG_DIRS:
        if (src / "assets/img" / d).exists():
            shutil.copytree(src / "assets/img" / d, DOCS / "assets/img" / d)
    for pf in re.findall(r"assets/img/([a-z0-9_-]+/[^\"')\s]+)", " ".join(
            (src / p[0] / "index.html").read_text() for p in PAGES)):
        s, t = src / "assets/img" / pf, DOCS / "assets/img" / pf
        if s.is_file() and not t.exists():
            t.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(s, t)
    shutil.copytree(ROOT / "site-src/coach", DOCS / "coach")
    (DOCS / "coach/data").mkdir(exist_ok=True)

    built = []
    for slug, title, prize, short in PAGES:
        ann = ROOT / "annotations" / f"{slug}.json"
        if not ann.exists():
            continue
        a = json.loads(ann.read_text())
        skip = SKIP_IN_PAGE.get(slug, [])
        shutil.copytree(src / slug, DOCS / slug, ignore=lambda d, names: [n for n in names if n in skip])
        used = {i for n in a["notes"] for i in n.get("excerpts", [])}
        data = {"page": slug, "title": title, "prizeName": prize, "summary": a.get("summary"),
                "notes": a["notes"], "excerpts": {i: bank[i] for i in sorted(used) if i in bank}}
        missing = sorted(used - set(bank))
        if missing:
            print(f"  {slug}: excerpt ids not in any bank: {missing}")
        (DOCS / "coach/data" / f"{slug}.js").write_text(
            "window.COACH = " + json.dumps(data, ensure_ascii=False) + ";\n")
        p = DOCS / slug / "index.html"
        h = p.read_text()
        h = h.replace("</head>", f'  <link rel="stylesheet" href="../coach/coach.css?v={VER}" />\n</head>', 1)
        h = h.replace("</body>", f'  <script src="../coach/data/{slug}.js?v={VER}"></script>\n'
                                 f'  <script src="../coach/coach.js?v={VER}"></script>\n</body>', 1)
        for d in skip:
            h = h.replace(f'href="{d}/', f'href="{LIVE}{slug}/{d}/')
        p.write_text(h)
        counts = {t: sum(1 for n in a["notes"] if n["type"] == t) for t, _ in TYPES}
        built.append((slug, title, prize, short, a, counts))
        print(f"  {slug}: {len(a['notes'])} notes, {len(data['excerpts'])} winner passages")

    (DOCS / "index.html").write_text(landing(built, bank))
    (DOCS / ".nojekyll").write_text("")
    print("built", len(built), "pages into", DOCS)


def esc(s):
    return html.escape(s or "", quote=True)


def landing(built, bank):
    teams = sorted({(x["team"], x["year"], x["track"], x["url"].split("/")[2] + "/" + x["url"].split("/")[3])
                    for x in bank.values()}, key=lambda t: (-t[1], t[0]))
    win = {(x["team"], x["year"]) for x in bank.values() if x.get("prize") in ("ihp", "education", "entrepreneurship", "sustainability")}
    prec_set = sorted({(x["team"], x["year"]) for x in bank.values() if x.get("prize") in ("laws", "gis")} - win, key=lambda t: (-t[1], t[0]))
    prec = ", ".join(f"{t} {y}" for t, y in prec_set)
    cards = []
    for slug, title, prize, short, a, counts in built:
        chips = "".join(f'<li class="cx-{t}">{name} {counts[t]}</li>' for t, name in TYPES if counts[t])
        pri = a.get("summary", {}).get("priorities", [])[:1]
        cards.append(f'''
      <a class="lp-card" href="{slug}/">
        <span class="lp-card__prize">{esc(prize)}</span>
        <h3>{esc(title)}</h3>
        <p>{esc(a.get("summary", {}).get("verdict", ""))}</p>
        {f'<p class="lp-card__first"><b>Fix first</b>{esc(pri[0])}</p>' if pri else ""}
        <ul class="cx-sum__counts">{chips}</ul>
      </a>''')
    names = {"human-practices": ["Human Practices", "IHP"], "education": ["Education"],
             "entrepreneurship": ["Entrepreneurship"], "sustainability": ["Sustainability"],
             "laws-and-regulations": ["Laws and Regulations", "Laws page"], "geospatial-analysis": ["Geospatial", "GIS page"],
             "data-physicalization": ["Data Physicalization"]}
    wiki_pages = ["Results", "Plants", "Protein Design", "Description", "Engineering", "Biomanufacturing", "Development", "Safety"]
    cross = []
    for slug, title, prize, short, a, counts in built:
        other = re.compile(r"\b(" + "|".join(re.escape(x) for k, v in names.items() if k != slug for x in v) +
                           "|" + "|".join(wiki_pages) + r")\b")
        for n in a["notes"]:
            if n["type"] == "mistake" and other.search(n["body"]):
                cross.append(f'<li><a href="{slug}/#cx-{n["id"]}"><span>{esc(title)}</span><b>{esc(n["title"])}</b>{esc(n["body"])}</a></li>')
    cross_html = (f'<section class="lp-cross"><h2>Facts that disagree between pages</h2>'
                  f'<p>A judge who reads two pages will notice these. Agree on one version as a team, then fix every page that carries the other.</p>'
                  f'<ul>{"".join(cross)}</ul></section>') if cross else ""
    waiting = [p for p in PAGES if p[0] not in {b[0] for b in built}]
    wait_html = "".join(f'<li>{esc(p[1])}</li>' for p in waiting)
    credit = "".join(f'<li><a href="https://{t[3]}/">{esc(t[0])} {t[1]}</a> <span>{"Overgrad" if t[2]=="OG" else "Undergrad" if t[2]=="UG" else esc(t[2])}</span></li>' for t in teams)
    legend = "".join(f'<li class="cx-{t}"><b>{name}</b>{d}</li>' for (t, name), d in zip(TYPES, [
        "writing that already works, and why a judge rewards it",
        "the same facts in a clearer order",
        "words the page does not need",
        "jargon, missing context, or knowledge the reader is assumed to have",
        "errors, and facts that disagree with another page",
        "what the judges' ballot asks for that the page does not yet give"]))
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Engagement Writing Coach | ReLeaf</title>
  <link rel="icon" href="assets/img/logo.png" />
  <link rel="stylesheet" href="assets/css/tokens.css" />
  <link rel="stylesheet" href="coach/coach.css?v={VER}" />
  <link rel="stylesheet" href="coach/landing.css?v={VER}" />
</head>
<body class="lp">
  <header class="lp-head">
    <img src="assets/img/logo.png" alt="ReLeaf logo" width="44" height="44" />
    <p class="lp-eyebrow">ReLeaf · GEMS Taiwan · iGEM 2026</p>
    <h1>Engagement writing coach</h1>
    <p class="lp-lede">Our seven Engagement pages as they stand on the wiki, with notes in the margin. Each note sits beside a passage from a team that won the matching iGEM special prize in 2023, 2024 or 2025, so you can see how they wrote the same part.</p>
  </header>
  <main class="lp-main">
    <section class="lp-grid">{"".join(cards)}
    </section>
    {f'<section class="lp-wait"><h2>Still in review</h2><ul>{wait_html}</ul></section>' if waiting else ''}
    {cross_html}
    <section class="lp-legend">
      <h2>The six kinds of note</h2>
      <ul>{legend}</ul>
    </section>
    <section class="lp-credit">
      <h2>Teams quoted</h2>
      <p>Undergrad and overgrad winners of Best Integrated Human Practices, Best Education, Best Entrepreneurship and Best Sustainable Development Impact, 2023 to 2025. No prize covers law or GIS pages, so those notes quote the closest precedents: {esc(prec)}. All iGEM wiki text is licensed CC BY 4.0; every passage links to its source page.</p>
      <ul>{credit}</ul>
    </section>
  </main>
</body>
</html>
'''


if __name__ == "__main__":
    main(sys.argv[1])
