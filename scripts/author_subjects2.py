"""Phase D batch 2: Science & Technology, Art & Culture, Ancient and Medieval History (in the History subject),
Society, Governance, International Relations, Security, Disaster Management. Same rules as batch 1:
AI-written from general knowledge, `draft-unreviewed`, no book chapters, no statistics.
"""
import author_polity as P
import author_subjects as S
from author_subjects import X

NEW_RES = [
    dict(id="R-DRDO", title="DRDO", author="Defence Research and Development Organisation", type="official-primary", url="https://www.drdo.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-DAE", title="Department of Atomic Energy", author="Govt. of India", type="official-primary", url="https://dae.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-DST", title="Department of Science & Technology", author="Govt. of India", type="official-primary", url="https://dst.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-MEITY", title="Ministry of Electronics and IT", author="Govt. of India", type="official-primary", url="https://www.meity.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-CERT", title="CERT-In (Indian Computer Emergency Response Team)", author="MeitY", type="official-primary", url="https://www.cert-in.org.in/", access="free-online", url_status="http-200"),
    dict(id="R-MEA", title="Ministry of External Affairs", author="Govt. of India", type="official-primary", url="https://www.mea.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-UN", title="United Nations", author="UN", type="official-primary", url="https://www.un.org/", access="free-online", url_status="http-200"),
    dict(id="R-MHA", title="Ministry of Home Affairs", author="Govt. of India", type="official-primary", url="https://www.mha.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-NDMA", title="National Disaster Management Authority", author="NDMA", type="official-primary", url="https://ndma.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-UNESCO", title="UNESCO World Heritage Centre", author="UNESCO", type="official-primary", url="https://whc.unesco.org/", access="free-online", url_status="http-200"),
    dict(id="R-ASI", title="Archaeological Survey of India", author="Govt. of India", type="official-primary", url="https://asi.nic.in/", access="free-online", url_status="http-200"),
    dict(id="R-SNA", title="Sangeet Natak Akademi", author="Govt. of India", type="official-primary", url="https://www.sangeetnatak.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-WCD", title="Ministry of Women and Child Development", author="Govt. of India", type="official-primary", url="https://wcd.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-MSJE", title="Ministry of Social Justice and Empowerment", author="Govt. of India", type="official-primary", url="https://socialjustice.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-RTI", title="RTI Online portal", author="Govt. of India", type="official-primary", url="https://rti.gov.in/", access="free-online", url_status="http-200"),
    dict(id="R-SINGHANIA", title="Indian Art and Culture", author="Nitin Singhania", publisher="McGraw Hill", edition="not verified", type="standard-book", url=None, access="purchase", url_status="n/a"),
]
for r in NEW_RES:
    r["last_checked"] = P.CHECKED
    r.setdefault("publisher", None); r.setdefault("edition", None)
P.RES.extend(NEW_RES)

# history gets three more groups (ancient, medieval, culture); new subjects get their own groups
S.GROUPS["history"] = S.GROUPS["history"] + [("E", "Ancient India"), ("F", "Medieval India"), ("G", "Art, architecture and culture")]
S.GROUPS.update({
    "scitech": [("A", "Foundations: physics, chemistry, biology"), ("B", "Health and biotechnology"), ("C", "Space, defence and nuclear"), ("D", "Information technology and emerging fields")],
    "society": [("A", "Indian society and its diversity"), ("B", "Social issues and globalisation")],
    "governance": [("A", "Policy, delivery and accountability"), ("B", "Social sector and vulnerable sections")],
    "ir": [("A", "India and the world")],
    "security": [("A", "Internal security"), ("B", "Cyber and border security")],
    "disaster": [("A", "Disaster management")],
})

# ================================================================== SCIENCE & TECHNOLOGY  (scitech)
T = "scitech"
X(T, "physics-basics", "A", "Everyday physics: motion, energy, light and electricity",
  "Core physics ideas that recur in general-science questions: forces and motion, work and energy, waves and light, electricity and magnetism.",
  ["Newton's laws, momentum, gravitation", "Work, energy, power", "Heat and thermodynamics basics", "Sound and waves", "Reflection, refraction, lenses, total internal reflection", "Electric current, resistance, circuits", "Magnetism and electromagnetic induction", "Electromagnetic spectrum", "Semiconductors and superconductivity (qualitative)"],
  ["Mass vs weight", "Speed vs velocity", "AC vs DC"],
  [], "Definitions, units and standard examples.", "Link physics to technology (fibre optics, sensors, energy devices).", 5,
  ["S-P1-07", "S-GS3-11"], [r"\bNewton\b", r"velocity|acceleration", r"refraction|reflection|total internal", r"\blens\b", r"electric current|resistance", r"magnet", r"electromagnetic", r"sound|wave", r"superconduct|semiconductor", r"kinetic energy|potential energy", r"\bphoton\b|laser"], ["R-NCERT", "R-DST"], related=["materials-nanotechnology"])
X(T, "chemistry-basics", "A", "Everyday chemistry: elements, compounds, materials and reactions",
  "Basic chemistry used in general-science questions: atomic structure, periodic trends, acids and bases, metals, carbon compounds and common materials.",
  ["Atoms, isotopes, periodic table trends", "Chemical bonding", "Acids, bases, salts, pH", "Metals and non-metals; alloys", "Carbon compounds; hydrocarbons", "Polymers and plastics", "Fertilisers and pesticides", "Radioactivity (conceptual)", "Everyday chemicals: soaps, detergents, cement, glass"],
  ["Isotope vs isobar", "Alloy vs compound", "Thermoplastic vs thermosetting"],
  [], "Terms and common examples.", "Connect chemistry to pollution, health and materials technology.", 4,
  ["S-P1-07", "S-GS3-11"], [r"isotope", r"periodic table", r"\bacid|\bbase\b|\bpH\b", r"\balloy", r"polymer", r"hydrocarbon", r"\bplastic", r"chemical (reaction|compound|element)", r"fertili[sz]er|pesticide", r"catalyst", r"\bgas(es)? (is|are) used|noble gas"], ["R-NCERT"], related=["materials-nanotechnology"])
X(T, "biology-basics", "A", "Life science basics: cell, genetics, physiology and plants",
  "Fundamentals of biology that underlie health, agriculture and biotechnology questions.",
  ["Cell structure and cell division", "DNA, RNA, genes, heredity", "Human body systems", "Nutrition: vitamins, minerals, deficiency diseases", "Photosynthesis and respiration", "Plant hormones and tissues", "Microorganisms: bacteria, viruses, fungi", "Evolution basics", "Animal classification"],
  ["DNA vs RNA", "Mitosis vs meiosis", "Vitamin vs mineral deficiency"],
  [], "Terms, structures and standard examples.", "Link biology to disease, agriculture and biotechnology.", 5,
  ["S-P1-07", "S-GS3-11"], [r"\bcell\b|chromosome", r"\bDNA\b|\bRNA\b|\bgene\b", r"vitamin", r"photosynthesis|respiration", r"enzyme|hormone", r"bacteri|virus|fung", r"mitosis|meiosis", r"deficiency", r"blood (group|cell|pressure|clot)|kidney|liver"], ["R-NCERT", "R-DST"], related=["health-diseases", "biotechnology-genetics"])
