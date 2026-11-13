"""Phase D batch 6: deepens Economy, Geography and Environment.
Same rules: AI-written from general knowledge, draft-unreviewed, no book chapters/editions, no statistics, no invented quotes."""
import author_polity as P
import author_subjects as S
from author_subjects import X

S.GROUPS["economy"] = S.GROUPS["economy"]
# ================================================================ ECONOMY
E = "economy"
X(E, "microeconomics-basics", "A", "Microeconomic basics: demand, supply and market structures",
  "Core micro concepts used across economy questions: demand, supply, elasticity, costs and market forms.",
  ["Law of demand and supply; equilibrium", "Elasticity of demand and supply", "Consumer surplus, utility", "Production, costs and returns to scale", "Perfect competition, monopoly, oligopoly", "Public goods, externalities, market failure", "Price controls and subsidies' effects", "Giffen and Veblen goods"],
  ["Normal vs inferior vs Giffen good", "Public good vs merit good", "Monopoly vs monopsony"],
  [], "Definitions and diagrams.", "Apply to price controls, taxes and subsidies.", 4,
  ["S-P1-05", "S-GS3-01"], [r"elasticity", r"law of demand|demand curve|supply curve", r"Giffen|Veblen|inferior good", r"monopol|oligopol|perfect competition", r"public good|merit good|externalit", r"consumer surplus|marginal utility", r"market failure", r"opportunity cost", r"returns to scale"], ["R-RSINGH", "R-NCERT"], related=["national-income-growth", "subsidies-direct-transfers"])
X(E, "unemployment-labour-markets", "A", "Unemployment, labour markets and labour codes",
  "Types and measurement of unemployment, the informal sector and recent labour reforms.",
  ["Types: structural, frictional, cyclical, disguised, seasonal", "Periodic Labour Force Survey measures", "Formal vs informal employment", "Four labour codes", "Gender and youth employment", "Skilling missions", "Gig and platform work", "Jobless growth and demographic dividend"],
  ["Disguised vs seasonal unemployment", "Unemployment rate vs labour force participation"],
  ["human-development-poverty-employment"], "Definitions and surveys.", "Discuss quality of jobs and policy responses.", 3,
  ["S-GS3-02", "S-P1-05"], [r"unemploy", r"labour (force|code|market|reform)", r"\bPLFS\b|Periodic Labour", r"informal (sector|employment|economy)", r"disguised", r"gig (work|economy)|platform worker", r"jobless growth", r"minimum wage", r"\bEPFO\b|provident fund"], ["R-SURVEY", "R-RSINGH", "R-PIB"], cross_ids=["governance-rural-development-schemes"], related=["human-development-poverty-employment"])
X(E, "sdg-inclusive-growth", "A", "Sustainable development, inclusive growth and development indices",
  "SDGs, inclusive growth and the main global and national development indicators.",
  ["Sustainable Development Goals and the SDG India Index", "Inclusive growth", "Human Development Index, Multidimensional Poverty Index", "Gender Inequality and Gender Gap indices", "Happiness and hunger indices", "Green GDP and natural capital accounting", "Gini coefficient and Lorenz curve", "Growth vs development"],
  ["Growth vs development", "HDI vs MPI", "Gini coefficient vs Lorenz curve"],
  ["national-income-growth"], "Index names, publishers and what they measure.", "Critique indices and India's rank interpretations.", 3,
  ["S-GS3-01", "S-GS3-02", "S-P1-05"], [r"Sustainable Development Goal|\bSDG", r"inclusive growth", r"Human Development Index|\bHDI\b", r"Multidimensional Poverty", r"Gender (Inequality|Gap) Index", r"Global Hunger Index|Happiness", r"Gini|Lorenz", r"green GDP", r"SDG India Index"], ["R-SURVEY", "R-NITI", "R-RSINGH"], cross_ids=["environment-sustainable-development-green-economy"], related=["human-development-poverty-employment"])
