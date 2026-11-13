"""Phase D batch 7: deepens Science & Technology, Disaster Management and Security.
Same rules: AI-written from general knowledge, draft-unreviewed, no book chapters/editions, no statistics, no invented quotes."""
import author_polity as P
import author_subjects as S
from author_subjects import X

S.GROUPS["security"] = S.GROUPS["security"]
# ================================================================ SCIENCE & TECHNOLOGY
T = "scitech"
X(T, "electricity-electronics-communication", "A", "Electricity, electronics and communication technology",
  "Circuits, semiconductors and the technologies behind radio, radar, optical fibre and mobile communication.",
  ["Ohm's law, series and parallel circuits, power", "Diodes, transistors, LEDs, solar cells", "Integrated circuits and chips", "Radio waves, radar and sonar", "Optical fibre and total internal reflection", "Mobile communication and satellites", "Superconductivity and its uses", "Lasers and their applications"],
  ["Analog vs digital signal", "LED vs LCD vs OLED", "Radar vs sonar"],
  ["physics-basics"], "Definitions, devices and uses.", "Link electronics to digital infrastructure and defence.", 3,
  ["S-P1-07", "S-GS3-11", "S-GS3-13"], [r"semiconductor|transistor|diode", r"\bLED\b|\bOLED\b|\bLCD\b", r"\bradar\b|\bsonar\b", r"optical fi[bv]re", r"integrated circuit|microchip|\bchip\b", r"\blaser\b", r"Ohm", r"radio wave|microwave", r"superconduct"], ["R-NCERT", "R-DST", "R-MEITY"], related=["information-technology-cyber", "physics-basics"])
X(T, "organic-chemistry-everyday", "A", "Organic chemistry and everyday products",
  "Carbon compounds, polymers, fuels, food additives and household chemicals.",
  ["Hydrocarbons and functional groups", "Petroleum products and fuels; biofuels", "Polymers, plastics, synthetic fibres, rubber", "Soaps, detergents, dyes", "Food additives and preservatives", "Fertilisers and pesticides", "Pharmaceuticals basics", "Green chemistry"],
  ["Soap vs detergent", "Biodegradable vs non-biodegradable", "LPG vs CNG vs PNG"],
  ["chemistry-basics"], "Compounds and uses.", "Link to pollution, health and energy policy.", 3,
  ["S-P1-07", "S-GS3-11"], [r"hydrocarbon|methane|ethanol|ethylene", r"\bLPG\b|\bCNG\b|\bPNG\b|biofuel|biodiesel", r"polymer|plastic|nylon|polythene|\bPVC\b|rubber", r"soap|detergent", r"preservative|food additive", r"pesticide|DDT|insecticide", r"green chemistry", r"vulcani[sz]ation", r"petroleum product"], ["R-NCERT", "R-DST"], related=["chemistry-basics"])
X(T, "human-physiology-nutrition", "A", "Human physiology, nutrition and common disorders",
  "Body systems, nutrients, deficiency diseases and lifestyle disorders.",
  ["Digestive, circulatory, respiratory, excretory, nervous systems", "Endocrine glands and hormones", "Vitamins, minerals and deficiency diseases", "Carbohydrates, proteins, fats", "Blood groups and immunity", "Lifestyle diseases: diabetes, hypertension", "Fortification and malnutrition", "Genetic and hormonal disorders"],
  ["Hormone vs enzyme", "Vitamin deficiency diseases"],
  ["biology-basics"], "Organs, nutrients and disorders.", "Link nutrition to public-health programmes.", 3,
  ["S-P1-07", "S-GS3-11"], [r"digestive|circulatory|respiratory|excretory|nervous system", r"endocrine|hormone|insulin|thyroid", r"vitamin [A-K]|scurvy|rickets|beriberi|night blindness", r"protein|carbohydrate|\bfats?\b", r"blood group|haemoglobin|hemoglobin", r"diabetes|hypertension|obesity", r"fortification|anaemia|anemia", r"\bpancreas|\bliver\b|\bkidney"], ["R-NCERT", "R-DST"], cross_ids=["governance-food-security-pds"], related=["biology-basics", "health-diseases"])
