"""Phase D batch 5: deepens History (Ancient, Medieval) and adds post-independence India (GS-I syllabus item S-GS1-04).
Same rules: AI-written from general knowledge, draft-unreviewed, no book chapters/editions, no statistics, no invented quotes."""
import author_polity as P
import author_subjects as S
from author_subjects import X

S.GROUPS["history"] = S.GROUPS["history"] + [("I", "Post-independence India")]
H = "history"

# ------------------------------------------------------------ ANCIENT
X(H, "ancient-sources-archaeology", "E", "Sources of ancient history: archaeology, epigraphy, coins and accounts",
  "How ancient Indian history is reconstructed: material remains, inscriptions, coins, literature and foreign accounts.",
  ["Archaeological methods and dating (stratigraphy, radiocarbon)", "Inscriptions: Ashokan edicts, Allahabad Pillar, Hathigumpha, land grants", "Coins: punch-marked, Indo-Greek, Kushana, Gupta", "Literary sources: Vedic, epic, Buddhist, Jain, Sangam, Puranic", "Foreign accounts: Megasthenes, Pliny, Fa-Hien, Hiuen Tsang, Al-Biruni", "Scripts and their decipherment (Brahmi, Kharosthi; James Prinsep)", "Monuments and sites", "Limits and biases of sources"],
  ["Primary vs secondary source", "Epigraphy vs numismatics"],
  [], "Source types with one example each.", "Assess what each source can and cannot tell historians.", 3,
  ["S-P1-02", "S-GS1-01"], [r"epigraph|inscription", r"numismat|\bcoins?\b|punch[- ]marked", r"archaeolog", r"Prinsep|decipher", r"Allahabad (Pillar|Prashasti)|Hathigumpha|Junagadh|Rudradaman", r"foreign (traveller|account)", r"Megasthenes|Fa[- ]?Hien|Hiuen|Xuanzang|Pliny|Periplus", r"radiocarbon|stratigraph", r"literary source"], ["R-ASI", "R-NCERT"], related=["indus-vedic-ancient-foundations", "mauryan-gupta-empires"])
X(H, "sangam-south-india", "E", "Sangam age and early South India",
  "Early historic Tamilakam: Sangam literature, the Chera, Chola and Pandya kingdoms, trade and society.",
  ["Sangam literature: Tolkappiyam, Ettuttokai, Pattuppattu, Silappadikaram, Manimekalai", "Chera, Chola and Pandya kingdoms", "Roman trade and port towns (Muziris, Arikamedu)", "Tinai: landscape-based society", "Kings, chieftains and warrior culture", "Role of women poets", "Megalithic background", "Religion: early Tamil gods, Buddhism, Jainism"],
  ["Sangam vs Gupta age", "Tinai vs varna"],
  ["indus-vedic-ancient-foundations"], "Texts, kingdoms and trade centres.", "Link Roman trade to economy and urbanisation in the south.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Sangam", r"Tolkappiyam|Silappadikaram|Manimekalai|Ettuttokai|Pattuppattu|Tirukkural", r"Chera|Pandya|Early Chola", r"Muziris|Arikamedu|Roman trade|Yavana", r"Tamilakam|Tamil\b", r"tinai", r"Karikala|Senguttuvan"], ["R-NCERT", "R-ASI"], related=["mauryan-gupta-empires", "early-medieval-regional-kingdoms"])
X(H, "post-mauryan-foreign-rule", "E", "Post-Mauryan states and foreign rule",
  "Successor states and the Indo-Greeks, Shakas, Parthians and Kushanas between the Mauryas and the Guptas.",
  ["Sungas, Kanvas, Satavahanas", "Indo-Greeks and the Gandhara region", "Shakas and Parthians", "Kushanas: Kanishka, Silk Route trade", "Gold coinage and trade with Rome", "Gandhara and Mathura art", "Mahayana Buddhism's development", "Society: foreigners' integration into varna order"],
  ["Indo-Greeks vs Kushanas", "Gandhara vs Mathura school"],
  ["mauryan-gupta-empires"], "Dynasties, rulers and contributions.", "Explain cultural exchange along trade routes.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Indo-Greek|Bactrian|Menander|Milinda", r"Shaka|Saka\b|Parthian|Pahlava", r"Kushan|Kanishka", r"Satavahana|Gautamiputra", r"Silk Route|Silk Road", r"Gandhara", r"Sunga|Pushyamitra|Kanva", r"Mahayana"], ["R-NCERT"], related=["art-architecture-sculpture"])
