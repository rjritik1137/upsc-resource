"""Phase D batch 4: deepens the thinnest subjects (Disaster Management, Security, Society, IR, Governance).
Same rules: AI-written from general knowledge, draft-unreviewed, no book chapters/editions, no statistics, no invented quotes."""
import author_polity as P
import author_subjects as S
from author_subjects import X

S.GROUPS["disaster"] = [("A", "Disaster management"), ("B", "Hazard types"), ("C", "Resilience, relief and recovery")]
S.GROUPS["security"] = [("A", "Internal security"), ("B", "Cyber, border and maritime security"), ("C", "Defence reform")]
S.GROUPS["ir"] = [("A", "India and the world"), ("B", "Major bilateral relationships")]
S.GROUPS["society"] = [("A", "Indian society and its diversity"), ("B", "Social issues and globalisation")]
S.GROUPS["governance"] = [("A", "Policy, delivery and accountability"), ("B", "Social sector and vulnerable sections"), ("C", "Sectoral governance")]

# ================================================================ DISASTER MANAGEMENT
D = "disaster"
X(D, "hydro-meteorological-disasters", "B", "Floods, cyclones, droughts and other weather disasters",
  "Causes, vulnerability patterns and management of climate- and weather-driven hazards in India.",
  ["Floods: causes, flood plains, urban flooding, flood forecasting", "Tropical cyclones: formation, naming, warning systems, coastal impact", "Droughts: meteorological, hydrological, agricultural", "Cloudbursts, heat waves, cold waves", "Glacial lake outburst floods", "Structural vs non-structural measures", "Early warning and forecasting (IMD, CWC)", "Regional vulnerability: Brahmaputra, Kosi, east coast, Himalaya"],
  ["Flood vs flash flood", "Meteorological vs agricultural drought", "Structural vs non-structural mitigation"],
  ["disaster-disaster-management-framework"], "Causes, regions and warning agencies.", "Evaluate flood and cyclone management, and the shift to impact-based forecasting.", 4,
  ["S-GS3-15"], [r"\bflood", r"cyclone", r"drought", r"cloudburst", r"heat ?wave|cold wave", r"glacial lake", r"urban flooding", r"\bIMD\b|India Meteorological", r"flash flood", r"storm surge"], ["R-NDMA", "R-MHA", "R-NCERT"], cross_ids=["geography-indian-monsoon-climate"], related=["geological-disasters", "climate-risk-resilience"])
X(D, "geological-disasters", "B", "Earthquakes, tsunamis, landslides and other geological hazards",
  "Origins and management of earthquakes, tsunamis, landslides, avalanches and volcanic hazards.",
  ["Earthquake causes and seismic zones of India", "Building codes and earthquake-resistant construction", "Tsunami: cause, warning systems, 2004 event", "Landslides: causes and mapping in the Himalaya and Western Ghats", "Avalanches and snow hazards", "Volcanoes (India's Barren Island)", "Land subsidence", "Mitigation, mapping and community preparedness"],
  ["Epicentre vs focus", "Magnitude vs intensity", "Landslide vs avalanche"],
  ["disaster-disaster-management-framework"], "Zones, causes and warning systems.", "Link development in fragile terrain to hazard risk.", 3,
  ["S-GS3-15"], [r"earthquake|seismic", r"tsunami", r"landslide", r"avalanche", r"volcan", r"subsidence", r"Richter|magnitude", r"building code", r"seismic zone"], ["R-NDMA", "R-NCERT"], cross_ids=["geography-geophysical-hazards"], related=["hydro-meteorological-disasters"])