X(T, "health-diseases", "B", "Health, diseases and public-health technology",
  "Common communicable and non-communicable diseases, vaccines, antimicrobial resistance and public-health programmes.",
  ["Bacterial, viral, protozoan and fungal diseases and vectors", "Vaccines and immunity", "Antibiotics and antimicrobial resistance", "Non-communicable diseases", "Epidemics, pandemics, zoonosis", "Diagnostics: PCR, antigen tests", "Mission-mode health programmes", "Nutrition and malnutrition"],
  ["Epidemic vs pandemic vs endemic", "Active vs passive immunity", "Vaccine vs antibiotic"],
  ["biology-basics"], "Diseases, vectors and vaccines.", "Discuss public-health policy, AMR and health-technology.", 4,
  ["S-GS3-11", "S-GS2-13", "S-P1-07"], [r"disease", r"vaccin", r"antibiotic|antimicrobial", r"pandemic|epidemic|endemic", r"malaria|tuberculosis|dengue|HIV|hepatitis|cholera|polio|measles|COVID", r"\bPCR\b", r"immun", r"zoono", r"cancer|diabetes"], ["R-NCERT", "R-DST", "R-PIB"], cross_ids=["governance-social-sector-welfare"], related=["biotechnology-genetics"])
X(T, "biotechnology-genetics", "B", "Biotechnology and genetics",
  "Tools and applications of biotechnology: recombinant DNA, genome editing, GM crops, stem cells, biosafety and IPR.",
  ["Recombinant DNA technology", "PCR and gene sequencing", "Genome editing (CRISPR-Cas9)", "Genetically modified crops and biosafety", "Stem cells and cloning", "Tissue culture", "Biofertilisers and biopesticides", "Gene therapy", "Bioethics and IPR in biotech"],
  ["GM crop vs hybrid crop", "Somatic cell vs embryonic stem cell", "Cloning vs genome editing"],
  ["biology-basics"], "Techniques and applications.", "Evaluate benefits, risks and regulation (e.g. GM crops).", 4,
  ["S-GS3-13", "S-GS3-11", "S-P1-07"], [r"biotechnolog", r"recombinant", r"CRISPR|genome edit", r"genetically modified|\bGM crop|Bt cotton|Bt brinjal", r"stem cell", r"\bcloning", r"tissue culture", r"gene therapy|gene editing", r"genome", r"biosafety", r"transgenic"], ["R-NCERT", "R-DST"], cross_ids=["environment-sustainable-agriculture-forestry"], related=["health-diseases"])
X(T, "space-technology", "C", "Space technology and ISRO",
  "Launch vehicles, satellites, planetary missions and applications of space technology.",
  ["Launch vehicles: PSLV, GSLV, SSLV and orbit types", "Satellite types: communication, remote sensing, navigation (NavIC)", "Geostationary vs polar orbits", "Chandrayaan, Mangalyaan, Aditya-L1, Gaganyaan", "Space applications in agriculture, disaster, communications", "Space economy and private participation", "Global missions and space debris", "Astronomy basics: planets, stars, black holes"],
  ["Geostationary vs polar satellite orbit", "Cryogenic vs semi-cryogenic engine", "Remote sensing vs navigation satellite"],
  ["physics-basics"], "Vehicles, orbits and missions.", "Discuss applications, strategic value and commercialisation of space.", 4,
  ["S-GS3-13", "S-GS3-12", "S-P1-07"], [r"\bISRO\b", r"\bPSLV\b|\bGSLV\b|\bSSLV\b", r"satellite", r"Chandrayaan|Mangalyaan|Aditya|Gaganyaan", r"geostationary|polar orbit|orbit", r"\bNavIC\b|GPS|navigation system", r"space (mission|station|debris|technology)", r"rocket|launch vehicle", r"cryogenic", r"black hole|exoplanet|telescope"], ["R-ISRO", "R-NCERT", "R-DST"], related=["defence-technology", "physics-basics"])
X(T, "defence-technology", "C", "Defence technology and indigenisation",
  "Missiles, platforms and indigenous defence programmes, plus nuclear doctrine basics.",
  ["Missile classes: ballistic, cruise, surface-to-air; Agni, Prithvi, BrahMos, Akash", "Integrated Guided Missile Development Programme", "Indigenous platforms (aircraft, ships, tanks)", "DRDO and defence public-sector units", "Atmanirbhar defence policy and procurement", "Nuclear triad and no-first-use", "Hypersonic and directed-energy technology", "Defence exercises (conceptual)"],
  ["Ballistic vs cruise missile", "Strategic vs tactical weapon"],
  ["space-technology"], "Names, ranges and categories.", "Discuss indigenisation and strategic autonomy in defence.", 3,
  ["S-GS3-12", "S-GS3-20", "S-P1-07"], [r"\bDRDO\b", r"missile", r"\bAgni\b|\bPrithvi\b|BrahMos|\bAkash\b", r"INS |aircraft carrier|submarine", r"\bTejas\b|\bLCA\b", r"nuclear (triad|doctrine|weapon)", r"no[- ]first[- ]use", r"hypersonic", r"indigenous(ly)? (developed|designed)", r"defence (procurement|technology)"], ["R-DRDO", "R-PIB"], cross_ids=["security-security-forces-agencies"], related=["space-technology"])
X(T, "nuclear-energy", "C", "Nuclear science and energy",
  "Nuclear fission and fusion, India's three-stage programme, safeguards and radiation.",
  ["Fission vs fusion", "Reactors: PHWR, light water, fast breeder", "India's three-stage nuclear programme and thorium", "Nuclear safeguards, NPT, NSG, CTBT", "Radioisotopes and applications", "Radiation safety", "Nuclear liability law", "Small modular reactors"],
  ["Fission vs fusion", "Moderator vs coolant"],
  ["physics-basics"], "Concepts and Indian programme stages.", "Evaluate nuclear energy in India's energy transition.", 3,
  ["S-GS3-13", "S-GS3-12", "S-P1-07"], [r"nuclear (energy|power|reactor|fission|fusion)", r"\bfission\b|\bfusion\b", r"thorium", r"breeder", r"heavy water", r"\bNPT\b|\bNSG\b|\bCTBT\b|Nuclear Suppliers", r"uranium|plutonium", r"radioactiv", r"Department of Atomic Energy"], ["R-DAE", "R-NCERT"], cross_ids=["environment-renewable-energy-green-tech"], related=["physics-basics"])
