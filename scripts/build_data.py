"""Assemble questions + review queue + proposed PYQ-concept links into app/data and app/public/data.

usage: build_data.py <work_dir> <data_dir>
Inputs  : work/prelims_raw.json, work/mains_raw.json, work/mains_raw_fragments.json, data/concepts.json
Outputs : data/questions_prelims.json, questions_mains.json, review_queue.json, question_links.json, coverage.json
All concept<->question links are `proposed` (keyword/label rules, not human reviewed).
"""
import json, os, re, sys, shutil, collections

work, data = sys.argv[1], sys.argv[2]
L = lambda p: json.load(open(p, encoding="utf-8"))
prelims, mains = L(f"{work}/prelims_raw.json"), L(f"{work}/mains_raw.json")
frags = L(f"{work}/mains_raw_fragments.json")
concepts = L(f"{data}/concepts.json")

BENIGN = {"marks-derived-from-word-limit", "ocr-wordlimit-normalised", "closed-by-next-number", "text-from-alt-ocr-psm6", "renumbered-by-order", "number-from-marker-group"}
def serious(flags):
    return [f for f in flags if f.split("(")[0] not in BENIGN]

# ---- review queue -------------------------------------------------------------------------
queue = []
for q in prelims + mains:
    s = serious(q["flags"])
    if s:
        queue.append({"kind": "question-flagged", "id": q["id"], "stage": q["stage"], "year": q["year"], "paper": q["paper"],
                      "source_file": q["source_file"], "source_page": q["source_page"], "issues": s})
for f in frags:
    queue.append({"kind": "unattached-fragment", "id": None, "stage": "Mains", "year": f["year"], "paper": f["paper"],
                  "source_file": f["source_file"], "source_page": f["source_page"], "issues": [f["reason"]], "text": f["text"][:200]})
by = collections.defaultdict(set)
for q in mains:
    by[(q["year"], q["paper"])].add(q["number"])
missing = []
for y in range(2016, 2027):
    for n in (1, 2, 3):
        got = by.get((y, f"GS-{n}"), set())
        for k in range(1, 21):
            if k not in got:
                missing.append({"year": y, "paper": f"GS-{n}", "number": k})
for m in missing:
    queue.append({"kind": "missing-question", "id": None, "stage": "Mains", "year": m["year"], "paper": m["paper"], "source_file": f"UPSC_Mains_{m['year']}_{m['paper'].replace('-', '')}.pdf", "source_page": None, "issues": [f"expected question {m['number']} not found"]})
for y in (2013, 2014, 2015):
    for n in (1, 2, 3, 4):
        queue.append({"kind": "missing-paper", "id": None, "stage": "Mains", "year": y, "paper": f"GS-{n}", "source_file": None, "source_page": None, "issues": ["paper not published on the UPSC previous-question-papers page or its archive; not downloaded"]})

# ---- proposed links to concepts (all subjects) ----------------------------------------------------
SUBJ_OF_LABEL = {"Indian Polity": "polity", "Indian Economy": "economy", "Geography": "geography", "Environment & Ecology": "environment",
                 "Modern History": "history", "Ancient History": "history", "Medieval History": "history", "Art & Culture": "history",
                 "Science & Technology": "scitech"}
# compiler topics inside "Science & Technology" that are really aptitude/reasoning/other: not linked
NOT_SCITECH = {"Quantitative Aptitude", "Logical Reasoning & Puzzles", "Logical Reasoning", "Data Interpretation", "Number systems / Roman numerals",
               "Infrastructure & Industry", "Printing / Colour Technology"}
CURRENT_AFFAIRS = {"International Organisations & Groupings": "ir", "International Relations & Treaties": "ir", "International Conflicts & Security": "ir",
                   "Disasters & Humanitarian Issues": "disaster"}


def subj_of(q):
    lab, top = q["subject_label"], q["topic_label"]
    if lab == "Current Affairs":
        return CURRENT_AFFAIRS.get(top)
    if lab == "Science & Technology" and top in NOT_SCITECH:
        return None
    return SUBJ_OF_LABEL.get(lab)


HOME_PAPERS = {"polity": {"GS-2"}, "economy": {"GS-3"}, "geography": {"GS-1"}, "environment": {"GS-3"}, "history": {"GS-1"},
               "scitech": {"GS-3"}, "society": {"GS-1"}, "governance": {"GS-2"}, "ir": {"GS-2"}, "security": {"GS-3"}, "disaster": {"GS-3"}, "ethics": {"GS-4"}}
