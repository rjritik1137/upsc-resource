"""Authoring source for the Indian Polity pilot (concepts, resources, concept links).

Emits app/data/{concepts,resources,concept_links,subjects}.json.
Everything authored here is `review_status: "draft-unreviewed"` — it was written
by the AI assistant from general knowledge, NOT checked line-by-line against a
textbook. Book chapter numbers are deliberately NOT given (not verifiable in
this environment); Constitution article ranges are given as locators but are
marked unverified. PYQ links are NOT authored here (see link_pyqs.py).

usage: author_polity.py <out_data_dir>
"""
import json, os, sys

SUBJECT = "polity"
CHECKED = "2026-11-13"

# ----------------------------------------------------------------- resources
# access: free-legal-download | free-online | purchase | user-provided
RES = [
    dict(id="R-CONST", title="The Constitution of India (official text)", author="Legislative Department, Ministry of Law and Justice, Govt. of India",
         type="official-primary", url="https://legislative.gov.in/constitution-of-india/", access="free-online", url_status="http-200"),
    dict(id="R-INDIACODE", title="India Code (central Acts repository)", author="Legislative Department, Govt. of India",
         type="official-primary", url="https://www.indiacode.nic.in/", access="free-online", url_status="http-200"),
    dict(id="R-LAXMI", title="Indian Polity", author="M. Laxmikanth", publisher="McGraw Hill", edition="not verified",
         type="standard-book", url=None, access="purchase", url_status="n/a"),
    dict(id="R-NCERT", title="NCERT Political Science textbooks (Class XI 'Indian Constitution at Work'; Class XII 'Politics in India since Independence')",
         author="NCERT", type="official-textbook", url="https://ncert.nic.in/", access="free-legal-download", url_status="http-200 (home page only; book/chapter links not verified)"),
    dict(id="R-PRS", title="PRS Legislative Research (bill summaries, Parliament and state-legislature explainers)", author="PRS Legislative Research",
         type="credible-non-government", url="https://prsindia.org/", access="free-online", url_status="http-200"),
    dict(id="R-SANSAD", title="Sansad (Parliament of India: Lok Sabha / Rajya Sabha)", author="Parliament of India",
         type="official-primary", url="https://sansad.in/", access="free-online", url_status="http-200"),
    dict(id="R-ECI", title="Election Commission of India", author="ECI", type="official-primary", url="https://eci.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-SCI", title="Supreme Court of India", author="Supreme Court of India", type="official-primary", url="https://www.sci.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-CAG", title="Comptroller and Auditor General of India", author="CAG", type="official-primary", url="https://cag.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-UPSC", title="Union Public Service Commission", author="UPSC", type="official-primary", url="https://www.upsc.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-FINCOM", title="Finance Commission of India", author="Finance Commission", type="official-primary", url="https://fincomindia.nic.in/", access="free-online", url_status="http-200"),
    dict(id="R-ARC", title="Administrative Reforms Commission reports (2nd ARC)", author="DARPG, Govt. of India", type="official-primary", url="https://darpg.gov.in/arc-reports", access="free-online", url_status="http-200"),
    dict(id="R-NHRC", title="National Human Rights Commission", author="NHRC", type="official-primary", url="https://nhrc.nic.in/", access="free-online", url_status="http-200"),
    dict(id="R-CIC", title="Central Information Commission", author="CIC", type="official-primary", url="https://cic.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-LOKPAL", title="Lokpal of India", author="Lokpal", type="official-primary", url="https://lokpal.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-PANCHAYAT", title="Ministry of Panchayati Raj", author="Govt. of India", type="official-primary", url="https://panchayat.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-CONSTNET", title="Constitution of India net (annotated Constituent Assembly Debates, amendments)", author="constitutionofindia.net", type="credible-non-government", url="https://www.constitutionofindia.net/", access="free-online", url_status="http-200"),
    dict(id="R-UPSC-SYL", title="UPSC Civil Services Examination syllabus (supplied syllabus.pdf)", author="UPSC", type="official-primary", url=None, access="user-provided", url_status="n/a"),
]
for r in RES:
    r["last_checked"] = CHECKED
    r.setdefault("publisher", None); r.setdefault("edition", None)

# ------------------------------------------------------------------ groups
GROUPS = [
    ("A", "Foundations of the Constitution"), ("B", "Rights, Duties and Directives"), ("C", "Amendment and Basic Structure"),
    ("D", "Union Executive"), ("E", "Parliament"), ("F", "State Government"), ("G", "Federalism and Emergency"),
    ("H", "Judiciary and Dispute Redressal"), ("I", "Local Government"), ("J", "Constitutional and Statutory Bodies"),
    ("K", "Elections and Political Parties"),
]

CONST = "R-CONST"
# concept tuple helper -------------------------------------------------------
CONCEPTS = []


def C(cid, grp, title, definition, subs, dist, prereq, found, mains, hrs, syl, kw, res, cross=(), related=(), const_loc=None, prelims_only=False):
    CONCEPTS.append(dict(
        id=f"polity-{cid}", subject=SUBJECT, group=grp, title=title, definition=definition,
        subconcepts=subs, distinctions=dist, prerequisites=[f"polity-{p}" for p in prereq],
        foundation_focus=found, mains_focus=mains, effort_hours_editorial=hrs,
        syllabus_ids=list(syl), keywords=list(kw), resource_ids=list(res) + [CONST],
        constitution_locator=const_loc, cross_subject=list(cross), related=[f"polity-{r}" for r in related],
        review_status="draft-unreviewed", confidence="medium",
    ))


# ===== A. Foundations ========================================================
C("constitution-constitutionalism", "A", "Constitution and constitutionalism",
  "A constitution is the fundamental law that sets up the organs of the State, distributes power among them and limits it; constitutionalism is the idea that governmental power must be exercised within those limits.",
  ["Written vs unwritten constitution", "Rigid vs flexible", "Federal vs unitary", "Constitutional supremacy vs parliamentary sovereignty", "Rule of law", "Limited government", "Separation of powers", "Checks and balances"],
  ["Constitution vs constitutionalism", "Constitutional supremacy (India) vs parliamentary sovereignty (UK)"],
  [], "Be able to define a constitution, list its functions and say where India sits on each classification axis.",
  "Be able to argue why a written, mostly rigid-flexible hybrid constitution suits a diverse democracy, and the limits of constitutional supremacy.", 3,
  ["S-GS2-01", "S-P1-04"], [r"constitutionalism", r"rule of law", r"supremacy", r"separation of powers"], ["R-LAXMI", "R-NCERT"], related=["salient-features", "separation-of-powers"])

C("historical-underpinnings", "A", "Historical underpinnings: from the Regulating Act to the Government of India Act, 1935",
  "The sequence of British-era enactments and reforms whose institutions, ideas and structures were carried into the Constitution of India.",
  ["Regulating Act 1773", "Pitt's India Act 1784", "Charter Acts of 1813, 1833, 1853", "Government of India Act 1858", "Indian Councils Acts 1861, 1892, 1909", "Government of India Act 1919 (dyarchy)", "Government of India Act 1935 (provincial autonomy, federal scheme)", "Indian Independence Act 1947"],
  ["Dyarchy (1919, provinces) vs provincial autonomy (1935)", "Communal electorates (1909) vs separate electorates for Depressed Classes (1932)"],
  ["constitution-constitutionalism"], "Learn the Acts as a timeline and what each added (e.g. codification, legislative council, dyarchy).",
  "Trace which features of the 1935 Act reappear in the Constitution (federal scheme, emergency powers, Public Service Commissions, Governor's office).", 4,
  ["S-GS2-01", "S-GS1-02"], [r"Regulating Act", r"Charter Act", r"Government of India Act", r"Indian Councils Act", r"1935", r"dyarchy", r"Morley", r"Montagu", r"Simon Commission", r"Cabinet Mission", r"Independence Act"],
  ["R-LAXMI", "R-NCERT", "R-CONSTNET"], cross=["xs-history-constitutional-developments"], related=["constituent-assembly"])

C("constituent-assembly", "A", "Constituent Assembly and making of the Constitution",
  "The body formed under the Cabinet Mission Plan (1946) that framed the Constitution, adopted on 26 November 1949 and brought into force on 26 January 1950.",
  ["Composition and election of the Assembly", "Objectives Resolution (Dec 1946)", "Role of the Drafting Committee and its chairman", "Major committees", "Sessions and time taken", "Adoption vs commencement of different provisions", "Debates on key issues (federalism, language, minority rights)"],
  ["Adoption date (26 Nov 1949) vs commencement (26 Jan 1950)", "Constituent power vs legislative power"],
  ["historical-underpinnings"], "Dates, key committees, Objectives Resolution and the Drafting Committee.",
  "Link Assembly debates to design choices (strong Centre, language provisions, minority safeguards).", 3,
  ["S-GS2-01", "S-GS1-02"], [r"Constituent Assembly", r"Drafting Committee", r"Objectives Resolution", r"Ambedkar", r"B\.?\s*N\.?\s*Rau", r"Cabinet Mission", r"framing of the Constitution", r"Constitution.{0,30}(adopted|came into force)"],
  ["R-LAXMI", "R-NCERT", "R-CONSTNET"], related=["preamble", "salient-features"])