X(T, "genetics-evolution", "A", "Genetics, heredity and evolution",
  "Mendelian genetics, DNA structure, mutations, genomics and theories of evolution.",
  ["Mendel's laws; dominant and recessive traits", "Chromosomes, genes, sex determination", "DNA replication, transcription, translation", "Mutation and genetic disorders", "Human genome project and genome sequencing", "Darwin, natural selection, speciation", "Population genetics basics", "DNA fingerprinting and forensics"],
  ["Genotype vs phenotype", "Gene vs allele", "Natural vs artificial selection"],
  ["biology-basics"], "Definitions and examples.", "Connect genetics to biotechnology and ethics.", 3,
  ["S-P1-07", "S-GS3-11", "S-GS3-13"], [r"Mendel", r"chromosome|allele|genotype|phenotype", r"mutation", r"Human Genome|genome sequencing|\bGenomeIndia\b", r"Darwin|natural selection|\bevolution(ary)?\b|speciation", r"DNA (finger)?print", r"genetic (disorder|disease)|sickle cell|thalassemia|Down syndrome", r"transcription|translation|replication"], ["R-NCERT", "R-DST"], related=["biotechnology-genetics", "biology-basics"])
X(T, "vaccines-immunology", "B", "Vaccines, immunity and pandemics",
  "Types of vaccines, immunisation programmes and pandemic response technology.",
  ["Innate and adaptive immunity; antibodies", "Vaccine types: live attenuated, inactivated, mRNA, vector", "Universal Immunisation Programme and Mission Indradhanush", "Herd immunity", "COVID-19 vaccines and their development", "Cold chain and logistics", "Epidemic Diseases Act and disease surveillance", "Vaccine hesitancy and misinformation"],
  ["Vaccine vs antiserum", "Live vs inactivated vaccine", "Herd immunity vs natural immunity"],
  ["health-diseases"], "Types and programmes.", "Evaluate vaccine delivery and surveillance.", 3,
  ["S-GS3-11", "S-GS3-12", "S-P1-07"], [r"vaccin", r"mRNA|viral vector", r"herd immunity", r"antibod|antigen", r"Indradhanush|Universal Immunisation", r"cold chain", r"Epidemic Diseases Act", r"COVID|Covaxin|Covishield|coronavirus", r"immunity|immunisation"], ["R-DST", "R-PIB", "R-NCERT"], cross_ids=["disaster-epidemics-biological-disasters"], related=["health-diseases"])
X(T, "medical-technology-drugs", "B", "Medical technology, drugs and diagnostics",
  "Imaging, robotics and digital health, and regulation of drugs and medical devices.",
  ["Imaging: X-ray, CT, MRI, ultrasound", "Robotic surgery and telemedicine", "Generic drugs and patents; compulsory licensing", "Drug regulation (CDSCO) and clinical trials", "Medical devices regulation", "AYUSH and traditional medicine", "Digital health records", "Antimicrobial resistance"],
  ["Generic vs branded drug", "CT vs MRI", "Patent vs compulsory licence"],
  ["health-diseases"], "Techniques and regulations.", "Discuss affordability, regulation and indigenous drug capacity.", 3,
  ["S-GS3-11", "S-GS3-13", "S-P1-07"], [r"\bMRI\b|\bCT scan|X-ray|ultrasound", r"robotic surgery|telemedicine|e-?Sanjeevani", r"generic (drug|medicine)", r"compulsory licen[cs]", r"\bCDSCO\b|clinical trial", r"\bAYUSH\b|Ayurveda|Unani|Siddha", r"medical device", r"antimicrobial resistance|\bAMR\b", r"pharmaceutical"], ["R-DST", "R-PIB"], cross_ids=["governance-health-policy"], related=["health-diseases"])
X(T, "astronomy-astrophysics", "C", "Astronomy and astrophysics",
  "Stars, galaxies, black holes, telescopes and recent discoveries.",
  ["Life cycle of stars; supernova, neutron star, black hole", "Galaxies, Milky Way and the Big Bang", "Gravitational waves and LIGO-India", "Exoplanets and habitability", "Telescopes: Hubble, James Webb, Astrosat", "Solar physics and space weather", "Dark matter and dark energy", "Observatories in India"],
  ["Black hole vs neutron star", "Asteroid vs comet vs meteor"],
  ["space-technology"], "Terms and instruments.", "Link discoveries to Indian science missions.", 3,
  ["S-GS3-13", "S-GS3-11", "S-P1-07"], [r"black hole|neutron star|supernova|pulsar", r"gravitational wave|\bLIGO\b", r"exoplanet|habitable", r"James Webb|Hubble|Astrosat|telescope", r"Big Bang|dark matter|dark energy", r"galax", r"asteroid|comet|meteor", r"solar (flare|wind|storm)|sunspot", r"Milky Way"], ["R-ISRO", "R-DST", "R-NCERT"], cross_ids=["geography-astronomy-earth-sun"], related=["space-technology"])
