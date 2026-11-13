"""Phase D batch 3: Ethics (GS-IV) and World History (added to the History subject).
Same rules as batches 1-2: AI-written from general knowledge, draft-unreviewed, no book chapters, no statistics, no invented quotes."""
import author_polity as P
import author_subjects as S
from author_subjects import X

S.GROUPS["history"] = S.GROUPS["history"] + [("H", "World history")]
S.GROUPS["ethics"] = [("A", "Ethics and human interface"), ("B", "Attitude, aptitude and emotional intelligence"), ("C", "Thinkers and public-service values"), ("D", "Probity in governance and case studies")]

# ===================================================================== ETHICS (GS-IV)
T = "ethics"
X(T, "essence-dimensions", "A", "Essence, determinants and dimensions of ethics",
  "What ethics is, what shapes human conduct, and the main branches and contexts of ethics.",
  ["Ethics, morals, values, laws: meaning and overlap", "Determinants: family, society, institutions, education, religion, law", "Consequences of ethics in human action", "Normative, meta- and applied ethics", "Ethics in private and public relationships", "Role of family, society and educational institutions in values", "Ethics vs morality vs law", "Moral intuition and conscience"],
  ["Ethics vs morality", "Ethics vs law", "Values vs norms", "Public vs private ethics"],
  [], "Definitions and the distinctions above.", "Illustrate each idea with administrative examples; link to civil-service conduct.", 4,
  ["S-GS4-02"], [r"\bethic", r"moral", r"\bvalues?\b", r"conscience", r"human (action|conduct)", r"private (and|vs) public", r"determinants? of"], ["R-ARC"], related=["moral-thinkers-philosophers", "ethical-dilemmas-conflict-of-interest"])
X(T, "ethical-dilemmas-conflict-of-interest", "A", "Ethical dilemmas, conflict of interest and accountability",
  "Handling situations where values or duties conflict, and managing personal vs public interest.",
  ["Ethical dilemma vs ethical issue", "Conflict of interest: actual, potential, perceived", "Resolving dilemmas: law, conscience, consequences, consultation", "Accountability and answerability", "Dual loyalty and divided duties", "Personal vs official ethics", "Gift, hospitality and post-retirement concerns", "Public interest test"],
  ["Dilemma vs temptation", "Conflict of interest vs corruption"],
  ["essence-dimensions"], "Definitions and steps for resolving a dilemma.", "Structure answers: stakeholders, options, consequences, chosen course and justification.", 4,
  ["S-GS4-07", "S-GS4-09"], [r"dilemma", r"conflict of interest", r"\bconflict\b.*(duty|interest|loyalty)", r"accountab", r"public interest", r"divided (loyalty|duty)", r"whistle"], ["R-ARC"], related=["probity-governance-corruption", "civil-service-values-aptitude"])
X(T, "attitude-persuasion", "B", "Attitude, social influence and persuasion",
  "Content, structure and function of attitudes, and how they relate to behaviour and change.",
  ["Components: cognitive, affective, behavioural", "Functions of attitude", "Attitude and behaviour; cognitive dissonance", "Moral and political attitudes", "Prejudice, stereotypes, bias", "Social influence: conformity, obedience", "Persuasion and attitude change", "Media and public opinion"],
  ["Attitude vs opinion vs belief", "Prejudice vs stereotype vs discrimination"],
  [], "Definitions and components.", "Apply to administration: bias, public perception, behaviour change campaigns.", 3,
  ["S-GS4-03"], [r"attitude", r"persuasion", r"prejudice|stereotype|bias", r"cognitive dissonance", r"conformity|obedience", r"social influence", r"public opinion", r"political attitude"], ["R-ARC"], related=["emotional-intelligence"])