C("preamble", "A", "Preamble",
  "The introductory statement of the Constitution that declares its source (We, the People), the nature of the State and the objectives it secures.",
  ["Source of authority", "Sovereign, Socialist, Secular, Democratic, Republic", "Justice, Liberty, Equality, Fraternity", "Amendment by the 42nd Amendment Act, 1976", "Berubari Union case and Kesavananda Bharati on whether it is part of the Constitution"],
  ["Preamble as part of the Constitution vs enforceable source of power", "Republic vs monarchy; secularism (Indian model) vs strict separation"],
  ["constituent-assembly"], "Word-by-word meaning, what the 42nd Amendment changed, judicial status.",
  "Be able to use Preamble values (justice, liberty, equality, fraternity) as the frame for any governance answer.", 2,
  ["S-GS2-01", "S-P1-04"], [r"Preamble", r"secular", r"socialist", r"fraternity"], ["R-LAXMI", "R-NCERT"], related=["basic-structure-doctrine"], const_loc="Preamble")

C("salient-features", "A", "Salient features and comparison with other constitutions",
  "The distinctive design choices of the Indian Constitution, many drawn from other constitutions and adapted to Indian conditions.",
  ["Lengthiest written constitution", "Parliamentary form of government", "Federal system with unitary bias", "Fundamental Rights and DPSP", "Independent integrated judiciary", "Single citizenship, universal adult franchise", "Emergency provisions", "Features borrowed from the UK, US, Ireland, Canada, Australia, Weimar Germany, USSR, France, South Africa, Japan"],
  ["India vs US (federalism, judiciary, Executive)", "India vs UK (written vs unwritten, sovereignty)", "Quasi-federal / federal with unitary bias"],
  ["constitution-constitutionalism", "constituent-assembly"], "List the features and their sources accurately (high Prelims match-the-following value).",
  "Compare India with one or two constitutions on a single feature and defend the Indian choice.", 4,
  ["S-GS2-01", "S-GS2-04", "S-P1-04"], [r"borrowed", r"features? of the Constitution", r"salient features", r"quasi-?federal", r"comparison.*constitution", r"Constitution of (the )?(USA|United States|UK|Canada|Australia|Ireland)", r"similarit"],
  ["R-LAXMI", "R-NCERT"], related=["preamble", "federalism-centre-state"])

C("union-territory-citizenship", "A", "Union and its territory; citizenship",
  "Part I governs the Union and its territory (admission, formation, alteration of states); Part II governs who is a citizen and how citizenship is acquired and lost.",
  ["Articles 1–4 and Parliament's power to reorganise states", "Reorganisation of states (States Reorganisation Act 1956; later states)", "Citizenship at commencement (Arts 5–9)", "Citizenship Act 1955: birth, descent, registration, naturalisation, incorporation of territory", "Loss: renunciation, termination, deprivation", "Overseas Citizen of India", "Citizenship (Amendment) Act 2019"],
  ["Citizen vs alien", "Citizenship vs domicile", "Art 3 (ordinary law) vs Art 368 (amendment)"],
  ["constituent-assembly"], "Memorise the modes of acquiring/losing citizenship and the procedure under Art 3.",
  "Be able to discuss citizenship law debates (e.g. CAA 2019) and state reorganisation as a federal question.", 3,
  ["S-GS2-01", "S-P1-04"], [r"citizenship", r"Overseas Citizen", r"State(s)? Reorganisation", r"creation of (a )?new State", r"Article 3\b", r"formation of new States"], ["R-LAXMI", "R-NCERT", "R-INDIACODE"], related=["federalism-centre-state"], const_loc="Arts 1–11 (Parts I–II)")

# ===== B. Rights, duties, directives ========================================
C("fr-overview-art-12-13", "B", "Fundamental Rights: definition of State and judicial review (Arts 12–13)",
  "Articles 12–13 define 'State' for Part III and make laws inconsistent with Fundamental Rights void, creating the basis for judicial review of legislation.",
  ["Definition of State under Art 12", "'Other authorities' and 'instrumentality of the State'", "'Law' under Art 13", "Pre- and post-Constitution laws", "Doctrine of eclipse", "Doctrine of severability", "Doctrine of waiver", "Art 13(4) and constitutional amendments"],
  ["Doctrine of eclipse vs severability", "Void ab initio vs void on inconsistency"],
  ["preamble"], "Understand who counts as 'State' and why it matters for enforcing rights.",
  "Explain how Art 13 anchors judicial review and its interaction with Art 368.", 3,
  ["S-GS2-01", "S-P1-04"], [r"Article 12\b", r"Article 13\b", r"definition of .?State", r"doctrine of (eclipse|severability|waiver)", r"instrumentality", r"Fundamental Rights\b.*(State|law)"], ["R-LAXMI", "R-NCERT"], const_loc="Arts 12–13")

C("fr-equality", "B", "Right to Equality (Arts 14–18)",
  "Guarantees equality before law and equal protection, prohibits discrimination, ensures equality of opportunity in public employment and abolishes untouchability and titles.",
  ["Art 14: equality before law, equal protection, reasonable classification", "Art 15: non-discrimination; special provisions (15(3), 15(4), 15(5), 15(6))", "Art 16: equality in public employment; reservations; Indra Sawhney (creamy layer, 50% rule)", "Art 17: abolition of untouchability", "Art 18: abolition of titles", "Rule against arbitrariness"],
  ["Equality before law vs equal protection of laws", "Formal vs substantive equality", "Art 15 (discrimination) vs Art 16 (employment)"],
  ["fr-overview-art-12-13"], "Know each Article's text-level content, especially clauses added by amendments.",
  "Argue formal vs substantive equality and reservation jurisprudence.", 5,
  ["S-GS2-01", "S-GS2-12"], [r"Article 14\b", r"Article 15\b", r"Article 16\b", r"Article 17\b", r"equality before (the )?law", r"reservation", r"untouchab", r"creamy layer", r"Indra Sawhney", r"equal protection", r"discriminat", r"Right to Equality"], ["R-LAXMI", "R-NCERT"], cross=["xs-society-social-justice"], related=["fr-freedoms", "constitutional-amendments-major"], const_loc="Arts 14–18")

C("fr-freedoms", "B", "Right to Freedom (Arts 19–22) and Art 21",
  "Six freedoms under Art 19 (with reasonable restrictions), protection in respect of conviction (Art 20), life and personal liberty (Art 21), education (21A) and protection against arrest and detention (Art 22).",
  ["Art 19(1)(a)–(g) and grounds for restrictions under 19(2)–(6)", "Freedom of the press", "Art 20: ex post facto laws, double jeopardy, self-incrimination", "Art 21: procedure established by law → due process (Maneka Gandhi)", "Expanding content of Art 21 (privacy, dignity, health, environment)", "Art 21A: education", "Art 22: preventive detention safeguards"],
  ["Procedure established by law vs due process", "Preventive vs punitive detention", "Absolute vs reasonable restrictions on freedoms"],
  ["fr-overview-art-12-13"], "Know the freedoms, restrictions and the major interpretations of Art 21.",
  "Weigh liberty against public order, security and morality using case-law examples.", 6,
  ["S-GS2-01", "S-P1-04"], [r"Article 19\b", r"Article 20\b", r"Article 21\b", r"Article 22\b", r"freedom of (speech|expression|the press)", r"right to (life|privacy)", r"personal liberty", r"preventive detention", r"privacy", r"Right to Freedom", r"Right to Life", r"sedition", r"hate speech", r"free speech"], ["R-LAXMI", "R-NCERT"], related=["fr-equality", "judicial-review-activism-pil"], const_loc="Arts 19–22")

C("fr-exploitation-religion-cultural", "B", "Rights against exploitation, to religion, and cultural-educational rights (Arts 23–30)",
  "Prohibits trafficking and forced labour, guarantees freedom of religion, and protects minority cultural and educational interests.",
  ["Art 23: trafficking, forced labour (begar)", "Art 24: child labour in hazardous work", "Arts 25–28: freedom of conscience, practice and propagation; religious denominations; no compulsory taxes/instruction", "Essential religious practices doctrine", "Art 29: protection of minorities' language, script, culture", "Art 30: minorities' right to establish and administer educational institutions"],
  ["Art 25 (individual) vs Art 26 (denominations)", "Art 29 (any section of citizens) vs Art 30 (minorities)"],
  ["fr-overview-art-12-13"], "Know scope and limits of each Article.",
  "Discuss secularism in India through freedom of religion and minority rights.", 3,
  ["S-GS2-01", "S-GS1-09"], [r"Article 2[3-9]\b", r"Article 30\b", r"freedom of religion", r"minority educational", r"forced labour", r"trafficking", r"religious denomination", r"essential religious practice", r"secularism", r"minorit"], ["R-LAXMI", "R-NCERT"], related=["preamble"], const_loc="Arts 23–30")

