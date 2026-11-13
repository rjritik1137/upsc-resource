"""Phase D batch 1: Economy, Geography, Environment, Modern History concepts (authoring source).

Same rules as author_polity.py: AI-written from general knowledge, `draft-unreviewed`, no book chapters,
no statistics. Imported by author_all.py (not run directly). Keywords drive the *proposed* PYQ links.
"""
import author_polity as P

CONST = "R-CONST"
NEW_RES = [
    dict(id="R-SURVEY", title="Economic Survey (annual)", author="Ministry of Finance, Govt. of India", type="official-primary", url="https://www.indiabudget.gov.in/economicsurvey/", access="free-online", url_status="http-200"),
    dict(id="R-BUDGET", title="Union Budget documents", author="Ministry of Finance, Govt. of India", type="official-primary", url="https://www.indiabudget.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-RBI", title="Reserve Bank of India (publications, FAQs, monetary policy statements)", author="RBI", type="official-primary", url="https://www.rbi.org.in/", access="free-online", url_status="http-200"),
    dict(id="R-SEBI", title="SEBI (investor education and regulations)", author="SEBI", type="official-primary", url="https://www.sebi.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-NITI", title="NITI Aayog", author="Govt. of India", type="official-primary", url="https://niti.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-AGRI", title="Ministry of Agriculture & Farmers Welfare", author="Govt. of India", type="official-primary", url="https://agriwelfare.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-WTO", title="World Trade Organization (agreements explained)", author="WTO", type="official-primary", url="https://www.wto.org/", access="free-online", url_status="http-200"),
    dict(id="R-PIB", title="Press Information Bureau (backgrounders)", author="Govt. of India", type="official-primary", url="https://pib.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-RSINGH", title="Indian Economy", author="Ramesh Singh", publisher="McGraw Hill", edition="not verified", type="standard-book", url=None, access="purchase", url_status="n/a"),
    dict(id="R-IMD", title="India Meteorological Department", author="IMD", type="official-primary", url="https://mausam.imd.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-SOI", title="Survey of India", author="Survey of India", type="official-primary", url="https://surveyofindia.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-CENSUS", title="Census of India", author="Office of the Registrar General & Census Commissioner", type="official-primary", url="https://censusindia.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-LEONG", title="Certificate Physical and Human Geography", author="G.C. Leong", publisher="Oxford University Press", edition="not verified", type="standard-book", url=None, access="purchase", url_status="n/a"),
    dict(id="R-ISRO", title="ISRO", author="Indian Space Research Organisation", type="official-primary", url="https://www.isro.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-MOEF", title="Ministry of Environment, Forest and Climate Change", author="Govt. of India", type="official-primary", url="https://moef.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-CPCB", title="Central Pollution Control Board", author="CPCB", type="official-primary", url="https://cpcb.nic.in/", access="free-online", url_status="http-200"),
    dict(id="R-IPCC", title="IPCC assessment reports", author="IPCC", type="official-primary", url="https://www.ipcc.ch/", access="free-online", url_status="http-200"),
    dict(id="R-CBD", title="Convention on Biological Diversity", author="CBD Secretariat", type="official-primary", url="https://www.cbd.int/", access="free-online", url_status="http-200"),
    dict(id="R-UNFCCC", title="UNFCCC", author="UNFCCC Secretariat", type="official-primary", url="https://unfccc.int/", access="free-online", url_status="http-200"),
    dict(id="R-SPECTRUM", title="A Brief History of Modern India", author="Rajiv Ahir (verify authorship on the edition)", publisher="Spectrum Books", edition="not verified", type="standard-book", url=None, access="purchase", url_status="n/a"),
    dict(id="R-NARCH", title="National Archives of India", author="Govt. of India", type="official-primary", url="https://www.nationalarchives.nic.in/", access="free-online", url_status="http-200"),
]
for r in NEW_RES:
    r["last_checked"] = P.CHECKED
    r.setdefault("publisher", None); r.setdefault("edition", None)
P.RES.extend(NEW_RES)

GROUPS = {
    "economy": [("A", "Growth, prices and development"), ("B", "Money, banking and markets"), ("C", "Government finance and the external sector"), ("D", "Agriculture and rural economy"), ("E", "Industry and infrastructure")],
    "geography": [("A", "The Earth: interior, landforms, space"), ("B", "Atmosphere and oceans"), ("C", "India: physical geography"), ("D", "Resources, agriculture and industry"), ("E", "Human and political geography")],
    "environment": [("A", "Ecology foundations"), ("B", "Biodiversity and conservation"), ("C", "Pollution and climate"), ("D", "Law, governance and international regimes")],
    "history": [("A", "Colonial consolidation"), ("B", "Colonial economy and society"), ("C", "Nationalism and the freedom struggle"), ("D", "Constitutional steps and independence")],
}


def X(subj, cid, grp, title, definition, subs, dist, prereq, found, mains, hrs, syl, kw, res, cross=(), related=(), cross_ids=()):
    P.CONCEPTS.append(dict(
        id=f"{subj}-{cid}", subject=subj, group=grp, title=title, definition=definition, subconcepts=subs, distinctions=dist,
        prerequisites=[p if p.count("-") and p.split("-")[0] in P.PREFIXES else f"{subj}-{p}" for p in prereq],
        foundation_focus=found, mains_focus=mains, effort_hours_editorial=hrs, syllabus_ids=list(syl), keywords=list(kw),
        resource_ids=list(res), constitution_locator=None, cross_subject=list(cross) + list(cross_ids),
        related=[r if r.split("-")[0] in P.PREFIXES else f"{subj}-{r}" for r in related],
        review_status="draft-unreviewed", confidence="medium"))


# ================================================================== ECONOMY
E = "economy"
X(E, "economic-reforms-1991", "A", "Economic planning, 1991 reforms and NITI Aayog",
  "India's move from centrally directed Five-Year Plans to a market-oriented economy after 1991, and the replacement of the Planning Commission by NITI Aayog (2015).",
  ["Planned development: Five-Year Plans and their emphasis", "Mahalanobis model, public-sector-led industrialisation", "1991 balance-of-payments crisis", "Liberalisation, privatisation, globalisation", "Industrial licensing abolition and FERA to FEMA", "Planning Commission vs NITI Aayog", "National Development Council", "Cooperative federalism role of NITI Aayog"],
  ["Planning Commission (allocative, Plan-based) vs NITI Aayog (think tank, no fund allocation)", "Liberalisation vs privatisation vs globalisation"],
  [], "Know the sequence: plans, crisis, reforms, NITI Aayog.", "Evaluate the effects of liberalisation on growth, industry and inequality.", 4,
  ["S-GS3-01", "S-GS3-08", "S-P1-05"], [r"Five[- ]Year Plan", r"Planning Commission", r"NITI Aayog", r"liberali[sz]ation", r"1991", r"economic reforms", r"Mahalanobis", r"licen[cs]ing", r"National Development Council"], ["R-RSINGH", "R-NCERT", "R-NITI", "R-SURVEY"], related=["polity-finance-commission-fiscal-federalism"])
X(E, "national-income-growth", "A", "National income and economic growth",
  "How the size and growth of an economy is measured (GDP, GNP, GVA and related aggregates) and the concepts needed to read growth data.",
  ["GDP, GNP, NDP, NNP", "Gross value added vs GDP at market prices", "Factor cost vs market prices", "Nominal vs real; base year; GDP deflator", "Per-capita income", "Purchasing power parity", "Sectoral composition (primary, secondary, tertiary)", "Demographic dividend and potential growth"],
  ["GDP vs GNP", "GVA vs GDP (net product taxes)", "Nominal vs real GDP"],
  [], "Definitions and the accounting identities.", "Discuss sources of growth, jobless growth and inclusiveness.", 4,
  ["S-GS3-01", "S-GS3-02", "S-P1-05"], [r"\bGDP\b", r"\bGNP\b", r"national income", r"gross value added", r"\bGVA\b", r"per[- ]capita income", r"purchasing power parity", r"economic growth", r"base year", r"factor cost"], ["R-RSINGH", "R-NCERT", "R-SURVEY"], related=["inflation-price-indices", "human-development-poverty-employment"])
X(E, "inflation-price-indices", "A", "Inflation and price indices",
  "Sustained rise in the general price level, how it is measured, and how policy responds.",
  ["CPI vs WPI", "Types: demand-pull, cost-push, structural", "Deflation, disinflation, reflation, stagflation", "Base effect", "Core vs headline inflation", "Flexible inflation targeting and the Monetary Policy Committee", "Effects on savers, borrowers, exports", "Supply-side measures (buffer stocks, imports)"],
  ["CPI vs WPI", "Demand-pull vs cost-push", "Deflation vs disinflation"],
  ["national-income-growth"], "Indices, causes and types.", "Evaluate monetary vs supply-side responses to food inflation.", 3,
  ["S-GS3-01", "S-P1-05"], [r"inflation", r"consumer price", r"wholesale price", r"\bCPI\b", r"\bWPI\b", r"deflation", r"stagflation", r"base effect", r"price (index|indices)"], ["R-RSINGH", "R-RBI", "R-SURVEY"], related=["money-supply-monetary-policy"])