X(T, "space-sector-commercial", "C", "Space sector reforms, private players and space policy",
  "Opening up the space sector, regulator IN-SPACe, and space law and policy.",
  ["IN-SPACe and NewSpace India Limited", "Private launch vehicles and satellites (Skyroot, Agnikul)", "Space policy and FDI", "Satellite communication and spectrum", "Space debris and sustainability", "Outer Space Treaty and Artemis Accords", "Earth observation commercial use", "Space for defence and strategic needs"],
  ["ISRO vs IN-SPACe vs NSIL"],
  ["space-technology"], "Bodies and roles.", "Evaluate private participation and space security.", 2,
  ["S-GS3-13", "S-GS3-12"], [r"IN-?SPACe|NewSpace India|\bNSIL\b", r"Skyroot|Agnikul|private (space|satellite|launch)", r"space (policy|sector|economy|law)", r"Outer Space Treaty|Artemis Accords", r"space debris", r"satellite (communication|internet)|Starlink", r"Earth observation"], ["R-ISRO", "R-PIB"], cross_ids=["security-defence-reforms-procurement"], related=["space-technology"])
X(T, "energy-storage-ev-hydrogen", "D", "Batteries, electric vehicles, hydrogen and clean energy technologies",
  "Technologies behind storage, mobility and the hydrogen economy.",
  ["Lithium-ion and alternative batteries; recycling", "Electric vehicles and charging; FAME and PLI", "Fuel cells and green hydrogen", "Solar PV, wind and hybrid systems", "Smart grids and storage", "Small modular reactors", "Biofuels and ethanol blending", "Critical minerals for the energy transition"],
  ["Green vs grey vs blue hydrogen", "Battery vs fuel cell"],
  ["materials-nanotechnology"], "Technologies and missions.", "Assess technology readiness and supply-chain risks.", 3,
  ["S-GS3-13", "S-GS3-11", "S-P1-07"], [r"lithium|battery|batteries", r"electric vehicle|\bEV\b|\bFAME\b", r"green hydrogen|hydrogen (fuel|economy|mission|energy)|fuel cell", r"smart grid|energy storage", r"solar (cell|panel|PV)|photovoltaic", r"ethanol blending|biofuel", r"small modular reactor", r"critical mineral"], ["R-PIB", "R-DST", "R-NITI"], cross_ids=["environment-renewable-energy-green-tech", "economy-energy-sector-economy"], related=["materials-nanotechnology", "nuclear-energy"])
X(T, "ocean-polar-science-missions", "D", "Ocean, polar and mission-mode science programmes",
  "India's deep-ocean, Antarctic and Arctic science and recent national missions.",
  ["Deep Ocean Mission and Samudrayaan", "Antarctic stations: Maitri, Bharati; Arctic: Himadri", "Indian Antarctic programme and Antarctic Treaty", "INCOIS and tsunami warning", "National Quantum Mission, IndiaAI and Semicon India", "Mission Shakti and defence tech missions", "Weather and climate missions (Mission Mausam)", "Science and Technology diplomacy"],
  ["Antarctic Treaty vs Arctic Council"],
  [], "Names, locations and aims.", "Link science missions to strategy and resources.", 2,
  ["S-GS3-12", "S-GS3-13"], [r"Deep Ocean Mission|Samudrayaan|Matsya", r"Antarctic|Maitri|Bharati station|Arctic|Himadri", r"\bINCOIS\b", r"National Quantum Mission|IndiaAI|Semicon India", r"Mission Shakti", r"Mission Mausam", r"polar (research|region)"], ["R-DST", "R-PIB"], cross_ids=["environment-marine-coastal-crz"], related=["science-institutions-achievements"])