C("fr-remedies-writs", "B", "Right to Constitutional Remedies and writs (Arts 32, 226)",
  "The right to move the Supreme Court (Art 32) and High Courts (Art 226) for enforcement of rights, chiefly through the five writs.",
  ["Habeas corpus", "Mandamus", "Prohibition", "Certiorari", "Quo warranto", "Art 32 vs Art 226 (scope and territorial reach)", "Suspension of Art 32 during Emergency (Art 359)", "Locus standi and PIL"],
  ["Art 32 (a fundamental right itself) vs Art 226 (wider, non-fundamental-rights purposes too)", "Prohibition (before/while) vs certiorari (after)"],
  ["fr-overview-art-12-13"], "Know each writ's purpose and when it is available.",
  "Be able to explain why the right to remedies is called the 'heart and soul' of the Constitution and the role of PIL.", 3,
  ["S-GS2-01", "S-GS2-03", "S-P1-04"], [r"habeas corpus", r"mandamus", r"certiorari", r"quo warranto", r"prohibition", r"\bwrit", r"Article 32\b", r"Article 226\b", r"constitutional remed"], ["R-LAXMI", "R-NCERT", "R-SCI"], related=["judicial-review-activism-pil", "high-courts-subordinate"], const_loc="Arts 32, 226")

C("dpsp", "B", "Directive Principles of State Policy",
  "Non-justiciable guidelines in Part IV directing the State to secure social and economic justice and build a welfare state.",
  ["Socialistic, Gandhian and liberal-intellectual principles", "Art 39(b)–(c), 39A", "Art 40 (village panchayats), 41, 43, 44 (UCC), 45, 46, 47, 48, 48A, 49, 50, 51", "Non-justiciability and Art 37", "42nd, 44th, 86th Amendments' changes", "Use of DPSPs by courts"],
  ["Fundamental Rights (justiciable, negative) vs DPSP (non-justiciable, positive)", "Gandhian vs socialist vs liberal directives"],
  ["preamble"], "Group the directives by type and identify Articles.",
  "Evaluate DPSPs as tools of welfare policy and how courts read them into rights.", 4,
  ["S-GS2-01", "S-GS2-12", "S-P1-04"], [r"Directive Principles", r"DPSP", r"Article (3[6-9]|4[0-9]|5[01])\b", r"uniform civil code", r"welfare state", r"Part IV\b"], ["R-LAXMI", "R-NCERT"], cross=["xs-society-social-justice"], related=["fr-dpsp-relationship"], const_loc="Arts 36–51 (Part IV)")

C("fundamental-duties", "B", "Fundamental Duties",
  "Duties of citizens listed in Art 51A, added by the 42nd Amendment (1976) on the recommendation of the Swaran Singh Committee, with the eleventh added by the 86th Amendment (2002).",
  ["Origin: Swaran Singh Committee, 42nd Amendment", "Art 51A list of duties", "86th Amendment (duty of parents on education)", "Non-justiciable, no direct penalty", "Judicial use in interpreting statutes"],
  ["Fundamental Rights vs Fundamental Duties", "Duties (citizens only) vs DPSP (State)"],
  ["dpsp"], "List the duties and the amendments.",
  "Discuss balance between rights and duties and whether duties should be enforceable.", 1,
  ["S-GS2-01", "S-P1-04"], [r"Fundamental Duties", r"Article 51A\b", r"Swaran Singh"], ["R-LAXMI", "R-NCERT"], related=["dpsp", "fr-equality"], const_loc="Art 51A (Part IVA)")

C("fr-dpsp-relationship", "B", "Relationship between Fundamental Rights and DPSP",
  "The evolving judicial and legislative position on which prevails when rights and directives conflict, culminating in the 'harmony and balance' position.",
  ["Champakam Dorairajan (1951)", "Golaknath and Kesavananda Bharati", "Art 31C (25th and 42nd Amendments)", "Minerva Mills (1980): harmony and balance", "Later judicial use of DPSP to expand Art 21"],
  ["Primacy of FR vs primacy of DPSP vs harmonious construction"],
  ["fr-overview-art-12-13", "dpsp"], "Know the cases and the sequence.",
  "Explain how the Court moved from FR-primacy to a harmonious reading.", 2,
  ["S-GS2-01", "S-GS2-03"], [r"Fundamental Rights and (the )?Directive", r"Directive Principles.*Fundamental Rights", r"Minerva Mills", r"Champakam", r"Article 31C\b"], ["R-LAXMI"], related=["basic-structure-doctrine"])

# ===== C. Amendment ==========================================================
C("amendment-procedure", "C", "Amending the Constitution (Art 368)",
  "Art 368 prescribes how Parliament may amend the Constitution, with different majorities and, for some provisions, ratification by states.",
  ["Simple majority provisions outside Art 368", "Special majority (majority of the House plus two-thirds present and voting)", "Special majority plus ratification by half of the states", "Provisions needing state ratification", "President's assent is compulsory (24th Amendment)", "Amendment vs ordinary law"],
  ["Amendment by simple majority (e.g. Art 3, 4) vs Art 368 amendment", "Constituent power vs legislative power"],
  ["constitution-constitutionalism"], "Memorise the three methods and examples of each.",
  "Argue whether the amending procedure is balanced between flexibility and rigidity.", 3,
  ["S-GS2-01", "S-P1-04"], [r"Article 368\b", r"amend(ing|ment of) the Constitution", r"constitutional amendment", r"ratification (by|of) .*(State|Legislature)", r"special majority", r"amendment (bill|procedure)"], ["R-LAXMI", "R-NCERT"], related=["basic-structure-doctrine", "constitutional-amendments-major"], const_loc="Art 368 (Part XX)")

C("basic-structure-doctrine", "C", "Basic structure doctrine",
  "Judicially evolved limit on Parliament's amending power: amendments cannot alter the basic structure or framework of the Constitution.",
  ["Shankari Prasad and Sajjan Singh", "Golaknath (1967)", "Kesavananda Bharati (1973)", "Indira Nehru Gandhi v Raj Narain (1975)", "Minerva Mills (1980)", "Waman Rao (1981): 24 April 1973 cut-off for Ninth Schedule", "I.R. Coelho (2007)", "Illustrative features: supremacy, secularism, federalism, free and fair elections, judicial review, separation of powers"],
  ["Basic structure vs basic features (no exhaustive list)", "Amending power vs ordinary legislative power"],
  ["amendment-procedure", "fr-overview-art-12-13"], "Case sequence and the holding of each.",
  "Argue the democratic legitimacy of judicial limits on constitutional amendment.", 5,
  ["S-GS2-01", "S-GS2-03"], [r"basic structure", r"Kesavananda", r"Golaknath", r"Minerva Mills", r"Ninth Schedule", r"I\.?\s?R\.? Coelho", r"Shankari Prasad", r"Sajjan Singh", r"basic feature"], ["R-LAXMI", "R-SCI", "R-CONSTNET"], related=["amendment-procedure", "judicial-review-activism-pil", "separation-of-powers"])

C("constitutional-amendments-major", "C", "Landmark constitutional amendments",
  "Selected amendments that reshaped the polity, grouped by theme: rights and reservation, federal-fiscal, local government, electoral and parliamentary reform.",
  ["7th (1956): reorganisation of states", "24th and 25th (1971)", "42nd (1976): 'mini-Constitution'", "44th (1978): reversal of many 42nd changes", "52nd (1985): anti-defection", "61st (1988): voting age 18", "73rd and 74th (1992): local government", "86th (2002): education", "91st (2003): size of ministries; strengthened anti-defection", "101st (2016): GST", "103rd (2019): EWS reservation", "104th–106th (2019–2023)"],
  ["42nd vs 44th Amendments", "73rd (rural) vs 74th (urban)"],
  ["amendment-procedure"], "Number–year–subject triplets for the amendments listed.",
  "Group amendments by theme to support analytical answers on constitutional change.", 4,
  ["S-GS2-01"], [r"Constitution \((.{0,20})Amendment\) Act", r"\d+(st|nd|rd|th) (Constitution )?Amendment", r"Amendment Act"], ["R-LAXMI", "R-INDIACODE", "R-CONSTNET"], related=["amendment-procedure", "panchayati-raj", "anti-defection-law"])

# ===== D. Union Executive ====================================================
C("parliamentary-system", "D", "Parliamentary system of government",
  "A system where the Executive emerges from, and is collectively responsible to, the legislature.",
  ["Nominal vs real executive", "Collective responsibility (Art 75)", "Individual responsibility", "Fusion of Executive and Legislature", "Dissolution and no-confidence", "Comparison with presidential system", "Constitutional conventions"],
  ["Parliamentary vs presidential system", "Collective vs individual responsibility", "Convention vs law"],
  ["constitution-constitutionalism"], "Core features and examples of each.",
  "Debate stability, accountability and the strengthening of the Prime Minister's office.", 2,
  ["S-GS2-05", "S-GS2-06"], [r"parliamentary (system|form|democracy)", r"presidential system", r"collective responsibility", r"cabinet system", r"no-confidence"], ["R-LAXMI", "R-NCERT"], related=["pm-council-of-ministers", "president"])