X(E, "human-development-poverty-employment", "A", "Human development, poverty and employment",
  "Measures and policies concerning living standards, poverty, inequality, employment and social-sector schemes.",
  ["Poverty line and poverty estimation committees", "Multidimensional poverty index", "Human Development Index components", "Unemployment concepts: open, disguised, seasonal, structural", "Employment guarantee and skill schemes", "Gini coefficient and inequality", "Inclusive growth", "Informal sector and labour codes"],
  ["Absolute vs relative poverty", "Disguised vs seasonal unemployment", "HDI vs MPI"],
  ["national-income-growth"], "Definitions, indices and flagship schemes.", "Critically assess welfare delivery and the link between growth and poverty reduction.", 4,
  ["S-GS3-02", "S-GS3-01", "S-P1-05"], [r"poverty", r"Human Development", r"unemployment", r"employment", r"MGNREGA|Mahatma Gandhi National Rural", r"Gini", r"inclusive growth", r"multidimensional", r"inequality", r"skill", r"labour code"], ["R-RSINGH", "R-NCERT", "R-SURVEY", "R-NITI"], cross=["xs-society-social-justice"], related=["agriculture-rural-development"])
X(E, "money-supply-monetary-policy", "B", "Money supply and monetary policy",
  "How the central bank influences money, credit and prices using policy rates and reserve requirements.",
  ["Money aggregates M0 to M3", "Repo, reverse repo, marginal standing facility, bank rate", "CRR and SLR", "Open market operations and liquidity adjustment facility", "Monetary Policy Committee", "Transmission of policy rates", "Quantitative vs qualitative tools", "Money multiplier"],
  ["Repo vs reverse repo", "CRR vs SLR", "Monetary vs fiscal policy"],
  ["inflation-price-indices"], "Instruments and what each does to liquidity.", "Assess the limits of monetary policy against supply-driven inflation.", 4,
  ["S-GS3-01", "S-P1-05"], [r"\brepo\b", r"reverse repo", r"\bCRR\b|cash reserve ratio", r"\bSLR\b|statutory liquidity ratio", r"monetary policy", r"money supply", r"open market operation", r"Monetary Policy Committee", r"bank rate", r"marginal standing facility", r"\bM[0-3]\b"], ["R-RSINGH", "R-RBI"], related=["banking-structure"])
X(E, "banking-structure", "B", "Banking structure and the RBI",
  "The institutions of the banking system, the RBI's roles, and issues such as bad loans and resolution.",
  ["RBI functions: issuer, banker, regulator, FX manager", "Scheduled commercial, regional rural, cooperative banks", "Small finance and payments banks", "NBFCs and shadow banking", "NPAs, Insolvency and Bankruptcy Code", "Basel norms and capital adequacy", "Bank nationalisation and consolidation", "Priority sector lending"],
  ["Commercial bank vs NBFC", "Payments bank vs small finance bank", "NPA vs written-off loan"],
  ["money-supply-monetary-policy"], "Types of banks and the RBI's functions.", "Discuss NPA resolution, governance of public-sector banks and financial stability.", 4,
  ["S-GS3-01", "S-P1-05"], [r"Reserve Bank", r"\bRBI\b", r"\bNPA\b|non[- ]performing", r"\bNBFC", r"commercial bank", r"payments? bank", r"small finance bank", r"Basel", r"Insolvency and Bankruptcy", r"regional rural bank", r"co-?operative bank", r"priority sector"], ["R-RSINGH", "R-RBI"], related=["financial-inclusion-digital-payments"])
X(E, "financial-markets", "B", "Financial markets and SEBI",
  "Markets for money, debt and equity, their instruments, and regulation.",
  ["Money market instruments (T-bills, commercial paper, certificates of deposit)", "Capital market: primary and secondary", "Equity, bonds, debentures, mutual funds", "Derivatives: futures and options", "SEBI's role", "FPI vs FDI", "Stock exchanges and indices", "Sovereign and green bonds"],
  ["Primary vs secondary market", "Money market vs capital market", "Futures vs options"],
  ["banking-structure"], "Instruments and who regulates them.", "Assess the effect of foreign portfolio flows on stability.", 3,
  ["S-GS3-01", "S-GS3-10", "S-P1-05"], [r"\bSEBI\b", r"capital market", r"money market", r"mutual fund", r"derivative", r"stock exchange", r"Sensex|Nifty", r"treasury bill", r"commercial paper", r"\bbond", r"debenture", r"portfolio investment|\bFPI\b", r"initial public offer"], ["R-RSINGH", "R-SEBI", "R-RBI"], related=["external-sector-bop"])
X(E, "financial-inclusion-digital-payments", "B", "Financial inclusion and digital payments",
  "Policies and technology that extend banking, credit, insurance and payment services to all.",
  ["Jan Dhan Yojana and direct benefit transfer", "UPI and NPCI", "RTGS, NEFT, IMPS", "Central bank digital currency", "Microfinance and self-help groups", "Insurance and pension penetration", "Aadhaar-enabled services", "Cybersecurity and digital-payment risks"],
  ["Financial inclusion vs financial literacy", "UPI vs RTGS/NEFT"],
  ["banking-structure"], "Schemes and systems.", "Evaluate gains and risks of digital finance for rural and vulnerable users.", 2,
  ["S-GS3-02", "S-P1-05"], [r"Jan Dhan", r"\bUPI\b|Unified Payments", r"\bNPCI\b", r"financial inclusion", r"digital (payment|currency)", r"\bCBDC\b|Central Bank Digital", r"\bRTGS\b|\bNEFT\b", r"microfinance", r"self[- ]help group", r"direct benefit transfer"], ["R-RBI", "R-SURVEY", "R-PIB"], related=["human-development-poverty-employment"])
X(E, "fiscal-policy-budget", "C", "Fiscal policy and the budget",
  "How the government raises and spends money, the deficit measures, and the legal framework for fiscal discipline.",
  ["Revenue vs capital receipts and expenditure", "Fiscal, revenue, effective revenue and primary deficits", "FRBM Act and fiscal rules", "Budget documents", "Public debt", "Subsidies and their rationalisation", "Outcome budget, zero-based budgeting, gender budgeting", "Fiscal multiplier and crowding out"],
  ["Fiscal deficit vs primary deficit vs revenue deficit", "Plan vs non-plan (historical)", "Direct vs indirect taxes"],
  ["national-income-growth"], "Definitions and the formulas for each deficit.", "Evaluate fiscal consolidation against growth and welfare needs.", 5,
  ["S-GS3-03", "S-GS3-01", "S-P1-05"], [r"fiscal deficit", r"revenue deficit", r"primary deficit", r"\bFRBM\b|Fiscal Responsibility", r"\bbudget", r"public debt", r"subsid", r"capital expenditure", r"revenue (receipts|expenditure)", r"fiscal policy", r"outcome budget", r"gender budget"], ["R-RSINGH", "R-BUDGET", "R-SURVEY"], cross_ids=["polity-budget-financial-control"], related=["taxation"])
X(E, "taxation", "C", "Taxation and GST",
  "Types of taxes, the structure of Union and state taxation, and the Goods and Services Tax framework.",
  ["Direct vs indirect taxes", "Progressive, proportional and regressive taxes", "GST: CGST, SGST, IGST and UTGST", "GST Council", "Cesses and surcharges", "Tax buoyancy; tax-GDP ratio", "Customs and excise", "Black money, tax evasion vs avoidance"],
  ["Direct vs indirect tax", "Cess vs surcharge", "Tax evasion vs avoidance"],
  ["fiscal-policy-budget"], "Know the taxes and the GST design.", "Assess GST outcomes and Centre-State fiscal tension.", 3,
  ["S-GS3-03", "S-P1-05"], [r"\bGST\b|Goods and Services Tax", r"direct tax", r"indirect tax", r"progressive tax", r"income tax", r"customs duty", r"excise", r"\bcess\b", r"surcharge", r"tax[- ]GDP", r"tax evasion", r"black money"], ["R-RSINGH", "R-BUDGET", "R-SURVEY"], cross_ids=["polity-finance-commission-fiscal-federalism"], related=["fiscal-policy-budget"])