X(D, "man-made-disasters", "B", "Industrial, chemical, fire and other human-induced disasters",
  "Hazards arising from industry, infrastructure and human activity, with lessons from major events.",
  ["Chemical and industrial accidents (Bhopal gas tragedy)", "Nuclear and radiological emergencies", "Fires: forests, buildings, factories", "Building and bridge collapses; stampedes", "Oil spills and marine pollution", "Mining accidents", "Road and rail accidents", "Legal framework: Factories Act, Environment Protection Act, Public Liability Insurance Act"],
  ["Natural vs man-made disaster", "Hazard vs risk"],
  ["disaster-disaster-management-framework"], "Examples and laws.", "Assess regulatory failures and safety culture.", 3,
  ["S-GS3-15"], [r"Bhopal", r"industrial (accident|disaster)|chemical (accident|disaster)", r"man-?made disaster", r"stampede", r"building collapse|bridge collapse", r"oil spill", r"fire (safety|accident)|forest fire", r"nuclear (accident|emergency)|radiological", r"mining accident"], ["R-NDMA", "R-MOEF"], cross_ids=["environment-pollution-waste-management"], related=["disaster-disaster-management-framework"])
X(D, "climate-risk-resilience", "C", "Climate risk, adaptation and resilient infrastructure",
  "How climate change reshapes disaster risk, and the adaptation and resilience tools used in India and internationally.",
  ["Climate-induced hazard trends", "Adaptation vs mitigation", "Coastal and sea-level risk; coastal regulation", "Sendai Framework priorities", "Coalition for Disaster Resilient Infrastructure (CDRI)", "Loss and damage", "Nature-based solutions (mangroves, wetlands)", "Climate-resilient agriculture and housing", "Vulnerability and risk assessments"],
  ["Adaptation vs mitigation", "Resilience vs preparedness"],
  ["disaster-disaster-management-framework"], "Terms and international frameworks.", "Argue for integrating DRR into development planning.", 3,
  ["S-GS3-15", "S-GS3-10"], [r"\bresilien", r"adaptation", r"Sendai", r"\bCDRI\b|Disaster Resilient Infrastructure", r"loss and damage", r"sea[- ]level", r"nature-based", r"climate[- ](risk|resilient)", r"coastal (regulation|zone)"], ["R-NDMA", "R-MOEF", "R-UN"], cross_ids=["environment-climate-change-ghg"], related=["hydro-meteorological-disasters"])
X(D, "relief-recovery-financing", "C", "Relief, rehabilitation and disaster financing",
  "Institutions, funds and practices for response, recovery and rebuilding.",
  ["NDRF and SDRF; National and State Disaster Mitigation Funds", "Role of the armed forces and civil defence", "Finance Commission allocation for disasters", "Disaster insurance and risk transfer", "Build back better and rehabilitation", "Role of NGOs, volunteers and communities", "Incident response system and command", "Humanitarian assistance and international aid", "Psychosocial care and gender-sensitive relief"],
  ["Relief vs rehabilitation vs reconstruction", "NDRF (force) vs NDRF (fund)"],
  ["disaster-disaster-management-framework"], "Bodies, funds and sequence.", "Evaluate federal financing and coordination in major disasters.", 3,
  ["S-GS3-15"], [r"\bNDRF\b|\bSDRF\b|State Disaster Response", r"relief|rehabilitation", r"build back better", r"civil defence", r"disaster (insurance|financing|fund)", r"Finance Commission.*disaster", r"humanitarian", r"incident response"], ["R-NDMA", "R-MHA"], cross_ids=["polity-finance-commission-fiscal-federalism"], related=["disaster-disaster-management-framework"])

# ================================================================ SECURITY
Sc = "security"
X(Sc, "terrorism-counter-terrorism", "A", "Terrorism and counter-terrorism architecture",
  "Forms of terrorism India faces, the legal and institutional counter-terror framework, and global cooperation.",
  ["Cross-border and domestic terrorism; lone-wolf and online radicalisation", "Major attacks and lessons (26/11)", "UAPA and counter-terror law debates", "NIA, NSG, NATGRID, Multi-Agency Centre", "Terror financing and FATF", "Global bodies and conventions", "Deradicalisation approaches", "Human rights safeguards"],
  ["Terrorism vs insurgency", "Preventive detention vs criminal prosecution"],
  [], "Laws, bodies and landmark events.", "Balance security measures with civil liberties.", 4,
  ["S-GS3-17", "S-GS3-16"], [r"terroris", r"\bUAPA\b|Unlawful Activities", r"\bNIA\b|National Investigation", r"\bNSG\b|National Security Guard", r"\bNATGRID\b|Multi-Agency Centre", r"26/11|Mumbai attack", r"lone[- ]wolf", r"counter[- ]terror", r"terror financ|\bFATF\b", r"radicali[sz]ation"], ["R-MHA", "R-ARC"], cross_ids=["polity-fr-freedoms", "ir-global-conflicts-treaties"], related=["external-actors-extremism", "security-security-forces-agencies"])