C("president", "D", "President of India",
  "Constitutional head of the Union Executive, elected indirectly, with executive, legislative, judicial, financial, diplomatic, military and emergency powers exercised on ministerial advice.",
  ["Qualification, election (Arts 54–55), oath, term, impeachment (Art 61)", "Executive and appointing powers", "Legislative powers incl. ordinance (Art 123)", "Veto powers (absolute, suspensive, pocket)", "Pardoning (Art 72)", "Emergency powers", "Discretion in hung Parliament; Art 74 and 42nd/44th Amendments"],
  ["Ordinance-making by President (Art 123) vs Governor (Art 213)", "Suspensive vs pocket veto", "President's pardoning vs Governor's (Art 161)"],
  ["parliamentary-system"], "Memorise the election method, term, removal and each power with its Article.",
  "Be able to discuss the 'rubber stamp' debate and discretionary situations.", 5,
  ["S-GS2-06"], [r"President of India", r"\bPresident\b.*(election|impeach|ordinance|pardon|veto|assent)", r"Article (5[2-9]|6[0-2]|72|123)\b", r"Ordinance", r"pocket veto", r"Electoral College"], ["R-LAXMI", "R-NCERT", "R-SANSAD"], related=["vice-president", "governor", "emergency-provisions"], const_loc="Arts 52–62, 72, 74, 111, 123")

C("vice-president", "D", "Vice-President of India",
  "Second-highest constitutional office; ex-officio Chairman of the Rajya Sabha and acts as President during vacancy or absence.",
  ["Election (Art 66) and term", "Removal (Art 67)", "Role as Rajya Sabha Chairman", "Acting as President (Art 65)", "Casting vote"],
  ["Vice-President's election vs President's election (electoral college composition)"],
  ["president"], "Election, removal and functions.",
  "Link to the role of presiding officers in legislative functioning.", 1,
  ["S-GS2-06"], [r"Vice-President", r"Chairman of the Rajya Sabha"], ["R-LAXMI", "R-SANSAD"], related=["presiding-officers"], const_loc="Arts 63–71")

C("pm-council-of-ministers", "D", "Prime Minister and Council of Ministers",
  "The real executive: the PM heads a council collectively responsible to the Lok Sabha, with a Cabinet at its core.",
  ["Appointment of PM and ministers (Arts 74–75)", "Cabinet vs Council of Ministers vs Cabinet committees", "Collective responsibility", "Size limit (91st Amendment: 15% of Lok Sabha strength)", "Role of PM", "Ministers who are not members of Parliament (six months)", "Parliamentary secretaries; Kitchen cabinet"],
  ["Cabinet vs Council of Ministers", "Prime Minister vs President (real vs nominal)"],
  ["parliamentary-system", "president"], "Cabinet/Council distinction and Articles.",
  "Examine the 'primus inter pares' vs presidentialisation debate.", 3,
  ["S-GS2-06", "S-GS2-05"], [r"Prime Minister", r"Council of Ministers", r"Cabinet\b", r"Article (74|75)\b", r"Cabinet Secretar", r"kitchen cabinet"], ["R-LAXMI", "R-NCERT", "R-SANSAD"], cross=["xs-governance-civil-services"], related=["parliamentary-system", "chief-minister-council"], const_loc="Arts 74–78")

# ===== E. Parliament =========================================================
C("parliament-houses", "E", "Parliament: composition, membership and disqualification",
  "Parliament consists of the President, the Lok Sabha and the Rajya Sabha; its composition, qualifications and disqualification rules are constitutionally fixed.",
  ["Lok Sabha and Rajya Sabha strength and term", "Representation of States/UTs; nominated members", "Qualifications and disqualifications (Art 84, 102, RPA 1951)", "Vacating seat; Tenth Schedule", "Delimitation", "Sessions, quorum, prorogation, dissolution", "Role of the Rajya Sabha"],
  ["Lok Sabha (directly elected, dissolvable) vs Rajya Sabha (permanent house)", "Adjournment vs prorogation vs dissolution"],
  ["parliamentary-system"], "Strength, term and mode of election of each House.",
  "Evaluate bicameralism and the role of the Rajya Sabha in a federal polity.", 5,
  ["S-GS2-05"], [r"Lok Sabha", r"Rajya Sabha", r"Parliament", r"delimitation", r"quorum", r"prorogation", r"bicameral", r"disqualif", r"sitting of the House"], ["R-LAXMI", "R-SANSAD", "R-PRS"], related=["presiding-officers", "legislative-procedure", "anti-defection-law"], const_loc="Arts 79–122")

C("presiding-officers", "E", "Presiding officers of Parliament",
  "The Speaker, Deputy Speaker, Chairman and Deputy Chairman, who preside over and regulate proceedings of the Houses.",
  ["Election and removal of Speaker (Art 93, 94, 96)", "Powers: adjournment, casting vote, certifying Money Bill, deciding disqualification under Tenth Schedule", "Pro-tem Speaker", "Chairman of Rajya Sabha (Vice-President) and Deputy Chairman", "Secretariat and Secretary-General", "Neutrality and the 'Once a Speaker always a Speaker' convention"],
  ["Speaker vs Chairman of Rajya Sabha (election, removal)", "Speaker's casting vote vs Chairman's"],
  ["parliament-houses"], "Election, removal and powers.",
  "Discuss the neutrality, anti-defection role and independence of the Speaker.", 2,
  ["S-GS2-05"], [r"\bSpeaker\b", r"Deputy Speaker", r"Deputy Chairman", r"presiding officer", r"pro-?tem"], ["R-LAXMI", "R-SANSAD", "R-PRS"], related=["anti-defection-law", "legislative-procedure"], const_loc="Arts 93–98")

C("legislative-procedure", "E", "Legislative process: bills, Money Bills and joint sitting",
  "The passage of ordinary, money, financial and constitutional amendment bills, and the mechanisms to resolve deadlock between the Houses.",
  ["Ordinary bill: three readings, committee stage", "Money Bill (Art 110) and Financial Bill categories", "Role of Rajya Sabha on Money Bills", "Joint sitting (Art 108)", "Assent and veto", "Private members' bills", "Ordinance-making and Art 123"],
  ["Money Bill vs Financial Bill", "Ordinary bill vs Constitution Amendment Bill", "Government bill vs private member's bill"],
  ["parliament-houses", "president"], "Steps, categories and what each House can do.",
  "Analyse efficacy of lawmaking: disruptions, scrutiny, delegated legislation, Money Bill route.", 4,
  ["S-GS2-05"], [r"Money Bill", r"Financial Bill", r"joint sitting", r"Ordinary Bill", r"private member", r"legislative process", r"passage of (a )?bill", r"delegated legislation", r"Article (108|109|110|111)\b"], ["R-LAXMI", "R-SANSAD", "R-PRS"], related=["budget-financial-control", "president"], const_loc="Arts 107–111")

C("budget-financial-control", "E", "Budget and parliamentary financial control",
  "The constitutional framework by which Parliament authorises revenue and expenditure of the Union.",
  ["Annual Financial Statement (Art 112)", "Consolidated Fund, Public Account, Contingency Fund", "Charged vs voted expenditure", "Appropriation Bill, Finance Bill, vote on account, supplementary grants", "Cut motions", "Fiscal discipline laws (FRBM)", "Role of CAG and PAC"],
  ["Consolidated Fund vs Public Account vs Contingency Fund", "Appropriation Bill vs Finance Bill", "Charged vs voted"],
  ["legislative-procedure"], "Funds, bills and stages in the budget cycle.",
  "Assess Parliament's weak financial oversight and propose reforms.", 4,
  ["S-GS2-05", "S-GS3-03"], [r"Consolidated Fund", r"Contingency Fund", r"Public Account", r"Appropriation", r"Budget", r"vote on account", r"cut motion", r"Finance Bill", r"charged (on|expenditure)"], ["R-LAXMI", "R-SANSAD", "R-PRS"], cross=["xs-economy-public-finance"], related=["cag-attorney-general", "parliamentary-committees"], const_loc="Arts 112–117, 265–267")

C("parliamentary-committees", "E", "Parliamentary committees",
  "Ad hoc and standing committees through which Parliament scrutinises the Executive and legislation.",
  ["Public Accounts Committee", "Estimates Committee", "Committee on Public Undertakings", "Departmentally related standing committees", "Joint Parliamentary Committees", "Committee on Subordinate Legislation", "Ad hoc vs standing"],
  ["PAC vs Estimates Committee", "Standing vs ad hoc committees"],
  ["parliament-houses"], "Composition and functions of each key committee.",
  "Argue the case for referring more bills to committees.", 3,
  ["S-GS2-05"], [r"(Parliamentary|Public Accounts|Estimates|Standing) Committee", r"Joint Parliamentary Committee", r"Committee on Public Undertakings", r"\bPAC\b", r"Committee on Estimates", r"parliamentary committee"], ["R-LAXMI", "R-SANSAD", "R-PRS"], related=["budget-financial-control", "legislative-procedure"])