X(E, "insurance-pension-sector", "B", "Insurance and pension sector",
  "Structure and regulation of insurance and pensions in India.",
  ["Life and general insurance; IRDAI", "Insurance penetration and FDI limits", "Crop and health insurance schemes", "Pension system: EPS, NPS, PFRDA", "Atal Pension Yojana", "Microinsurance and PMJJBY/PMSBY", "Reinsurance basics", "Unified Pension Scheme debate"],
  ["Insurance vs assurance", "NPS vs old pension scheme"],
  ["banking-structure"], "Regulators and schemes.", "Assess coverage gaps and regulation.", 2,
  ["S-GS3-02", "S-P1-05"], [r"insurance", r"\bIRDAI\b", r"pension", r"\bPFRDA\b|National Pension System|\bNPS\b", r"Atal Pension", r"PMJJBY|PMSBY|Fasal Bima", r"reinsurance"], ["R-RBI", "R-PIB", "R-SURVEY"], related=["financial-inclusion-digital-payments"])
X(E, "nbfc-npa-resolution", "B", "NBFCs, NPAs and bad-loan resolution",
  "Non-bank lenders, stressed assets and the legal tools for recovery.",
  ["NBFC vs bank; shadow banking", "Non-performing assets: classification and provisioning", "Insolvency and Bankruptcy Code and NCLT", "SARFAESI, DRTs, ARCs", "Bad bank (NARCL)", "Prompt corrective action", "Priority sector lending", "Bank recapitalisation and mergers"],
  ["NPA vs write-off", "NBFC vs HFC", "IBC vs SARFAESI"],
  ["banking-structure"], "Terms and laws.", "Evaluate resolution architecture and stress in NBFCs.", 3,
  ["S-GS3-01", "S-P1-05"], [r"\bNPA|non-?performing asset", r"NBFC|shadow bank", r"Insolvency and Bankruptcy|\bIBC\b|\bNCLT\b", r"SARFAESI|Debt Recovery Tribunal|asset reconstruction", r"bad bank|\bNARCL\b", r"Prompt Corrective Action", r"priority sector", r"recapitali[sz]ation", r"stressed asset"], ["R-RBI", "R-SURVEY"], related=["financial-markets"])
X(E, "subsidies-direct-transfers", "C", "Subsidies, direct benefit transfers and public expenditure",
  "Design and fiscal effects of subsidies and the shift to cash transfers.",
  ["Major subsidies: food, fertiliser, fuel", "Direct Benefit Transfer and JAM", "Targeting and leakages", "Merit vs non-merit subsidies", "Fiscal cost and crowding out", "WTO subsidy boxes", "Freebies debate", "Public expenditure quality; outcome budgeting"],
  ["Subsidy vs subvention", "Cash vs in-kind transfer"],
  ["fiscal-policy-budget"], "Names and types.", "Evaluate subsidy rationalisation and DBT.", 3,
  ["S-GS3-02", "S-GS3-05"], [r"subsid", r"direct benefit transfer|\bDBT\b", r"\bJAM\b|Jan Dhan", r"fertili[sz]er subsid|urea", r"food subsid", r"freebie|revdi", r"leakage", r"cash transfer", r"Green Box|Amber Box|Blue Box"], ["R-SURVEY", "R-BUDGET", "R-PIB"], cross_ids=["governance-food-security-pds"], related=["fiscal-policy-budget", "agriculture-marketing-pricing-credit"])
X(E, "disinvestment-public-sector", "E", "Public sector enterprises and disinvestment",
  "Role of PSUs, disinvestment methods and privatisation policy.",
  ["Maharatna, Navratna, Miniratna categories", "Disinvestment vs privatisation vs strategic sale", "Offer for sale and CPSE ETF", "Asset monetisation pipeline", "Public sector in strategic sectors", "Competition and regulatory issues", "Performance and governance of PSUs", "Bank privatisation debate"],
  ["Disinvestment vs privatisation", "Maharatna vs Navratna"],
  ["economic-reforms-1991"], "Categories and methods.", "Weigh efficiency gains against public-interest concerns.", 2,
  ["S-GS3-01", "S-P1-05"], [r"disinvest", r"privati[sz]ation", r"Maharatna|Navratna|Miniratna", r"strategic sale", r"public sector (undertaking|enterprise)|\bCPSE\b|\bPSU\b", r"asset monetisation", r"offer for sale"], ["R-SURVEY", "R-PIB"], related=["industry-infrastructure"])