# compiler topic label -> concept (fallback only when no keyword matched); concept ids are subject-prefixed
TOPIC_FALLBACK = {
    "Parliament & State Legislatures": "polity-parliament-houses", "Constitutional Framework & Development": "polity-salient-features",
    "Union & State Executive": "polity-president", "Judiciary": "polity-supreme-court", "Constitutional & Statutory Bodies": "polity-statutory-bodies",
    "Local Government & Panchayati Raj": "polity-panchayati-raj", "Social Justice & Vulnerable Sections": "polity-national-commissions-vulnerable-sections",
    "Elections & Electoral Reforms": "polity-rpa-electoral-system", "Federalism & Centre–State Relations": "polity-federalism-centre-state",
    "Fundamental Rights": "polity-fr-overview-art-12-13", "Political Theory & Concepts": "polity-constitution-constitutionalism",
    "Directive Principles Of State Policy": "polity-dpsp", "Public Finance & Finance Commission": "polity-finance-commission-fiscal-federalism",
    "Emergency Provisions": "polity-emergency-provisions", "Fundamental Duties": "polity-fundamental-duties",
    # economy
    "Infrastructure & Industry": "economy-industry-infrastructure", "Human Development, Poverty & Employment Schemes": "economy-human-development-poverty-employment",
    "Agriculture & Rural Development": "economy-agriculture-rural-development", "Banking & Financial Sector": "economy-banking-structure",
    "External Sector & Balance Of Payments": "economy-external-sector-bop", "Fiscal Policy & Budget": "economy-fiscal-policy-budget",
    "Financial Markets & Capital Markets": "economy-financial-markets", "International Trade & WTO": "economy-international-trade-wto",
    "International Institutions & Reports": "economy-international-economic-institutions", "National Income & Economic Growth": "economy-national-income-growth",
    "Monetary Policy & Money Supply": "economy-money-supply-monetary-policy", "Digital Payments & Financial Inclusion": "economy-financial-inclusion-digital-payments",
    "Taxation": "economy-taxation", "Economic Planning & Five-Year Plans": "economy-economic-reforms-1991", "Inflation & Price Indices": "economy-inflation-price-indices",
    # geography
    "Atmosphere & Climatology": "geography-atmosphere-climatology", "Population & Demography": "geography-population-demography-urbanisation",
    "Economic & Mineral Geography": "geography-minerals-industries-location", "World Political Geography & Borders": "geography-world-political-geography-borders",
    "Indian Rivers & Water Resources": "geography-rivers-water-resources", "Indian Physical Geography": "geography-indian-physical-geography",
    "Indian Agriculture & Land Use": "geography-indian-agriculture-land-use", "World Physical Geography": "geography-earth-structure-geomorphology",
    "Transport & Infrastructure Geography": "geography-transport-infrastructure-geography", "Astronomy & Earth–Sun System": "geography-astronomy-earth-sun",
    "Physical Geography & Geomorphology": "geography-earth-structure-geomorphology", "Oceanography": "geography-oceanography",
    "Biogeography & Natural Vegetation": "geography-biogeography-soils-vegetation",
    # environment
    "Protected Areas & Wildlife": "environment-protected-areas-wildlife", "Ecosystems & Ecology Concepts": "environment-ecosystem-ecology-basics",
    "Biodiversity & Conservation": "environment-biodiversity-types-hotspots", "International Environmental Treaties & Summits": "environment-international-treaties-summits",
    "Pollution & Waste Management": "environment-pollution-waste-management", "Environmental Governance & Legislation": "environment-environmental-governance-legislation",
    "Climate Change & Greenhouse Gases": "environment-climate-change-ghg", "Sustainable Agriculture & Forestry": "environment-sustainable-agriculture-forestry",
    "Water & Wetland Conservation": "environment-wetlands-water-conservation", "Renewable Energy & Green Technologies": "environment-renewable-energy-green-tech",
    "Biogeochemical Cycles & Earth Systems": "environment-biogeochemical-cycles",
    # modern history
    "Gandhian Mass Movements (1915-1942)": "history-gandhian-mass-movements", "Constitutional Developments & British Plans (1909-1947)": "history-constitutional-developments-1909-1947",
    "British Administration & Economic Policies": "history-british-administration-economy", "Advent Of Europeans & British Expansion": "history-advent-british-expansion",
    "Early Nationalism & Indian National Congress (1885-1915)": "history-early-nationalism-inc", "Key Personalities & Ideologies": "history-key-personalities-ideologies",
    "Revolutionary & Communist Movements": "history-revolutionary-communist-movements", "Social & Religious Reform Movements": "history-social-religious-reform",
    "Peasant, Tribal & Labour Movements": "history-peasant-tribal-labour-movements", "Transfer Of Power & Partition (1945-1947)": "history-transfer-of-power-partition",
    # ancient / medieval / culture
    "Mauryan Empire": "history-mauryan-gupta-empires", "Gupta Empire": "history-mauryan-gupta-empires", "Post-Mauryan & Foreign Invasions": "history-mauryan-gupta-empires",
    "Vedic Period": "history-indus-vedic-ancient-foundations", "Indus Valley Civilization": "history-indus-vedic-ancient-foundations",
    "Buddhism & Jainism": "history-buddhism-jainism-mahajanapadas", "Mahajanapadas & Early Kingdoms": "history-buddhism-jainism-mahajanapadas",
    "Post-Gupta & Early Medieval Dynasties": "history-early-medieval-regional-kingdoms", "Delhi Sultanate": "history-delhi-sultanate",
    "Mughal Empire": "history-mughal-empire", "Maratha Empire": "history-mughal-empire", "Vijayanagara Empire": "history-bhakti-sufi-vijayanagara",
    "Bhakti Movement": "history-bhakti-sufi-vijayanagara", "Sufism": "history-bhakti-sufi-vijayanagara",
    "Architecture & World Heritage": "history-art-architecture-sculpture", "Painting & Visual Arts": "history-art-architecture-sculpture",
    "Sculpture & Iconography": "history-art-architecture-sculpture", "Music": "history-performing-arts-music-dance",
    "Classical Dance Forms": "history-performing-arts-music-dance", "Theatre & Cinema": "history-performing-arts-music-dance",
    "Literature & Languages": "history-literature-languages-philosophy", "Philosophy & Religion": "history-literature-languages-philosophy",
    "Cultural Institutions & Awards": "history-heritage-institutions-crafts", "Festivals, Crafts & Folk Traditions": "history-heritage-institutions-crafts",
    # science & technology
    "Physics": "scitech-physics-basics", "Chemistry": "scitech-chemistry-basics", "Chemistry – Radioactivity": "scitech-nuclear-energy",
    "Biology": "scitech-biology-basics", "Health & Diseases": "scitech-health-diseases", "Biotechnology & Genetics": "scitech-biotechnology-genetics",
    "Space Technology & Astronomy": "scitech-space-technology", "Defence Technology": "scitech-defence-technology",
    "Computer & Information Technology": "scitech-information-technology-cyber", "Materials & Engineering": "scitech-materials-nanotechnology",
    "Science & Technology Institutions": "scitech-science-institutions-achievements", "Science & Technology History": "scitech-science-institutions-achievements",
    # current affairs mapped to a subject
    "International Organisations & Groupings": "ir-global-groupings-agreements", "International Relations & Treaties": "ir-global-conflicts-treaties",
    "International Conflicts & Security": "ir-global-conflicts-treaties", "Disasters & Humanitarian Issues": "disaster-disaster-management-framework",
}
concept_ids = {c["id"] for c in concepts}
assert all(v in concept_ids for v in TOPIC_FALLBACK.values()), [v for v in TOPIC_FALLBACK.values() if v not in concept_ids]
by_subj = collections.defaultdict(list)
for c in concepts:
    by_subj[c["subject"]].append(c)