# ================================================================ DISASTER MANAGEMENT
D = "disaster"
X(D, "epidemics-biological-disasters", "B", "Epidemics, pandemics and biological disasters",
  "Biological hazards, surveillance and pandemic management in India.",
  ["Epidemic, pandemic, endemic: meaning", "Epidemic Diseases Act and Disaster Management Act use during COVID-19", "Integrated Disease Surveillance Programme", "International Health Regulations and WHO", "Zoonotic spillover and One Health", "Biosafety and bioterrorism", "Lockdowns, containment and health logistics", "Lessons: preparedness, vaccines, data"],
  ["Epidemic vs pandemic", "Biosafety vs biosecurity"],
  ["disaster-disaster-management-framework"], "Acts and concepts.", "Evaluate pandemic governance and federal coordination.", 3,
  ["S-GS3-15", "S-GS3-11"], [r"pandemic|epidemic", r"Epidemic Diseases Act", r"COVID|coronavirus|lockdown", r"One Health|zoono", r"International Health Regulations|\bWHO\b(?=.*(emergency|PHEIC))", r"bioterror|biological (weapon|hazard|disaster)", r"disease surveillance|\bIDSP\b", r"quarantine"], ["R-NDMA", "R-MHA", "R-DST"], cross_ids=["scitech-vaccines-immunology"], related=["man-made-disasters"])
X(D, "cbrn-hazards", "B", "Chemical, biological, radiological and nuclear (CBRN) hazards",
  "Mass-casualty hazards from CBRN agents and the response framework.",
  ["Chemical agents and industrial chemical hazards", "Radiological dispersal and nuclear accidents (Chernobyl, Fukushima)", "Biological agents", "NDMA CBRN guidelines and specialised NDRF units", "Hazardous waste and transportation rules", "Chemical Weapons Convention and OPCW", "Nuclear safety: AERB", "Emergency planning and evacuation"],
  ["Nuclear accident vs radiological emergency", "Chemical vs biological weapon"],
  ["disaster-disaster-management-framework"], "Agents, accidents and bodies.", "Assess preparedness for low-probability high-impact events.", 2,
  ["S-GS3-15", "S-GS3-13"], [r"\bCBRN\b|chemical, biological, radiological", r"Chernobyl|Fukushima|Three Mile Island", r"Chemical Weapons Convention|\bOPCW\b", r"\bAERB\b|Atomic Energy Regulatory", r"radiological|radiation (hazard|emergency)", r"hazardous (waste|chemical)", r"nuclear (accident|safety|emergency)"], ["R-NDMA", "R-DAE"], cross_ids=["scitech-nuclear-energy"], related=["man-made-disasters"])
X(D, "wildfires-heat-waves", "B", "Forest fires, heat waves and extreme temperature hazards",
  "Causes, impacts and management of wildfires and heat and cold waves.",
  ["Forest fire causes and seasons in India", "Forest Survey fire alerts and fire lines", "Heat wave criteria and heat action plans", "Urban heat island and vulnerable groups", "Cold waves and fog", "Health impacts and cooling strategies", "Climate change and extreme temperatures", "Community fire management"],
  ["Wildfire vs controlled burning", "Heat wave vs heat stroke"],
  ["disaster-disaster-management-framework"], "Criteria and plans.", "Evaluate early warning and local action plans.", 2,
  ["S-GS3-15", "S-GS3-14"], [r"forest fire|wildfire", r"heat ?wave|heat action plan|heat stroke", r"urban heat island", r"cold wave|fog", r"fire line|fire alert", r"controlled burning", r"extreme temperature"], ["R-NDMA", "R-IMD", "R-MOEF"], cross_ids=["environment-forest-resources-policy"], related=["hydro-meteorological-disasters"])
X(D, "community-preparedness-capacity", "C", "Community preparedness, capacity building and technology in disaster management",
  "Training, awareness, early warning and inclusive approaches at local level.",
  ["Aapda Mitra and civil defence volunteers", "NIDM and training institutions", "Mock drills and school safety", "Common Alerting Protocol and cell broadcast", "Gender- and disability-inclusive DRR", "Role of media and social media", "Local knowledge and traditional practices", "Insurance and livelihoods protection"],
  ["Capacity building vs awareness", "Top-down vs community-based approach"],
  ["disaster-disaster-management-framework"], "Bodies and tools.", "Argue for bottom-up resilience.", 2,
  ["S-GS3-15"], [r"Aapda Mitra|volunteer", r"\bNIDM\b|National Institute of Disaster", r"mock drill|school safety", r"Common Alerting Protocol|cell broadcast|early warning", r"community[- ]based", r"traditional (knowledge|practice)", r"capacity building", r"gender-sensitive|disability-inclusive"], ["R-NDMA"], related=["relief-recovery-financing"])