X(E, "msme-startups-manufacturing", "E", "MSMEs, start-ups and manufacturing policy",
  "Definition, support schemes and the manufacturing push.",
  ["MSME classification and credit support", "Make in India, PLI schemes", "Start-up India and unicorns", "Ease of doing business and compliance reforms", "National manufacturing policy and industrial corridors", "Special Economic Zones and export hubs", "Clusters and ODOP", "Atmanirbhar Bharat package"],
  ["MSME vs start-up", "SEZ vs industrial corridor"],
  ["industry-infrastructure"], "Definitions and schemes.", "Assess manufacturing share, employment and credit gaps.", 3,
  ["S-GS3-01", "S-GS3-04", "S-P1-05"], [r"\bMSME|micro, small and medium", r"Make in India", r"Production[- ]Linked Incentive|\bPLI\b", r"Start-?up India|start-?up|unicorn", r"ease of doing business", r"Special Economic Zone|\bSEZ\b", r"industrial corridor", r"Atmanirbhar", r"cluster|One District One Product"], ["R-SURVEY", "R-PIB", "R-NITI"], related=["industry-infrastructure", "unemployment-labour-markets"])
X(E, "energy-sector-economy", "E", "Energy sector: coal, power, oil and gas",
  "Structure, reforms and security issues of India's energy sector.",
  ["Coal: reserves, commercial mining, imports", "Power sector: generation, transmission, distribution; DISCOM losses", "Electricity Act and reforms", "Petroleum and natural gas: pricing, imports, strategic reserves", "Energy security and import dependence", "Renewable targets and grid integration", "Energy efficiency and BEE", "Hydrogen mission"],
  ["Installed capacity vs generation", "Energy security vs energy independence"],
  ["industry-infrastructure"], "Sources, bodies and policies.", "Evaluate energy security and transition costs.", 3,
  ["S-GS3-06", "S-GS3-01"], [r"\bcoal", r"power sector|\bDISCOM|electricity (act|sector|distribution)", r"petroleum|crude oil|natural gas|\bLNG\b", r"strategic (petroleum )?reserve", r"energy (security|efficiency)|\bBEE\b", r"hydrogen", r"transmission", r"UDAY"], ["R-SURVEY", "R-PIB", "R-NITI"], cross_ids=["environment-renewable-energy-green-tech", "geography-indian-energy-industry-regions"], related=["industry-infrastructure"])
X(E, "agriculture-marketing-pricing-credit", "D", "Agricultural marketing, pricing and credit",
  "Markets, price support and finance for farmers.",
  ["APMC mandis and e-NAM", "MSP and procurement; price deficiency ideas", "Farm laws and their repeal", "Farmer producer organisations and cooperatives", "Kisan Credit Card, NABARD, priority lending", "Crop insurance", "Contract farming and warehousing", "Land reforms and tenancy"],
  ["MSP vs market price", "Cooperative vs FPO"],
  ["agriculture-rural-development"], "Institutions and schemes.", "Assess price support, market access and credit gaps.", 4,
  ["S-GS3-03", "S-P1-05"], [r"\bAPMC|mandi", r"\be-NAM\b", r"\bMSP\b|minimum support price", r"farm laws|Farmers.? Produce Trade", r"\bFPO\b|farmer producer", r"Kisan Credit|\bNABARD\b", r"contract farming", r"warehous", r"land reform|tenancy", r"cooperative"], ["R-SURVEY", "R-AGRI", "R-PIB"], cross_ids=["governance-food-security-pds"], related=["agriculture-rural-development", "subsidies-direct-transfers"])
X(E, "services-tourism-it", "E", "Services sector, IT and tourism",
  "The services-led growth model and its key components.",
  ["Share of services in output and exports", "IT and IT-enabled services; GCCs", "Tourism policy and heritage circuits", "Transport and logistics: National Logistics Policy", "Telecom sector", "Financial and professional services", "Medical tourism", "Services trade and GATS"],
  ["Goods vs services trade", "Mode 1 vs Mode 4 GATS"],
  ["national-income-growth"], "Sectors and policies.", "Discuss whether services can drive employment.", 2,
  ["S-GS3-01", "S-P1-05"], [r"services sector", r"\bIT[- ]?(BPM|sector|services)|information technology (sector|exports)|software exports", r"tourism", r"logistics", r"telecom", r"\bGATS\b", r"Global Capability Cent", r"medical tourism"], ["R-SURVEY", "R-PIB"], related=["national-income-growth", "international-trade-wto"])