X(T, "information-technology-cyber", "D", "Information technology, communications and AI",
  "Computing, networks, mobile technology, artificial intelligence and related policy questions.",
  ["Internet, protocols, cloud, big data", "Mobile generations (4G, 5G) and spectrum", "Artificial intelligence, machine learning, generative AI", "Blockchain and cryptocurrencies", "Internet of Things", "Quantum technologies (qualitative)", "Semiconductors and chip manufacturing", "Data protection and digital public infrastructure", "Cyber attacks: phishing, ransomware, malware"],
  ["AI vs machine learning vs deep learning", "4G vs 5G", "Blockchain vs cryptocurrency"],
  ["physics-basics"], "Terms and what each technology does.", "Discuss opportunity, risk and regulation of emerging digital technology.", 4,
  ["S-GS3-13", "S-GS3-18"], [r"artificial intelligence|machine learning|generative AI|deep learning", r"blockchain|cryptocurrenc|bitcoin", r"\b5G\b|\b4G\b|spectrum", r"Internet of Things|\bIoT\b", r"quantum (computing|technology|key)", r"cloud computing|big data", r"semiconductor", r"data protection|digital public infrastructure", r"phishing|ransomware|malware|cyber", r"\bWi-?Fi\b|broadband|optical fi[bv]re"], ["R-MEITY", "R-CERT", "R-PIB"], cross_ids=["security-cyber-security"], related=["materials-nanotechnology"])
X(T, "materials-nanotechnology", "D", "Materials, nanotechnology and robotics",
  "Advanced materials, nanoscale science, robotics and automation, and their applications.",
  ["Nanomaterials: properties and uses", "Graphene and carbon nanotubes", "Smart and composite materials", "3D printing (additive manufacturing)", "Robotics and automation", "Drones and unmanned systems", "Superconductors and new batteries", "Biodegradable and bio-based materials"],
  ["Nanoparticle vs nanotube", "Additive vs subtractive manufacturing"],
  ["chemistry-basics", "physics-basics"], "Terms and use-cases.", "Assess benefits, safety and regulation of emerging materials.", 2,
  ["S-GS3-13", "S-GS3-11"], [r"nano", r"graphene", r"3D print|additive manufacturing", r"robot", r"drone|unmanned", r"composite material|smart material", r"lithium|battery", r"carbon fi[bv]re"], ["R-DST", "R-PIB"], related=["information-technology-cyber"])
X(T, "science-institutions-achievements", "D", "Science institutions, policy and achievements of Indians",
  "Indian scientific institutions, missions, awards and notable scientists, plus indigenisation of technology and IPR.",
  ["CSIR, ICMR, DST, DBT, DRDO, DAE, ISRO roles", "Science policy and missions", "Intellectual property rights: patents, copyrights, trademarks, GI", "Indigenisation: vaccines, defence, semiconductors", "Notable Indian scientists and discoveries", "Nobel laureates linked to India", "International research collaborations"],
  ["Patent vs copyright vs trademark vs geographical indication"],
  [], "Institutions and what each does.", "Discuss self-reliance in technology and the role of IPR.", 2,
  ["S-GS3-12", "S-GS3-13"], [r"\bCSIR\b|\bICMR\b|Department of Science", r"intellectual property|\bpatent|copyright|trademark|geographical indication|\bGI tag", r"Nobel", r"scientist", r"Bhabha|Raman|Sarabhai|Kalam|Bose\b.*(scientist|physicist)", r"indigenous", r"research institute"], ["R-DST", "R-PIB"], related=["defence-technology", "space-technology"])

# ================================================================== ART & CULTURE, ANCIENT, MEDIEVAL (history)
H = "history"
X(H, "indus-vedic-ancient-foundations", "E", "Prehistory, Indus Valley and the Vedic age",
  "Early human cultures, the Harappan civilisation and the Vedic period.",
  ["Palaeolithic, Mesolithic, Neolithic, Chalcolithic cultures", "Harappan sites, town planning, trade, decline", "Early and later Vedic society and polity", "Vedic literature", "Ironage and Painted Grey Ware", "Rivers of the Rigveda", "Megalithic cultures of the south"],
  ["Early vs later Vedic society", "Harappan vs Vedic culture"],
  [], "Sites, features and periodisation.", "Interpret archaeological evidence and continuity between phases.", 4,
  ["S-P1-02"], [r"Harappa|Indus (Valley|Civili[sz]ation)|Mohenjo", r"Vedic|Rigveda|Atharvaveda|Upanishad", r"Neolithic|Palaeolithic|Paleolithic|Mesolithic|Chalcolithic", r"Painted Grey", r"Lothal|Dholavira|Kalibangan", r"megalith"], ["R-NCERT", "R-ASI"], related=["mauryan-gupta-empires"])
X(H, "buddhism-jainism-mahajanapadas", "E", "Mahajanapadas, Buddhism and Jainism",
  "Sixth-century BCE political change and the rise of heterodox religions.",
  ["Mahajanapadas and Magadha's rise", "Life and teachings of the Buddha", "Buddhist councils, schools, texts", "Mahavira and Jain principles", "Reasons for spread and decline", "Patronage and monasteries", "Buddhist and Jain art and architecture"],
  ["Hinayana vs Mahayana", "Digambara vs Shvetambara"],
  ["indus-vedic-ancient-foundations"], "Teachings, councils and texts.", "Explain social and economic bases of the new religions.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Buddha|Buddhis", r"Jain|Mahavira", r"Mahajanapada", r"Magadha", r"Tripitaka|Jataka", r"Hinayana|Mahayana|Theravada|Vajrayana", r"Buddhist council", r"stupa|vihara|chaitya"], ["R-NCERT", "R-SINGHANIA"], cross_ids=["history-art-architecture-sculpture"], related=["mauryan-gupta-empires"])
X(H, "mauryan-gupta-empires", "E", "Mauryan, post-Mauryan and Gupta periods",
  "Imperial and regional states from the Mauryas to the Guptas: administration, economy, society and culture.",
  ["Chandragupta, Bindusara, Ashoka and the dhamma", "Mauryan administration and Arthashastra", "Edicts and Brahmi script", "Sungas, Kanvas, Kushanas, Satavahanas", "Sangam age", "Gupta polity, economy and culture", "Gold coinage and trade", "Foreign accounts (Megasthenes, Fa-Hien, Hiuen Tsang)", "Harsha and post-Gupta states"],
  ["Mauryan vs Gupta administration", "Ashoka's dhamma vs Buddhism"],
  ["buddhism-jainism-mahajanapadas"], "Rulers, institutions and sources.", "Assess continuity and change in state, economy and society.", 5,
  ["S-P1-02", "S-GS1-01"], [r"Maurya|Ashoka|Asoka|Chandragupta", r"Gupta (period|empire|age)|Samudragupta|Chandragupta II|Kalidasa", r"Satavahana|Kushana|Sunga|Kanva", r"Sangam", r"Arthashastra|Kautilya", r"Megasthenes|Fa[- ]?Hien|Hiuen|Xuanzang", r"Harsha|Harshavardhana", r"edict", r"Brahmi"], ["R-NCERT", "R-ASI"], related=["early-medieval-regional-kingdoms"])