X(Sc, "jk-northeast-security", "A", "Jammu & Kashmir and North-East security challenges",
  "Historical roots, groups and policy responses in India's two main insurgency-affected regions.",
  ["Jammu & Kashmir: accession, conflict, Article 370 and 2019 changes", "Cross-border infiltration and ceasefire", "North-East: ethnic aspirations, migration, insurgent groups", "Peace accords and Naga talks", "AFSPA: provisions and criticism", "Border and connectivity development", "Role of Assam Rifles and Army", "Political and developmental responses"],
  ["Insurgency vs separatism", "Disturbed Area vs Special Powers"],
  ["external-actors-extremism"], "Timeline, groups and accords.", "Assess whether security-led or dialogue-led approaches work.", 4,
  ["S-GS3-16", "S-GS3-17"], [r"Jammu (and|&) Kashmir|\bJ&K\b|Kashmir", r"Article 370", r"North[- ]East", r"Nagaland|Naga\b|Manipur|Mizoram|Assam|ULFA|NSCN", r"AFSPA|Armed Forces \(Special", r"infiltration", r"peace (accord|talks|agreement)", r"Bodo|Bru\b|Mizo Accord"], ["R-MHA", "R-ARC"], cross_ids=["polity-special-provisions-schedules"], related=["external-actors-extremism"])
X(Sc, "maritime-security-indian-ocean", "B", "Maritime and coastal security in the Indian Ocean",
  "India's maritime interests, coastal security architecture and Indian Ocean strategy.",
  ["Coastal security after 26/11: Coastal Police, Coast Guard, Navy", "Piracy and the Gulf of Aden", "Indian Ocean Region geopolitics and SLOCs", "Blue economy and EEZ", "SAGAR/MAHASAGAR outlook and Indo-Pacific", "Maritime domain awareness and information fusion", "Island territories' strategic value", "UNCLOS dispute settlement"],
  ["EEZ vs territorial waters", "Coast Guard vs Navy mandates"],
  [], "Concepts and agencies.", "Link maritime power to trade, energy and strategic competition.", 3,
  ["S-GS3-19", "S-GS3-20"], [r"coastal security|coastal police", r"Coast Guard", r"piracy", r"Indian Ocean|\bIOR\b", r"\bEEZ\b|exclusive economic zone", r"blue economy", r"UNCLOS", r"sea lanes?|\bSLOC", r"Andaman|Lakshadweep|island territor"], ["R-MHA", "R-MEA"], cross_ids=["ir-india-neighbourhood"], related=["border-management-organised-crime"])
X(Sc, "defence-reforms-procurement", "C", "Defence reforms, indigenisation and procurement",
  "Higher defence organisation, procurement policy and the push for self-reliance.",
  ["Chief of Defence Staff and Department of Military Affairs", "Theatre commands", "Defence Acquisition Council and Procurement Procedure", "Make in India in defence; positive indigenisation lists", "FDI in defence and offsets", "iDEX and start-ups; defence corridors", "Agnipath and manpower reforms", "Defence budget and pensions"],
  ["Procurement vs acquisition", "Joint vs integrated commands"],
  ["security-security-forces-agencies"], "Bodies, policies and schemes.", "Evaluate reform trade-offs: cost, jointness and indigenisation.", 3,
  ["S-GS3-20", "S-GS3-12"], [r"Chief of Defence Staff|\bCDS\b", r"Department of Military Affairs", r"theatre command", r"Defence Acquisition|procurement", r"indigenisation|Atmanirbhar", r"defence corridor|iDEX", r"Agnipath|Agniveer", r"offset", r"defence budget"], ["R-DRDO", "R-MHA", "R-PIB"], cross_ids=["scitech-defence-technology"], related=["security-security-forces-agencies"])