X(T, "civil-service-values-aptitude", "B", "Foundational values and aptitude for civil service",
  "Integrity, impartiality, non-partisanship, objectivity, dedication, empathy, tolerance and compassion as civil-service values.",
  ["Integrity and honesty", "Impartiality and non-partisanship", "Objectivity and neutrality", "Dedication to public service", "Empathy, tolerance, compassion toward the weak", "Courage and moral courage", "Aptitude for civil service", "Selflessness and leadership"],
  ["Impartiality vs neutrality", "Empathy vs sympathy vs compassion", "Objectivity vs non-partisanship"],
  ["essence-dimensions"], "Meaning of each value with one example.", "Show how each value is tested in decisions.", 4,
  ["S-GS4-04"], [r"integrity", r"impartial", r"non-?partisan", r"objectiv", r"empathy|compassion|tolerance", r"dedication", r"moral courage|courage", r"neutrality", r"civil servant", r"aptitude"], ["R-ARC", "R-UPSC"], cross_ids=["governance-civil-services-role"], related=["emotional-intelligence", "public-service-ethics"])
X(T, "emotional-intelligence", "B", "Emotional intelligence in administration",
  "Concepts and components of emotional intelligence and their use in governance.",
  ["Components: self-awareness, self-regulation, motivation, empathy, social skills", "Goleman and Salovey–Mayer models (conceptual)", "EI vs IQ", "Use in decision-making, leadership and conflict handling", "Developing EI", "Stress management and resilience", "EI in public dealing and teams"],
  ["EI vs IQ", "Empathy vs emotional control"],
  [], "Components and an example of each.", "Link EI to field administration and crisis handling.", 2,
  ["S-GS4-05"], [r"emotional intelligence", r"self[- ]awareness", r"self[- ]regulation", r"empathy", r"\bEQ\b", r"stress (management|handling)", r"resilien"], ["R-ARC"], related=["attitude-persuasion", "civil-service-values-aptitude"])
X(T, "moral-thinkers-philosophers", "C", "Moral thinkers and philosophers from India and the world",
  "Contributions of Indian and Western thinkers to ethics and their relevance for administration.",
  ["Indian: Gandhi, Ambedkar, Vivekananda, Tagore, Buddha, Mahavira, Kautilya, Thiruvalluvar", "Concepts: ahimsa, satyagraha, trusteeship, dhamma, nishkama karma", "Western: Socrates, Plato, Aristotle (virtue ethics)", "Kant (deontology), Mill and Bentham (utilitarianism), Rawls (justice)", "Confucius and Eastern traditions", "Care ethics and modern thinkers", "Relevance to governance today"],
  ["Deontology vs utilitarianism vs virtue ethics", "Gandhian vs utilitarian view of means and ends"],
  ["essence-dimensions"], "Name the thinker, the core idea and one application.", "Apply a thinker's idea to a modern administrative problem without misquoting.", 5,
  ["S-GS4-06"], [r"Gandhi", r"Ambedkar", r"Vivekananda", r"Kant", r"utilitarian|Bentham|Mill\b", r"Aristotle|Plato|Socrates", r"Rawls", r"Buddha|Mahavira", r"Kautilya", r"virtue ethics|deontolog", r"Thiruvalluvar|Tagore", r"means and ends|trusteeship|ahimsa|satyagraha"], ["R-NCERT"], related=["essence-dimensions"])
X(T, "public-service-ethics", "C", "Ethics in public administration",
  "Status and problems of ethics in government and private institutions, laws and codes that support ethical conduct.",
  ["Codes of ethics and conduct; Seven Principles of Public Life (Nolan)", "Conduct rules for civil servants", "Ethical concerns in public and private institutions", "Ethical governance and corporate governance", "Corporate social responsibility", "Laws, rules, regulations and conscience as sources of guidance", "Accountability and ethical audit", "Ethics in international relations and funding"],
  ["Code of ethics vs code of conduct", "Public vs private sector ethics"],
  ["civil-service-values-aptitude"], "Codes and bodies.", "Evaluate institutional safeguards against unethical conduct.", 3,
  ["S-GS4-07"], [r"code of (ethics|conduct)", r"Nolan|public life", r"conduct rules", r"corporate (governance|social responsibility)|\bCSR\b", r"ethical (governance|concern|audit)", r"private (sector|institution)", r"public administration"], ["R-ARC", "R-UPSC"], cross_ids=["governance-civil-services-role"], related=["probity-governance-corruption"])