X(H, "early-medieval-regional-kingdoms", "F", "Early medieval and regional kingdoms",
  "Post-Gupta dynasties of north and south India, their administration and society.",
  ["Rajputs, Palas, Pratiharas, Rashtrakutas", "Cholas: local government and maritime power", "Pallavas, Chalukyas", "Temple economy and land grants", "Feudalism debate", "Arab and Turkish incursions", "Kalhana and other chroniclers", "Regional languages and literature"],
  ["Tripartite struggle participants", "Chola vs Mauryan local administration"],
  ["mauryan-gupta-empires"], "Dynasties, regions, features.", "Explain regional state formation and temple-centred economy.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Chola", r"Pallava|Chalukya|Rashtrakuta|Pala\b|Pratihara", r"Rajput", r"Kalhana|Rajatarangini", r"Mahmud of Ghazni|Muhammad (of )?Ghor|Ghori", r"land grant|agrahara", r"Alberuni|Al-?Biruni"], ["R-NCERT"], related=["delhi-sultanate"])
X(H, "delhi-sultanate", "F", "Delhi Sultanate",
  "The Turko-Afghan dynasties of north India (1206–1526): rulers, administration, economy and culture.",
  ["Slave, Khalji, Tughlaq, Sayyid, Lodi dynasties", "Iltutmish, Balban, Alauddin Khalji, Muhammad bin Tughlaq, Firoz Shah", "Iqta system and revenue", "Market control and currency experiments", "Provincial and central administration", "Indo-Islamic architecture and literature", "Invasions: Mongols, Timur"],
  ["Iqta vs jagir (broadly)", "Alauddin's market reforms vs Tughlaq's experiments"],
  ["early-medieval-regional-kingdoms"], "Rulers and their policies.", "Assess state, economy and society under the Sultanate.", 4,
  ["S-P1-02", "S-GS1-01"], [r"Delhi Sultan", r"Iltutmish|Balban|Razia", r"Alauddin Khalji|Alauddin Khilji|Khalji|Khilji", r"Tughlaq|Tughluq", r"Lodi|Sayyid", r"\biqta\b", r"Qutb ?ud[- ]?din|Qutub", r"Ibn Battuta|Amir Khusro|Barani", r"market control|token currency"], ["R-NCERT", "R-SINGHANIA"], related=["mughal-empire"])
X(H, "mughal-empire", "F", "Mughal Empire and the Marathas",
  "Rise, administration, economy and decline of the Mughal Empire and the emergence of the Marathas.",
  ["Babur, Humayun, Sher Shah, Akbar, Jahangir, Shah Jahan, Aurangzeb", "Mansabdari and jagirdari", "Land revenue: Zabt, Dahsala", "Akbar's religious policy", "Mughal art, architecture, painting", "Economy, trade and European companies", "Causes of decline", "Shivaji and the Maratha administration", "Sikh gurus and the Khalsa"],
  ["Mansab vs jagir", "Akbar's vs Aurangzeb's religious policy"],
  ["delhi-sultanate"], "Rulers, institutions and monuments.", "Assess Mughal administration and causes of decline.", 5,
  ["S-P1-02", "S-GS1-01"], [r"Mughal", r"Akbar|Babur|Humayun|Jahangir|Shah Jahan|Aurangzeb", r"Sher Shah", r"mansab|jagirdar|zabt|dahsala", r"Din-i-Ilahi|Sulh-i-kul", r"Shivaji|Maratha|Peshwa", r"Ain-i-Akbari|Abul Fazl", r"Red Fort|Taj Mahal|Fatehpur Sikri", r"Guru (Nanak|Arjan|Gobind|Tegh)|Khalsa"], ["R-NCERT", "R-SINGHANIA"], related=["advent-british-expansion", "delhi-sultanate"])
X(H, "bhakti-sufi-vijayanagara", "F", "Bhakti, Sufism and the Vijayanagara and regional states",
  "Medieval devotional movements and Sufi orders, and the Vijayanagara and Bahmani kingdoms.",
  ["Alvars and Nayanars", "Ramananda, Kabir, Nanak, Chaitanya, Mirabai", "Sufi silsilas: Chishti, Suhrawardi", "Syncretism and vernacular literature", "Vijayanagara polity, Krishnadevaraya", "Bahmani kingdom and successors", "Temple and urban economy in the south"],
  ["Bhakti vs Sufi movement", "Saguna vs nirguna bhakti"],
  ["delhi-sultanate"], "Saints, orders and states.", "Discuss cultural synthesis and social impact.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Bhakti", r"Sufi|Chishti|Suhrawardi|Nizamuddin|Moinuddin", r"Kabir|Guru Nanak|Chaitanya|Mirabai|Tulsidas|Ramananda|Ramanuja|Shankaracharya|Basava", r"Alvar|Nayanar", r"Vijayanagara|Vijayanagar|Krishnadevaraya", r"Bahmani"], ["R-NCERT", "R-SINGHANIA"], related=["mughal-empire"])
X(H, "art-architecture-sculpture", "G", "Indian architecture, sculpture and painting",
  "Styles of temple, cave, stupa and Indo-Islamic architecture, sculpture schools and painting traditions.",
  ["Harappan and Mauryan art", "Stupas, chaityas, viharas, rock-cut caves", "Gandhara, Mathura, Amaravati schools", "Nagara, Dravida, Vesara temple styles", "Indo-Islamic architecture and Mughal gardens", "Mural, miniature and folk painting traditions", "Colonial and modern art", "Iconography of deities and symbols"],
  ["Nagara vs Dravida vs Vesara", "Gandhara vs Mathura school", "Stupa vs chaitya vs vihara"],
  [], "Styles, sites and distinguishing features.", "Relate art forms to patronage, religion and society.", 5,
  ["S-GS1-01", "S-P1-02"], [r"stupa|chaitya|vihara", r"Gandhara|Mathura school|Amaravati", r"Nagara|Dravida|Vesara|shikhara|gopuram", r"temple architecture", r"rock[- ]cut|Ajanta|Ellora|Elephanta", r"miniature|mural|painting|Madhubani|Warli|Pattachitra|Kalamkari", r"sculpture|iconography", r"Konark|Khajuraho|Brihadeshwara|Hampi|Sanchi", r"Indo-Islamic|Qutub Minar|Taj Mahal|Fatehpur", r"Bagh|Pahari|Rajput painting"], ["R-SINGHANIA", "R-NCERT", "R-ASI", "R-UNESCO"], related=["performing-arts-music-dance"])
X(H, "performing-arts-music-dance", "G", "Music, dance and theatre",
  "Classical and folk performing arts of India and the institutions that support them.",
  ["Hindustani and Carnatic music, gharanas, instruments", "Eight classical dance forms and their regions", "Folk dances and theatre forms", "Natyashastra and rasa theory", "Cinema and modern performing arts", "Sangeet Natak Akademi and national awards", "UNESCO intangible cultural heritage in India"],
  ["Hindustani vs Carnatic music", "Classical vs folk dance"],
  [], "Forms, regions and exponents.", "Discuss preservation and promotion of intangible heritage.", 3,
  ["S-GS1-01"], [r"Hindustani|Carnatic|raga|gharana", r"Bharatanatyam|Kathak|Kathakali|Odissi|Kuchipudi|Manipuri|Mohiniyattam|Sattriya", r"folk (dance|theatre|music)", r"Natyashastra", r"Sangeet Natak", r"intangible cultural heritage", r"Yakshagana|Ramlila|Nautanki|Tamasha", r"sitar|sarod|veena|tabla|santoor"], ["R-SINGHANIA", "R-SNA", "R-UNESCO"], related=["art-architecture-sculpture", "literature-languages-philosophy"])