# ================================================================ GEOGRAPHY
G = "geography"
X(G, "geomorphic-processes-landforms", "A", "Geomorphic processes and landforms",
  "Weathering, erosion and deposition by rivers, glaciers, wind, waves and groundwater, and the landforms they form.",
  ["Weathering: physical, chemical, biological; mass wasting", "Fluvial landforms: valleys, meanders, deltas, oxbow lakes", "Glacial landforms: cirques, moraines, drumlins, fjords", "Aeolian landforms: dunes, loess, mushroom rocks", "Coastal landforms: cliffs, stacks, spits, lagoons", "Karst topography", "Erosion cycles", "Rocks and the rock cycle"],
  ["Weathering vs erosion", "Delta vs estuary", "Igneous vs sedimentary vs metamorphic rock"],
  ["earth-structure-geomorphology"], "Processes and named landforms.", "Link landforms to processes and to hazards.", 4,
  ["S-GS1-10", "S-P1-06"], [r"weathering", r"erosion|deposition", r"\bdelta\b|oxbow|meander", r"glacier|glacial|moraine|fjord|cirque", r"dune|loess|aeolian", r"karst|limestone cave|stalactite", r"landform", r"igneous|sedimentary|metamorphic", r"rock cycle", r"coastal (landform|erosion)|lagoon|spit"], ["R-NCERT", "R-LEONG"], related=["earth-structure-geomorphology"])
X(G, "climate-phenomena-enso-jetstreams", "B", "Jet streams, ENSO, IOD and other climate phenomena",
  "Large-scale circulation features that shape weather and the monsoon.",
  ["Jet streams: subtropical and polar", "El Niño, La Niña and the Southern Oscillation", "Indian Ocean Dipole", "Madden–Julian Oscillation", "Western disturbances", "Intertropical Convergence Zone", "Walker and Hadley circulations", "Teleconnections and monsoon forecasting"],
  ["El Niño vs La Niña", "ENSO vs IOD", "Western disturbance vs tropical cyclone"],
  ["atmosphere-climatology"], "Mechanisms and effects.", "Explain impacts on Indian monsoon and agriculture.", 3,
  ["S-GS1-10", "S-P1-06"], [r"jet stream", r"El Ni[nñ]o|La Ni[nñ]a|ENSO|Southern Oscillation", r"Indian Ocean Dipole|\bIOD\b", r"Madden|\bMJO\b", r"western disturbance", r"ITCZ|Inter-?tropical Convergence", r"Walker|Hadley", r"teleconnection"], ["R-NCERT", "R-IMD", "R-LEONG"], related=["indian-monsoon-climate", "atmosphere-climatology"])
X(G, "world-climate-regions-biomes", "B", "World climate regions and biomes",
  "Köppen-style climatic types and the natural vegetation and human life of each.",
  ["Equatorial, tropical monsoon, savanna", "Hot deserts and steppes", "Mediterranean, temperate maritime and continental", "Taiga, tundra, polar", "Biomes and vegetation belts", "Altitudinal zonation", "Climate and human activity", "Climate change and shifting zones"],
  ["Savanna vs steppe", "Taiga vs tundra"],
  ["atmosphere-climatology"], "Regions, features and examples.", "Link climate type to agriculture and settlement.", 3,
  ["S-GS1-10"], [r"equatorial|savanna|steppe|prairie|pampas|veld", r"Mediterranean (climate|region)", r"taiga|tundra", r"tropical (rainforest|monsoon|desert)", r"temperate (grassland|forest)", r"biome", r"K[oö]ppen", r"hot desert|Sahara|Atacama|Kalahari"], ["R-NCERT", "R-LEONG"], related=["biogeography-soils-vegetation"])
X(G, "world-regional-geography-features", "E", "World physical features: mountains, rivers, deserts, lakes and straits",
  "Locational knowledge of major features worldwide, tested often in map-based and 'in news' questions.",
  ["Major mountain ranges and plateaus", "Major rivers, basins and lakes", "Deserts of the world", "Seas, straits, gulfs and canals", "Islands and archipelagos", "Rift valleys", "Volcanic belts: Ring of Fire", "Countries and capitals in the news"],
  ["Strait vs channel", "Gulf vs bay"],
  [], "Locations and neighbours.", "Link features to trade, chokepoints and conflicts.", 4,
  ["S-GS1-10", "S-P1-06"], [r"strait of|\bstrait\b", r"\bGulf of", r"\bSea\b.*(bordered|located|lies)", r"\bAndes|\bAlps\b|Rockies|\bUrals\b|Atlas Mountains", r"Amazon|Nile|Danube|Mississippi|Yangtze|Mekong|Euphrates", r"Lake (Victoria|Baikal|Titicaca|Superior|Chad)", r"Suez|Panama Canal", r"Ring of Fire", r"Rift Valley", r"archipelago"], ["R-NCERT", "R-LEONG"], cross_ids=["geography-world-political-geography-borders"], related=["transport-infrastructure-geography"])