GENERIC = {r"salient features", r"Parliament", r"Supreme Court", r"sovereign", r"secular", r"federal", r"Prime Minister", r"Cabinet\b", r"Governor", r"\bSpeaker\b",
           r"High Court", r"tribunal", r"village", r"minorit", r"reservation", r"Emergency", r"Budget", r"Lok Sabha", r"Rajya Sabha", r"Panchayat",
           r"socialist", r"\bPresident\b.*(election|impeach|ordinance|pardon|veto|assent)", r"regulator", r"discriminat", r"delimitation", r"civil society",
           r"coalition", r"mediation", r"arbitration", r"mayor", r"\bwrit", r"Municipal", r"Amendment Act", r"contempt", r"privilege", r"\bPAC\b", r"mandamus", r"prohibition",
           r"\bbudget", r"export", r"infrastructure", r"railway", r"\bport", r"Gandhi", r"river", r"\bsoil", r"flood", r"drought", r"cyclone", r"census", r"migration",
           r"employment", r"poverty", r"agricultur", r"farmer", r"subsid", r"plastic", r"solar", r"\bbond", r"rupee", r"inflation", r"coal", r"Ghats", r"Himalaya", r"biodiversity",
           r"climate change", r"pollut", r"peasant", r"Moderate", r"Extremist", r"revolutionar", r"famine", r"1857", r"1935", r"estuar", r"coral", r"mangrove", r"tide", r"\btide",
           r"conflict|war\b", r"treaty", r"\bscheme", r"\bwomen", r"\bgender", r"\beducation", r"\bdisease", r"terroris", r"extremis", r"\bcyber", r"festival", r"foreign policy",
           r"transparency", r"accountability", r"stakeholder", r"\bscientist", r"\bsatellite", r"\bmissile", r"\bcell\b", r"\bhazard", r"\bdisaster", r"\bstupa|vihara", r"urbani[sz]ation", r"\bmarriage|family", r"\bethic", r"moral", r"\bvalues?\b", r"civil servant", r"public administration", r"stakeholder"}