X(E, "external-sector-bop", "C", "External sector and balance of payments",
  "India's transactions with the rest of the world: BoP accounts, exchange rates, reserves and capital flows.",
  ["Current account vs capital account", "Current account deficit and its financing", "Foreign exchange reserves", "Exchange-rate regimes: fixed, floating, managed", "Convertibility of the rupee", "FDI, FPI, external commercial borrowings", "Nominal vs real effective exchange rate", "Remittances and invisibles"],
  ["Current account vs capital account", "FDI vs FPI", "Devaluation vs depreciation"],
  ["national-income-growth"], "BoP components and exchange-rate terms.", "Analyse causes and risks of a widening current account deficit.", 4,
  ["S-GS3-01", "S-GS3-10", "S-P1-05"], [r"balance of payments", r"current account", r"capital account", r"forex|foreign exchange", r"exchange rate", r"\bFDI\b|foreign direct investment", r"depreciation", r"devaluation", r"rupee", r"external commercial borrowing", r"remittance", r"convertib"], ["R-RSINGH", "R-RBI", "R-SURVEY"], related=["international-trade-wto"])
X(E, "international-trade-wto", "C", "International trade and the WTO",
  "The rules and institutions of international trade and India's trade policy.",
  ["WTO agreements: GATT, GATS, TRIPS, AoA, TRIMS", "Most-favoured-nation and national treatment", "Tariff and non-tariff barriers", "Dumping, anti-dumping and countervailing duty", "Free-trade and regional agreements", "Special economic zones and export promotion", "Doha Round and agricultural subsidies disputes", "Trade deficit and terms of trade"],
  ["Tariff vs non-tariff barrier", "Anti-dumping vs countervailing duty", "Bilateral vs regional vs multilateral agreements"],
  ["external-sector-bop"], "Agreements and principles.", "Discuss India's stand on agriculture subsidies and public stockholding at the WTO.", 3,
  ["S-GS3-01", "S-GS3-08", "S-P1-05"], [r"\bWTO\b|World Trade Organi[sz]ation", r"\bGATT\b", r"\bTRIPS\b", r"Agreement on Agriculture", r"anti-dumping", r"countervailing", r"free trade agreement|\bFTA\b", r"most[- ]favoured", r"\bSEZ\b|special economic zone", r"Doha", r"tariff", r"trade deficit", r"export"], ["R-RSINGH", "R-WTO", "R-SURVEY"], related=["external-sector-bop"])
X(E, "international-economic-institutions", "C", "International economic institutions and reports",
  "Multilateral financial institutions and the major reports and indices they publish.",
  ["IMF: functions, quotas, special drawing rights", "World Bank Group", "Asian Development Bank, AIIB, New Development Bank", "BIS and Basel Committee", "Reports and indices that regularly appear in exams (published by which body)", "BRICS and G20 economic tracks", "India's membership and quota"],
  ["IMF vs World Bank", "AIIB vs NDB"],
  ["external-sector-bop"], "Which institution does what, and which report belongs to whom.", "Discuss reform of global economic governance.", 2,
  ["S-GS3-01", "S-P1-05"], [r"\bIMF\b|International Monetary Fund", r"World Bank", r"Asian Development Bank", r"\bAIIB\b|Asian Infrastructure Investment", r"New Development Bank", r"Special Drawing Right", r"\bSDR\b", r"World Economic Forum", r"Human Development Report", r"Global (Hunger|Competitiveness|Innovation)", r"\bG20\b|\bBRICS\b"], ["R-RSINGH", "R-PIB"], related=["international-trade-wto"])
X(E, "agriculture-rural-development", "D", "Agriculture, food security and rural development",
  "Cropping patterns, irrigation, support prices, subsidies, public distribution and land reforms.",
  ["Kharif, rabi and zaid crops", "Irrigation sources and methods", "Minimum support price and procurement", "Public Distribution System and National Food Security Act", "Buffer stocks", "Fertiliser and power subsidies", "Land reforms: zamindari abolition, tenancy, ceilings", "Agricultural markets: APMC, e-NAM", "Cooperatives and farmer producer organisations", "Food processing"],
  ["MSP vs procurement price vs issue price", "Land ceiling vs tenancy reform"],
  ["human-development-poverty-employment"], "Terms, schemes and institutions.", "Evaluate MSP, subsidies and market reforms in the context of farmer income and food security.", 6,
  ["S-GS3-04", "S-GS3-05", "S-GS3-06", "S-GS3-07", "S-P1-05"], [r"minimum support price|\bMSP\b", r"Public Distribution System|\bPDS\b", r"food security", r"agricultur", r"irrigation", r"kharif|rabi", r"land reform", r"\bAPMC\b|e-NAM", r"farmer", r"fertili[sz]er", r"food processing", r"cooperative"], ["R-RSINGH", "R-NCERT", "R-AGRI", "R-SURVEY"], cross_ids=["geography-indian-agriculture-land-use"], related=["human-development-poverty-employment"])
X(E, "industry-infrastructure", "E", "Industry and infrastructure",
  "Industrial policy, MSMEs and the infrastructure sectors that support growth.",
  ["Industrial policy since 1991", "MSME classification and support", "Production-linked incentives and Make in India", "Energy sector: coal, power, renewables", "Ports, roads, railways, airports", "Public-private partnership and investment models", "Special economic zones and industrial corridors", "Logistics policy"],
  ["Public vs private vs PPP projects", "Large industry vs MSME"],
  ["economic-reforms-1991"], "Policies and sector basics.", "Assess constraints on manufacturing growth and infrastructure financing.", 5,
  ["S-GS3-08", "S-GS3-09", "S-GS3-10", "S-P1-05"], [r"\bMSME|micro, small and medium", r"industrial policy", r"Make in India", r"production[- ]linked", r"infrastructure", r"public[- ]private partnership|\bPPP\b", r"\bport", r"railway", r"airport", r"highway|National Highway", r"power sector|electricity", r"industrial corridor", r"logistics"], ["R-RSINGH", "R-SURVEY", "R-NITI"], related=["economic-reforms-1991"])

# ================================================================== GEOGRAPHY
G = "geography"
X(G, "earth-structure-geomorphology", "A", "Earth's interior, plate tectonics and landforms",
  "The structure and materials of the Earth and the processes that shape landforms.",
  ["Layers: crust, mantle, core", "Continental drift and plate tectonics", "Plate boundaries and associated landforms", "Rocks: igneous, sedimentary, metamorphic", "Weathering and erosion", "Fluvial, glacial, aeolian, coastal landforms", "Mountains, plateaus, plains", "Isostasy and geomorphic cycles"],
  ["Weathering vs erosion", "Convergent vs divergent vs transform boundaries"],
  [], "Layers, plates and rock types.", "Explain a landform or hazard by linking it to plate tectonics.", 5,
  ["S-GS1-10", "S-P1-03"], [r"plate tectonic", r"continental drift", r"\bmantle\b", r"earth.s (interior|crust)", r"igneous|sedimentary|metamorphic", r"weathering", r"erosion", r"landform", r"geomorpholog", r"glacier", r"\bcore\b.*earth"], ["R-NCERT", "R-LEONG"], related=["geophysical-hazards"])
X(G, "astronomy-earth-sun", "A", "Earth-Sun system, latitudes, longitudes and time",
  "Motions of the Earth, seasons, eclipses, coordinates and time zones.",
  ["Rotation and revolution", "Seasons and the inclination of the axis", "Equinoxes and solstices", "Latitude, longitude, Indian Standard Time", "International Date Line", "Solar and lunar eclipses", "Tides in relation to Sun and Moon", "Solar system bodies"],
  ["Rotation vs revolution", "Solar vs lunar eclipse"],
  [], "Definitions and the causes of seasons and time differences.", "Use geography reasoning for questions on day length, seasons and time.", 3,
  ["S-GS1-10", "S-P1-03"], [r"solstice", r"equinox", r"latitude", r"longitude", r"time zone|Standard Time", r"eclipse", r"revolution of the Earth|rotation of the Earth", r"Tropic of Cancer", r"International Date Line", r"solar system", r"perihelion|aphelion"], ["R-NCERT", "R-LEONG"], related=["atmosphere-climatology"])
X(G, "atmosphere-climatology", "B", "Atmosphere and climatology",
  "Composition and structure of the atmosphere, heat balance, pressure, winds, cyclones and climate classification.",
  ["Layers of the atmosphere", "Insolation and heat budget", "Pressure belts and planetary winds", "Jet streams", "Air masses and fronts", "Tropical and temperate cyclones", "Humidity, clouds, precipitation types", "Climate types (Koeppen)", "El Nino, La Nina and ENSO", "Greenhouse effect and ozone layer"],
  ["Weather vs climate", "Tropical vs temperate cyclone", "Convectional vs orographic vs cyclonic rainfall"],
  ["astronomy-earth-sun"], "Structure, belts and wind systems.", "Explain regional climates and extreme events with causes.", 6,
  ["S-GS1-10", "S-GS1-12", "S-P1-03"], [r"atmospher", r"troposphere|stratosphere|mesosphere|ionosphere", r"jet stream", r"cyclone", r"El Ni[nñ]o|La Ni[nñ]a|\bENSO\b", r"pressure belt", r"trade wind|westerlies", r"insolation", r"rainfall|precipitation", r"humidity", r"Koeppen", r"ozone", r"front(s)?\b"], ["R-NCERT", "R-LEONG", "R-IMD"], related=["indian-monsoon-climate", "oceanography"])