X(H, "literature-languages-philosophy", "G", "Literature, languages, philosophy and religion",
  "Classical and regional languages, major texts, schools of philosophy and religious traditions of India.",
  ["Sanskrit, Pali, Prakrit and classical languages of India", "Epics and Puranas", "Sangam and regional literature", "Six schools of Indian philosophy and Charvaka", "Religious traditions: Hinduism, Buddhism, Jainism, Sikhism, Islam, Christianity, Zoroastrianism", "Scripts: Brahmi, Kharosthi", "Sahitya Akademi and literary awards", "Medieval saints' literature"],
  ["Orthodox vs heterodox schools", "Classical language status vs scheduled language"],
  [], "Texts, authors and schools.", "Discuss the plural philosophical and religious heritage.", 3,
  ["S-GS1-01", "S-P1-02"], [r"classical language", r"Sanskrit|Pali|Prakrit|Tamil literature", r"Mahabharata|Ramayana|Purana", r"Sangam literature", r"Samkhya|Yoga|Nyaya|Vaisheshika|Mimamsa|Vedanta|Charvaka", r"Sahitya Akademi|Jnanpith", r"Kharosthi|script", r"Upanishad|Bhagavad Gita", r"Eighth Schedule"], ["R-SINGHANIA", "R-NCERT"], related=["performing-arts-music-dance"])
X(H, "heritage-institutions-crafts", "G", "Heritage sites, cultural institutions, crafts and festivals",
  "World Heritage and protected monuments, bodies that preserve culture, crafts and GI-tagged products, and festivals.",
  ["UNESCO World Heritage Sites in India", "Archaeological Survey of India and protected monuments", "Cultural institutions: Akademis, National Museum, Indira Gandhi National Centre for the Arts", "Handicrafts and geographical indications", "Festivals and fairs", "Tribal art and communities", "Awards in arts and letters"],
  ["Cultural vs natural vs mixed World Heritage Site", "Monument of national importance vs state-protected"],
  [], "Lists with locations and categories.", "Discuss conservation and promotion of heritage.", 3,
  ["S-GS1-01"], [r"World Heritage", r"Archaeological Survey", r"geographical indication|\bGI tag", r"handicraft|handloom|craft", r"festival", r"Sahitya Akademi|Lalit Kala|Sangeet Natak", r"Bharat Ratna|Padma|Jnanpith|award", r"tribe|tribal art"], ["R-ASI", "R-UNESCO", "R-SINGHANIA"], related=["art-architecture-sculpture"])

# ================================================================== SOCIETY
Y = "society"
X(Y, "indian-society-diversity", "A", "Salient features of Indian society and diversity",
  "Caste, tribe, religion, language, region and the ideas of unity in diversity, secularism and pluralism.",
  ["Caste system and its changes", "Tribal society and challenges", "Religious and linguistic diversity", "Regionalism and sub-nationalism", "Family, kinship and marriage", "Rural-urban differences", "Unity in diversity and national integration", "Social stratification and mobility"],
  ["Caste vs class", "Sanskritisation vs westernisation", "Secularism (Indian) vs separation of religion and state"],
  [], "Concepts and examples.", "Evaluate pluralism, identity politics and national integration.", 4,
  ["S-GS1-06", "S-GS1-09"], [r"caste", r"tribe|tribal", r"diversity", r"regionalism", r"secularism", r"communalism", r"pluralism", r"family|marriage|kinship", r"linguistic", r"Sanskriti[sz]ation|westerni[sz]ation"], ["R-NCERT"], cross_ids=["polity-fr-exploitation-religion-cultural"], related=["social-empowerment-women"])
X(Y, "social-empowerment-women", "A", "Women, social empowerment and vulnerable groups",
  "Role of women and women's organisations, empowerment of marginalised groups and associated laws.",
  ["Women's movements and organisations", "Gender gap indicators and violence against women", "Political and economic participation of women", "Reservation for women in legislatures", "Rights of children, elderly, persons with disabilities, transgender persons", "Self-help groups", "Dalit and tribal empowerment", "Laws: dowry, domestic violence, workplace harassment"],
  ["Gender equality vs gender equity", "Empowerment vs welfare approach"],
  ["indian-society-diversity"], "Laws, schemes and indicators.", "Assess the effectiveness of laws and the barriers to empowerment.", 4,
  ["S-GS1-07", "S-GS1-09", "S-GS2-12"], [r"women", r"gender", r"Women.s Reservation|Nari Shakti", r"transgender", r"disabilit|Divyang", r"self[- ]help group", r"dowry|domestic violence|sexual harassment", r"empowerment", r"child(ren)?\b.*(right|labour|marriage)", r"elderly|senior citizen"], ["R-WCD", "R-MSJE", "R-NCERT"], cross_ids=["governance-social-sector-welfare"], related=["population-poverty-urbanisation"])
X(Y, "population-poverty-urbanisation", "B", "Population, poverty, development and urbanisation",
  "Social effects of population change, poverty and development issues, and urbanisation with its problems.",
  ["Population composition and growth", "Poverty, hunger and development", "Urban growth: slums, housing, transport, sanitation", "Migration and its social impact", "Smart cities and urban missions", "Ageing and demographic dividend", "Regional disparities and development"],
  ["Rural vs urban poverty", "Planned vs unplanned urbanisation"],
  ["indian-society-diversity"], "Concepts and indicators.", "Analyse causes and solutions for urban and developmental problems.", 3,
  ["S-GS1-07"], [r"urbani[sz]ation", r"slum", r"smart cit", r"population (growth|policy)", r"demographic dividend", r"migration", r"poverty", r"regional disparit", r"housing", r"sanitation"], ["R-NCERT", "R-CENSUS"], cross_ids=["geography-population-demography-urbanisation"], related=["globalisation-social-change"])
X(Y, "globalisation-social-change", "B", "Globalisation and social change",
  "Effects of globalisation on culture, family, work, identity and inequality in India.",
  ["Cultural homogenisation and glocalisation", "Impact on family and gender roles", "Impact on employment and informal work", "Consumerism and media", "Diaspora and transnationalism", "Impact on tribal and rural communities", "Digital divide", "Resistance and identity assertion"],
  ["Globalisation vs localisation", "Cultural diffusion vs cultural imperialism"],
  ["indian-society-diversity"], "Concepts and examples.", "Weigh costs and benefits of globalisation for society.", 3,
  ["S-GS1-08"], [r"globali[sz]ation", r"glocali[sz]ation", r"cultural (homogeni|diffusion|identity)", r"consumerism", r"diaspora", r"digital divide", r"social media", r"westerni[sz]ation"], ["R-NCERT"], cross_ids=["economy-economic-reforms-1991"], related=["population-poverty-urbanisation"])