pats = {sid: [(c["id"], [re.compile(k, re.I) for k in c["keywords"]], c["keywords"]) for c in cs] for sid, cs in by_subj.items()}
links, unclassified = [], collections.defaultdict(list)
MAXC = 3


def match(text, subj, min_score=0.4):
    """[(concept_id, matched_keywords, score)] within one subject. Generic keywords score 0.4, specific 1.0."""
    hits = []
    for cid, rx, raw in pats[subj]:
        m = [(raw[i], 0.4 if raw[i] in GENERIC else 1.0) for i, r in enumerate(rx) if r.search(text)]
        score = sum(w for _, w in m)
        if score >= min_score:
            hits.append((cid, [k for k, _ in m], score))
    hits.sort(key=lambda h: -h[2])
    return hits[:MAXC]


for q in prelims:
    subj = subj_of(q)
    if not subj:
        continue  # aptitude/reasoning, sports, awards and other Current Affairs topics: no concept subject
    stem = q["text"]; full = stem + " " + " ".join(o["text"] for o in q["options"])
    hits = match(stem, subj) or match(full, subj)  # stem first; options only if the stem has no hit
    if hits:
        for cid, kws, sc in hits:
            links.append({"question_id": q["id"], "concept_id": cid, "relation": "tests", "status": "proposed",
                          "evidence": "keyword match: " + "; ".join(kws[:3]) + f" (compiler topic: {q['topic_label'] or 'n/a'})"})
    elif q["topic_label"] in TOPIC_FALLBACK and TOPIC_FALLBACK[q["topic_label"]].split("-")[0] == subj:
        links.append({"question_id": q["id"], "concept_id": TOPIC_FALLBACK[q["topic_label"]], "relation": "tests", "status": "proposed",
                      "evidence": f"fallback from compiler topic label: {q['topic_label']} (no keyword match)"})
    else:
        unclassified[subj].append(q["id"])

for q in mains:
    best = []
    for subj in by_subj:
        home = q["paper"] in HOME_PAPERS[subj]
        for cid, kws, sc in match(q["text"], subj, 0.4 if home else 0.8):
            best.append((sc + (0.5 if home else 0), cid, kws, home))
    best.sort(key=lambda h: -h[0])
    for sc, cid, kws, home in best[:MAXC]:
        links.append({"question_id": q["id"], "concept_id": cid, "relation": "tests", "status": "proposed",
                      "evidence": "keyword match: " + "; ".join(kws[:3]) + ("" if home else f" (outside the subject's home paper: {q['paper']})")})
    if not best:
        unclassified["mains-" + q["paper"]].append(q["id"])

# ---- write -------------------------------------------------------------------------------------
out = {"questions_prelims": prelims, "questions_mains": mains, "review_queue": queue, "question_links": links}
for k, v in out.items():
    json.dump(v, open(f"{data}/{k}.json", "w"), ensure_ascii=False)
json.dump(unclassified, open(f"{data}/unclassified_questions.json", "w"))
print("links", len(links), "| unclassified", {k: len(v) for k, v in unclassified.items()}, "| queue", len(queue), collections.Counter(x["kind"] for x in queue))