X(G, "oceanography", "B", "Oceanography",
  "Ocean relief, water properties, circulation, tides and marine resources.",
  ["Ocean floor relief", "Temperature and salinity distribution", "Ocean currents and their causes", "Warm vs cold currents and climatic effects", "Tides: spring and neap", "Coral reefs and mangroves", "Marine resources, EEZ", "Sea-level change"],
  ["Waves vs tides vs currents", "Spring vs neap tide"],
  ["atmosphere-climatology"], "Relief, currents and tides.", "Link currents to climate, fisheries and trade routes.", 3,
  ["S-GS1-10", "S-P1-03"], [r"ocean current", r"\btide", r"salinity", r"ocean (floor|relief)", r"Gulf Stream|Kuroshio|Humboldt|Benguela|Agulhas", r"coral", r"continental shelf", r"Exclusive Economic Zone|\bEEZ\b", r"sea[- ]level", r"oceanograph", r"thermocline"], ["R-NCERT", "R-LEONG"], related=["atmosphere-climatology"])
X(G, "indian-physical-geography", "C", "Physical features of India",
  "The Himalayas, northern plains, peninsular plateau, coastal plains, islands and desert.",
  ["Himalayan ranges and divisions", "Northern plains: bhabar, terai, bhangar, khadar", "Peninsular plateau and Western and Eastern Ghats", "Coastal plains of the west and east", "Thar desert", "Island groups: Andaman and Nicobar, Lakshadweep", "Passes and peaks", "Geological history of the subcontinent"],
  ["Western Ghats vs Eastern Ghats", "Bhangar vs khadar"],
  ["earth-structure-geomorphology"], "Features, names and locations.", "Explain how relief shapes climate, rivers and settlement.", 4,
  ["S-P1-03", "S-GS1-10"], [r"Himalaya", r"Western Ghats", r"Eastern Ghats", r"Deccan", r"peninsular", r"Thar", r"coastal plain", r"Andaman|Nicobar|Lakshadweep", r"northern plains", r"\bpass(es)?\b", r"Shivalik|Himadri|Himachal ranges", r"bhabar|terai"], ["R-NCERT", "R-LEONG"], related=["rivers-water-resources", "indian-monsoon-climate"])
X(G, "indian-monsoon-climate", "C", "Indian monsoon and climate",
  "The mechanism, onset, variability and regional effects of the Indian monsoon.",
  ["Seasons of India", "Mechanism: differential heating, ITCZ, jet streams", "Onset and retreat; Western Disturbances", "Role of El Nino and Indian Ocean Dipole", "Distribution of rainfall; rain shadow", "Monsoon breaks and variability", "Climate regions of India", "Monsoon and agriculture"],
  ["Southwest vs northeast monsoon", "El Nino vs Indian Ocean Dipole"],
  ["atmosphere-climatology", "indian-physical-geography"], "Mechanism and seasons.", "Explain how monsoon variability links to agriculture, floods and the economy.", 4,
  ["S-P1-03", "S-GS1-10"], [r"monsoon", r"Western Disturbance", r"\bITCZ\b|Inter[- ]Tropical Convergence", r"Indian Ocean Dipole", r"rain[- ]shadow", r"retreating monsoon", r"north[- ]?east monsoon", r"Mawsynram|Cherrapunji"], ["R-NCERT", "R-IMD", "R-LEONG"], cross_ids=["economy-agriculture-rural-development"], related=["rivers-water-resources"])
X(G, "rivers-water-resources", "C", "Rivers, drainage and water resources",
  "River systems of India, their features, disputes and water-resource management.",
  ["Himalayan vs peninsular rivers", "Indus, Ganga and Brahmaputra systems", "Major peninsular rivers and west-flowing rivers", "Drainage patterns", "Dams, multipurpose projects and barrages", "River-linking proposals", "Inter-state and international water disputes", "Groundwater, water stress and conservation"],
  ["Himalayan vs peninsular rivers", "Delta vs estuary", "Dam vs barrage"],
  ["indian-physical-geography"], "Rivers, tributaries and projects.", "Discuss water disputes, interlinking and groundwater depletion.", 5,
  ["S-P1-03", "S-GS1-11"], [r"river", r"tributar", r"Ganga|Ganges|Brahmaputra|Indus|Godavari|Krishna|Kaveri|Narmada|Mahanadi", r"\bdam\b|barrage|multipurpose", r"drainage", r"river[- ]linking|interlinking", r"water (dispute|stress|resources)", r"groundwater", r"watershed", r"Indus Waters"], ["R-NCERT", "R-LEONG"], cross_ids=["polity-inter-state-relations"], related=["indian-monsoon-climate"])
X(G, "biogeography-soils-vegetation", "D", "Soils and natural vegetation",
  "Soil types and formation, and the natural vegetation zones of India and the world.",
  ["Soil formation and profile", "Alluvial, black, red, laterite, desert, mountain soils", "Soil erosion and conservation", "Forest types of India", "World biomes", "Mangroves and alpine vegetation", "Relation of soils and vegetation to climate"],
  ["Black vs red vs laterite soil", "Tropical evergreen vs deciduous forest"],
  ["indian-monsoon-climate"], "Soil and vegetation types and where they occur.", "Link soil and vegetation to cropping patterns and conservation.", 3,
  ["S-P1-03", "S-GS1-11"], [r"\bsoil", r"alluvial", r"laterite", r"black soil|regur", r"natural vegetation", r"tropical (evergreen|deciduous|thorn)", r"mangrove", r"biome", r"savanna|taiga|tundra|steppe"], ["R-NCERT", "R-LEONG"], related=["indian-agriculture-land-use"])
X(G, "indian-agriculture-land-use", "D", "Indian agriculture: geography of crops and land use",
  "Where and why crops are grown, land-use categories and agro-climatic regions.",
  ["Land-use classification", "Cropping seasons and major crops by region", "Irrigation geography", "Green Revolution regions", "Plantation and cash crops", "Agro-climatic regions", "Dryland farming and shifting cultivation", "Constraints: fragmentation, soil degradation"],
  ["Net sown area vs gross cropped area", "Intensive vs extensive farming"],
  ["biogeography-soils-vegetation"], "Crops, regions and seasons.", "Explain regional patterns of cropping and agrarian issues.", 4,
  ["S-P1-03", "S-GS3-04"], [r"cropping pattern", r"net sown area|gross cropped", r"Green Revolution", r"shifting cultivation|jhum", r"plantation", r"tea|coffee|rubber|jute|cotton|sugarcane", r"millet", r"agro-climatic", r"land use"], ["R-NCERT", "R-LEONG", "R-AGRI"], cross_ids=["economy-agriculture-rural-development"], related=["biogeography-soils-vegetation"])
X(G, "minerals-industries-location", "D", "Minerals, energy resources and industrial location",
  "Distribution of key minerals and energy resources and factors that decide where industries locate.",
  ["Iron ore, coal, bauxite, mica, manganese, copper distribution", "Petroleum and natural gas basins", "Power resources", "Weber's and other location factors", "Major industrial regions of India and the world", "Iron and steel, cotton textile, sugar, cement", "Resource curse and sustainability", "Strategic and critical minerals"],
  ["Renewable vs non-renewable resources", "Raw-material vs market-oriented industries"],
  ["indian-physical-geography"], "Where key resources occur.", "Explain location of an industry or resource and issues of extraction.", 5,
  ["S-GS1-11", "S-P1-03"], [r"mineral", r"iron ore|bauxite|manganese|mica|copper|coal", r"petroleum|crude oil|natural gas", r"industrial (region|location)", r"iron and steel", r"cotton textile", r"location of industr", r"rare earth", r"coalfield"], ["R-NCERT", "R-LEONG", "R-SURVEY"], cross_ids=["economy-industry-infrastructure"], related=["transport-infrastructure-geography"])