C("parliamentary-devices-privileges", "E", "Parliamentary devices and privileges",
  "Instruments (question hour, motions) used to hold the Executive to account, and the privileges that protect legislators and Houses.",
  ["Question Hour, Zero Hour", "Adjournment, no-confidence, censure, calling-attention motions", "Short-duration discussion", "Parliamentary privileges (Arts 105, 194)", "Breach of privilege and contempt", "Freedom of speech in the House", "Disruptions and decorum"],
  ["Adjournment motion vs no-confidence motion", "Privilege vs fundamental rights"],
  ["parliament-houses"], "Know each device and its purpose.",
  "Discuss declining functioning of legislatures and measures to improve accountability.", 3,
  ["S-GS2-05"], [r"Question Hour", r"Zero Hour", r"adjournment motion", r"no-confidence", r"privilege", r"calling attention", r"censure", r"parliamentary (functioning|disruption|proceedings)", r"productivity of (the )?Parliament"], ["R-LAXMI", "R-SANSAD", "R-PRS"], related=["presiding-officers", "state-legislature"])

# ===== F. State ==============================================================
C("governor", "F", "Governor",
  "The constitutional head of a State, appointed by the President, with executive, legislative and limited discretionary powers.",
  ["Appointment, term and removal (Arts 155–156)", "Executive powers and appointments", "Legislative powers incl. ordinances (Art 213) and reserving bills (Arts 200–201)", "Discretionary powers", "Report under Art 356", "Pardoning (Art 161)", "Sarkaria, Punchhi and other commission views"],
  ["Governor vs President (appointment, impeachment, discretion)", "Governor's discretion vs advice of the CoM"],
  ["president"], "Powers and Articles.",
  "Evaluate the Governor's role in a federal system: appointments, floor tests, assent.", 4,
  ["S-GS2-02", "S-GS2-06"], [r"Governor", r"Article (153|154|155|156|161|163|164|200|201|213)\b", r"Sarkaria", r"Punchhi", r"Raj Bhavan"], ["R-LAXMI", "R-NCERT", "R-ARC"], related=["chief-minister-council", "state-legislature", "emergency-provisions", "federalism-centre-state"], const_loc="Arts 153–162, 163–167, 200–201, 213")

C("chief-minister-council", "F", "Chief Minister and State Council of Ministers",
  "The real executive of a State, collectively responsible to the Legislative Assembly.",
  ["Appointment of CM and ministers (Arts 163–164)", "Size limit (91st Amendment)", "Collective responsibility", "CM's role with Governor and Council", "Advocate General (Art 165)"],
  ["Chief Minister vs Prime Minister (parallel roles)"],
  ["governor", "pm-council-of-ministers"], "Appointment, responsibility and size limits.",
  "Link to state-level governance and coalition politics.", 2,
  ["S-GS2-06", "S-GS2-02"], [r"Chief Minister", r"State Council of Ministers", r"Advocate General"], ["R-LAXMI", "R-NCERT"], related=["governor", "state-legislature"], const_loc="Arts 163–167")

C("state-legislature", "F", "State Legislature",
  "The Legislative Assembly (and, in some states, the Legislative Council) with powers broadly parallel to Parliament within the State List and Concurrent List.",
  ["Composition of Assembly and Council", "Creation/abolition of Councils (Art 169)", "Legislative procedure and Money Bills in states", "Privileges", "Comparison of Parliament and State Legislature", "Speaker and Chairman", "Reservation of seats"],
  ["Legislative Council vs Rajya Sabha (weaker role)", "State Legislature vs Parliament"],
  ["parliament-houses"], "Differences in composition and powers.",
  "Evaluate whether second chambers in states are useful.", 3,
  ["S-GS2-05"], [r"State Legislat", r"Legislative Assembly", r"Legislative Council", r"Article 169\b", r"bicameral.*State", r"MLA"], ["R-LAXMI", "R-NCERT", "R-PRS"], related=["parliament-houses", "governor"], const_loc="Arts 168–212")

# ===== G. Federalism =========================================================
C("federalism-centre-state", "G", "Federalism and Centre–State relations",
  "The distribution of legislative, administrative and financial powers between the Union and the States.",
  ["Federal features and unitary bias", "Seventh Schedule: Union, State, Concurrent Lists", "Residuary powers (Art 248)", "Parliament's power to legislate on State List (Arts 249, 250, 252, 253)", "Administrative relations (Arts 256–263)", "Financial relations (Arts 268–293)", "Commissions: Sarkaria, Punchhi", "Cooperative, competitive and asymmetric federalism"],
  ["Federal vs unitary features", "Cooperative vs competitive federalism", "Legislative vs administrative vs financial relations"],
  ["salient-features"], "Know the lists and the conditions under which Parliament can legislate on State subjects.",
  "Evaluate recent flashpoints (GST, agriculture laws, Governor's role, central schemes).", 6,
  ["S-GS2-02"], [r"federal", r"Centre.?State", r"Union and (the )?States", r"Seventh Schedule", r"Concurrent List", r"State List", r"Union List", r"residuary", r"Sarkaria", r"Punchhi", r"cooperative federalism", r"devolution"], ["R-LAXMI", "R-NCERT", "R-ARC"], cross=["xs-economy-public-finance"], related=["inter-state-relations", "finance-commission-fiscal-federalism", "emergency-provisions", "special-provisions-schedules"], const_loc="Arts 245–293; Seventh Schedule")

C("inter-state-relations", "G", "Inter-State relations and coordination bodies",
  "Constitutional and statutory mechanisms for resolving inter-state disputes and coordinating policy.",
  ["Inter-State water disputes (Art 262; Inter-State River Water Disputes Act 1956)", "Inter-State Council (Art 263)", "Zonal Councils (statutory under the States Reorganisation Act 1956)", "Full faith and credit (Art 261)", "Freedom of inter-state trade (Arts 301–307)", "Public acts, records and judicial proceedings", "NITI Aayog as a federal forum; GST Council"],
  ["Inter-State Council (constitutional provision, set up by President order) vs Zonal Councils (statutory)"],
  ["federalism-centre-state"], "Bodies, Articles, how disputes are resolved.",
  "Discuss river-water disputes and cooperative federalism.", 3,
  ["S-GS2-02"], [r"Inter-State (Council|Water|River|dispute)", r"Zonal Council", r"Article 262\b", r"Article 263\b", r"river water dispute", r"inter-state"], ["R-LAXMI", "R-ARC"], related=["federalism-centre-state"], const_loc="Arts 261–263, 301–307")

C("emergency-provisions", "G", "Emergency provisions",
  "National Emergency (Art 352), President's Rule (Art 356) and Financial Emergency (Art 360) and their effects on federal and rights provisions.",
  ["Grounds and procedure for each emergency", "Effect on Centre–State relations and Fundamental Rights (Arts 358–359)", "Parliamentary approval and duration", "44th Amendment safeguards", "S.R. Bommai (1994)", "Misuse of Art 356", "Proclamation by the President"],
  ["National vs State vs Financial Emergency", "Art 358 (Art 19 suspended automatically) vs Art 359 (enforcement of rights suspended by order)"],
  ["president", "federalism-centre-state"], "Grounds, procedure, approval, duration.",
  "Evaluate S.R. Bommai and the misuse of Art 356.", 4,
  ["S-GS2-02", "S-GS2-03"], [r"Emergency", r"President.?s Rule", r"Article (352|356|358|359|360)\b", r"Bommai", r"Financial Emergency"], ["R-LAXMI", "R-NCERT", "R-ARC"], cross=["xs-security-internal"], related=["president", "governor", "fr-freedoms"], const_loc="Arts 352–360 (Part XVIII)")

C("finance-commission-fiscal-federalism", "G", "Finance Commission and fiscal federalism",
  "The constitutional body that recommends sharing of Union taxes with the States and principles for grants-in-aid; part of the larger system of fiscal transfers including the GST Council.",
  ["Art 280: constitution and functions", "Vertical and horizontal devolution", "Grants-in-aid (Art 275, 282)", "State Finance Commission (Arts 243I, 243Y)", "GST Council (Art 279A)", "Finance Commission vs Planning Commission/NITI Aayog", "Terms of reference and criteria"],
  ["Finance Commission vs NITI Aayog", "Vertical vs horizontal devolution"],
  ["federalism-centre-state"], "Know the Articles and the roles of the bodies.",
  "Analyse fiscal federalism issues: cesses and surcharges, GST compensation, devolution criteria.", 4,
  ["S-GS2-02", "S-GS3-03"], [r"Finance Commission", r"Article (280|275|282|279A)\b", r"GST Council", r"horizontal devolution", r"grants-in-aid", r"fiscal federalism", r"devolution of (funds|taxes)", r"Planning Commission", r"NITI Aayog"], ["R-LAXMI", "R-FINCOM"], cross=["xs-economy-public-finance"], related=["federalism-centre-state"], const_loc="Arts 268–293, 279A, 280")

C("special-provisions-schedules", "G", "Special provisions, Fifth/Sixth Schedules and Union Territories",
  "Asymmetric arrangements for particular states and regions: Art 370 (now abrogated), Art 371 series, tribal-area governance and the administration of Union Territories.",
  ["Art 370 and its abrogation (2019)", "Art 371 to 371J special provisions", "Fifth Schedule (Scheduled Areas) and Sixth Schedule (tribal areas of Assam, Meghalaya, Tripura, Mizoram)", "Autonomous District/Regional Councils", "Union Territories (Art 239 onwards)", "Special status of Delhi (Art 239AA)", "Jammu and Kashmir Reorganisation Act 2019"],
  ["Fifth Schedule vs Sixth Schedule", "UT with legislature vs without"],
  ["federalism-centre-state"], "Know which state has which provision.",
  "Assess asymmetric federalism and tribal self-governance.", 4,
  ["S-GS2-02", "S-GS2-12"], [r"Article 370\b", r"Article 371", r"Fifth Schedule", r"Sixth Schedule", r"Scheduled Area", r"Union Territor", r"Autonomous (District|Council)", r"special (status|category|provision)", r"Article 239", r"Delhi.*(Government|Lieutenant|NCT)"], ["R-LAXMI", "R-NCERT", "R-INDIACODE"], cross=["xs-society-social-justice"], related=["federalism-centre-state", "panchayati-raj"], const_loc="Arts 239–242, 244, 370–371J; Fifth and Sixth Schedules")