# ================================================================ SOCIETY
Y = "society"
X(Y, "tribal-society-issues", "A", "Tribal society, rights and development",
  "Characteristics of India's tribal communities, constitutional protection and recurring issues.",
  ["Scheduled Tribes and PVTGs", "Fifth and Sixth Schedules; PESA; Forest Rights Act", "Displacement and land alienation", "Tribal health, education and livelihood", "Tribal movements and identity", "Assimilation, isolation and integration debates", "Development schemes and Tribal Sub-Plan", "Culture and language preservation"],
  ["Scheduled Tribe vs PVTG", "Assimilation vs integration"],
  ["indian-society-diversity"], "Provisions and terms.", "Weigh development, displacement and autonomy.", 3,
  ["S-GS1-06", "S-GS1-09"], [r"tribe|tribal", r"\bPVTG|Particularly Vulnerable", r"Forest Rights Act|\bFRA\b", r"\bPESA\b", r"Fifth Schedule|Sixth Schedule", r"displacement", r"Adivasi", r"Scheduled Tribe", r"land alienation"], ["R-NCERT", "R-MSJE"], cross_ids=["polity-special-provisions-schedules", "governance-vulnerable-sections-welfare"], related=["indian-society-diversity"])
X(Y, "religion-secularism-communalism", "A", "Religion, secularism and communalism",
  "Religious diversity, the Indian model of secularism and the causes and effects of communalism.",
  ["Religious composition and diversity", "Indian secularism: equal respect vs strict separation", "Communalism: causes, history, consequences", "Role of media and politics in communal tension", "Fundamentalism and radicalisation", "Interfaith harmony and syncretic traditions", "Legal protection: IPC provisions, Places of Worship Act", "Role of education and civil society"],
  ["Secularism (Indian) vs Western", "Communalism vs fundamentalism"],
  ["indian-society-diversity"], "Definitions and models.", "Evaluate secularism and remedies for communal polarisation.", 3,
  ["S-GS1-06", "S-GS1-09"], [r"secular", r"communal", r"fundamentalism", r"religious (diversity|minorit|harmony|freedom)", r"Places of Worship", r"interfaith|syncretic", r"religion"], ["R-NCERT"], cross_ids=["polity-fr-exploitation-religion-cultural"], related=["indian-society-diversity"])
X(Y, "family-marriage-changes", "A", "Family, marriage and kinship: continuity and change",
  "How family forms, marriage patterns and kinship are changing in India.",
  ["Joint, nuclear and extended families", "Changes in marriage age, choice and divorce", "Inter-caste and inter-faith marriage", "Live-in relationships and the law", "Child marriage and dowry", "Ageing and intergenerational support", "Urbanisation, migration and family", "Domestic violence and women's status"],
  ["Joint vs nuclear family", "Endogamy vs exogamy"],
  ["indian-society-diversity"], "Types and terms.", "Explain drivers of change and policy implications.", 3,
  ["S-GS1-06", "S-GS1-07"], [r"joint family|nuclear family", r"marriage", r"live-in", r"dowry", r"child marriage", r"divorce", r"family (structure|system)", r"kinship", r"inter-?caste"], ["R-NCERT", "R-WCD"], related=["social-empowerment-women"])
X(Y, "social-movements-civil-society", "B", "Social movements and civil society",
  "Major movements in post-independence India and the role of civil society.",
  ["Environmental movements: Chipko, Narmada Bachao", "Dalit, women's and tribal movements", "Farmers' and labour movements", "Anti-corruption and RTI movements", "NGOs, SHGs and community organisations", "Role of social media in mobilisation", "Types of movements: reformist, revolutionary", "Impact on law and policy"],
  ["Reform vs revolutionary movement", "NGO vs social movement"],
  [], "Names, causes and outcomes.", "Assess how movements have shaped policy and democracy.", 3,
  ["S-GS1-08", "S-GS1-09"], [r"Chipko", r"Narmada", r"social movement", r"civil society", r"farmers.? (protest|movement)", r"Dalit (movement|Panthers)", r"women.s movement", r"\bNGO", r"RTI movement", r"mass movement"], ["R-NCERT"], cross_ids=["governance-policy-design-implementation"], related=["globalisation-social-change"])