# ================================================================== GOVERNANCE
Gv = "governance"
X(Gv, "policy-design-implementation", "A", "Government policies, interventions and the development industry",
  "How policies and schemes are designed and implemented, and the role of NGOs, SHGs and other stakeholders.",
  ["Policy cycle: agenda, formulation, implementation, evaluation", "Centrally sponsored vs central sector schemes", "Role of NGOs, SHGs, donors, charities", "Public-private partnership in service delivery", "Evaluation and outcome budgeting", "Convergence and last-mile delivery", "Direct benefit transfer"],
  ["Centrally sponsored vs central sector scheme", "Output vs outcome"],
  [], "Terms and institutions.", "Assess design flaws and implementation gaps in major schemes.", 3,
  ["S-GS2-10", "S-GS2-11"], [r"\bNGO|non-?governmental", r"self[- ]help group", r"centrally sponsored", r"scheme", r"policy (design|implementation|making)", r"public[- ]private", r"direct benefit transfer|\bDBT\b", r"last[- ]mile", r"stakeholder"], ["R-NITI", "R-ARC", "R-PIB"], related=["transparency-e-governance-citizens-charter"])
X(Gv, "transparency-e-governance-citizens-charter", "A", "Transparency, accountability and e-governance",
  "Institutions and tools for open, accountable and technology-enabled government.",
  ["Right to Information Act 2005", "Citizens' charters and grievance redressal", "e-governance models and digital public infrastructure", "Social audit", "Whistleblower protection", "Lokpal and Lokayuktas", "Ombudsman concept", "Good governance and ethics link"],
  ["RTI vs Official Secrets Act", "e-governance vs m-governance"],
  ["policy-design-implementation"], "Acts, bodies and models.", "Evaluate e-governance and accountability mechanisms.", 4,
  ["S-GS2-15"], [r"Right to Information|\bRTI\b", r"citizen.?s? charter", r"e-governance|digital governance", r"social audit", r"whistle[- ]?blower", r"Lokpal|Lokayukta", r"grievance", r"accountability", r"transparency", r"good governance", r"Digital India|\bAadhaar\b"], ["R-RTI", "R-ARC", "R-CIC"], cross_ids=["polity-statutory-bodies"], related=["civil-services-role"])
X(Gv, "civil-services-role", "A", "Role of civil services in a democracy",
  "Constitutional position, accountability and reform of the permanent executive.",
  ["All-India services and Part XIV", "Political neutrality and civil-service values", "Generalist vs specialist debate", "Civil service reforms (2nd ARC, Mission Karmayogi)", "Lateral entry", "Civil servants and ministers", "Probity and ethics link", "Performance appraisal"],
  ["Generalist vs specialist", "Political executive vs permanent executive"],
  ["policy-design-implementation"], "Constitutional provisions and reforms.", "Discuss civil-service reform and neutrality.", 3,
  ["S-GS2-16", "S-GS2-06"], [r"civil servic", r"All[- ]India Services?", r"lateral entry", r"Karmayogi", r"bureaucra", r"permanent executive", r"civil servant", r"administrative reform"], ["R-ARC", "R-UPSC"], cross_ids=["polity-upsc-spsc"], related=["transparency-e-governance-citizens-charter"])
X(Gv, "social-sector-welfare", "B", "Health, education and human resources",
  "Policy issues in health, education and skilling, and flagship schemes.",
  ["Right to Education and National Education Policy 2020", "Public health system and insurance (Ayushman Bharat)", "Nutrition programmes (POSHAN, mid-day meal)", "Skill development missions", "Human development indicators", "Drinking water and sanitation missions", "Housing for all"],
  ["Universal vs targeted welfare", "Public health vs health care"],
  [], "Schemes and indicators.", "Evaluate quality, access and financing in health and education.", 5,
  ["S-GS2-13", "S-GS2-12", "S-GS2-14"], [r"Right to Education|\bRTE\b", r"National Education Policy|\bNEP\b", r"Ayushman|health (insurance|care|policy)", r"mid-?day meal|POSHAN|nutrition", r"skill (development|India)", r"Swachh|sanitation|drinking water|Jal Jeevan", r"education", r"public health", r"hunger"], ["R-PIB", "R-NITI", "R-MSJE"], cross_ids=["scitech-health-diseases"], related=["vulnerable-sections-welfare"])
X(Gv, "vulnerable-sections-welfare", "B", "Welfare of vulnerable sections",
  "Laws, institutions and schemes for SCs, STs, OBCs, minorities, women, children, elderly and persons with disabilities.",
  ["Reservation and constitutional safeguards", "SC/ST (Prevention of Atrocities) Act", "Forest Rights Act and tribal development", "Welfare schemes for women and children", "Disability law and schemes", "Minority welfare", "National commissions", "Manual scavenging prohibition"],
  ["Reservation vs welfare scheme", "Constitutional vs statutory protection"],
  ["social-sector-welfare"], "Acts, bodies and schemes.", "Assess outcomes and gaps in protection of vulnerable sections.", 4,
  ["S-GS2-12"], [r"Scheduled Castes?|Scheduled Tribes?", r"Atrocities", r"Forest Rights", r"minorit", r"manual scavenging", r"disabilit", r"backward class", r"vulnerable (section|group)", r"tribal (development|welfare)", r"reservation"], ["R-MSJE", "R-WCD", "R-INDIACODE"], cross_ids=["polity-national-commissions-vulnerable-sections", "society-social-empowerment-women"], related=["social-sector-welfare"])

# ================================================================== INTERNATIONAL RELATIONS
I = "ir"
X(I, "india-neighbourhood", "A", "India and its neighbourhood",
  "Bilateral relations, disputes and cooperation with India's immediate neighbours and the Indian Ocean region.",
  ["Neighbourhood First policy", "Pakistan, China, Nepal, Bhutan, Bangladesh, Sri Lanka, Myanmar, Afghanistan, Maldives", "Border and water disputes", "Connectivity and trade projects", "Indian Ocean strategy: SAGAR, Indo-Pacific", "Regional groupings: SAARC, BIMSTEC", "Refugees and migration issues"],
  ["SAARC vs BIMSTEC", "Look East vs Act East"],
  [], "Country-by-country facts and agreements.", "Evaluate India's neighbourhood policy and challenges (China's influence).", 5,
  ["S-GS2-17"], [r"neighbou?rhood", r"Pakistan|Bangladesh|Nepal|Bhutan|Sri Lanka|Maldives|Myanmar|Afghanistan", r"\bSAARC\b|BIMSTEC", r"Indian Ocean", r"Act East|Look East", r"Indo-Pacific", r"Teesta|Indus Waters|Ganga Water", r"Line of Actual Control|\bLAC\b|Line of Control", r"Belt and Road|CPEC"], ["R-MEA", "R-PIB"], cross_ids=["geography-world-political-geography-borders"], related=["global-groupings-agreements"])