# ===== H. Judiciary ==========================================================
C("supreme-court", "H", "Supreme Court of India",
  "The apex court with original, appellate, advisory and writ jurisdiction, custodian of the Constitution.",
  ["Composition and appointment (Arts 124–125): collegium system", "Qualifications, removal of judges", "Original jurisdiction (Art 131)", "Writ (Art 32), appellate and advisory (Art 143) jurisdiction", "Special leave petition (Art 136)", "Court of record, review, curative petition", "NJAC and the Fourth Judges case (2015)"],
  ["Original vs appellate vs advisory jurisdiction", "Collegium vs NJAC"],
  ["fr-remedies-writs"], "Composition, jurisdictions and Articles.",
  "Debate judicial appointments, pendency and the Court's role.", 5,
  ["S-GS2-06", "S-GS2-03"], [r"Supreme Court", r"collegium", r"NJAC", r"National Judicial Appointments", r"Article (124|129|131|136|137|141|142|143)\b", r"judges.? (appointment|removal)", r"curative petition", r"advisory jurisdiction", r"Chief Justice of India"], ["R-LAXMI", "R-NCERT", "R-SCI"], related=["high-courts-subordinate", "judicial-review-activism-pil"], const_loc="Arts 124–147")

C("high-courts-subordinate", "H", "High Courts and subordinate courts",
  "The judicial hierarchy below the Supreme Court: High Courts with writ and supervisory powers, and district and subordinate courts.",
  ["Composition, appointment and removal of HC judges (Arts 214–217)", "Writ jurisdiction (Art 226) vs SC (Art 32)", "Superintendence over subordinate courts (Art 227)", "District judges and subordinate judiciary (Arts 233–237)", "Transfer of judges", "National Judicial Infrastructure and pendency issues"],
  ["High Court vs Supreme Court jurisdiction", "Art 226 vs Art 227"],
  ["supreme-court", "fr-remedies-writs"], "Hierarchy and Articles.",
  "Discuss pendency and judicial reform in lower courts.", 3,
  ["S-GS2-06"], [r"High Court", r"subordinate (court|judiciary)", r"district (court|judge)", r"Article (214|215|226|227|233)\b", r"pendency"], ["R-LAXMI", "R-NCERT"], related=["supreme-court", "tribunals-dispute-redressal"], const_loc="Arts 214–237")

C("judicial-review-activism-pil", "H", "Judicial review, judicial activism and PIL",
  "The power of courts to test laws and executive action against the Constitution, and its expansion through activism and public interest litigation.",
  ["Judicial review sources (Arts 13, 32, 226, 131–136)", "Judicial activism vs judicial restraint vs overreach", "PIL: origin, relaxation of locus standi", "Contempt of court", "Doctrine of political question", "Landmark rights-expanding rulings"],
  ["Judicial review vs judicial activism vs judicial overreach", "PIL vs ordinary litigation"],
  ["supreme-court", "fr-remedies-writs"], "Definitions and landmark examples.",
  "Argue merits and limits of judicial activism and PIL.", 4,
  ["S-GS2-03", "S-GS2-06"], [r"judicial review", r"judicial activism", r"judicial overreach", r"Public Interest Litigation", r"\bPIL\b", r"contempt", r"locus standi"], ["R-LAXMI", "R-SCI"], related=["basic-structure-doctrine", "separation-of-powers"])

C("separation-of-powers", "H", "Separation of powers among organs",
  "How legislative, executive and judicial functions are distributed and checked in India, which follows functional overlap and checks rather than strict separation.",
  ["Constitutional basis and doctrine", "Overlaps: ministers in the legislature, delegated legislation, tribunals", "Judicial independence", "Judicial review as a check", "Disputes between organs (e.g. legislative privilege vs judicial review)", "Comparison with the US"],
  ["Separation of powers vs checks and balances", "India vs US"],
  ["constitution-constitutionalism", "parliamentary-system"], "Doctrine and Indian departures.",
  "Evaluate conflicts between organs and ways to resolve them.", 2,
  ["S-GS2-03"], [r"separation of powers", r"doctrine of separation", r"organs of (the )?(government|State)", r"independence of the judiciary", r"judicial independence"], ["R-LAXMI", "R-NCERT"], related=["judicial-review-activism-pil", "basic-structure-doctrine"])

C("tribunals-dispute-redressal", "H", "Tribunals and alternative dispute redressal",
  "Quasi-judicial and alternative mechanisms to reduce court load and provide specialised or quicker justice.",
  ["Administrative tribunals (Arts 323A, 323B)", "Tribunals Reforms Act 2021", "Lok Adalats and Legal Services Authorities Act 1987", "Gram Nyayalayas", "Mediation and arbitration", "Free legal aid (Art 39A)", "National Green Tribunal and other statutory tribunals"],
  ["Tribunal vs court", "Lok Adalat vs Arbitration"],
  ["high-courts-subordinate"], "Names, Acts and basic features.",
  "Assess effectiveness and independence of tribunals and ADR.", 2,
  ["S-GS2-03", "S-GS2-09"], [r"tribunal", r"Lok Adalat", r"Gram Nyayalaya", r"arbitration", r"mediation", r"legal aid", r"alternative dispute", r"dispute redressal", r"National Green Tribunal"], ["R-LAXMI", "R-INDIACODE"], related=["high-courts-subordinate", "statutory-bodies"], const_loc="Arts 323A–323B")

# ===== I. Local government ===================================================
C("panchayati-raj", "I", "Panchayati Raj (73rd Amendment)",
  "The constitutionally mandated three-tier system of rural local government under Part IX and the Eleventh Schedule.",
  ["Evolution: Balwant Rai Mehta, Ashok Mehta, L.M. Singhvi, Sarkaria", "73rd Amendment: Gram Sabha, three-tier structure, direct elections, reservation, State Election Commission, State Finance Commission", "Eleventh Schedule", "District Planning Committees", "PESA Act 1996", "Compulsory vs voluntary provisions", "Devolution of funds, functions and functionaries (3 Fs)"],
  ["Compulsory vs voluntary provisions", "Panchayat vs Municipality (73rd vs 74th)", "PESA vs 73rd Amendment in Fifth Schedule areas"],
  ["federalism-centre-state", "constitutional-amendments-major"], "Provisions and committees.",
  "Evaluate why devolution to local bodies has lagged.", 5,
  ["S-GS2-02", "S-GS2-11"], [r"Panchayat", r"73rd", r"Gram Sabha", r"Eleventh Schedule", r"PESA", r"Balwant Rai", r"Ashok Mehta", r"rural local", r"village", r"local self-government", r"local bod"], ["R-LAXMI", "R-NCERT", "R-PANCHAYAT", "R-ARC"], related=["urban-local-bodies", "federalism-centre-state"], const_loc="Arts 243–243O (Part IX); Eleventh Schedule")

C("urban-local-bodies", "I", "Urban local bodies (74th Amendment)",
  "The constitutional framework (Part IXA, Twelfth Schedule) for municipal governance in cities and towns.",
  ["Types of urban bodies: Municipal Corporation, Municipality, Notified Area Committee, Cantonment Board, Township etc.", "74th Amendment provisions", "Twelfth Schedule", "Metropolitan Planning Committees", "Mayor and Commissioner roles", "Finance of urban local bodies", "Urban governance challenges"],
  ["Municipal Corporation vs Municipality", "Elected vs bureaucratic control in cities"],
  ["panchayati-raj"], "Types of bodies and amendment provisions.",
  "Discuss reforms in urban governance and finance.", 3,
  ["S-GS2-02", "S-GS2-11"], [r"Municipal", r"74th", r"Twelfth Schedule", r"urban local", r"Urban (governance|local)", r"Metropolitan Planning", r"Cantonment", r"Mayor"], ["R-LAXMI", "R-NCERT", "R-ARC"], cross=["xs-society-social-justice"], related=["panchayati-raj"], const_loc="Arts 243P–243ZG (Part IXA); Twelfth Schedule")

# ===== J. Bodies =============================================================
C("election-commission", "J", "Election Commission of India",
  "The constitutional body under Art 324 superintending, directing and controlling elections to Parliament, State Legislatures and the offices of President and Vice-President.",
  ["Composition and appointment of the CEC and Election Commissioners", "Removal of CEC", "Powers and functions", "Model Code of Conduct", "Registration and recognition of political parties and symbols", "State Election Commissions", "Recent appointment-law developments"],
  ["Election Commission of India vs State Election Commission", "Constitutional vs statutory body"],
  ["parliament-houses"], "Composition, powers, MCC.",
  "Discuss independence of the Election Commission and electoral integrity.", 3,
  ["S-GS2-08", "S-GS2-07"], [r"Election Commission", r"Model Code of Conduct", r"Chief Election Commissioner", r"Article 324\b", r"electoral roll", r"election symbols?"], ["R-LAXMI", "R-ECI"], related=["rpa-electoral-system", "electoral-reforms"], const_loc="Arts 324–329")