X(T, "probity-governance-corruption", "D", "Probity in governance, corruption and transparency",
  "Concept of public service, philosophical basis of probity, and tools for transparency and the fight against corruption.",
  ["Concept of public service and probity", "Philosophical basis of governance", "RTI and information sharing", "Codes of ethics and citizens' charters", "Work culture and quality of service delivery", "Corruption: causes, effects, remedies", "Lokpal, CVC, Prevention of Corruption Act", "Whistleblower protection", "Utilisation of public funds"],
  ["Probity vs integrity", "Corruption vs conflict of interest"],
  ["civil-service-values-aptitude"], "Institutions and laws.", "Evaluate anti-corruption architecture and its gaps.", 4,
  ["S-GS4-08", "S-GS4-01"], [r"probity", r"corruption", r"\bRTI\b|Right to Information", r"citizen.?s charter", r"Lokpal|Lokayukta", r"Central Vigilance|\bCVC\b", r"Prevention of Corruption", r"whistle[- ]?blower", r"public funds", r"work culture", r"service delivery"], ["R-ARC", "R-RTI", "R-CIC"], cross_ids=["governance-transparency-e-governance-citizens-charter"], related=["ethical-dilemmas-conflict-of-interest", "public-service-ethics"])
X(T, "case-study-method", "D", "Case-study answer method (GS-IV)",
  "A repeatable way to read, structure and answer GS-IV case studies, with the values and laws each type usually tests.",
  ["Identify stakeholders and their interests", "Identify the ethical issues and the conflicting values", "List options with pros, cons and consequences", "Choose a course consistent with law, values and public interest", "Justify the choice and mention mitigation and follow-up", "Typical settings: field administration, corruption, whistleblowing, gender, communal harmony, environment", "Time and word management"],
  ["Issue vs dilemma vs option", "Short-term fix vs systemic solution"],
  ["ethical-dilemmas-conflict-of-interest", "civil-service-values-aptitude"], "Know the steps.", "Practise with the supplied GS-IV questions once their OCR text is verified.", 3,
  ["S-GS4-09"], [r"you are (the )?(District|Collector|Superintendent|Secretary|Chief|Commissioner|an? (officer|IAS|engineer|official))", r"case study", r"what (would|will|are) (be )?(your|the) (options|course)", r"stakeholder", r"as (a|the) (District|Collector|officer)", r"examine the options"], ["R-ARC"], related=["ethical-dilemmas-conflict-of-interest"])

# ===================================================================== WORLD HISTORY (in History subject)
H = "history"
X(H, "industrial-revolution-capitalism", "H", "Industrial Revolution, capitalism and the age of revolutions",
  "Technological and economic change in 18th–19th century Europe and the political revolutions (American, French) that reshaped the world.",
  ["Causes of the Industrial Revolution in Britain", "Spread to Europe, the US and Japan", "Social effects: urbanisation, working class, reform", "Capitalism, liberalism, socialism", "American Revolution", "French Revolution and Napoleon", "Unification of Italy and Germany", "Impact on colonies and trade"],
  ["First vs second industrial revolution", "Liberalism vs socialism"],
  [], "Causes, sequence and effects.", "Link industrialisation to colonialism and to India's de-industrialisation.", 4,
  ["S-GS1-05"], [r"Industrial Revolution", r"French Revolution|Napoleon", r"American (Revolution|War of Independence)", r"unification of (Italy|Germany)", r"capitalism", r"socialism|Marx", r"liberalism", r"Enlightenment"], ["R-NCERT"], related=["colonisation-imperialism"])