X(G, "global-resources-distribution", "D", "Global distribution of resources, agriculture and industry",
  "Where major minerals, energy, crops and industries are located worldwide.",
  ["World distribution of iron, coal, oil, gas and critical minerals", "Rare earths and critical mineral supply chains", "Major crops and agricultural regions", "Fisheries and fishing grounds", "Industrial regions of the world", "Energy chokepoints", "Resource geopolitics", "Shifts in industrial location"],
  ["Renewable vs non-renewable resource", "Primary vs secondary vs tertiary activity"],
  ["minerals-industries-location"], "Locations and leading producers.", "Discuss resource geopolitics and supply chains.", 3,
  ["S-GS1-11", "S-GS1-10"], [r"rare earth|critical mineral|lithium|cobalt", r"iron ore|coal (reserves|belt)|oil (reserves|fields)", r"fishing ground|fisher", r"industrial region", r"leading producer|largest producer", r"OPEC", r"resource (nationalism|geopolitics)", r"supply chain"], ["R-NCERT", "R-LEONG"], cross_ids=["economy-international-trade-wto"], related=["minerals-industries-location"])
X(G, "indian-energy-industry-regions", "D", "Indian energy resources and industrial regions",
  "Location of coal, oil, gas, nuclear and renewable energy, and India's industrial regions.",
  ["Coalfields: Gondwana and Tertiary", "Oil and gas basins: Assam, Mumbai High, Krishna–Godavari", "Thermal, hydro, nuclear and renewable plant locations", "Iron and steel clusters", "Cotton textile, sugar, cement, automobile, IT industry location", "Industrial regions and corridors", "Factors of location", "Resource-linked regional disparities"],
  ["Gondwana vs Tertiary coal", "Industrial region vs corridor"],
  ["minerals-industries-location"], "Names and locations.", "Explain location factors and regional imbalance.", 4,
  ["S-GS1-11"], [r"coalfield|Gondwana coal|Jharia|Raniganj", r"Mumbai High|Krishna[- ]Godavari|Digboi", r"thermal power|hydro(electric)? (power|project)|nuclear power plant", r"iron and steel|Bhilai|Jamshedpur|Rourkela|Bokaro", r"cotton textile|sugar industry|cement industry|automobile (hub|industry)", r"industrial (region|corridor|belt)", r"location of (industries|industry)", r"Kudankulam|Tarapur|Narora"], ["R-NCERT", "R-LEONG", "R-SOI"], cross_ids=["economy-energy-sector-economy"], related=["minerals-industries-location"])
X(G, "human-geography-settlements-migration", "E", "Human geography: settlements, migration and cultural regions",
  "Settlement patterns, migration, races, tribes and cultural landscapes.",
  ["Rural and urban settlement types and patterns", "Site and situation of cities", "Push and pull factors of migration", "Races, tribes and languages of the world", "Cultural landscapes and diffusion", "Human development and spatial inequality", "Urban hierarchy and primate cities", "Land use and urban sprawl"],
  ["Site vs situation", "Push vs pull factor", "Migration vs immigration"],
  ["population-demography-urbanisation"], "Terms and examples.", "Analyse migration and urban growth problems.", 3,
  ["S-GS1-07", "S-GS1-11"], [r"settlement", r"push (and|vs) pull|push factor|pull factor", r"migration", r"urban (sprawl|hierarchy|agglomeration)|primate city|megacity|million[- ]plus", r"\brace\b|ethnic group|tribes of", r"cultural (landscape|region|diffusion)", r"site and situation"], ["R-NCERT", "R-CENSUS"], related=["population-demography-urbanisation"])