C("upsc-spsc", "J", "Union and State Public Service Commissions",
  "Constitutional bodies (Part XIV) that recruit to civil services and advise on service matters, safeguarding merit-based recruitment.",
  ["Composition, appointment, removal of members (Arts 315–317)", "Functions (Art 320)", "Limitations", "Independence safeguards", "Joint State Public Service Commission", "Role in civil service reforms"],
  ["UPSC vs SPSC (appointment and removal)", "Advisory vs binding role"],
  ["parliament-houses"], "Composition, functions and removal.",
  "Evaluate civil-service recruitment reforms.", 2,
  ["S-GS2-08", "S-GS2-16"], [r"Public Service Commission", r"\bUPSC\b", r"Article (315|316|317|320)\b", r"civil service reform"], ["R-LAXMI", "R-UPSC"], cross=["xs-governance-civil-services"], related=["cag-attorney-general"], const_loc="Arts 315–323 (Part XIV)")

C("cag-attorney-general", "J", "CAG and law officers",
  "The Comptroller and Auditor General audits public accounts and the Attorney General is the Union's chief law officer.",
  ["CAG: appointment, tenure, removal (Art 148)", "Duties and powers (Art 149)", "Audit reports and PAC", "Concept of propriety audit", "Attorney General (Art 76) and Solicitor General", "Advocate General (Art 165)"],
  ["CAG vs Attorney General", "Regularity audit vs propriety audit"],
  ["budget-financial-control"], "Appointment, term and functions.",
  "Discuss CAG's independence and role in accountability.", 3,
  ["S-GS2-08", "S-GS2-15"], [r"Comptroller and Auditor", r"\bCAG\b", r"Attorney[- ]General", r"Solicitor General", r"Advocate General", r"Article (148|149|76|165)\b"], ["R-LAXMI", "R-CAG"], related=["budget-financial-control", "parliamentary-committees"], const_loc="Arts 76, 148–151, 165")

C("national-commissions-vulnerable-sections", "J", "National commissions for vulnerable sections",
  "Constitutional and statutory commissions protecting SCs, STs, backward classes, minorities, women and linguistic minorities.",
  ["NCSC (Art 338), NCST (Art 338A)", "NCBC (Art 338B, 102nd Amendment 2018)", "National Commission for Minorities (statutory)", "National Commission for Women (statutory)", "Special Officer for Linguistic Minorities (Art 350B)", "Functions and powers", "Constitutional vs statutory"],
  ["Constitutional vs statutory commissions", "Advisory vs investigative functions"],
  ["fr-equality", "fr-exploitation-religion-cultural"], "Which body has which basis.",
  "Assess effectiveness of commissions as accountability mechanisms.", 2,
  ["S-GS2-08", "S-GS2-12"], [r"National Commission", r"Article 338", r"Scheduled Castes?\b.*Commission", r"Backward Classes", r"linguistic minorit", r"Commission for (Women|Minorities)"], ["R-LAXMI", "R-INDIACODE"], cross=["xs-society-social-justice"], related=["statutory-bodies"], const_loc="Arts 338–338B, 350A–350B")

C("statutory-bodies", "J", "Statutory, regulatory and quasi-judicial bodies",
  "Bodies created by Acts of Parliament rather than the Constitution — human-rights, information, vigilance, anti-corruption and sectoral regulators.",
  ["NHRC (Protection of Human Rights Act 1993)", "Central Information Commission (RTI Act 2005)", "Central Vigilance Commission", "Lokpal and Lokayuktas Act 2013", "NITI Aayog (executive body)", "Sectoral regulators (SEBI, TRAI, CCI etc.)", "Constitutional vs statutory vs executive bodies"],
  ["NHRC vs courts", "Statutory vs constitutional bodies", "Lokpal vs CVC"],
  ["parliament-houses"], "Parent Act, composition and role of each body.",
  "Discuss effectiveness and independence of watchdog bodies.", 4,
  ["S-GS2-09", "S-GS2-15"], [r"Human Rights Commission", r"\bNHRC\b", r"Information Commission", r"Right to Information", r"\bRTI\b", r"Central Vigilance", r"Lokpal", r"Lokayukta", r"regulator", r"SEBI", r"TRAI", r"Competition Commission", r"statutory bod", r"quasi-judicial"], ["R-LAXMI", "R-NHRC", "R-CIC", "R-LOKPAL", "R-INDIACODE"], cross=["xs-governance-rti"], related=["tribunals-dispute-redressal", "national-commissions-vulnerable-sections"])

# ===== K. Elections & parties ================================================
C("rpa-electoral-system", "K", "Representation of the People Acts and the electoral system",
  "The statutes (RPA 1950, 1951) governing electoral rolls, conduct of elections, qualifications, disqualifications and disputes, and the first-past-the-post system used in India.",
  ["RPA 1950: delimitation, rolls, allocation of seats", "RPA 1951: conduct, corrupt practices, disqualification (Sec 8), election petitions", "First-past-the-post vs proportional representation", "Single transferable vote for RS/President elections", "EVM and VVPAT", "Reservation of seats in legislatures", "Delimitation Commission"],
  ["FPTP vs proportional representation", "RPA 1950 vs RPA 1951", "Lok Sabha vs Rajya Sabha election methods"],
  ["election-commission"], "What each Act covers and the electoral methods.",
  "Compare electoral systems and argue for or against reform.", 4,
  ["S-GS2-07", "S-GS2-05"], [r"Representation of the People", r"first[- ]past[- ]the[- ]post", r"proportional representation", r"single transferable", r"EVM", r"VVPAT", r"election petition", r"corrupt practice", r"delimitation", r"electoral system"], ["R-LAXMI", "R-ECI", "R-INDIACODE"], related=["election-commission", "electoral-reforms"])

C("electoral-reforms", "K", "Electoral reforms",
  "Proposals and judicial/legislative changes to improve the fairness, transparency and inclusiveness of elections.",
  ["Committees (e.g. Dinesh Goswami, Tarkunde, Law Commission reports)", "Criminalisation of politics; Lily Thomas (2013)", "Right to know candidates' antecedents (ADR cases)", "NOTA (2013)", "Political funding and electoral bonds", "Simultaneous elections debate", "Paid news, MCC enforcement"],
  ["Electoral reforms by court vs by legislature"],
  ["rpa-electoral-system"], "Know the major reforms and cases.",
  "Argue pros and cons of specific reforms (simultaneous elections, state funding).", 3,
  ["S-GS2-07"], [r"electoral reform", r"criminali[sz]ation of politics", r"NOTA", r"electoral bond", r"simultaneous election", r"one nation.{0,20}one election", r"political fund", r"Lily Thomas", r"Goswami"], ["R-LAXMI", "R-ECI", "R-PRS"], related=["rpa-electoral-system", "anti-defection-law"])

C("anti-defection-law", "K", "Anti-defection law (Tenth Schedule)",
  "The 52nd Amendment (1985) added the Tenth Schedule disqualifying legislators for defection; the 91st Amendment (2003) removed the one-third split exception.",
  ["Grounds of disqualification", "Role of the Speaker/Chairman as decision-maker", "Exceptions: merger by two-thirds, 91st Amendment", "Kihoto Hollohan (1992)", "Judicial review of Speaker's decision", "Time limits and delays", "Criticisms and reform proposals"],
  ["Defection vs merger", "Speaker's role vs Election Commission's role (advice proposals)"],
  ["presiding-officers", "constitutional-amendments-major"], "Grounds, exceptions, key case.",
  "Evaluate whether the Speaker should decide defection cases.", 3,
  ["S-GS2-05", "S-GS2-07"], [r"anti-defection", r"Tenth Schedule", r"defection", r"Kihoto"], ["R-LAXMI", "R-PRS"], related=["presiding-officers", "electoral-reforms"], const_loc="Tenth Schedule")

C("political-parties-pressure-groups", "K", "Political parties, party system and pressure groups",
  "How parties and organised interests function in the polity: recognition, funding, internal democracy, and the role of formal and informal associations.",
  ["National and state party recognition criteria", "Party system (one-party dominance to coalitions)", "Internal democracy and funding", "Pressure groups, interest groups and movements", "Formal vs informal associations", "Role in policy-making"],
  ["Political party vs pressure group", "Interest groups vs social movements"],
  ["election-commission"], "Classification and recognition basics.",
  "Discuss the role of civil society and parties in a democracy.", 2,
  ["S-GS2-06", "S-GS2-11"], [r"political part", r"party system", r"pressure group", r"interest group", r"coalition", r"recogni[sz]ed .*party", r"formal and informal association", r"civil society"], ["R-LAXMI", "R-NCERT"], related=["electoral-reforms", "election-commission"])