X(G, "population-demography-urbanisation", "E", "Population, demography and urbanisation",
  "Census concepts, population distribution and change, migration and urban growth.",
  ["Census terms: density, sex ratio, literacy", "Demographic transition", "Birth, death and fertility rates", "Age structure and demographic dividend", "Migration types and causes", "Urban agglomeration and census town", "Slums and urban problems", "Population policy"],
  ["Birth rate vs fertility rate", "Urban agglomeration vs census town"],
  [], "Definitions and data trends.", "Link population change to resources, urbanisation and policy.", 3,
  ["S-P1-03", "S-GS1-07"], [r"census", r"sex ratio", r"population density|density of population", r"demograph", r"fertility rate", r"birth rate|death rate", r"migration", r"urbani[sz]ation|urban agglomeration", r"literacy", r"age structure", r"slum"], ["R-NCERT", "R-CENSUS"], cross_ids=["xs-society-social-justice"], related=["transport-infrastructure-geography"])
X(G, "transport-infrastructure-geography", "E", "Transport networks, ports and chokepoints",
  "Geography of roads, railways, waterways, ports and strategic sea routes.",
  ["National highway network and corridors", "Railway zones and freight corridors", "Inland waterways", "Major and minor ports of India", "Air transport hubs", "Straits and canals (Suez, Panama, Malacca, Hormuz)", "Sea lanes and trade routes", "Pipelines"],
  ["Major vs minor ports", "Strait vs canal"],
  ["indian-physical-geography"], "Locations and names.", "Explain strategic and economic importance of routes and ports.", 3,
  ["S-P1-03", "S-GS3-09"], [r"\bport", r"railway", r"national highway", r"inland waterway", r"Suez|Panama|Malacca|Hormuz|Bosphorus|Bab[- ]el[- ]Mandeb", r"\bstrait", r"sea route|shipping", r"freight corridor", r"airport"], ["R-NCERT", "R-SOI"], cross_ids=["economy-industry-infrastructure"], related=["minerals-industries-location"])
X(G, "world-political-geography-borders", "E", "World political geography and borders",
  "Countries, capitals, boundaries, seas and recurring border questions in the news.",
  ["Continents and countries bordering key waters", "Boundary lines and disputes", "India's neighbours and land borders", "Seas, gulfs and straits and bordering countries", "Landlocked countries", "Capitals and important cities", "Maps and map-based reasoning"],
  ["Boundary vs border vs frontier", "Landlocked vs coastal"],
  [], "Locate countries and water bodies.", "Use maps to analyse geopolitical questions.", 3,
  ["S-P1-03", "S-GS1-10"], [r"border", r"boundary", r"borders? (with|on)", r"landlocked", r"\bSea\b", r"Gulf of", r"countries? (are )?(share|bordering|located)", r"capital of", r"Radcliffe|Durand|McMahon"], ["R-NCERT", "R-LEONG", "R-SOI"], cross_ids=["xs-security-internal"], related=["transport-infrastructure-geography"])
X(G, "geophysical-hazards", "A", "Geophysical phenomena: earthquakes, volcanoes, tsunamis, cyclones",
  "Causes, distribution and effects of major natural hazards.",
  ["Earthquake waves, focus and epicentre, seismic zones of India", "Volcano types and distribution; Ring of Fire", "Tsunami generation and warning", "Cyclone formation and naming", "Floods, droughts, landslides", "Cloudburst and glacial lake outburst floods", "Mitigation and early warning"],
  ["Focus vs epicentre", "Active vs dormant vs extinct volcano"],
  ["earth-structure-geomorphology"], "Mechanisms and distribution.", "Link hazards to causes, vulnerability and disaster-management responses.", 4,
  ["S-GS1-12", "S-GS3-15", "S-P1-03"], [r"earthquake", r"seismic", r"volcan", r"tsunami", r"Ring of Fire", r"cyclone", r"landslide", r"cloudburst", r"glacial lake", r"flood", r"drought", r"epicentre|epicenter"], ["R-NCERT", "R-LEONG", "R-IMD"], related=["atmosphere-climatology"])

# ================================================================== ENVIRONMENT
V = "environment"
X(V, "ecosystem-ecology-basics", "A", "Ecosystem and ecology basics",
  "Structure and function of ecosystems: energy flow, food webs, succession and interactions.",
  ["Biotic and abiotic components", "Food chain, food web, trophic levels", "Ecological pyramids", "Energy flow and the ten per cent rule", "Primary productivity", "Ecological succession", "Niche, habitat, keystone species", "Species interactions: predation, competition, mutualism, commensalism, parasitism", "Ecotone and edge effect", "Terrestrial and aquatic ecosystems"],
  ["Food chain vs food web", "Habitat vs niche", "Primary vs secondary succession"],
  [], "Core terms and diagrams.", "Apply ecological concepts to conservation and human impacts.", 4,
  ["S-P1-06", "S-GS3-14"], [r"ecosystem", r"food (chain|web)", r"trophic", r"ecological pyramid", r"succession", r"\bniche\b", r"keystone", r"producer|decomposer", r"ecotone", r"commensalism|mutualism|parasitism", r"primary productivity"], ["R-NCERT", "R-MOEF"], related=["biogeochemical-cycles", "biodiversity-types-hotspots"])
X(V, "biogeochemical-cycles", "A", "Biogeochemical cycles",
  "The cycling of carbon, nitrogen, phosphorus, water and sulphur between living and non-living parts of the Earth.",
  ["Carbon cycle and sinks", "Nitrogen cycle: fixation, nitrification, denitrification", "Phosphorus cycle", "Water (hydrological) cycle", "Sulphur cycle", "Gaseous vs sedimentary cycles", "Human disturbance of cycles", "Eutrophication"],
  ["Gaseous vs sedimentary cycle", "Nitrification vs denitrification"],
  ["ecosystem-ecology-basics"], "Steps and organisms involved.", "Relate disturbed cycles to climate change and eutrophication.", 3,
  ["S-P1-06"], [r"carbon cycle", r"nitrogen (cycle|fixation)", r"phosphorus", r"hydrological cycle|water cycle", r"sulphur cycle", r"denitrif|nitrif", r"eutrophication", r"biogeochemical", r"carbon sink"], ["R-NCERT"], related=["climate-change-ghg"])
X(V, "biodiversity-types-hotspots", "B", "Biodiversity: types, hotspots and threat categories",
  "Levels of biodiversity, global and Indian hotspots, and how species are classified by extinction risk.",
  ["Genetic, species and ecosystem diversity", "Biodiversity hotspots and India's hotspots", "Endemism", "Threats: habitat loss, poaching, invasive species, human-wildlife conflict", "IUCN Red List categories", "In-situ vs ex-situ conservation", "Gene banks, seed banks, botanical and zoological gardens", "Keystone and flagship species"],
  ["In-situ vs ex-situ conservation", "Endangered vs vulnerable vs critically endangered", "Native vs invasive species"],
  ["ecosystem-ecology-basics"], "Terms, hotspots and Red List categories.", "Discuss pressures on biodiversity and conservation approaches.", 4,
  ["S-P1-06", "S-GS3-14"], [r"biodiversity", r"hotspot", r"endemi", r"IUCN", r"Red List", r"in[- ]situ|ex[- ]situ", r"invasive", r"endangered|vulnerable species|critically endangered", r"extinct", r"gene bank|seed bank", r"flagship"], ["R-NCERT", "R-MOEF", "R-CBD"], related=["protected-areas-wildlife"])
X(V, "protected-areas-wildlife", "B", "Protected areas and wildlife conservation",
  "National parks, sanctuaries, reserves and flagship species programmes.",
  ["National parks vs wildlife sanctuaries vs conservation and community reserves", "Tiger reserves and Project Tiger", "Biosphere reserves and the UNESCO list", "Elephant reserves and Project Elephant", "World Heritage natural sites", "Wildlife Protection Act 1972 schedules", "Critical wildlife habitats", "Eco-sensitive zones"],
  ["National park vs wildlife sanctuary", "Biosphere reserve vs national park", "Core vs buffer zone"],
  ["biodiversity-types-hotspots"], "Types of areas and what is allowed in each.", "Discuss human-wildlife conflict and rights of forest dwellers in protected areas.", 4,
  ["S-P1-06", "S-GS3-14"], [r"national park", r"wildlife sanctuar", r"tiger reserve", r"Project Tiger", r"biosphere reserve", r"elephant reserve|Project Elephant", r"Wildlife \(?Protection\)? Act", r"eco-?sensitive zone", r"conservation reserve|community reserve", r"world heritage", r"\bcore zone|buffer zone"], ["R-NCERT", "R-MOEF"], related=["environmental-governance-legislation"])