X(G, "india-map-locations", "C", "India map and locations: passes, ports, parks, power plants and places in news",
  "Locational facts about India's physical and economic geography that are frequently asked in map-linked questions.",
  ["Mountain passes of the Himalaya", "Major and minor ports", "National parks, sanctuaries and biosphere reserves by State", "Hill ranges, plateaus and peaks", "Rivers' origin and confluences; waterfalls", "Lakes and wetlands", "Dams and multipurpose projects", "Union Territories, capitals and international borders", "Places in the news"],
  ["Pass vs gap", "Major vs minor port"],
  ["indian-physical-geography"], "Locations and neighbours.", "Link locations to strategy and resource use.", 4,
  ["S-GS1-10", "S-P1-06"], [r"Nathu La|Zoji La|Khardung|Shipki La|Bara-?lacha|Rohtang|Banihal|Jelep La", r"major port|Kandla|Paradip|Tuticorin|Ennore|Kolkata port|Mormugao", r"national park|biosphere reserve", r"Western Ghats|Eastern Ghats|Aravalli|Satpura|Vindhya|Nilgiri", r"waterfall|Jog Falls|Dudhsagar", r"\bdam\b|Bhakra|Tehri|Hirakud|Sardar Sarovar", r"Union Territor", r"Chilika|Wular|Sambhar|Loktak|Pulicat", r"peak (of|in)|Kanchenjunga|Nanda Devi|Anamudi"], ["R-SOI", "R-NCERT"], related=["indian-physical-geography", "rivers-water-resources"])
X(G, "remote-sensing-gis-maps", "E", "Maps, remote sensing, GIS and GPS",
  "Cartography basics and spatial technologies used in planning and disaster management.",
  ["Types of maps and map scales", "Toposheets and Survey of India", "Remote sensing: sensors and platforms", "GIS: layers, vector and raster", "GPS and NavIC", "Applications: land use, disaster, agriculture", "Bhuvan portal", "Drones and mapping"],
  ["Raster vs vector data", "Active vs passive sensors"],
  [], "Definitions and applications.", "Show applications in governance and disaster management.", 2,
  ["S-GS1-10", "S-GS3-11"], [r"remote sensing", r"\bGIS\b|geographic information", r"\bGPS\b|\bNavIC\b|navigation", r"toposheet|Survey of India", r"map scale|cartograph", r"\bBhuvan\b", r"satellite (imagery|data)|resourcesat"], ["R-SOI", "R-ISRO"], cross_ids=["scitech-space-technology"], related=["transport-infrastructure-geography"])

# ================================================================ ENVIRONMENT
V = "environment"
X(V, "species-conservation-iucn-cites", "B", "Species conservation: IUCN Red List, CITES and conservation strategies",
  "Categories of threat, trade regulation and in-situ and ex-situ conservation of species.",
  ["IUCN Red List categories", "CITES appendices and wildlife trade", "In-situ vs ex-situ conservation; zoos, gene banks, seed banks", "Project Tiger, Project Elephant and other species projects", "Keystone, flagship, umbrella species", "Wildlife Protection Act schedules", "Convention on Migratory Species", "Reintroduction programmes (cheetah)"],
  ["In-situ vs ex-situ", "Endangered vs vulnerable vs critically endangered", "CITES vs CMS"],
  ["biodiversity-types-hotspots"], "Categories, instruments and projects.", "Evaluate species projects and trade controls.", 4,
  ["S-GS3-09", "S-P1-08"], [r"IUCN|Red List", r"\bCITES\b", r"in-?situ|ex-?situ", r"Project (Tiger|Elephant|Cheetah|Snow Leopard)", r"keystone|flagship species|umbrella species", r"Wildlife \(Protection\) Act|Schedule I", r"Migratory Species|\bCMS\b", r"critically endangered|endangered species", r"gene bank|seed bank"], ["R-MOEF", "R-CBD", "R-NCERT"], related=["protected-areas-wildlife"])