X(H, "ancient-economy-society-science", "E", "Ancient economy, society, education and science",
  "Agrarian and trade economy, social structure, education and scientific achievements of ancient India.",
  ["Agriculture, land grants and revenue", "Trade routes, guilds (shrenis) and ports", "Urbanisation and decline of towns", "Varna, jati and slavery; status of women", "Education centres: Takshashila, Nalanda, Vikramashila", "Mathematics and astronomy: Aryabhata, Brahmagupta, Varahamihira", "Medicine: Charaka, Sushruta", "Metallurgy and technology", "Law and polity: Smritis, Arthashastra"],
  ["Shreni vs guild in medieval period", "Varna vs jati"],
  [], "Names, centres and contributions.", "Discuss continuity and change in economy and society.", 4,
  ["S-P1-02", "S-GS1-01"], [r"guild|shreni", r"Takshashila|Taxila|Nalanda|Vikramashila", r"Aryabhata|Brahmagupta|Varahamihira|Bhaskara", r"Charaka|Sushruta|Ayurved", r"land grant|agrahara", r"varna|jati", r"Smriti|Manusmriti|Dharmashastra", r"slavery|status of women", r"ancient (trade|economy|science)", r"metallurg|iron pillar"], ["R-NCERT"], cross_ids=["scitech-science-institutions-achievements"], related=["mauryan-gupta-empires"])

# ------------------------------------------------------------ MEDIEVAL
X(H, "south-indian-dynasties-chola", "F", "Cholas, Pallavas, Chalukyas and South Indian polity",
  "Administration, temple culture and maritime power of the major South Indian dynasties.",
  ["Pallavas and Chalukyas of Badami: rivalry and art", "Rashtrakutas", "Imperial Cholas: Rajaraja I, Rajendra I", "Chola local government: uttaramerur inscriptions, ur and sabha", "Maritime expeditions and trade with Southeast Asia", "Temple economy: Brihadeshwara, Gangaikondacholapuram", "Bronze sculpture", "Later Chalukyas, Hoysalas, Kakatiyas"],
  ["Chola vs Pallava temple styles", "Ur vs sabha vs nagaram"],
  ["early-medieval-regional-kingdoms"], "Rulers, institutions and monuments.", "Assess village self-government and maritime reach.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Chola", r"Rajaraja|Rajendra", r"Pallava|Mahabalipuram|Mamallapuram", r"Chalukya|Badami|Pulakeshin|Aihole|Pattadakal", r"Rashtrakuta", r"Hoysala|Kakatiya|Yadava", r"uttaramerur", r"Brihadeshwara|Gangaikonda", r"Southeast Asia"], ["R-NCERT", "R-ASI"], related=["early-medieval-regional-kingdoms", "bhakti-sufi-vijayanagara"])
X(H, "mughal-administration-economy", "F", "Mughal administration, revenue and economy",
  "The Mughal imperial system: mansabdari, revenue settlements, agrarian economy, crafts and trade.",
  ["Mansabdari: zat and sawar ranks", "Jagirdari crisis", "Land revenue: Zabt, Dahsala, Todar Mal", "Provinces, subas and local officials", "Agrarian relations: zamindars, peasants", "Crafts, textiles and urban centres", "Trade, silver inflow and European companies", "Currency and banking (hundi)"],
  ["Zat vs sawar", "Khalisa vs jagir land", "Zabt vs batai"],
  ["mughal-empire"], "Terms and systems.", "Explain how the revenue and mansab system sustained and then strained the empire.", 4,
  ["S-P1-02"], [r"mansab|zat\b|sawar", r"jagir|khalisa", r"Todar Mal|Zabt|Dahsala|batai|revenue (system|settlement)", r"zamindar", r"\bsuba\b|sarkar|pargana", r"hundi", r"Mughal (administration|economy|revenue)", r"silver", r"karkhana"], ["R-NCERT", "R-SPECTRUM"], related=["mughal-empire", "medieval-economy-society-trade"])
X(H, "maratha-sikh-regional-powers", "F", "Marathas, Sikhs, Rajputs and eighteenth-century regional states",
  "Successor and rival powers as Mughal authority weakened.",
  ["Shivaji: administration, Ashtapradhan, chauth and sardeshmukhi", "Peshwas and Maratha confederacy; Panipat 1761", "Sikh gurus, Khalsa and Ranjit Singh", "Rajput states and Mughal relations", "Hyderabad, Awadh, Bengal and Mysore", "Jats and other regional powers", "Economy and fiscal pressures", "Political fragmentation and the British entry"],
  ["Chauth vs sardeshmukhi", "Successor states vs independent kingdoms"],
  ["mughal-empire"], "Rulers, institutions and battles.", "Evaluate why no successor power unified India before the British.", 3,
  ["S-P1-02", "S-P1-03"], [r"Shivaji|Maratha|Peshwa|Ashtapradhan|chauth|sardeshmukhi", r"Panipat", r"Ranjit Singh|Khalsa|Sikh (gurus|empire|Misl)", r"Rajput", r"Hyderabad|Awadh|Nawab|Murshid Quli", r"Haider Ali|Tipu", r"successor state|eighteenth[- ]century", r"Jat\b"], ["R-NCERT", "R-SPECTRUM"], cross_ids=["history-advent-british-expansion"], related=["mughal-empire"])