X(V, "wetlands-water-conservation", "B", "Wetlands, mangroves, coral reefs and water conservation",
  "Wetland types and conservation frameworks, and coastal and freshwater ecosystems.",
  ["Ramsar Convention and Ramsar sites in India", "Wetlands (Conservation and Management) Rules", "Mangrove ecosystems and coastal regulation zones", "Coral reefs and bleaching", "Lakes, estuaries, lagoons", "Water conservation methods", "Montreux Record", "Rainwater harvesting"],
  ["Estuary vs lagoon", "Ramsar site vs Montreux Record"],
  ["ecosystem-ecology-basics"], "Convention, sites and ecosystem types.", "Discuss threats to wetlands and coastal ecosystems and their services.", 3,
  ["S-P1-06", "S-GS3-14"], [r"Ramsar", r"wetland", r"mangrove", r"coral", r"Montreux", r"estuar|lagoon", r"Coastal Regulation Zone|\bCRZ\b", r"rainwater harvesting", r"Chilika|Loktak|Sambhar|Wular"], ["R-NCERT", "R-MOEF"], cross_ids=["geography-rivers-water-resources"], related=["protected-areas-wildlife"])
X(V, "pollution-waste-management", "C", "Pollution and waste management",
  "Air, water, soil and noise pollution, and rules for managing solid, plastic, e-waste and hazardous waste.",
  ["Air pollutants and the air quality index", "Water pollution: BOD, COD, eutrophication", "Noise and soil pollution", "Solid waste, plastic, e-waste, biomedical and hazardous waste rules", "Bioremediation and phytoremediation", "Extended producer responsibility", "Vehicle emission norms", "Stubble burning and smog"],
  ["BOD vs COD", "Primary vs secondary pollutants"],
  ["ecosystem-ecology-basics"], "Pollutants, indices and rules.", "Evaluate policy responses to urban air quality and plastic waste.", 5,
  ["S-P1-06", "S-GS3-14"], [r"pollut", r"\bAQI\b|air quality", r"\bBOD\b|biochemical oxygen", r"e-waste", r"plastic", r"solid waste", r"hazardous waste", r"bioremediation|phytoremediation", r"particulate|PM ?2\.5|PM ?10", r"noise", r"stubble", r"Bharat Stage|emission norm", r"extended producer"], ["R-NCERT", "R-CPCB", "R-MOEF"], related=["environmental-governance-legislation"])
X(V, "climate-change-ghg", "C", "Climate change and greenhouse gases",
  "Causes, impacts, mitigation and adaptation of human-induced climate change.",
  ["Greenhouse gases and global warming potential", "Carbon footprint, carbon credits, carbon markets", "Ozone depletion and the Montreal Protocol", "Impacts: sea-level rise, extreme weather, glaciers", "Mitigation vs adaptation", "Net zero and nationally determined contributions", "Carbon capture and storage", "Climate finance and common but differentiated responsibilities"],
  ["Mitigation vs adaptation", "Global warming vs climate change", "Ozone hole vs global warming"],
  ["biogeochemical-cycles"], "Gases, effects and instruments.", "Discuss India's climate commitments and equity issues.", 5,
  ["S-P1-06", "S-GS3-14"], [r"climate change", r"global warming", r"greenhouse", r"carbon (credit|market|footprint|capture|neutral)", r"net[- ]zero", r"ozone", r"Montreal Protocol", r"nationally determined contribution|\bNDC", r"mitigation|adaptation", r"sea[- ]level rise", r"methane|nitrous oxide|CFC"], ["R-NCERT", "R-IPCC", "R-UNFCCC", "R-MOEF"], cross_ids=["geography-atmosphere-climatology"], related=["international-treaties-summits"])
X(V, "international-treaties-summits", "D", "International environmental treaties and summits",
  "The major conventions, protocols and summits and what each regulates.",
  ["Stockholm 1972, Rio 1992, Johannesburg 2002, Rio+20", "UNFCCC, Kyoto Protocol, Paris Agreement and COP meetings", "Convention on Biological Diversity, Cartagena and Nagoya Protocols", "Montreal Protocol and Kigali Amendment", "CITES, CMS, Ramsar, Basel, Rotterdam, Stockholm Conventions", "UNCCD", "Global Environment Facility", "International Solar Alliance"],
  ["Convention vs protocol", "Cartagena vs Nagoya Protocol", "Basel vs Rotterdam vs Stockholm Convention"],
  ["climate-change-ghg"], "Which treaty covers what, and the years.", "Discuss India's positions and the equity debate in global environmental governance.", 4,
  ["S-P1-06", "S-GS3-14"], [r"Kyoto", r"Paris Agreement", r"\bUNFCCC\b", r"\bCOP ?\d+", r"Convention on Biological Diversity|\bCBD\b", r"Cartagena|Nagoya", r"CITES", r"Basel Convention|Rotterdam|Stockholm Convention", r"\bUNCCD\b|desertification", r"Global Environment Facility", r"Rio (Earth )?Summit|Stockholm Conference", r"Convention on Migratory"], ["R-UNFCCC", "R-CBD", "R-MOEF"], related=["environmental-governance-legislation"])
X(V, "environmental-governance-legislation", "D", "Environmental governance and legislation in India",
  "Key Indian environmental laws, institutions and community-rights provisions.",
  ["Environment (Protection) Act 1986", "Wildlife (Protection) Act 1972", "Forest (Conservation) Act 1980", "Biological Diversity Act 2002", "Forest Rights Act 2006", "Water and Air Acts and the pollution control boards", "National Green Tribunal Act 2010", "Article 48A and 51A(g)", "Compensatory afforestation (CAMPA)", "Coastal Regulation Zone notifications"],
  ["Statutory vs constitutional environmental provisions", "NGT vs High Courts for environmental cases"],
  ["pollution-waste-management", "protected-areas-wildlife"], "Acts, years and what each does.", "Evaluate effectiveness of environmental governance and balance with development.", 5,
  ["S-P1-06", "S-GS3-14"], [r"Environment \(Protection\) Act", r"Forest \(Conservation\)|Forest Conservation Act", r"Biological Diversity Act", r"Forest Rights Act|Scheduled Tribes and Other Traditional Forest Dwellers", r"National Green Tribunal|\bNGT\b", r"Water \(Prevention", r"Air \(Prevention", r"\bCAMPA\b|compensatory afforestation", r"Article 48A", r"Central Pollution Control Board|State Pollution Control Board"], ["R-MOEF", "R-INDIACODE", "R-CPCB"], cross_ids=["polity-tribunals-dispute-redressal"], related=["environmental-impact-assessment"])
X(V, "environmental-impact-assessment", "D", "Environmental impact assessment",
  "The process of assessing project impacts before clearance, and its legal framework in India.",
  ["Screening, scoping, public hearing, appraisal", "EIA notification and categories of projects", "Environmental management plan", "Strategic environmental assessment", "Environmental clearance and forest clearance", "Criticisms: weak enforcement and compliance", "Carrying-capacity studies"],
  ["EIA vs SEA", "Category A vs Category B projects"],
  ["environmental-governance-legislation"], "Stages of the process.", "Discuss the trade-off between development and environmental safeguards.", 2,
  ["S-GS3-14"], [r"environmental impact assessment|\bEIA\b", r"environmental clearance", r"public hearing", r"strategic environmental", r"environmental management plan", r"scoping"], ["R-MOEF", "R-INDIACODE"], related=["environmental-governance-legislation"])
X(V, "renewable-energy-green-tech", "C", "Renewable energy and green technologies",
  "Solar, wind, hydro, bioenergy, hydrogen and other clean-energy options and the policies around them.",
  ["Solar power: PV vs thermal; National Solar Mission", "Wind and offshore wind", "Hydropower and pumped storage", "Biofuels and ethanol blending", "Green hydrogen", "Nuclear energy basics", "Energy storage and electric mobility", "International Solar Alliance", "Energy transition and just transition"],
  ["Renewable vs non-renewable", "First- vs second-generation biofuels"],
  ["climate-change-ghg"], "Technologies and flagship missions.", "Evaluate India's energy transition: costs, grid and equity.", 3,
  ["S-P1-06", "S-GS3-09", "S-GS3-14"], [r"solar", r"wind (energy|power)|offshore wind", r"biofuel|ethanol", r"green hydrogen|\bhydrogen\b", r"renewable", r"hydropower|hydroelectric|pumped storage", r"nuclear (power|energy|reactor)", r"electric (vehicle|mobility)", r"energy storage|battery", r"International Solar Alliance"], ["R-MOEF", "R-PIB", "R-SURVEY"], cross_ids=["economy-industry-infrastructure"], related=["climate-change-ghg"])