X(V, "forest-resources-policy", "B", "Forest resources, forest cover and forest policy",
  "Types of forests, forest cover assessment, policy and community rights.",
  ["Forest types of India", "India State of Forest Report", "National Forest Policy and Forest Conservation Act", "Compensatory afforestation and CAMPA", "Joint Forest Management and community rights", "Deforestation and its drivers", "REDD+", "Agroforestry and green cover targets"],
  ["Forest cover vs tree cover", "Reserved vs protected forest"],
  ["ecosystem-ecology-basics"], "Types, laws and reports.", "Weigh development needs against forest conservation.", 3,
  ["S-GS3-09", "S-P1-08"], [r"forest (cover|type|report|policy|conservation)", r"State of Forest Report|\bISFR\b", r"Forest Conservation Act", r"\bCAMPA\b|compensatory afforestation", r"Joint Forest Management|\bJFM\b", r"deforestation", r"\bREDD\b", r"agroforestry", r"reserved forest|protected forest"], ["R-MOEF", "R-NCERT"], cross_ids=["society-tribal-society-issues"], related=["sustainable-agriculture-forestry", "environmental-governance-legislation"])
X(V, "marine-coastal-crz", "B", "Marine and coastal ecosystems and coastal regulation",
  "Oceans, estuaries and coasts: ecology, threats and regulation.",
  ["Coastal Regulation Zone notifications", "Marine protected areas and biosphere reserves", "Coral bleaching, ocean acidification", "Mangroves and sea-grass", "Marine pollution: plastics, oil spills, ballast water", "Fisheries and overfishing", "Blue economy", "Ocean-related treaties and the High Seas treaty"],
  ["Estuary vs lagoon", "Coastal Regulation Zone categories"],
  ["wetlands-water-conservation"], "Concepts and regulations.", "Link coastal regulation to development and vulnerability.", 3,
  ["S-GS3-09", "S-P1-08"], [r"Coastal Regulation Zone|\bCRZ\b", r"marine (protected|ecosystem|pollution|biodiversity)", r"coral|bleaching", r"ocean acidification", r"mangrove|sea-?grass", r"ballast water|oil spill", r"overfishing|fisheries", r"High Seas|BBNJ", r"blue economy"], ["R-MOEF", "R-NCERT"], cross_ids=["security-maritime-security-indian-ocean"], related=["wetlands-water-conservation"])
X(V, "invasive-species-human-wildlife-conflict", "B", "Invasive species and human–wildlife conflict",
  "Alien species, their impacts and managing conflict between people and wildlife.",
  ["Invasive alien species: water hyacinth, Lantana, Prosopis", "Pathways of introduction; biosecurity", "Impacts on native biodiversity and livelihoods", "Human–elephant, tiger and leopard conflict", "Compensation and mitigation measures", "Corridors and habitat connectivity", "Poaching and illegal wildlife trade", "Zoonotic spillover link"],
  ["Alien vs invasive species", "Native vs endemic"],
  ["species-conservation-iucn-cites"], "Examples and measures.", "Discuss coexistence strategies and policy tools.", 2,
  ["S-GS3-09", "S-P1-08"], [r"invasive", r"alien species", r"water hyacinth|Lantana|Prosopis|Parthenium", r"human[- ]wildlife|human[- ]elephant|man[- ]animal conflict", r"wildlife corridor|elephant corridor", r"poaching", r"illegal wildlife trade", r"endemic"], ["R-MOEF", "R-CBD"], related=["protected-areas-wildlife"])
X(V, "carbon-markets-climate-finance", "C", "Carbon markets, climate finance and net-zero targets",
  "Market and finance instruments for climate action and national targets.",
  ["Carbon credits and trading; Paris Agreement Article 6", "Carbon Credit Trading Scheme in India", "Carbon tax and CBAM", "Green Climate Fund and climate finance", "Net-zero pledges and NDCs; India's 2070 target", "Green bonds", "Offsets, additionality and permanence", "Just transition"],
  ["Carbon tax vs carbon trading", "Mitigation vs adaptation finance"],
  ["climate-change-ghg"], "Instruments and agreements.", "Assess market-based tools and equity concerns.", 3,
  ["S-GS3-10", "S-P1-08"], [r"carbon (credit|market|trading|tax|offset)", r"\bCBAM\b|border adjustment", r"Green Climate Fund|climate finance", r"net[- ]zero|NDC|nationally determined", r"green bond", r"Article 6", r"just transition", r"Paris Agreement"], ["R-UNFCCC", "R-IPCC", "R-MOEF"], cross_ids=["economy-international-economic-institutions"], related=["international-treaties-summits"])