X(Y, "regionalism-language-integration", "A", "Regionalism, language and national integration",
  "Roots and effects of regional identity and linguistic politics, and the tools of national integration.",
  ["Linguistic reorganisation of States", "Three-language formula and language politics", "Regionalism and sons-of-the-soil politics", "Demand for new States", "Inter-State disputes", "Centre–State friction and federal balance", "Role of National Integration Council", "Cultural pluralism and shared symbols"],
  ["Regionalism vs separatism", "Language vs dialect"],
  ["indian-society-diversity"], "Events and provisions.", "Argue for managing diversity through federal accommodation.", 3,
  ["S-GS1-06", "S-GS1-09"], [r"regionalism", r"linguistic (reorgani|State|diversity|minorit)", r"three[- ]language", r"sons of the soil", r"new State|separate State|statehood", r"national integration", r"Hindi|official language", r"States Reorganisation"], ["R-NCERT"], cross_ids=["polity-federalism-centre-state"], related=["indian-society-diversity", "religion-secularism-communalism"])

# ================================================================ INTERNATIONAL RELATIONS
I = "ir"
X(I, "india-china-relations", "B", "India–China relations",
  "History, border dispute, trade and strategic competition between India and China.",
  ["1962 war, LAC and boundary disputes", "Doklam and Galwan", "Trade deficit and supply-chain dependence", "Belt and Road, CPEC and the Indian Ocean", "Tibet, Brahmaputra and water issues", "China–Pakistan axis", "Engagement mechanisms and border talks", "Quad and balancing"],
  ["LAC vs LoC", "Strategic competition vs cooperation"],
  ["india-neighbourhood"], "Timeline, issues and agreements.", "Assess India's mix of deterrence, diplomacy and economic de-risking.", 4,
  ["S-GS2-17", "S-GS2-19"], [r"\bChina\b|Chinese", r"\bLAC\b|Line of Actual Control", r"Doklam|Galwan|Arunachal", r"Belt and Road|\bBRI\b|CPEC", r"Tibet", r"trade deficit", r"Panchsheel", r"String of Pearls"], ["R-MEA", "R-PIB"], related=["global-groupings-agreements"])
X(I, "india-us-relations", "B", "India–US relations",
  "Evolution of strategic, defence, trade and technology ties between India and the United States.",
  ["Cold War distance to strategic partnership", "Civil nuclear deal", "Defence agreements (LEMOA, COMCASA, BECA)", "Trade, tariffs and technology (iCET)", "Quad and Indo-Pacific", "Diaspora, visas and education", "Divergences: Russia, human rights", "Counter-terror cooperation"],
  ["Strategic partner vs ally", "Strategic autonomy vs alignment"],
  ["global-groupings-agreements"], "Agreements and milestones.", "Evaluate convergence, divergence and hedging.", 3,
  ["S-GS2-19", "S-GS2-17"], [r"United States|\bUSA?\b(?! of)|American", r"civil nuclear", r"\bLEMOA\b|COMCASA|\bBECA\b|foundational (agreement|pact)", r"\bQuad\b", r"\biCET\b", r"H-1B|visa", r"Indo-Pacific", r"Strategic Trade Authori"], ["R-MEA", "R-PIB"], related=["india-china-relations"])
X(I, "india-russia-central-asia", "B", "India–Russia and Central Asia",
  "Defence, energy and strategic ties with Russia, and India's Central Asia outreach.",
  ["Historic defence and nuclear partnership", "Oil and energy trade; sanctions context", "Connectivity: INSTC, Chabahar", "Central Asia: Connect Central Asia policy", "SCO and Eurasian groupings", "Defence diversification", "Arctic and Far East cooperation", "Multi-alignment and the Ukraine war"],
  ["INSTC vs Belt and Road"],
  ["global-groupings-agreements"], "Agreements and projects.", "Weigh dependence against diversification.", 3,
  ["S-GS2-19", "S-GS2-17"], [r"Russia|Soviet", r"Central Asia", r"\bINSTC\b|North[- ]South Transport", r"Chabahar", r"\bS-400\b", r"Eurasian", r"Ukraine", r"Kazakhstan|Uzbekistan|Turkmenistan|Tajikistan|Kyrgyz"], ["R-MEA"], related=["india-china-relations"])