X(V, "sustainable-agriculture-forestry", "B", "Sustainable agriculture and forestry",
  "Farming and forest-management approaches that conserve soil, water and biodiversity.",
  ["Organic and natural farming", "Integrated pest management", "Agroforestry and social forestry", "Joint forest management and community forestry", "Forest types, cover and carbon sequestration", "REDD+ and carbon sequestration", "Soil and water conservation", "Zero budget natural farming"],
  ["Social forestry vs agroforestry", "Organic vs natural farming"],
  ["ecosystem-ecology-basics"], "Practices and policies.", "Discuss sustainable intensification and forest governance.", 3,
  ["S-P1-06", "S-GS3-14", "S-GS3-04"], [r"organic farming|natural farming|zero budget", r"agroforestry|social forestry", r"joint forest management", r"forest cover|forest types?", r"REDD", r"integrated pest", r"sustainable agricultur", r"soil conservation", r"afforestation|deforestation"], ["R-NCERT", "R-MOEF", "R-AGRI"], cross_ids=["economy-agriculture-rural-development"], related=["biodiversity-types-hotspots"])

# ================================================================== MODERN HISTORY  (subject id: history)
H = "history"
X(H, "advent-british-expansion", "A", "Advent of Europeans and British expansion",
  "How the British East India Company gained political control through wars, treaties and policies between the mid-eighteenth and mid-nineteenth centuries.",
  ["European trading companies in India", "Carnatic Wars", "Battle of Plassey 1757 and Buxar 1764", "Dual government in Bengal", "Anglo-Mysore, Anglo-Maratha and Anglo-Sikh wars", "Subsidiary Alliance", "Doctrine of Lapse", "Regulating Act 1773 and Pitt's India Act 1784", "Annexation of Awadh and Sindh"],
  ["Subsidiary Alliance vs Doctrine of Lapse", "Plassey (political) vs Buxar (legal-diwani consequence)"],
  [], "Dates, treaties and policy names.", "Explain how military, diplomatic and administrative means combined in colonial expansion.", 5,
  ["S-GS1-02", "S-P1-02"], [r"Plassey", r"Buxar", r"Carnatic War", r"Subsidiary Alliance", r"Doctrine of Lapse", r"Anglo-(Mysore|Maratha|Sikh)", r"Tipu Sultan", r"East India Company", r"Wellesley|Dalhousie|Cornwallis|Warren Hastings", r"dual government", r"Treaty of (Bassein|Srirangapatna)"], ["R-SPECTRUM", "R-NCERT", "R-NARCH"], related=["british-administration-economy"])
X(H, "british-administration-economy", "B", "British administration and economic policies",
  "Colonial revenue systems, trade and industrial policy, and the machinery of administration and its economic effects.",
  ["Permanent Settlement, Ryotwari, Mahalwari", "Commercialisation of agriculture", "Deindustrialisation and the drain of wealth", "Railways, telegraph and their purposes", "Civil services, army, police, judiciary", "Famines and famine commissions", "Economic nationalists' critique", "Tariff policy and Indian industries"],
  ["Permanent Settlement vs Ryotwari vs Mahalwari", "Drain theory vs deindustrialisation"],
  ["advent-british-expansion"], "Settlement systems and their regions.", "Assess the economic impact of colonial rule.", 5,
  ["S-GS1-02", "S-P1-02"], [r"Permanent Settlement", r"Ryotwari", r"Mahalwari", r"drain of wealth", r"de-?industriali[sz]ation", r"commerciali[sz]ation", r"famine", r"railways? in India|Indian railways", r"Dadabhai Naoroji", r"Lord Cornwallis", r"revenue (system|settlement)"], ["R-SPECTRUM", "R-NCERT"], cross_ids=["economy-agriculture-rural-development"], related=["peasant-tribal-labour-movements"])
X(H, "revolt-of-1857", "A", "The Revolt of 1857",
  "The widespread uprising against Company rule, its causes, leaders, character and consequences.",
  ["Political, economic, social, military causes", "Greased cartridge and the spark at Meerut", "Centres and leaders", "Nature debate: mutiny, revolt, first war of independence", "Why it failed", "Government of India Act 1858 and Queen's Proclamation", "Reorganisation of the army and policy toward princes"],
  ["Mutiny vs revolt vs first war of independence", "Pre-1857 and post-1857 policy"],
  ["advent-british-expansion"], "Causes, centres and leaders.", "Evaluate the nature and legacy of 1857.", 3,
  ["S-GS1-02", "S-GS1-03", "S-P1-02"], [r"1857", r"Sepoy|mutiny", r"Rani (of )?Jhansi|Lakshmibai", r"Bahadur Shah", r"Nana Sahib", r"Queen.s Proclamation", r"Government of India Act,? 1858", r"Mangal Pandey", r"Tatya Tope"], ["R-SPECTRUM", "R-NCERT"], related=["early-nationalism-inc"])
X(H, "social-religious-reform", "B", "Social and religious reform movements",
  "Nineteenth- and early-twentieth-century movements that challenged social evils and reinterpreted religion.",
  ["Raja Ram Mohan Roy and the Brahmo Samaj", "Young Bengal and Derozio", "Arya Samaj and Dayananda", "Ramakrishna Mission and Vivekananda", "Aligarh movement and Deoband", "Jyotiba Phule and Satyashodhak Samaj", "Narayana Guru and SNDP", "Self-respect movement", "Reform of widow remarriage, sati and child marriage; related laws", "Singh Sabha and Parsi reforms"],
  ["Revivalist vs reformist movements", "Brahmo Samaj vs Arya Samaj"],
  ["advent-british-expansion"], "Founders, years and ideas.", "Assess the role of reform movements in shaping nationalism and gender and caste debates.", 4,
  ["S-GS1-02", "S-GS1-03", "S-P1-02"], [r"Brahmo Samaj", r"Arya Samaj", r"Ramakrishna", r"Vivekananda", r"Aligarh", r"Phule", r"Narayana Guru", r"self[- ]respect movement", r"Ram Mohan Roy", r"Derozio|Young Bengal", r"widow remarriage|sati\b", r"Singh Sabha", r"Prarthana Samaj", r"social reform"], ["R-SPECTRUM", "R-NCERT"], cross_ids=["xs-society-social-justice"], related=["early-nationalism-inc"])
X(H, "early-nationalism-inc", "C", "Early nationalism and the Indian National Congress",
  "Rise of organised nationalism, the Moderate phase, the Swadeshi movement and the split in the Congress.",
  ["Pre-Congress associations", "Formation of the INC in 1885", "Moderates: methods and achievements", "Partition of Bengal 1905 and Swadeshi", "Extremists: Tilak, Bipin Chandra Pal, Lala Lajpat Rai", "Surat split 1907", "Morley-Minto Reforms 1909", "Muslim League 1906", "Home Rule Movement and Lucknow Pact 1916"],
  ["Moderates vs Extremists", "Swadeshi vs Boycott"],
  ["revolt-of-1857", "social-religious-reform"], "Dates, leaders and demands.", "Compare Moderate and Extremist politics and assess their contributions.", 4,
  ["S-GS1-03", "S-P1-02"], [r"Indian National Congress", r"Moderate", r"Extremist", r"Swadeshi", r"Partition of Bengal", r"Surat (Session|split)", r"Home Rule", r"Lucknow Pact", r"Muslim League", r"Tilak", r"Gokhale", r"Morley[- ]Minto", r"A\.?\s?O\.? Hume"], ["R-SPECTRUM", "R-NCERT"], related=["gandhian-mass-movements"])
X(H, "revolutionary-communist-movements", "C", "Revolutionary and communist movements",
  "Armed and radical strands of the freedom struggle and the rise of the left.",
  ["Anushilan Samiti and Jugantar", "Ghadar Party", "Hindustan Socialist Republican Association; Bhagat Singh", "Chittagong armoury raid", "Indian revolutionaries abroad", "Communist Party of India (1925) and left in Congress", "Congress Socialist Party", "Kakori case and Lahore conspiracy"],
  ["Revolutionary terrorism vs non-violent mass movement"],
  ["early-nationalism-inc"], "Organisations, events and years.", "Assess the contribution and limits of revolutionary nationalism.", 3,
  ["S-GS1-03", "S-P1-02"], [r"Ghadar", r"Anushilan|Jugantar", r"Bhagat Singh", r"Chandra ?shekhar Azad", r"Chittagong|Surya Sen", r"Hindustan Socialist", r"Kakori", r"Communist Party", r"Congress Socialist", r"revolutionar"], ["R-SPECTRUM", "R-NCERT"], related=["gandhian-mass-movements"])