X(D, "lessons-major-disasters", "C", "Lessons from major disasters in India and abroad",
  "Case studies of major disasters and the policy changes they triggered.",
  ["Bhuj earthquake 2001 and the Disaster Management Act", "Indian Ocean tsunami 2004", "Uttarakhand floods 2013 and Himalayan development", "Kerala floods 2018 and dam management", "Odisha cyclones and zero-casualty approach", "Bhopal gas tragedy", "Japan's Tohoku and Nepal's 2015 earthquake", "Common lessons: governance and land use"],
  ["Preparedness vs response failure"],
  ["disaster-disaster-management-framework"], "Events and outcomes.", "Use cases as evidence in answers.", 2,
  ["S-GS3-15"], [r"Bhuj|Gujarat earthquake", r"Indian Ocean tsunami|2004 tsunami", r"Uttarakhand (flood|disaster)|Kedarnath", r"Kerala flood", r"Odisha cyclone|Phailin|Fani|Super Cyclone", r"Nepal earthquake|Tohoku|Fukushima", r"Bhopal", r"Chamoli|Joshimath|Wayanad"], ["R-NDMA", "R-MHA"], related=["hydro-meteorological-disasters", "geological-disasters"])

# ================================================================ SECURITY
Sc = "security"
X(Sc, "lwe-naxalism", "A", "Left-wing extremism (Naxalism)",
  "Origins, geography, causes and policy response to Left-wing extremism.",
  ["Naxalbari movement 1967 to Maoist consolidation", "Affected regions: Red Corridor and Bastar", "Causes: land, forest rights, displacement, governance gaps", "Policy: SAMADHAN, security and development approach", "Salwa Judum and the Supreme Court", "Surrender and rehabilitation policies", "Role of CAPFs and state police; Greyhounds", "Aspirational districts and road connectivity"],
  ["Naxalism vs insurgency", "Security approach vs development approach"],
  ["external-actors-extremism"], "Timeline, regions and schemes.", "Assess integrated security–development strategy.", 4,
  ["S-GS3-16", "S-GS3-17"], [r"Naxal|Maoist|Left[- ]Wing Extremis", r"Red Corridor|Bastar|Dantewada", r"SAMADHAN|Salwa Judum|Greyhounds", r"aspirational district", r"tribal.*(displacement|alienation)", r"Scheduled Areas.*extremis"], ["R-MHA", "R-ARC"], cross_ids=["society-tribal-society-issues"], related=["external-actors-extremism"])
X(Sc, "organised-crime-narcotics", "A", "Organised crime and narcotics trafficking",
  "Drug trafficking, arms and human smuggling, and legal responses.",
  ["NDPS Act and Narcotics Control Bureau", "Golden Crescent and Golden Triangle routes", "Drone-based smuggling across borders", "Arms trafficking and counterfeit currency", "Hawala and money laundering", "Narco-terror and gang networks", "International conventions on drugs", "Prevention, treatment and rehabilitation"],
  ["Narcotic vs psychotropic substance", "Smuggling vs trafficking"],
  ["border-management-organised-crime"], "Laws, bodies and routes.", "Balance enforcement with public-health approaches.", 3,
  ["S-GS3-19", "S-GS3-17"], [r"NDPS|narcotic|drug (trafficking|abuse|menace)", r"Golden (Crescent|Triangle)", r"\bNCB\b|Narcotics Control", r"counterfeit (currency|note)", r"hawala", r"arms (trafficking|smuggling)", r"narco[- ]terror", r"organi[sz]ed crime|gang"], ["R-MHA", "R-UN"], related=["border-management-organised-crime", "terrorism-counter-terrorism"])
X(Sc, "social-media-information-warfare", "B", "Social media, disinformation and information warfare",
  "How communication networks and social media create security risks and how the State regulates them.",
  ["Radicalisation and recruitment online", "Fake news, deepfakes and election influence", "IT Act Section 69A blocking and IT Rules 2021", "Intermediary liability and safe harbour", "Internet shutdowns and rights", "Hybrid and information warfare", "Role of media in security reporting and ethics", "Data localisation and platform regulation"],
  ["Misinformation vs disinformation", "Censorship vs regulation"],
  ["cyber-security"], "Laws and risks.", "Balance security and free expression.", 3,
  ["S-GS3-18"], [r"social media|social networking", r"fake news|disinformation|misinformation|deepfake", r"Section 69A|IT Rules|Information Technology Rules|intermediary", r"internet shutdown", r"information warfare|hybrid war|propaganda", r"radicali[sz]ation", r"data localisation", r"safe harbour"], ["R-MEITY", "R-CERT", "R-MHA"], cross_ids=["polity-fr-freedoms"], related=["cyber-security"])