# ------------------------------------------------- cross-subject stubs (planned)
STUBS = [
    ("xs-history-constitutional-developments", "history", "Constitutional developments under British rule (Modern History)"),
    ("xs-economy-public-finance", "economy", "Public finance, Union Budget and GST (Economy)"),
    ("xs-governance-rti", "governance", "RTI and transparency institutions (Governance)"),
    ("xs-governance-civil-services", "governance", "Role of civil services in a democracy (Governance)"),
    ("xs-society-social-justice", "society", "Welfare and protection of vulnerable sections (Social Justice)"),
    ("xs-security-internal", "security", "Internal security and emergency powers (Security)"),
]

# --------------------------------------- concept-level 'related' rationales
RATIONALE = {
    ("fr-equality", "fr-freedoms"): "Articles 14, 19 and 21 are read together (the 'golden triangle'); arbitrariness is tested under Art 14 and reasonableness of restrictions under Art 19.",
    ("fr-equality", "constitutional-amendments-major"): "Reservation changes (e.g. 103rd, 104th, 105th, 106th Amendments) are amendments touching Arts 15–16, 330, 332.",
    ("fr-freedoms", "judicial-review-activism-pil"): "Expansion of Art 21 is the best-known product of judicial activism and PIL.",
    ("fr-remedies-writs", "judicial-review-activism-pil"): "Writ jurisdiction is the instrument through which judicial review of executive action is exercised.",
    ("fr-remedies-writs", "high-courts-subordinate"): "Art 226 gives High Courts a wider writ power than Art 32.",
    ("basic-structure-doctrine", "amendment-procedure"): "The doctrine limits the amending power conferred by Art 368.",
    ("basic-structure-doctrine", "judicial-review-activism-pil"): "Basic-structure review is the strongest form of judicial review, applied to constitutional amendments.",
    ("basic-structure-doctrine", "separation-of-powers"): "Separation of powers and judicial review are among the features read into the basic structure.",
    ("basic-structure-doctrine", "preamble"): "Many basic-structure features (secularism, democracy, republic) are Preamble values.",
    ("basic-structure-doctrine", "fr-dpsp-relationship"): "The Fundamental Rights–DPSP conflict was one of the strands that produced the basic-structure doctrine (Art 31C, Kesavananda, Minerva Mills).",
    ("president", "emergency-provisions"): "Emergency proclamations are issued by the President on Cabinet advice (Art 74(1) as amended by the 44th Amendment).",
    ("president", "governor"): "The Governor's powers (ordinance, assent, pardon) parallel the President's but differ in election mode and discretion.",
    ("governor", "federalism-centre-state"): "The Governor is the principal Centre–State link; Sarkaria and Punchhi recommendations concern the office.",
    ("governor", "emergency-provisions"): "Art 356 proclamations rest on the Governor's report or the President's satisfaction.",
    ("federalism-centre-state", "finance-commission-fiscal-federalism"): "Financial relations are one of three arms of Centre–State relations; the FC and GST Council operationalise them.",
    ("federalism-centre-state", "special-provisions-schedules"): "Art 370/371 and Fifth/Sixth Schedules are asymmetric departures from the standard federal scheme.",
    ("federalism-centre-state", "inter-state-relations"): "Inter-state bodies complement Centre–State arrangements.",
    ("federalism-centre-state", "emergency-provisions"): "Emergency provisions convert the federal structure into a largely unitary one.",
    ("federalism-centre-state", "salient-features"): "Federal-with-unitary-bias is one of the salient features compared with other constitutions.",
    ("legislative-procedure", "budget-financial-control"): "Money Bills and Appropriation/Finance Bills are the legislative route for the budget.",
    ("parliament-houses", "anti-defection-law"): "Tenth Schedule disqualification affects membership of both Houses.",
    ("presiding-officers", "anti-defection-law"): "The Speaker/Chairman adjudicates disqualification under the Tenth Schedule.",
    ("budget-financial-control", "cag-attorney-general"): "CAG audit reports are examined by the PAC and underpin parliamentary financial control.",
    ("panchayati-raj", "urban-local-bodies"): "The 73rd and 74th Amendments created parallel structures for rural and urban local government.",
    ("election-commission", "rpa-electoral-system"): "The ECI administers the RPA 1950/1951 framework.",
    ("rpa-electoral-system", "electoral-reforms"): "Reform proposals largely amend or supplement the RPA framework.",
    ("electoral-reforms", "anti-defection-law"): "Anti-defection is a major strand of electoral/political reform debate.",
    ("tribunals-dispute-redressal", "statutory-bodies"): "Many statutory regulators exercise quasi-judicial functions through tribunals.",
}


PREFIXES = ("polity", "economy", "geography", "environment", "history", "scitech", "society", "governance", "ir", "security", "disaster", "ethics")


def build_links():
    ids = {c["id"] for c in CONCEPTS}
    links, seen = [], set()
    n = 0

    def add(src, tgt, rel, why, ev):
        nonlocal n
        key = (src, tgt, rel)
        if key in seen:
            return
        seen.add(key); n += 1
        links.append(dict(id=f"L-{n:04d}", source=src, target=tgt, relation=rel, rationale=why, evidence=ev, verification="authored-unreviewed"))

    for c in CONCEPTS:
        for p in c["prerequisites"]:
            assert p in ids, (c["id"], p)
            add(c["id"], p, "prerequisite", f"'{c['title']}' builds on '{next(x['title'] for x in CONCEPTS if x['id']==p)}'.", "authoring judgement (study-order)")
        for s in c["syllabus_ids"]:
            add(c["id"], s, "tests", "Concept lies within this syllabus point.", "UPSC syllabus text (supplied)")
        for x in c["cross_subject"]:
            if x in ids:
                add(c["id"], x, "related", f"Cross-subject connection to '{next(t['title'] for t in CONCEPTS if t['id'] == x)}'.", "authoring judgement; rationale generic — refine on review")
            else:
                lab = next(t for t in STUBS if t[0] == x)[2]
                add(c["id"], x, "related", f"Cross-subject connection to {lab}.", "authoring judgement; target page not yet authored")
    for (a, b), why in RATIONALE.items():
        a = a if a.split("-")[0] in PREFIXES else f"polity-{a}"; b = b if b.split("-")[0] in PREFIXES else f"polity-{b}"
        assert a in ids and b in ids, (a, b)
        add(a, b, "related", why, "authoring judgement (see Constitution / standard texts)")
    for c in CONCEPTS:
        for r in c["related"]:
            assert r in ids, (c["id"], r)
            if (c["id"], r, "related") not in seen and (r, c["id"], "related") not in seen:
                add(c["id"], r, "related", f"Topics are studied together: '{c['title']}' and '{next(x['title'] for x in CONCEPTS if x['id']==r)}'.", "authoring judgement; rationale generic — refine on review")
    return links


SUBJECTS = [
        dict(id="polity", title="Polity & Constitution", status="authored", papers=["Prelims GS-I", "Mains GS-II"], groups=[dict(id=g, title=t) for g, t in GROUPS]),
        dict(id="history", title="History & Culture", status="not-started", papers=["Prelims GS-I", "Mains GS-I"]),
        dict(id="geography", title="Geography", status="not-started", papers=["Prelims GS-I", "Mains GS-I"]),
        dict(id="society", title="Indian Society", status="not-started", papers=["Mains GS-I"]),
        dict(id="governance", title="Governance & Social Justice", status="not-started", papers=["Mains GS-II"]),
        dict(id="ir", title="International Relations", status="not-started", papers=["Mains GS-II"]),
        dict(id="economy", title="Economy & Agriculture", status="not-started", papers=["Prelims GS-I", "Mains GS-III"]),
        dict(id="environment", title="Environment & Ecology", status="not-started", papers=["Prelims GS-I", "Mains GS-III"]),
        dict(id="scitech", title="Science & Technology", status="not-started", papers=["Prelims GS-I", "Mains GS-III"]),
        dict(id="security", title="Security", status="not-started", papers=["Mains GS-III"]),
        dict(id="disaster", title="Disaster Management", status="not-started", papers=["Mains GS-III"]),
        dict(id="ethics", title="Ethics & GS-IV case studies", status="not-started", papers=["Mains GS-IV"]),
    ]


def main(out):
    os.makedirs(out, exist_ok=True)
    ids = [c["id"] for c in CONCEPTS]
    assert len(ids) == len(set(ids))
    rids = {r["id"] for r in RES}
    for c in CONCEPTS:
        c["resource_ids"] = list(dict.fromkeys(c["resource_ids"]))
        for r in c["resource_ids"]:
            assert r in rids, (c["id"], r)
    subjects = SUBJECTS
    stubs = [dict(id=i, subject=s, title=t, status="planned-not-authored") for i, s, t in STUBS]
    links = build_links()
    for name, obj in [("concepts", CONCEPTS), ("resources", RES), ("concept_links", links), ("subjects", subjects), ("concept_stubs", stubs)]:
        json.dump(obj, open(os.path.join(out, name + ".json"), "w"), ensure_ascii=False, indent=1)
    print(len(CONCEPTS), "concepts;", len(RES), "resources;", len(links), "links")


if __name__ == "__main__":
    main(sys.argv[1])