X(I, "global-groupings-agreements", "A", "Bilateral, regional and global groupings",
  "Groupings and agreements in which India participates or that affect its interests.",
  ["BRICS, SCO, Quad, G20, G7", "ASEAN, EAS, RCEP and India's stance", "Commonwealth and NAM", "India-US, India-Russia, India-EU, India-Japan, India-Gulf relations", "Free-trade and strategic partnerships", "Africa and Central Asia outreach", "Multilateral reform and Global South", "International Solar Alliance"],
  ["BRICS vs SCO", "Quad vs AUKUS", "NAM vs strategic autonomy"],
  ["india-neighbourhood"], "Membership, objectives and summits.", "Assess India's multi-alignment and the value of each grouping.", 5,
  ["S-GS2-18", "S-GS2-19"], [r"\bBRICS\b", r"\bSCO\b|Shanghai Cooperation", r"\bQuad\b", r"\bG-?20\b|\bG-?7\b", r"\bASEAN\b", r"\bRCEP\b", r"Commonwealth", r"Non[- ]Aligned", r"\bAUKUS\b", r"I2U2|IMEC|India-Middle East", r"Global South"], ["R-MEA", "R-PIB"], related=["international-institutions-un", "india-neighbourhood"])
X(I, "international-institutions-un", "A", "International institutions and the UN system",
  "Structure, mandate and reform of the UN, its agencies and other major international bodies.",
  ["UN organs: General Assembly, Security Council, ECOSOC, ICJ, Secretariat", "Specialised agencies: WHO, FAO, UNESCO, ILO, UNDP", "Security Council reform and India's claim", "UN peacekeeping", "International Court of Justice and ICC", "NATO and OSCE", "Nuclear regimes: NPT, MTCR, Wassenaar", "Global governance reform"],
  ["ICJ vs ICC", "Permanent vs non-permanent UNSC member", "General Assembly vs Security Council"],
  [], "Organs, agencies and membership.", "Evaluate UN reform and India's role.", 4,
  ["S-GS2-20"], [r"United Nations|\bUN\b|UNSC|Security Council", r"General Assembly", r"International Court of Justice|\bICJ\b|\bICC\b|International Criminal Court", r"World Health Organi[sz]ation|\bFAO\b|\bUNESCO\b|\bILO\b|\bUNDP\b|UNICEF", r"peacekeeping", r"\bNATO\b", r"\bMTCR\b|Wassenaar|Australia Group", r"international (organi[sz]ation|institution)"], ["R-UN", "R-MEA"], related=["global-groupings-agreements"])
X(I, "diaspora-foreign-policy-effects", "A", "Diaspora, foreign policy principles and effects of other countries' policies",
  "Principles guiding Indian foreign policy, the diaspora, and the effects of developed and developing countries' policies on India.",
  ["Panchsheel and non-alignment evolution", "Strategic autonomy and multi-alignment", "Indian diaspora and remittances", "Overseas Citizenship of India", "Impact of US, China and EU policies (trade, visas, climate, technology)", "Energy diplomacy", "Soft power and cultural diplomacy", "Evacuation operations and consular role"],
  ["Non-alignment vs strategic autonomy", "NRI vs PIO vs OCI"],
  ["global-groupings-agreements"], "Concepts and examples.", "Assess how external policies and diaspora shape Indian interests.", 3,
  ["S-GS2-19", "S-GS2-17"], [r"diaspora", r"Panchsheel", r"strategic autonomy|multi-?alignment", r"\bNRI\b|\bOCI\b|Overseas Citizen|Persons of Indian Origin", r"soft power", r"energy (security|diplomacy)", r"foreign policy", r"remittance", r"visa polic|H-1B"], ["R-MEA"], related=["global-groupings-agreements"])
X(I, "global-conflicts-treaties", "A", "Global conflicts, treaties and security issues in the news",
  "Major conflicts, treaties and security arrangements that regularly shape international questions.",
  ["West Asia, Ukraine, Indo-Pacific, Korean peninsula flashpoints", "Nuclear arms control treaties", "Arms trade and sanctions", "Maritime law (UNCLOS) and South China Sea", "Terrorism and global responses", "Humanitarian crises and refugee law", "India's positions on conflicts"],
  ["Treaty vs convention vs protocol", "Sanction vs embargo"],
  ["international-institutions-un"], "Parties, dates and issues.", "Explain India's stand and strategic interests in global conflicts.", 3,
  ["S-GS2-19", "S-GS2-20"], [r"conflict|war\b", r"treaty", r"sanction", r"UNCLOS|South China Sea", r"Ukraine|Gaza|Israel|Palestine|Taiwan|Korean", r"refugee", r"terroris", r"nuclear (arms|treaty)|arms control", r"peace (process|agreement|accord)"], ["R-MEA", "R-UN"], cross_ids=["security-external-actors-extremism"], related=["international-institutions-un"])

# ================================================================== SECURITY
Sc = "security"
X(Sc, "external-actors-extremism", "A", "Extremism, insurgency and external actors",
  "Left-wing extremism, insurgencies and terrorism, their drivers and the role of state and non-state external actors.",
  ["Left-wing extremism: causes, spread, policy", "Insurgency in the North-East and Jammu & Kashmir", "Links between underdevelopment and extremism", "External state and non-state actors", "Terror financing and radicalisation", "Policy responses: security and development", "Surrender and rehabilitation policies"],
  ["Insurgency vs terrorism", "Left-wing extremism vs separatism"],
  [], "Concepts and key policies.", "Explain the development–security nexus and balance of responses.", 4,
  ["S-GS3-16", "S-GS3-17"], [r"extremis", r"Naxal|Maoist|Left Wing", r"insurgen", r"terroris", r"radicali[sz]ation", r"North[- ]East.*(insurgen|militan)", r"non-state actor", r"terror financ", r"AFSPA|Armed Forces \(Special"], ["R-MHA", "R-ARC"], cross_ids=["ir-global-conflicts-treaties"], related=["security-security-forces-agencies"])
X(Sc, "security-forces-agencies", "A", "Security forces and agencies",
  "The central armed police forces, intelligence and investigative agencies, and the armed forces' mandates.",
  ["Central Armed Police Forces: BSF, CRPF, CISF, ITBP, SSB, Assam Rifles", "National Investigation Agency", "Intelligence agencies: IB, RAW", "NSA and National Security Council", "Military commands and theatre reform", "Coastal security architecture", "Police reforms", "Border management department"],
  ["CAPF vs armed forces", "IB vs RAW"],
  [], "Mandates and the parent ministry of each force.", "Discuss coordination, police reform and defence reform.", 3,
  ["S-GS3-20"], [r"\bBSF\b|Border Security Force", r"\bCRPF\b|\bCISF\b|\bITBP\b|Assam Rifles", r"National Investigation Agency|\bNIA\b", r"\bRAW\b|Intelligence Bureau", r"National Security (Adviser|Council)", r"theatre command|Chief of Defence Staff|\bCDS\b", r"police reform", r"Coast Guard", r"armed forces"], ["R-MHA", "R-ARC"], related=["external-actors-extremism"])