X(I, "india-west-asia", "B", "India and West Asia",
  "Energy, diaspora, trade and strategic ties across the Gulf and wider West Asia.",
  ["Energy security and Gulf oil/gas", "Diaspora and remittances", "Look West; Gulf Cooperation Council ties", "Israel, Iran and Palestine balancing", "I2U2 and India-Middle East-Europe corridor", "Chabahar and connectivity", "Evacuation operations", "Security and counter-terror cooperation"],
  ["Look West vs Link West", "Two-state solution"],
  ["global-groupings-agreements"], "Countries, corridors and issues.", "Assess India's balancing strategy.", 3,
  ["S-GS2-19", "S-GS2-18"], [r"West Asia|Middle East", r"Gulf|\bGCC\b|Saudi|\bUAE\b|Emirates|Qatar|Oman|Kuwait|Bahrain", r"\bIran\b|Israel|Palestine", r"\bI2U2\b|\bIMEC\b|Middle East-Europe", r"remittance", r"energy security"], ["R-MEA"], cross_ids=["economy-external-sector-bop"], related=["diaspora-foreign-policy-effects"])
X(I, "india-africa-global-south", "B", "India, Africa, Latin America and the Global South",
  "Development partnership, trade and diplomacy with Africa, Latin America and island regions.",
  ["India-Africa Forum Summit and African Union membership", "Lines of Credit and capacity building", "Energy and resource ties", "Pan-African e-Network and digital cooperation", "Latin America outreach", "Pacific Islands engagement", "Voice of Global South Summit", "Competition with China's footprint"],
  ["Development partnership vs aid"],
  ["global-groupings-agreements"], "Initiatives and partners.", "Evaluate India's soft-power-led approach.", 2,
  ["S-GS2-18", "S-GS2-19"], [r"Africa", r"Latin America", r"Global South", r"African Union", r"Lines? of Credit", r"Pacific Island", r"capacity building", r"development partnership"], ["R-MEA"], related=["global-groupings-agreements"])

# ================================================================ GOVERNANCE
Gv = "governance"
X(Gv, "rural-development-schemes", "C", "Rural development schemes and livelihood missions",
  "Major programmes for rural employment, housing, roads and livelihoods, and how they are delivered.",
  ["MGNREGA: demand-driven employment", "NRLM and self-help groups", "PMAY-G housing; PMGSY roads", "Deendayal Upadhyaya Grameen Kaushalya Yojana", "Social security pensions", "Panchayat role and social audit", "Convergence and leakages", "Evaluation and outcome issues"],
  ["Demand-driven vs supply-driven scheme", "Centrally sponsored vs state scheme"],
  ["policy-design-implementation"], "Scheme names and objectives.", "Assess design, financing and leakages.", 3,
  ["S-GS2-10", "S-GS2-12"], [r"MGNREGA|Mahatma Gandhi National Rural", r"\bNRLM\b|National Rural Livelihoods", r"PMAY|Pradhan Mantri Awas", r"PMGSY|Gram Sadak", r"rural (development|employment|livelihood)", r"self[- ]help group", r"social audit"], ["R-PIB", "R-NITI"], cross_ids=["economy-human-development-poverty-employment"], related=["policy-design-implementation"])