X(Sc, "police-reforms-criminal-law", "A", "Police reforms and the new criminal laws",
  "Structure and reform of policing and the replacement of colonial-era criminal codes.",
  ["Prakash Singh judgment and police reform directives", "Bharatiya Nyaya Sanhita, Nagarik Suraksha Sanhita, Sakshya Adhiniyam", "Police modernisation, CCTNS and forensic science", "Police–public relations and accountability", "Custodial violence and human rights", "State vs central police roles", "Crime and criminal justice statistics (NCRB)", "Community policing"],
  ["IPC vs BNS", "Police vs public order (List II)"],
  ["security-security-forces-agencies"], "Laws, bodies and judgments.", "Evaluate implementation and civil-liberty safeguards.", 3,
  ["S-GS3-20", "S-GS3-17"], [r"police reform", r"Prakash Singh", r"Bharatiya Nyaya|Nagarik Suraksha|Sakshya Adhiniyam|\bBNS\b|\bBNSS\b", r"\bIPC\b|Indian Penal Code|\bCrPC\b", r"\bNCRB\b", r"\bCCTNS\b|police modernisation", r"custodial (violence|death)", r"community policing", r"forensic"], ["R-MHA", "R-ARC", "R-INDIACODE"], cross_ids=["polity-fr-freedoms"], related=["security-security-forces-agencies"])
X(Sc, "national-security-strategy-intelligence", "C", "National security strategy, intelligence and strategic culture",
  "Doctrine, institutions and challenges of India's strategic policy.",
  ["National Security Council system and NSA", "Intelligence reforms after Kargil and 26/11", "Nuclear doctrine: credible minimum deterrence and no-first-use", "Two-front challenge and strategic partnerships", "Comprehensive national security: economic, energy, cyber", "Civil–military relations", "Strategic autonomy and defence diplomacy", "Crisis management and escalation"],
  ["Deterrence vs defence", "Credible minimum deterrence vs massive retaliation"],
  ["security-security-forces-agencies"], "Doctrine and bodies.", "Argue for an integrated national security strategy.", 3,
  ["S-GS3-20", "S-GS3-17"], [r"National Security (Council|Strategy|Adviser)|\bNSCS\b", r"Kargil Review|Group of Ministers", r"nuclear doctrine|credible minimum deterrence|no[- ]first[- ]use", r"two[- ]front", r"civil[- ]military", r"comprehensive (national )?security", r"strategic (culture|autonomy)", r"intelligence (reform|agenc)"], ["R-MHA", "R-MEA"], cross_ids=["scitech-defence-technology", "ir-global-conflicts-treaties"], related=["defence-reforms-procurement"])

RATIONALE = {
    ("scitech-vaccines-immunology", "disaster-epidemics-biological-disasters"): "Vaccines and surveillance are the technical tools of managing biological disasters.",
    ("scitech-space-sector-commercial", "security-defence-reforms-procurement"): "Space-sector reform and defence procurement overlap in satellite and launch capability for military use.",
    ("scitech-astronomy-astrophysics", "geography-astronomy-earth-sun"): "Earth–Sun geography is the near-field case of the wider astronomy studied here.",
    ("scitech-energy-storage-ev-hydrogen", "economy-energy-sector-economy"): "Storage, EVs and hydrogen change the costs and structure of the energy sector.",
    ("scitech-medical-technology-drugs", "governance-health-policy"): "Drug regulation and affordability link technology to health policy.",
    ("scitech-ocean-polar-science-missions", "environment-marine-coastal-crz"): "Ocean missions and coastal regulation both rely on marine science.",
    ("scitech-human-physiology-nutrition", "governance-food-security-pds"): "Nutrition science underpins food-security and fortification programmes.",
    ("disaster-cbrn-hazards", "scitech-nuclear-energy"): "Nuclear safety and radiological emergencies connect nuclear technology to disaster response.",
    ("disaster-wildfires-heat-waves", "environment-forest-resources-policy"): "Forest-fire management is part of forest policy and conservation.",
    ("security-lwe-naxalism", "society-tribal-society-issues"): "Tribal displacement and forest rights are root causes discussed under Society.",
    ("security-social-media-information-warfare", "polity-fr-freedoms"): "Blocking and regulation of online content is tested against Article 19(1)(a).",
    ("security-police-reforms-criminal-law", "polity-fr-freedoms"): "Policing powers are limited by Articles 20–22 and personal liberty.",
    ("security-national-security-strategy-intelligence", "scitech-defence-technology"): "Strategic doctrine depends on the technology base studied under Science & Technology.",
}