X(H, "gandhian-mass-movements", "C", "Gandhian mass movements (1915–1942)",
  "Gandhi's methods and the major all-India movements from Champaran to Quit India.",
  ["Champaran, Kheda and Ahmedabad", "Rowlatt Satyagraha and Jallianwala Bagh", "Khilafat and Non-Cooperation Movement", "Chauri Chaura and withdrawal", "Swaraj Party", "Salt March and Civil Disobedience Movement", "Gandhi-Irwin Pact and Round Table Conferences", "Communal Award and Poona Pact", "Individual satyagraha and Cripps Mission", "Quit India Movement 1942"],
  ["Non-Cooperation vs Civil Disobedience vs Quit India", "Satyagraha vs passive resistance"],
  ["early-nationalism-inc"], "Chronology, causes and outcomes of each movement.", "Evaluate Gandhi's strategy and the social base of each movement.", 6,
  ["S-GS1-03", "S-P1-02"], [r"Gandhi", r"Non[- ]Co-?operation", r"Civil Disobedience", r"Quit India", r"Champaran|Kheda|Ahmedabad (mill|strike)", r"Rowlatt", r"Jallianwala", r"Khilafat", r"Chauri Chaura", r"Dandi|Salt (March|Satyagraha)", r"Poona Pact", r"Round Table Conference", r"Gandhi[- ]Irwin"], ["R-SPECTRUM", "R-NCERT", "R-NARCH"], related=["constitutional-developments-1909-1947", "peasant-tribal-labour-movements"])
X(H, "peasant-tribal-labour-movements", "B", "Peasant, tribal and labour movements",
  "Popular movements arising from colonial agrarian, forest and industrial policies.",
  ["Indigo revolt and Deccan riots", "Moplah rebellion", "Bardoli and Kisan Sabha", "Tebhaga and Telangana", "Santhal rebellion, Munda Ulgulan, Kol and Bhil revolts", "Early trade unions and AITUC", "Peasant movements and Congress politics"],
  ["Tribal revolt vs peasant revolt", "Elite-led vs subaltern movement"],
  ["british-administration-economy"], "Which movement, where and why.", "Assess how colonial policies provoked subaltern resistance.", 3,
  ["S-GS1-02", "S-GS1-03", "S-P1-02"], [r"Indigo", r"Deccan (riots|Agriculturists)", r"Moplah|Mappila", r"Bardoli", r"Kisan Sabha", r"Tebhaga|Telangana", r"Santhal", r"Munda", r"tribal (revolt|movement|uprising)", r"peasant", r"\bAITUC\b|trade union"], ["R-SPECTRUM", "R-NCERT"], related=["british-administration-economy"])
X(H, "constitutional-developments-1909-1947", "D", "Constitutional developments and British plans (1909–1947)",
  "The Acts, commissions and proposals that shaped self-government and led to independence.",
  ["Indian Councils Act 1909", "Government of India Act 1919", "Simon Commission, Nehru Report, Jinnah's Fourteen Points", "Government of India Act 1935", "August Offer 1940, Cripps Mission 1942", "Wavell Plan and Simla Conference", "Cabinet Mission Plan 1946", "Mountbatten Plan and Indian Independence Act 1947"],
  ["1919 Act (dyarchy) vs 1935 Act (provincial autonomy)", "Cabinet Mission Plan vs Mountbatten Plan"],
  ["early-nationalism-inc"], "Chronology and provisions of each Act/plan.", "Trace how colonial constitutional steps influenced the Constitution of India.", 5,
  ["S-GS1-02", "S-GS1-03", "S-P1-02"], [r"Government of India Act", r"Indian Councils Act", r"Simon Commission", r"Nehru Report", r"Cripps", r"Wavell Plan", r"Cabinet Mission", r"Mountbatten", r"Indian Independence Act", r"August Offer", r"Montagu|Chelmsford", r"dyarchy", r"communal award"], ["R-SPECTRUM", "R-NCERT", "R-NARCH"], cross_ids=["polity-historical-underpinnings"], related=["transfer-of-power-partition"])
X(H, "transfer-of-power-partition", "D", "Transfer of power, Partition and integration",
  "The events of 1945–1950 from the end of the war to Independence, Partition and the integration of princely states.",
  ["INA trials and RIN mutiny", "Cabinet Mission and the Interim Government", "Direct Action Day 1946", "Mountbatten Plan and the Independence Act", "Radcliffe Award and Partition violence", "Integration of princely states", "Hyderabad, Junagadh and Kashmir", "Linguistic reorganisation debate"],
  ["Cabinet Mission Plan vs Mountbatten Plan", "Accession vs merger"],
  ["constitutional-developments-1909-1947"], "Sequence of events and key figures.", "Evaluate causes of Partition and the process of integration.", 4,
  ["S-GS1-03", "S-GS1-04", "S-P1-02"], [r"Partition", r"Radcliffe", r"Interim Government", r"Direct Action", r"princely state", r"Hyderabad|Junagadh", r"Sardar Patel|Vallabhbhai Patel", r"Instrument of Accession", r"INA trial|Indian National Army", r"Royal Indian Navy|\bRIN\b", r"Mountbatten"], ["R-SPECTRUM", "R-NCERT", "R-NARCH"], cross_ids=["polity-union-territory-citizenship"], related=["constitutional-developments-1909-1947"])
X(H, "key-personalities-ideologies", "C", "Key personalities and ideologies",
  "Leaders of the freedom struggle and the ideas they stood for.",
  ["Gandhi's ideas: satyagraha, swaraj, trusteeship", "Nehru: socialism and secularism", "Subhas Chandra Bose and the INA", "B.R. Ambedkar and Dalit rights", "Tilak, Gokhale, Naoroji, Lajpat Rai, Patel", "Jinnah and the Muslim League", "Tagore, Aurobindo, Iqbal", "Women leaders"],
  ["Gandhi vs Bose methods", "Gandhi vs Ambedkar on caste"],
  ["early-nationalism-inc"], "Associate each figure with ideas, organisations and works.", "Compare ideologies and their influence on later policy.", 4,
  ["S-GS1-03", "S-GS1-02", "S-P1-02"], [r"Subhas Chandra Bose|Netaji", r"Ambedkar", r"Jawaharlal Nehru", r"Sardar Patel", r"Jinnah", r"Tagore", r"Aurobindo", r"Iqbal", r"Sarojini Naidu|Annie Besant|Aruna Asaf Ali", r"Lala Lajpat Rai", r"trusteeship"], ["R-SPECTRUM", "R-NCERT"], related=["gandhian-mass-movements"])

SUBJECT_META = {
    "economy": ("Economy & Agriculture", "authored", ["Prelims GS-I", "Mains GS-III"]),
    "geography": ("Geography", "authored", ["Prelims GS-I", "Mains GS-I"]),
    "environment": ("Environment & Ecology", "authored", ["Prelims GS-I", "Mains GS-III"]),
    "history": ("History & Culture", "partial", ["Prelims GS-I", "Mains GS-I"]),
}
# stubs that now have a real concept page
STUB_RESOLVE = {"xs-economy-public-finance": "economy-fiscal-policy-budget", "xs-history-constitutional-developments": "history-constitutional-developments-1909-1947"}
# extra authored related-links with rationale (cross-subject)
RATIONALE = {
    ("economy-fiscal-policy-budget", "polity-budget-financial-control"): "The budget cycle is the Economy view of the constitutional framework (Consolidated Fund, Appropriation, Finance Bill) studied in Polity.",
    ("economy-taxation", "polity-finance-commission-fiscal-federalism"): "GST and the sharing of tax revenue are the working core of fiscal federalism.",
    ("history-constitutional-developments-1909-1947", "polity-historical-underpinnings"): "The same Acts are studied as history (chronology, politics) and as polity (institutions that survived into the Constitution).",
    ("environment-environmental-governance-legislation", "polity-tribunals-dispute-redressal"): "The National Green Tribunal is a specialised tribunal within the wider tribunal framework.",
    ("geography-rivers-water-resources", "polity-inter-state-relations"): "River-water disputes are resolved under Art 262 and the Inter-State River Water Disputes Act.",
    ("economy-agriculture-rural-development", "geography-indian-agriculture-land-use"): "Crops and regions (Geography) and prices, subsidies and markets (Economy) are two lenses on the same sector.",
    ("geography-indian-monsoon-climate", "economy-agriculture-rural-development"): "Monsoon variability drives crop output, food prices and rural distress.",
    ("geography-atmosphere-climatology", "environment-climate-change-ghg"): "Climate change builds on the atmosphere's heat balance and circulation.",
    ("geography-geophysical-hazards", "environment-climate-change-ghg"): "Climate change alters the frequency and intensity of cyclones, floods and droughts.",
    ("economy-industry-infrastructure", "geography-minerals-industries-location"): "Industrial policy and infrastructure meet resource geography in the location of industry.",
    ("environment-renewable-energy-green-tech", "economy-industry-infrastructure"): "Energy transition is both an environmental goal and an infrastructure-investment issue.",
    ("history-british-administration-economy", "economy-agriculture-rural-development"): "Colonial land-revenue systems explain agrarian structures and land-reform debates after independence.",
    ("history-transfer-of-power-partition", "polity-union-territory-citizenship"): "Partition and integration shaped citizenship provisions and the territorial structure of the Union.",
}