X(Gv, "food-security-pds", "C", "Food security, PDS and nutrition governance",
  "Legal entitlements, procurement and distribution systems, and nutrition programmes.",
  ["National Food Security Act", "Public Distribution System reforms", "MSP, procurement and buffer stock", "Food Corporation of India", "ICDS, POSHAN and mid-day meal", "One Nation One Ration Card", "Malnutrition indicators", "WTO and food subsidy issues"],
  ["Food security vs nutrition security", "MSP vs procurement price"],
  ["policy-design-implementation"], "Acts, bodies and schemes.", "Evaluate PDS efficiency, targeting and the cash-transfer debate.", 3,
  ["S-GS2-12", "S-GS2-13", "S-GS2-10"], [r"food security", r"Public Distribution System|\bPDS\b", r"National Food Security", r"\bMSP\b|minimum support price", r"buffer stock", r"Food Corporation", r"POSHAN|ICDS|mid-?day meal", r"malnutrition|hunger", r"ration card"], ["R-PIB", "R-NITI"], cross_ids=["economy-agriculture-rural-development"], related=["social-sector-welfare"])
X(Gv, "education-policy", "C", "Education policy and governance",
  "Structure, regulation and reform of school, higher and vocational education.",
  ["Right to Education Act", "National Education Policy 2020 principles", "Higher education regulation and accreditation", "Foundational literacy and learning outcomes", "Skilling and vocational education", "Digital learning and the digital divide", "Private participation and fees", "Teacher quality and governance"],
  ["Formal vs vocational education", "Access vs quality"],
  ["social-sector-welfare"], "Provisions and bodies.", "Evaluate implementation gaps in NEP and RTE.", 3,
  ["S-GS2-13", "S-GS2-12"], [r"Right to Education|\bRTE\b", r"National Education Policy|\bNEP\b", r"higher education|\bUGC\b|\bAICTE\b|\bNAAC\b", r"learning outcome|foundational literacy", r"skill (development|India)|vocational", r"school education", r"teacher", r"digital (learning|education)"], ["R-PIB", "R-NITI"], related=["social-sector-welfare"])
X(Gv, "health-policy", "C", "Health policy and governance",
  "Public health system design, financing, regulation and recent reforms.",
  ["National Health Mission and primary care", "Ayushman Bharat and health insurance", "Health infrastructure and workforce gaps", "Drug and device regulation", "Public vs private provision", "Digital Health Mission", "Maternal and child health indicators", "Communicable disease control programmes"],
  ["Public health vs medical care", "Insurance vs direct provision"],
  ["social-sector-welfare"], "Schemes and indicators.", "Assess access, affordability and quality.", 3,
  ["S-GS2-13"], [r"National Health Mission|\bNHM\b", r"Ayushman|health insurance", r"primary health|health infrastructure", r"drug regulation|Drugs and Cosmetics|\bCDSCO\b", r"Digital Health", r"maternal|infant mortality", r"public health", r"health (care|policy|system)"], ["R-PIB", "R-NITI"], cross_ids=["scitech-health-diseases"], related=["social-sector-welfare"])
X(Gv, "civil-society-media-pressure-groups", "A", "Civil society, media and pressure groups",
  "Role of non-state stakeholders in governance: media, NGOs, interest groups and citizens.",
  ["Pressure and interest groups", "NGOs and accountability concerns", "Media as watchdog; media ethics and regulation", "Social media and governance", "Citizen participation; Gram Sabha; participatory budgeting", "Foreign contribution regulation", "Think tanks and consultations", "Role in policy feedback"],
  ["Pressure group vs political party", "Civil society vs state"],
  ["policy-design-implementation"], "Definitions and roles.", "Weigh benefits and risks of non-state actors in policy.", 2,
  ["S-GS2-10", "S-GS2-15"], [r"pressure group|interest group", r"civil society", r"\bmedia\b", r"\bNGO", r"social media", r"\bFCRA\b|Foreign Contribution", r"participatory", r"citizen participation"], ["R-ARC"], cross_ids=["society-social-movements-civil-society"], related=["transparency-e-governance-citizens-charter"])