X(Sc, "cyber-security", "B", "Cyber security, media and money laundering",
  "Security challenges from communication networks and social media, basics of cyber security, and money laundering with its prevention.",
  ["Cyber crimes and cyber terrorism", "Information Technology Act and CERT-In", "National cyber policy and critical information infrastructure", "Disinformation, deepfakes and social media risks", "Money laundering and PMLA", "Financial Action Task Force", "Data security and privacy", "Hybrid and information warfare"],
  ["Cyber crime vs cyber terrorism", "Money laundering vs terror financing"],
  [], "Concepts, laws and bodies.", "Evaluate cyber governance and regulation of social media.", 3,
  ["S-GS3-18"], [r"cyber", r"CERT-In", r"Information Technology Act", r"money[- ]laundering|\bPMLA\b", r"Financial Action Task Force|\bFATF\b", r"deepfake|disinformation|fake news", r"social media", r"critical information infrastructure", r"data (security|privacy|breach)"], ["R-CERT", "R-MEITY", "R-MHA"], cross_ids=["scitech-information-technology-cyber"], related=["external-actors-extremism"])
X(Sc, "border-management-organised-crime", "B", "Border management and organised crime",
  "Security challenges at land and maritime borders and the links between organised crime and terrorism.",
  ["Land borders and fencing; Border Area Development", "Maritime and coastal security", "Smuggling, narcotics, arms and human trafficking", "Hawala and illicit finance", "Narco-terror links", "Border infrastructure and integrated check posts", "India's disputes and border agreements"],
  ["Border management vs border defence", "Smuggling vs trafficking"],
  [], "Concepts and bodies.", "Discuss border security challenges and coordination.", 3,
  ["S-GS3-19"], [r"border (management|area|security|fencing)", r"smuggl", r"narcotic|drug trafficking|Golden (Crescent|Triangle)", r"human trafficking", r"hawala", r"organi[sz]ed crime", r"maritime security|coastal security", r"integrated check post"], ["R-MHA", "R-ARC"], cross_ids=["geography-world-political-geography-borders"], related=["external-actors-extremism"])

# ================================================================== DISASTER MANAGEMENT
D = "disaster"
X(D, "disaster-management-framework", "A", "Disaster management framework in India",
  "Types of disasters, the legal and institutional framework, and the disaster management cycle.",
  ["Natural vs man-made disasters; hazard, vulnerability, risk", "Disaster Management Act 2005", "NDMA, SDMAs, DDMAs and NDRF", "Disaster management cycle: mitigation, preparedness, response, recovery", "Sendai Framework for Disaster Risk Reduction", "Early warning systems", "Community-based disaster management", "Cyclone, flood, earthquake, drought, landslide, urban flooding responses", "Role of media and technology"],
  ["Hazard vs disaster", "Mitigation vs preparedness", "NDMA vs NDRF"],
  [], "Acts, bodies and the cycle.", "Evaluate preparedness and resilience in the context of climate-driven disasters.", 4,
  ["S-GS3-15"], [r"disaster", r"\bNDMA\b|National Disaster", r"\bNDRF\b", r"Sendai", r"early warning", r"hazard", r"vulnerability", r"disaster management", r"resilien", r"Disaster Management Act"], ["R-NDMA", "R-MHA", "R-MOEF"], cross_ids=["geography-geophysical-hazards", "environment-climate-change-ghg"])

SUBJECT_META = {
    "scitech": ("Science & Technology", "authored", ["Prelims GS-I", "Mains GS-III"]),
    "society": ("Indian Society", "authored", ["Mains GS-I"]),
    "governance": ("Governance & Social Justice", "authored", ["Mains GS-II"]),
    "ir": ("International Relations", "authored", ["Mains GS-II"]),
    "security": ("Security", "authored", ["Mains GS-III"]),
    "disaster": ("Disaster Management", "authored", ["Mains GS-III"]),
    "history": ("History & Culture", "authored", ["Prelims GS-I", "Mains GS-I"]),
}
RATIONALE = {
    ("security-cyber-security", "scitech-information-technology-cyber"): "Cyber-security policy builds on the technologies (networks, AI, blockchain) studied under Science & Technology.",
    ("scitech-defence-technology", "security-security-forces-agencies"): "Defence technology and indigenisation serve the forces and agencies whose mandates are studied under Security.",
    ("scitech-health-diseases", "governance-social-sector-welfare"): "Disease burden and technology (Science) meet health policy and schemes (Governance).",
    ("scitech-biotechnology-genetics", "environment-sustainable-agriculture-forestry"): "GM crops and biofertilisers connect biotechnology to sustainable agriculture and biosafety law.",
    ("scitech-nuclear-energy", "environment-renewable-energy-green-tech"): "Nuclear power is part of the low-carbon energy mix alongside renewables.",
    ("history-art-architecture-sculpture", "history-buddhism-jainism-mahajanapadas"): "Stupas, chaityas and early sculpture are products of Buddhist and Jain patronage.",
    ("history-mughal-empire", "history-advent-british-expansion"): "The decline of Mughal authority created the political space in which the British expanded.",
    ("society-social-empowerment-women", "governance-social-sector-welfare"): "Women's empowerment is delivered largely through health, education and welfare schemes.",
    ("society-globalisation-social-change", "economy-economic-reforms-1991"): "Social effects of globalisation follow from the 1991 liberalisation.",
    ("society-population-poverty-urbanisation", "geography-population-demography-urbanisation"): "Census-based demography (Geography) and its social consequences (Society) are two views of the same trends.",
    ("governance-vulnerable-sections-welfare", "polity-national-commissions-vulnerable-sections"): "Welfare schemes and the commissions that monitor them operate together.",
    ("governance-transparency-e-governance-citizens-charter", "polity-statutory-bodies"): "RTI, Lokpal and information commissions are statutory bodies studied in Polity.",
    ("governance-civil-services-role", "polity-upsc-spsc"): "The UPSC recruits and advises on the civil services whose role is studied under Governance.",
    ("ir-global-conflicts-treaties", "security-external-actors-extremism"): "Global conflicts and non-state actors shape the external dimension of internal security.",
    ("security-border-management-organised-crime", "geography-world-political-geography-borders"): "Border management rests on political-geography facts about boundaries and neighbours.",
    ("ir-india-neighbourhood", "geography-world-political-geography-borders"): "Neighbourhood policy is tied to border, river and sea geography.",
    ("disaster-disaster-management-framework", "geography-geophysical-hazards"): "Disaster management applies to the hazards explained in Geography.",
    ("disaster-disaster-management-framework", "environment-climate-change-ghg"): "Climate change raises the frequency and severity of hydro-meteorological disasters.",
    ("economy-industry-infrastructure", "scitech-materials-nanotechnology"): "Industrial policy (PLI, semiconductors) depends on advanced materials and manufacturing technology.",
}