X(V, "environmental-organisations-indices", "D", "Environmental organisations, reports and indices",
  "Bodies, flagship reports and rankings that are asked as 'who publishes what'.",
  ["UNEP, UNDP, IUCN, WWF, IPBES, GEF, IPCC", "Reports: Emissions Gap, Living Planet, Global Environment Outlook, State of the World's Forests", "Indices: Environmental Performance Index, Climate Change Performance Index", "Ramsar, World Heritage and MAB programmes", "Indian bodies: CPCB, BSI, ZSI, WII, NGT", "Environmental awards", "International days and campaigns", "Initiatives like LiFE and Mission Green"],
  ["UNEP vs UNDP", "Publisher vs index"],
  [], "Name, mandate and key publication.", "Use to cite evidence in answers.", 2,
  ["S-GS3-09", "S-P1-08"], [r"\bUNEP\b|\bUNDP\b|\bIPBES\b|\bGEF\b|Global Environment Facility", r"Emissions Gap|Living Planet|Global Environment Outlook|Global Risks", r"Environmental Performance Index|\bEPI\b|Climate Change Performance", r"Botanical Survey|Zoological Survey|Wildlife Institute", r"\bWWF\b", r"Man and the Biosphere|\bMAB\b", r"Mission LiFE|Lifestyle for Environment", r"\bIPCC\b"], ["R-MOEF", "R-UNFCCC"], related=["international-treaties-summits", "environmental-governance-legislation"])
X(V, "sustainable-development-green-economy", "D", "Sustainable development, circular economy and green economy",
  "Frameworks that balance growth and environment: SDGs, circular economy, EPR and green finance.",
  ["Sustainable development: Brundtland definition and pillars", "Circular economy and waste hierarchy", "Extended Producer Responsibility", "Green GDP and ecosystem services", "Ecological footprint and carrying capacity", "Green buildings and ratings", "Sustainable consumption and lifestyle (LiFE)", "Environmental ethics and equity"],
  ["Sustainable development vs sustainable growth", "Carrying capacity vs ecological footprint"],
  ["ecosystem-ecology-basics"], "Concepts and instruments.", "Debate development–environment trade-offs.", 3,
  ["S-GS3-09", "S-GS3-01"], [r"sustainable development", r"circular economy", r"Extended Producer Responsibility|\bEPR\b", r"ecological footprint|carrying capacity", r"ecosystem services", r"green (building|economy|growth)|\bGRIHA\b|\bLEED\b", r"Brundtland", r"waste hierarchy|reduce, reuse"], ["R-MOEF", "R-NITI", "R-SURVEY"], cross_ids=["economy-sdg-inclusive-growth"], related=["pollution-waste-management"])

RATIONALE = {
    ("economy-sdg-inclusive-growth", "environment-sustainable-development-green-economy"): "SDG targets and green-economy tools are the same agenda seen from the economy and environment sides.",
    ("economy-energy-sector-economy", "environment-renewable-energy-green-tech"): "Energy sector economics (cost, DISCOM health) determines the pace of renewable adoption.",
    ("economy-energy-sector-economy", "geography-indian-energy-industry-regions"): "Where coal, oil and power plants are located shapes the economics of the energy sector.",
    ("economy-agriculture-marketing-pricing-credit", "governance-food-security-pds"): "MSP procurement feeds the PDS; both belong to the same food-policy loop.",
    ("economy-subsidies-direct-transfers", "governance-food-security-pds"): "The food subsidy is delivered through the PDS and increasingly through DBT.",
    ("economy-unemployment-labour-markets", "governance-rural-development-schemes"): "MGNREGA and skilling schemes are the state's main responses to unemployment.",
    ("geography-world-regional-geography-features", "geography-world-political-geography-borders"): "Physical features often define political borders and strategic chokepoints.",
    ("geography-global-resources-distribution", "economy-international-trade-wto"): "Resource location drives trade patterns and supply-chain risk.",
    ("geography-remote-sensing-gis-maps", "scitech-space-technology"): "Remote sensing relies on satellite technology studied under Science & Technology.",
    ("environment-forest-resources-policy", "society-tribal-society-issues"): "Forest rights and community forest management are central to tribal livelihoods.",
    ("environment-marine-coastal-crz", "security-maritime-security-indian-ocean"): "Coastal regulation and maritime security both depend on coastal-zone management.",
    ("environment-carbon-markets-climate-finance", "economy-international-economic-institutions"): "Climate finance flows through multilateral institutions such as the GCF and development banks.",
}