X(H, "colonisation-imperialism", "H", "Colonisation, imperialism and redrawal of boundaries",
  "European expansion into Africa and Asia, the scramble for colonies and the redrawing of national boundaries.",
  ["Mercantilism and early colonialism", "Scramble for Africa", "Opium Wars and China", "Japan's Meiji modernisation", "Imperialism: economic and ideological drivers", "Settler vs extractive colonies", "Redrawal of boundaries after wars", "Resistance movements"],
  ["Colonialism vs imperialism", "Settler vs plantation colonies"],
  ["industrial-revolution-capitalism"], "Regions, powers and motives.", "Explain economic motives and legacies of colonial boundaries.", 4,
  ["S-GS1-05"], [r"coloni[sz]ation|colonialism", r"imperialism", r"Scramble for Africa", r"Opium War", r"Meiji", r"redrawal|redrawing|boundar(y|ies)", r"mercantil", r"apartheid", r"Berlin Conference"], ["R-NCERT"], related=["world-wars-interwar"])
X(H, "world-wars-interwar", "H", "World Wars, revolutions and the interwar period",
  "Causes, course and consequences of the World Wars; Russian and Chinese revolutions; fascism and the Great Depression.",
  ["Causes of World War I; Versailles and the League of Nations", "Russian Revolution of 1917", "Rise of fascism and Nazism", "Great Depression", "Causes and course of World War II", "Holocaust and war crimes", "Atom bomb and end of the war", "Chinese Revolution", "Consequences for India's freedom struggle"],
  ["WWI vs WWII causes", "Fascism vs Nazism vs communism"],
  ["colonisation-imperialism"], "Chronology and causes.", "Assess consequences for the world order and decolonisation.", 5,
  ["S-GS1-05"], [r"World War", r"Versailles", r"League of Nations", r"Russian Revolution|Bolshevik|Lenin", r"fascis|Nazi|Hitler|Mussolini", r"Great Depression", r"Holocaust", r"Chinese Revolution|Mao\b", r"Hiroshima|Nagasaki"], ["R-NCERT"], related=["cold-war-decolonisation"])
X(H, "cold-war-decolonisation", "H", "Cold War, decolonisation and the post-war world",
  "Bipolar rivalry, decolonisation in Asia and Africa, and the end of the Cold War.",
  ["Origins of the Cold War; NATO and Warsaw Pact", "Korean and Vietnam Wars", "Non-Aligned Movement", "Decolonisation in Asia and Africa", "Arab–Israeli conflict (historical)", "Détente, arms control", "Collapse of the USSR and end of the Cold War", "European integration", "Rise of China and a multipolar world"],
  ["Cold War vs hot war", "NAM vs bloc politics"],
  ["world-wars-interwar"], "Events and alliances.", "Link post-war order to India's non-alignment and current IR.", 4,
  ["S-GS1-05", "S-GS2-19"], [r"Cold War", r"decoloni[sz]ation", r"Non[- ]Aligned", r"Warsaw Pact|\bNATO\b", r"Vietnam War|Korean War", r"collapse of (the )?(USSR|Soviet)|disintegration of (the )?(USSR|Soviet)", r"Berlin Wall", r"bipolar|unipolar|multipolar", r"European Union"], ["R-NCERT", "R-MEA"], cross_ids=["ir-global-conflicts-treaties"], related=["colonisation-imperialism"])

SUBJECT_META = {"ethics": ("Ethics & GS-IV case studies", "authored", ["Mains GS-IV"])}
RATIONALE = {
    ("ethics-civil-service-values-aptitude", "governance-civil-services-role"): "Civil-service values are tested through the role and reform of the services studied under Governance.",
    ("ethics-probity-governance-corruption", "governance-transparency-e-governance-citizens-charter"): "RTI, Lokpal and citizen's charters are the practical tools of probity.",
    ("history-cold-war-decolonisation", "ir-global-conflicts-treaties"): "Post-war alliances and conflicts form the background of today's IR questions.",
    ("history-colonisation-imperialism", "history-british-administration-economy"): "British rule in India is one case of the wider imperial system.",
    ("history-world-wars-interwar", "history-transfer-of-power-partition"): "The Second World War weakened Britain and shaped the transfer of power in India.",
}