X(Gv, "digital-public-infrastructure", "A", "Digital public infrastructure and data governance",
  "Aadhaar, UPI and other public digital platforms, and issues of privacy, inclusion and data protection.",
  ["Aadhaar and its legal framework", "UPI, DigiLocker, CoWIN, ONDC", "India Stack concept", "Data protection law and privacy judgment", "Digital divide and inclusion", "Cyber-security and platform risk", "JAM trinity and DBT", "Exporting DPI and global governance"],
  ["Digital public infrastructure vs private platform", "Privacy vs surveillance"],
  ["transparency-e-governance-citizens-charter"], "Platforms and laws.", "Evaluate inclusion, privacy and security trade-offs.", 3,
  ["S-GS2-15", "S-GS2-10"], [r"Aadhaar", r"\bUPI\b|DigiLocker|CoWIN|\bONDC\b", r"India Stack", r"data protection|privacy", r"digital (divide|inclusion|public)", r"\bJAM\b|Jan Dhan", r"direct benefit transfer", r"Digital India"], ["R-MEITY", "R-PIB"], cross_ids=["scitech-information-technology-cyber", "economy-financial-inclusion-digital-payments"], related=["transparency-e-governance-citizens-charter"])

RATIONALE = {
    ("disaster-hydro-meteorological-disasters", "geography-indian-monsoon-climate"): "Floods, droughts and cyclones follow the monsoon and ocean-atmosphere patterns studied in Geography.",
    ("disaster-geological-disasters", "geography-geophysical-hazards"): "Plate tectonics (Geography) explains the earthquakes, tsunamis and landslides managed here.",
    ("disaster-man-made-disasters", "environment-pollution-waste-management"): "Industrial accidents and spills overlap with pollution control and hazardous-waste rules.",
    ("disaster-climate-risk-resilience", "environment-climate-change-ghg"): "Adaptation and loss-and-damage follow from the climate-change science and negotiations.",
    ("disaster-relief-recovery-financing", "polity-finance-commission-fiscal-federalism"): "Disaster funds are shared between Centre and States through Finance Commission recommendations.",
    ("security-terrorism-counter-terrorism", "polity-fr-freedoms"): "Counter-terror law is tested against Article 19 and 21 freedoms.",
    ("security-terrorism-counter-terrorism", "ir-global-conflicts-treaties"): "Terrorism is both an internal-security and a global-cooperation issue.",
    ("security-jk-northeast-security", "polity-special-provisions-schedules"): "Articles 370, 371 and the Sixth Schedule frame the constitutional side of these regions.",
    ("security-maritime-security-indian-ocean", "ir-india-neighbourhood"): "Indian Ocean strategy links maritime security with neighbourhood policy.",
    ("security-defence-reforms-procurement", "scitech-defence-technology"): "Procurement reform and indigenisation drive the defence technology base.",
    ("society-tribal-society-issues", "polity-special-provisions-schedules"): "The Fifth and Sixth Schedules are the constitutional basis of tribal administration.",
    ("society-tribal-society-issues", "governance-vulnerable-sections-welfare"): "Tribal development is delivered through welfare schemes and commissions.",
    ("society-religion-secularism-communalism", "polity-fr-exploitation-religion-cultural"): "Articles 25–30 define the legal content of Indian secularism.",
    ("society-regionalism-language-integration", "polity-federalism-centre-state"): "Regional and linguistic politics play out through Centre–State relations.",
    ("society-social-movements-civil-society", "governance-policy-design-implementation"): "Movements and NGOs shape and monitor policy implementation.",
    ("ir-india-west-asia", "economy-external-sector-bop"): "Oil imports and remittances tie West Asia to the balance of payments.",
    ("governance-rural-development-schemes", "economy-human-development-poverty-employment"): "Rural schemes are the delivery arm of poverty and employment policy.",
    ("governance-food-security-pds", "economy-agriculture-rural-development"): "Procurement, MSP and the PDS link farm policy to food entitlements.",
    ("governance-health-policy", "scitech-health-diseases"): "Disease science and technology inform health policy and programmes.",
    ("governance-civil-society-media-pressure-groups", "society-social-movements-civil-society"): "Civil society and social movements are two views of non-state participation.",
    ("governance-digital-public-infrastructure", "scitech-information-technology-cyber"): "Digital public platforms rest on IT and cyber-security technology.",
    ("governance-digital-public-infrastructure", "economy-financial-inclusion-digital-payments"): "UPI and Jan Dhan are the payments side of digital public infrastructure.",
}