X(H, "medieval-economy-society-trade", "F", "Medieval economy, society, urban life and trade",
  "Agrarian change, towns and crafts, trade routes and the effects of early European contact.",
  ["Agricultural expansion, irrigation and crops", "Urban centres and crafts; guilds in the south", "Overland and maritime trade; Indian Ocean networks", "Social structure, caste and gender", "Slavery and the status of women", "Currency and trade policy", "Portuguese and early European contacts", "Technology: paper, spinning wheel, Persian wheel"],
  ["Overland vs maritime trade", "Rural vs urban economy"],
  [], "Concepts and examples.", "Discuss commercialisation and its social effects.", 3,
  ["S-P1-02"], [r"medieval (economy|trade|society)", r"Indian Ocean trade|maritime trade", r"Portuguese|Vasco da Gama|Albuquerque", r"Persian wheel|spinning wheel", r"urban (centre|centers|life)|\btown", r"crafts|artisan", r"\bhundi\b", r"slavery", r"caste", r"trade route"], ["R-NCERT"], related=["mughal-administration-economy", "delhi-sultanate"])
X(H, "medieval-culture-historiography", "F", "Medieval culture, languages and historians",
  "Indo-Persian culture, regional languages and literature, chroniclers and Indo-Islamic synthesis.",
  ["Persian histories: Barani, Abul Fazl, Badauni, Ferishta", "Urdu, Hindi and regional-language growth", "Travel accounts: Ibn Battuta, Bernier, Tavernier", "Music and painting traditions: Dhrupad, Mughal miniature", "Architecture: Indo-Islamic synthesis", "Sufi and bhakti literature", "Education and madrasas", "Historiographical debates"],
  ["Persian vs vernacular literature", "Court chronicle vs travel account"],
  [], "Names and works.", "Assess the cultural synthesis and use of sources.", 3,
  ["S-P1-02", "S-GS1-01"], [r"Barani|Abul Fazl|Badauni|Ferishta|Amir Khusro", r"Ibn Battuta|Bernier|Tavernier|Abdur Razzaq", r"Persian (literature|language|history)", r"\bUrdu\b", r"Dhrupad|miniature", r"chronicle|historiograph", r"Indo-Islamic|Indo-Persian", r"madrasa|Tulsidas|Malik Muhammad Jayasi"], ["R-NCERT", "R-SINGHANIA"], related=["literature-languages-philosophy", "art-architecture-sculpture"])

# ------------------------------------------------------------ POST-INDEPENDENCE
X(H, "post-independence-consolidation", "I", "Post-independence consolidation and reorganisation",
  "Integration of princely states, linguistic reorganisation and the major political and economic turning points after 1947.",
  ["Integration of princely states: Junagadh, Hyderabad, Kashmir", "Partition aftermath: refugees and rehabilitation", "Constitution-making and first general elections", "Linguistic reorganisation: States Reorganisation Commission, 1956", "Language and regional movements", "Planning, land reforms, Green Revolution", "Wars and foreign policy: 1962, 1965, 1971", "Emergency 1975–77 and the Janata experiment", "Coalition era and liberalisation 1991", "Movements: JP, Naxalbari, Mandal, Ayodhya"],
  ["Integration vs accession", "States reorganisation of 1956 vs later new States"],
  ["history-transfer-of-power-partition"], "Chronology and major events.", "Assess the success of nation-building and integration.", 5,
  ["S-GS1-04"], [r"princely State|integration of (the )?(princely|States)", r"Sardar Patel|V\.?P\.? Menon|Instrument of Accession", r"Junagadh|Hyderabad.*(Police|Operation)|Operation Polo", r"States Reorganisation|linguistic (reorgani|State|basis)|Fazl Ali", r"Emergency (of|in) 1975|National Emergency|Janata", r"Green Revolution", r"land reform", r"Mandal Commission", r"Naxalbari", r"Punjab Accord|Assam Accord|Mizo Accord", r"post-independence|after independence", r"Nehru"], ["R-NCERT", "R-SPECTRUM"], cross_ids=["polity-emergency-provisions", "society-regionalism-language-integration"], related=["transfer-of-power-partition", "key-personalities-ideologies"])
