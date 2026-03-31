#!/usr/bin/env python3
"""Generate the WTG multilingual slide deck: JSON lang files + copy template to en/fr/nl dirs."""
import json, os, shutil

BASE = '/tmp/wtg-slides'
for d in ['en', 'fr', 'nl', 'lang']:
    os.makedirs(f'{BASE}/{d}', exist_ok=True)

# ─── Link constants ──────────────────────────────────────────────────────────
LK_AB = '<a href="https://be.linkedin.com/in/abdelkrimboujraf" target="_blank" style="color:var(--green)">Abdelkrim Boujraf</a>'
LK_ALT = '<a href="https://www.alt-f1.be" target="_blank" style="color:var(--green)">ALT-F1 SRL</a>'
LK_XF = '<a href="https://xflowdata.com" target="_blank" style="color:var(--green)">XFlowData</a>'
LK_OC = '<a href="https://openclaw.ai" target="_blank">OpenClaw</a>'
LK_JEF = '<a href="https://www.linkedin.com/in/jefminsart/" target="_blank" style="color:var(--green)">Jef Minsart</a>'
LK_XFD = '<a href="https://www.xflowdata.com" target="_blank">XFlowdata</a>'
LK_MU = '<a href="https://www.meetup.com" target="_blank">meetup.com</a>'
LK_OUG = '<a href="https://www.meetup.com/openclaw-user-group-belgium/events" target="_blank">OpenClaw User Group Belgium</a>'
LK_MM = '<a href="https://github.com/mattermost/mattermost" target="_blank">Mattermost</a>'
LK_OP = '<a href="https://www.openproject.org" target="_blank">OpenProject</a>'
LK_OPSK = '<a href="https://clawhub.ai/abdelkrim/openproject-by-altf1be" target="_blank">openproject-by-altf1be</a>'
LK_DRAW = '<a href="https://draw.io" target="_blank">Draw.io</a>'
LK_JIRASK = '<a href="https://github.com/ALT-F1-OpenClaw/openclaw-skill-atlassian-jira-by-altf1be" target="_blank">atlassian-jira-by-altf1be</a>'
LK_CH = '<a href="https://clawhub.ai" target="_blank">ClawHub</a>'
LK_NLTK = '<a href="https://www.nltk.org/" target="_blank" style="color:var(--green)">NLTK</a>'
LK_RASA = '<a href="https://rasa.com/" target="_blank" style="color:var(--green)">Rasa</a>'
LK_LUIS = '<a href="https://luis.azure.us/" target="_blank" style="color:var(--green)">LUIS</a>'
GH = 'https://github.com/ALT-F1-OpenClaw'

T = {}
def t(key, en, fr, nl):
    T[key] = {'en': en, 'fr': fr, 'nl': nl}

# ── page title ────────────────────────────────────────────────────────────────
t('page-title',
  'How I Use OpenClaw and AI Skills to Run My Projects',
  "Comment j'utilise OpenClaw et les Skills IA pour gérer mes projets",
  'Hoe ik OpenClaw en AI Skills gebruik om mijn projecten te beheren')

# ── S0 ────────────────────────────────────────────────────────────────────────
t('s0-tag', 'openclaw-for-project-managers /// alt-f1 · 2026',
  'openclaw-pour-chefs-de-projet /// alt-f1 · 2026',
  'openclaw-voor-projectmanagers /// alt-f1 · 2026')
t('s0-glitch', 'How I Use OpenClaw', "Comment j'utilise OpenClaw", 'Hoe ik OpenClaw gebruik')
t('s0-title-2', 'and AI Skills', 'et les Skills IA', 'en AI Skills')
t('s0-title-3', 'to Run My Projects', 'pour gérer mes projets', 'om mijn projecten te beheren')
t('s0-subtitle', 'PRINCE2, PMBoK or PMI for dummies like me',
  'PRINCE2, PMBoK ou PMI pour les nuls comme moi',
  'PRINCE2, PMBoK of PMI voor dummies zoals ik')
t('s0-author', f'By {LK_AB} — 30 March 2026', f'Par {LK_AB} — 30 mars 2026', f'Door {LK_AB} — 30 maart 2026')
t('s0-org', f'Founder, {LK_ALT} · Partner, {LK_XF} · Brussels &amp; Tunisia',
  f'Fondateur, {LK_ALT} · Partenaire, {LK_XF} · Bruxelles &amp; Tunisie',
  f'Oprichter, {LK_ALT} · Partner, {LK_XF} · Brussel &amp; Tunesië')

# ── S1 ────────────────────────────────────────────────────────────────────────
t('s1-title-1', 'Project management tools are', 'Les outils de gestion de projet sont', 'Projectmanagementtools zijn')
t('s1-title-2', 'powerful.', 'puissants.', 'krachtig.')
t('s1-title-3', 'Until you use them.', "Jusqu'à ce qu'on les utilise.", 'Tot je ze gebruikt.')
t('s1-body',
  'Project management tools are powerful. OpenProject, Jira, HubSpot — they can do almost anything. But "can do" and "actually get things done" are separated by a simple gap: <span class="hl">the manual effort</span>.<br><br>Setting up a project properly — creating work streams, work packages, backlogs, sprints, assigning members, configuring versions, linking dependencies, writing descriptions, organizing categories — takes hours.<br><br>Not because it\'s hard. Because it\'s tedious. And tedious work gets skipped or postponed.<br><br>The result? Projects start with a Gantt chart that looks great on Monday and is outdated by Wednesday.<br><br>I tried, by chance to fix that.',
  "Les outils de gestion de projet sont puissants. OpenProject, Jira, HubSpot — ils peuvent presque tout faire. Mais \"pouvoir faire\" et \"faire vraiment les choses\" sont séparés par un simple fossé : <span class=\"hl\">l'effort manuel</span>.<br><br>Mettre en place un projet correctement — créer des flux de travail, des work packages, des backlogs, des sprints, assigner des membres, configurer des versions, lier les dépendances, écrire des descriptions, organiser les catégories — prend des heures.<br><br>Pas parce que c'est difficile. Parce que c'est fastidieux. Et le travail fastidieux est ignoré ou reporté.<br><br>Le résultat ? Les projets démarrent avec un diagramme de Gantt qui a fière allure le lundi et qui est obsolète le mercredi.<br><br>J'ai essayé, par hasard, de résoudre ça.",
  'Projectmanagementtools zijn krachtig. OpenProject, Jira, HubSpot — ze kunnen bijna alles. Maar "kunnen doen" en "daadwerkelijk dingen gedaan krijgen" worden gescheiden door een simpele kloof: <span class="hl">de handmatige inspanning</span>.<br><br>Een project goed opzetten — werkstromen aanmaken, work packages, backlogs, sprints, leden toewijzen, versies configureren, afhankelijkheden koppelen, beschrijvingen schrijven, categorieën organiseren — kost uren.<br><br>Niet omdat het moeilijk is. Omdat het vervelend is. En vervelend werk wordt overgeslagen of uitgesteld.<br><br>Het resultaat? Projecten starten met een Gantt-diagram dat er maandag geweldig uitziet en woensdag al verouderd is.<br><br>Ik probeerde, bij toeval, dat op te lossen.')

# ── S2 ────────────────────────────────────────────────────────────────────────
t('s2-title-1', '2017-10 Project', '2017-10 Project', '2017-10 Project')
t('s2-title-2', 'management by', 'management by', 'management by')
t('s2-body',
  'I got back to one of the many projects I never finished because that was too complex to build at the time.<br><br>Here is the name of the directory ... it says it all "2017-10 Project management by"<br><br>The description of the project resided in one screenshot named "smart editor.PNG".<br><br>The idea was simple: write in plain English a description of the activity and produces the equivalent in a structured database schema like Jira, Wrike etc: who does what, when, for how long, list dependencies etc etc',
  "Je suis revenu sur un des nombreux projets que je n'avais jamais terminés parce que c'était trop complexe à construire à l'époque.<br><br>Voici le nom du répertoire ... il dit tout \"2017-10 Project management by\"<br><br>La description du projet résidait dans une seule capture d'écran nommée \"smart editor.PNG\".<br><br>L'idée était simple : écrire en anglais courant une description de l'activité et produire l'équivalent dans un schéma de base de données structuré comme Jira, Wrike etc : qui fait quoi, quand, pour combien de temps, lister les dépendances etc etc",
  'Ik ging terug naar een van de vele projecten die ik nooit had afgemaakt omdat het te complex was om te bouwen op dat moment.<br><br>Hier is de naam van de map ... die zegt alles "2017-10 Project management by"<br><br>De beschrijving van het project zat in één screenshot genaamd "smart editor.PNG".<br><br>Het idee was simpel: schrijf in gewoon Engels een beschrijving van de activiteit en produceer het equivalent in een gestructureerd databaseschema zoals Jira, Wrike etc: wie doet wat, wanneer, hoe lang, afhankelijkheden opsommen etc etc')

# ── S3 ────────────────────────────────────────────────────────────────────────
t('s3-title-1', 'Several', 'Plusieurs', 'Meerdere')
t('s3-title-2', 'attempts', 'tentatives', 'pogingen')
t('s3-phase-1-desc',
  f'I tried a first time implementing Natural Language Processing (NLP) using {LK_NLTK}. Unfortunately NLTK required mastering advanced linguistic theories, probabilistic models, and sophisticated text-processing techniques, which made it particularly challenging at the time for me.',
  f"J'ai essayé une première fois d'implémenter le Natural Language Processing (NLP) avec {LK_NLTK}. Malheureusement, NLTK nécessitait la maîtrise de théories linguistiques avancées, de modèles probabilistes et de techniques sophistiquées de traitement de texte, ce qui le rendait particulièrement difficile pour moi à l'époque.",
  f'Ik probeerde een eerste keer Natural Language Processing (NLP) te implementeren met {LK_NLTK}. Helaas vereiste NLTK het beheersen van geavanceerde taalkundige theorieën, probabilistische modellen en geavanceerde tekstverwerkingstechnieken, wat het destijds bijzonder uitdagend maakte voor mij.')
t('s3-phase-2-desc',
  f'I tried a second time in 2019 using {LK_RASA}, an Open source machine learning framework; It was the beginning of the usage of the GPUs to mine Bitcoins',
  f"J'ai essayé une deuxième fois en 2019 avec {LK_RASA}, un framework open source de machine learning ; C'était le début de l'utilisation des GPUs pour miner des Bitcoins",
  f"Ik probeerde een tweede keer in 2019 met {LK_RASA}, een open source machine learning framework; Het was het begin van het gebruik van GPU's om Bitcoins te minen")
t('s3-phase-3-desc',
  f"Then a third time somewhere in 2020 Microsoft's Language Understanding Intelligent Service {LK_LUIS}, a cloud-based NLP tool but it didn't work neither.",
  f"Puis une troisième fois quelque part en 2020 avec le Language Understanding Intelligent Service de Microsoft {LK_LUIS}, un outil NLP cloud mais ça n'a pas marché non plus.",
  f"Toen een derde keer ergens in 2020 Microsoft's Language Understanding Intelligent Service {LK_LUIS}, een cloudgebaseerde NLP-tool maar het werkte ook niet.")
t('s3-phase-4-desc',
  'In February 2026, I decided to give it a try using OpenClaw combined with Large Language Models (LLM) and Skills I implemented. It took me a dozen of hours to reach my initial goal :-/',
  "En février 2026, j'ai décidé de tenter le coup en utilisant OpenClaw combiné avec des Large Language Models (LLM) et des Skills que j'ai implémentés. Il m'a fallu une douzaine d'heures pour atteindre mon objectif initial :-/",
  'In februari 2026 besloot ik het te proberen met OpenClaw gecombineerd met Large Language Models (LLM) en Skills die ik heb geïmplementeerd. Het kostte me een tiental uren om mijn oorspronkelijke doel te bereiken :-/')

# ── S4 ────────────────────────────────────────────────────────────────────────
t('s4-title-1', 'Enter', 'Voici', 'Maak kennis met')
t('s4-body-1',
  f'I have learned about {LK_OC} in February ... after reading the documentation I decided to pass this technology — I thought it was again a useless agent.',
  f"J'ai découvert {LK_OC} en février ... après avoir lu la documentation, j'ai décidé de passer cette technologie — je pensais que c'était encore un agent inutile.",
  f'Ik hoorde over {LK_OC} in februari ... na het lezen van de documentatie besloot ik deze technologie te negeren — ik dacht dat het weer een nutteloze agent was.')
t('s4-body-2',
  f'My colleague, {LK_JEF} from {LK_XFD} told me that he was participating to a {LK_MU} event organized by Toon Vanagt {LK_OUG}.<br><br>Jef "forced" me indirectly to study the technology.',
  f"Mon collègue, {LK_JEF} de {LK_XFD} m'a dit qu'il participait à un événement {LK_MU} organisé par Toon Vanagt {LK_OUG}.<br><br>Jef m'a \"forcé\" indirectement à étudier la technologie.",
  f'Mijn collega, {LK_JEF} van {LK_XFD} vertelde me dat hij deelnam aan een {LK_MU} evenement georganiseerd door Toon Vanagt {LK_OUG}.<br><br>Jef "dwong" me indirect om de technologie te bestuderen.')
t('s4-body-3',
  f'<span class="hl">In one sentence, OpenClaw is a Personal AI Assistant (PAT) running like a Linux Server : 24/7.</span><br><br>The user interacts with AI Agents through any Messaging platform like WhatsApp, Telegram, Discord, Signal, Slack, {LK_MM}.',
  f'<span class="hl">En une phrase, OpenClaw est un Assistant IA Personnel (PAT) qui tourne comme un serveur Linux : 24/7.</span><br><br>L\'utilisateur interagit avec les Agents IA via n\'importe quelle plateforme de messagerie comme WhatsApp, Telegram, Discord, Signal, Slack, {LK_MM}.',
  f'<span class="hl">In één zin: OpenClaw is een Persoonlijke AI Assistent (PAT) die draait als een Linux Server: 24/7.</span><br><br>De gebruiker communiceert met AI Agents via elk berichtenplatform zoals WhatsApp, Telegram, Discord, Signal, Slack, {LK_MM}.')
t('s4-body-4',
  'The difference with Chat Bots like ChatGPT, Gemini or Claude is that the server is alive and can interact with other systems even if you are not "connected".<br><br>For example, every morning I receive "the list of tasks updated in last 72h" in my feed.',
  'La différence avec les Chat Bots comme ChatGPT, Gemini ou Claude est que le serveur est vivant et peut interagir avec d\'autres systèmes même si vous n\'êtes pas "connecté".<br><br>Par exemple, chaque matin je reçois "la liste des tâches mises à jour dans les dernières 72h" dans mon fil.',
  'Het verschil met Chat Bots zoals ChatGPT, Gemini of Claude is dat de server leeft en kan communiceren met andere systemen zelfs als je niet "verbonden" bent.<br><br>Bijvoorbeeld, elke ochtend ontvang ik "de lijst van taken bijgewerkt in de laatste 72u" in mijn feed.')
t('s4-body-5',
  '<span class="hl">Nothing crazy one may say ?!?</span><br><br>Except that I asked to my "OpenProject or Jira Skill" to generate it using a simple sentence.',
  '<span class="hl">Rien de fou dirait-on ?!?</span><br><br>Sauf que j\'ai demandé à mon "Skill OpenProject ou Jira" de le générer en utilisant une simple phrase.',
  '<span class="hl">Niets geks zou men zeggen ?!?</span><br><br>Behalve dat ik mijn "OpenProject of Jira Skill" vroeg om het te genereren met een simpele zin.')
t('s4-body-6',
  '<span class="hl">A skill</span> is a packaged capability, a set of tools, scripts, and instructions that let the agent interact with real systems like Jira, HubSpot, SAP, Salesforce, Microsoft SharePoint, ServiceNow, Check Point Management, Fortinet, Google Cloud Dataplex, Kaseya etc ...<br><br>I built one of those skills. And it changed how I manage projects.',
  '<span class="hl">Un skill</span> est une capacité packagée, un ensemble d\'outils, de scripts et d\'instructions qui permettent à l\'agent d\'interagir avec des systèmes réels comme Jira, HubSpot, SAP, Salesforce, Microsoft SharePoint, ServiceNow, Check Point Management, Fortinet, Google Cloud Dataplex, Kaseya etc ...<br><br>J\'ai construit un de ces skills. Et ça a changé ma façon de gérer mes projets.',
  '<span class="hl">Een skill</span> is een verpakte mogelijkheid, een set tools, scripts en instructies die de agent laten communiceren met echte systemen zoals Jira, HubSpot, SAP, Salesforce, Microsoft SharePoint, ServiceNow, Check Point Management, Fortinet, Google Cloud Dataplex, Kaseya etc ...<br><br>Ik heb een van die skills gebouwd. En het veranderde hoe ik mijn projecten beheer.')

# ── S5 ────────────────────────────────────────────────────────────────────────
t('s5-title-1', 'The OpenProject Skill:', 'Le Skill OpenProject :', 'De OpenProject Skill:')
t('s5-title-2', 'What It Does', "Ce qu'il fait", 'Wat het doet')
t('s5-body', f'The {LK_OPSK} skill gives OpenClaw full operational access to an {LK_OP} instance via the API v3. OpenProject is a powerful Opensource Program/Project management system. We use it for our internal projects at XFlowdata.',
  f"Le skill {LK_OPSK} donne à OpenClaw un accès opérationnel complet à une instance {LK_OP} via l'API v3. OpenProject est un puissant système Open source de gestion de Programme/Projet. Nous l'utilisons pour nos projets internes chez XFlowdata.",
  f"De {LK_OPSK} skill geeft OpenClaw volledige operationele toegang tot een {LK_OP} instantie via de API v3. OpenProject is een krachtig Open source Programma/Projectmanagementsysteem. We gebruiken het voor onze interne projecten bij XFlowdata.")
t('s5-col-core-title', 'Core', 'Cœur', 'Kern')
t('s5-col-core-1', 'Work packages — create, read, update, delete, filter', 'Work packages — créer, lire, modifier, supprimer, filtrer', 'Work packages — aanmaken, lezen, bijwerken, verwijderen, filteren')
t('s5-col-core-2', 'Projects — create, configure, manage members and roles', 'Projets — créer, configurer, gérer membres et rôles', 'Projecten — aanmaken, configureren, leden en rollen beheren')
t('s5-col-core-3', 'Members &amp; roles — add users, assign roles', 'Membres &amp; rôles — ajouter des utilisateurs, assigner des rôles', 'Leden &amp; rollen — gebruikers toevoegen, rollen toewijzen')
t('s5-col-core-4', 'Versions/milestones — create sprints, set date ranges', 'Versions/jalons — créer des sprints, définir les plages de dates', 'Versies/mijlpalen — sprints aanmaken, datumbereiken instellen')
t('s5-col-core-5', 'Categories — organize work by domain', 'Catégories — organiser le travail par domaine', 'Categorieën — werk organiseren per domein')
t('s5-col-core-6', 'Relations — dependency chains (precedes, blocks, follows)', 'Relations — chaînes de dépendance (précède, bloque, suit)', 'Relaties — afhankelijkheidsketens (gaat vooraf, blokkeert, volgt)')
t('s5-col-ext-title', 'Extended', 'Étendu', 'Uitgebreid')
t('s5-col-ext-1', 'Comments &amp; attachments — add context to any work package', 'Commentaires &amp; pièces jointes — ajouter du contexte', 'Opmerkingen &amp; bijlagen — context toevoegen aan elk work package')
t('s5-col-ext-2', 'News — publish project announcements', 'Actualités — publier des annonces projet', 'Nieuws — projectaankondigingen publiceren')
t('s5-col-ext-3', 'Notifications, time entries, watchers, wiki pages', 'Notifications, saisie de temps, observateurs, pages wiki', "Notificaties, tijdregistratie, watchers, wikipagina's")
t('s5-col-ext-4', 'Custom fields, groups, documents, reminders', 'Champs personnalisés, groupes, documents, rappels', 'Aangepaste velden, groepen, documenten, herinneringen')
t('s5-body-2', '<span class="hl">All of this is accessible through natural language in a Discord channel.</span>',
  '<span class="hl">Tout cela est accessible en langage naturel dans un canal Discord.</span>',
  '<span class="hl">Dit alles is toegankelijk via natuurlijke taal in een Discord-kanaal.</span>')
t('s5-caption', 'Request made to OpenProject through an OpenClaw skill', 'Requête faite à OpenProject via un skill OpenClaw', 'Verzoek aan OpenProject via een OpenClaw skill')

# ── S6 ────────────────────────────────────────────────────────────────────────
LK_M_EN = '<a href="https://mistral.ai/news/mistral-ocr-3" target="_blank">Mistral AI\'s document processing</a>'
LK_M_FR = '<a href="https://mistral.ai/news/mistral-ocr-3" target="_blank">traitement de documents de Mistral AI</a>'
LK_M_NL = '<a href="https://mistral.ai/news/mistral-ocr-3" target="_blank">documentverwerkingsmogelijkheden van Mistral AI</a>'
t('s6-title-1', 'A Real Example:', 'Un exemple réel :', 'Een echt voorbeeld:')
t('s6-title-2', '15 Minutes', '15 Minutes', '15 Minuten')
t('s6-body', f'This week, I needed to set up a new project: <span class="hl">Mistral OCR Mastering</span> — a 10-day sprint to explore {LK_M_EN} capabilities and build a proof-of-concept.',
  f'Cette semaine, je devais mettre en place un nouveau projet : <span class="hl">Mistral OCR Mastering</span> — un sprint de 10 jours pour explorer les capacités de {LK_M_FR} et construire un proof-of-concept.',
  f'Deze week moest ik een nieuw project opzetten: <span class="hl">Mistral OCR Mastering</span> — een 10-daagse sprint om de {LK_M_NL} te verkennen en een proof-of-concept te bouwen.')
for i, (en, fr, nl) in enumerate([
    ('Create the project', 'Créer le projet', 'Het project aanmaken'),
    ('Add members with roles', 'Ajouter des membres avec des rôles', 'Leden toevoegen met rollen'),
    ('Write overview from Word doc', "Écrire la vue d'ensemble à partir d'un fichier Word", 'Overzicht schrijven vanuit Word-document'),
    ('Create work packages from whiteboard', 'Créer des work packages depuis le tableau blanc', 'Work packages aanmaken vanuit whiteboard'),
], start=1):
    t(f's6-phase-{i}-title', en, fr, nl)
t('s6-phase-1-desc', '"create a project mistral-ocr-mastering" → OpenClaw created the project on OpenProject in seconds.',
  '"create a project mistral-ocr-mastering" → OpenClaw a créé le projet sur OpenProject en quelques secondes.',
  '"create a project mistral-ocr-mastering" → OpenClaw maakte het project aan op OpenProject in seconden.')
t('s6-phase-2-desc', '"add Clémentine, Mohamed, Jeanne, Jean, Pauline as members. add Béatrice, Pierre and Oumaima as managers" → Five memberships + three with Project Admin roles. No clicking through settings pages.',
  '"add Clémentine, Mohamed, Jeanne, Jean, Pauline as members. add Béatrice, Pierre and Oumaima as managers" → Cinq memberships + trois avec des rôles Project Admin. Aucun clic dans les pages de paramètres.',
  '"add Clémentine, Mohamed, Jeanne, Jean, Pauline as members. add Béatrice, Pierre and Oumaima as managers" → Vijf lidmaatschappen + drie met Project Admin rollen. Geen geklik door instellingenpagina\'s.')
t('s6-phase-3-desc', 'Dropped a .docx file into the chat with meeting notes and said "write an overview of the project" → OpenClaw extracted the content, synthesized it into a structured project description, and pushed it directly to OpenProject. In markdown. With links.',
  'J\'ai déposé un fichier .docx dans le chat avec les notes de réunion et j\'ai dit "write an overview of the project" → OpenClaw a extrait le contenu, l\'a synthétisé en une description de projet structurée et l\'a poussé directement vers OpenProject. En markdown. Avec des liens.',
  'Ik dropte een .docx-bestand in de chat met vergadernotities en zei "write an overview of the project" → OpenClaw extraheerde de inhoud, synthetiseerde het tot een gestructureerde projectbeschrijving en pushte het direct naar OpenProject. In markdown. Met links.')
t('s6-phase-4-desc', 'Shared a photo of our architecture whiteboard and said "create work packages categories" → OpenClaw analyzed the image, identified workflow areas, and created 7 fully described work packages — each with acceptance criteria, technical details, and the right type.',
  'J\'ai partagé une photo de notre tableau blanc d\'architecture et dit "create work packages categories" → OpenClaw a analysé l\'image, identifié les zones de workflow, et créé 7 work packages entièrement décrits — chacun avec des critères d\'acceptation, des détails techniques et le bon type.',
  'Ik deelde een foto van ons architectuur-whiteboard en zei "create work packages categories" → OpenClaw analyseerde de afbeelding, identificeerde werkgebieden en maakte 7 volledig beschreven work packages aan — elk met acceptatiecriteria, technische details en het juiste type.')

# ── S7 ────────────────────────────────────────────────────────────────────────
t('s7-title-1', '15 Minutes', '15 Minutes', '15 Minuten')
t('s7-title-2', 'continued', 'suite', 'vervolg')
for i, (en, fr, nl) in enumerate([
    ('Create versions and compress timeline', 'Créer des versions et comprimer le planning', 'Versies aanmaken en tijdlijn comprimeren'),
    ('Assign everything at once', 'Tout assigner en une fois', 'Alles in één keer toewijzen'),
    ('Add deployment tasks', 'Ajouter les tâches de déploiement', 'Deployment-taken toevoegen'),
    ('Publish a news announcement', 'Publier une annonce', 'Nieuwsaankondiging publiceren'),
], start=5):
    t(f's7-phase-{i}-title', en, fr, nl)
t('s7-phase-5-desc', '"create versions" → 5 versions created. "the project should be finished in 10 network days" → All recompressed into 2-day sprints: March 30 → April 10.',
  '"create versions" → 5 versions créées. "the project should be finished in 10 network days" → Tout recompressé en sprints de 2 jours : 30 mars → 10 avril.',
  '"create versions" → 5 versies aangemaakt. "the project should be finished in 10 network days" → Alles gecomprimeerd tot 2-daagse sprints: 30 maart → 10 april.')
t('s7-phase-6-desc', '"assign tasks to Jeanne, assign accountable Oumaima, set the category itself, set the version itself" → All 7 work packages updated in one command.',
  '"assign tasks to Jeanne, assign accountable Oumaima, set the category itself, set the version itself" → Les 7 work packages mis à jour en une seule commande.',
  '"assign tasks to Jeanne, assign accountable Oumaima, set the category itself, set the version itself" → Alle 7 work packages bijgewerkt in één commando.')
t('s7-phase-7-desc', '"add missing tasks to deploy the application on our staging environment" → 7 deployment work packages created with sequential dependencies, detailed steps, and acceptance criteria.',
  '"add missing tasks to deploy the application on our staging environment" → 7 work packages de déploiement créés avec des dépendances séquentielles, des étapes détaillées et des critères d\'acceptation.',
  '"add missing tasks to deploy the application on our staging environment" → 7 deployment work packages aangemaakt met sequentiële afhankelijkheden, gedetailleerde stappen en acceptatiecriteria.')
t('s7-phase-8-desc', '"add a news" → A full project kickoff announcement published to the OpenProject news feed — team, objectives, timeline, links — all generated from context.',
  '"add a news" → Une annonce complète de lancement de projet publiée dans le fil d\'actualités OpenProject — équipe, objectifs, planning, liens — tout généré à partir du contexte.',
  '"add a news" → Een volledige project-kickoffaankondiging gepubliceerd in de OpenProject nieuwsfeed — team, doelen, tijdlijn, links — alles gegenereerd vanuit context.')
t('s7-body', f'<span class="hl">Total time: about 45 minutes of conversation.</span> What would this normally take? Conservatively, 4–5 hours of clicking, typing, correcting, browsing and context-switching between browser tabs, Excel, Word, {LK_DRAW}, Shared drives, Emails...',
  f'<span class="hl">Temps total : environ 45 minutes de conversation.</span> Combien de temps cela prendrait-il normalement ? Au bas mot, 4 à 5 heures de clics, de saisie, de corrections, de navigation et de changements de contexte entre onglets, Excel, Word, {LK_DRAW}, drives partagés, Emails...',
  f'<span class="hl">Totale tijd: ongeveer 45 minuten conversatie.</span> Hoeveel tijd zou dit normaal kosten? Conservatief geschat, 4–5 uur klikken, typen, corrigeren, browsen en context-switchen tussen browsertabs, Excel, Word, {LK_DRAW}, gedeelde drives, Emails...')
t('s7-metric-1-label', 'OpenClaw', 'OpenClaw', 'OpenClaw')
t('s7-metric-2-label', 'Manual', 'Manuel', 'Handmatig')
t('s7-metric-3-label', 'Work packages created', 'Work packages créés', 'Work packages aangemaakt')

# ── S8 ────────────────────────────────────────────────────────────────────────
t('s8-title-1', 'Why This', "Pourquoi c'est", 'Waarom dit')
t('s8-title-2', 'Matters', 'important', 'belangrijk is')
t('s8-phase-1-title', 'Projects start properly', 'Les projets démarrent correctement', 'Projecten starten goed')
t('s8-phase-1-desc', 'The #1 killer of project management quality is incomplete setup. When creating a work package takes 2 minutes of clicking, people create vague one-liners with no description, no assignee, no version, no dependencies. When creating a work package takes 0 effort — because you describe it in natural language and the agent handles the rest — <strong>every work package gets a proper description, acceptance criteria, and metadata from day one.</strong>',
  "Le tueur #1 de la qualité en gestion de projet est une mise en place incomplète. Quand créer un work package prend 2 minutes de clics, les gens créent des one-liners vagues sans description, sans assigné, sans version, sans dépendances. Quand créer un work package ne demande aucun effort — parce qu'on le décrit en langage naturel et l'agent fait le reste — <strong>chaque work package obtient une description correcte, des critères d'acceptation et des métadonnées dès le premier jour.</strong>",
  'De #1 killer van projectmanagementkwaliteit is onvolledige opzet. Wanneer het aanmaken van een work package 2 minuten klikken kost, maken mensen vage one-liners zonder beschrijving, geen toegewezene, geen versie, geen afhankelijkheden. Wanneer het aanmaken van een work package 0 inspanning kost — omdat je het beschrijft in natuurlijke taal en de agent de rest doet — <strong>krijgt elk work package een goede beschrijving, acceptatiecriteria en metadata vanaf dag één.</strong>')
t('s8-phase-2-title', 'Consistency at scale', 'Cohérence à grande échelle', 'Consistentie op schaal')
t('s8-phase-2-desc', 'I manage multiple projects across OpenProject, Jira, HubSpot, and GitHub. The OpenClaw skill approach means I interact with all of them the same way: through conversation. The agent handles the API differences. Need to mirror a user\'s memberships across 14 projects? "make Béatrice member of the same projects as Jeanne" — Done. Seven new memberships created, all with matching roles. In one sentence.',
  "Je gère plusieurs projets sur OpenProject, Jira, HubSpot et GitHub. L'approche par skills OpenClaw signifie que j'interagis avec tous de la même manière : par la conversation. L'agent gère les différences d'API. Besoin de dupliquer les adhésions d'un utilisateur sur 14 projets ? \"make Béatrice member of the same projects as Jeanne\" — Fait. Sept nouvelles adhésions créées, toutes avec les mêmes rôles. En une phrase.",
  'Ik beheer meerdere projecten over OpenProject, Jira, HubSpot en GitHub. De OpenClaw skill-aanpak betekent dat ik met allemaal op dezelfde manier communiceer: via conversatie. De agent handelt de API-verschillen af. Wil je de lidmaatschappen van een gebruiker spiegelen over 14 projecten? "make Béatrice member of the same projects as Jeanne" — Klaar. Zeven nieuwe lidmaatschappen aangemaakt, allemaal met overeenkomende rollen. In één zin.')
t('s8-phase-3-title', 'Documentation happens automatically', 'La documentation se fait automatiquement', 'Documentatie gebeurt automatisch')
t('s8-phase-3-desc', "Every work package I create through OpenClaw and my Skills gets: A structured description, Steps and acceptance criteria, Links to relevant resources (SharePoint, GitLab, docs), Proper categorization and versioning. Not because I'm disciplined. Because the agent does it by default. I master the theory and learned from the best. Now the machine enforces what I always meant to do.",
  "Chaque work package que je crée via OpenClaw et mes Skills reçoit : une description structurée, des étapes et critères d'acceptation, des liens vers les ressources pertinentes (SharePoint, GitLab, docs), une catégorisation et un versioning appropriés. Pas parce que je suis discipliné. Parce que l'agent le fait par défaut. Je maîtrise la théorie et j'ai appris des meilleurs. Maintenant la machine applique ce que j'ai toujours voulu faire.",
  'Elk work package dat ik aanmaak via OpenClaw en mijn Skills krijgt: een gestructureerde beschrijving, stappen en acceptatiecriteria, links naar relevante bronnen (SharePoint, GitLab, docs), juiste categorisering en versiebeheer. Niet omdat ik gedisciplineerd ben. Omdat de agent het standaard doet. Ik beheers de theorie en heb geleerd van de besten. Nu dwingt de machine af wat ik altijd wilde doen.')
t('s8-phase-4-title', 'Discord becomes the control plane', 'Discord devient le plan de contrôle', 'Discord wordt het controlepaneel')
t('s8-phase-4-desc', "My #bot-openproject Discord channel is now an operations console. I can: Create and manage projects, Query work package status, Generate reports and export them as files, Add members, set roles, configure versions — All without opening a browser. This matters for speed, but it matters even more for <strong>continuity</strong>. Every command and its result is visible in the chat history. It's a natural audit trail.",
  "Mon canal Discord #bot-openproject est maintenant une console d'opérations. Je peux : Créer et gérer des projets, Interroger le statut des work packages, Générer des rapports et les exporter en fichiers, Ajouter des membres, définir des rôles, configurer des versions — Le tout sans ouvrir un navigateur. C'est important pour la vitesse, mais encore plus pour la <strong>continuité</strong>. Chaque commande et son résultat est visible dans l'historique du chat. C'est une piste d'audit naturelle.",
  'Mijn #bot-openproject Discord-kanaal is nu een operatieconsole. Ik kan: Projecten aanmaken en beheren, Work package status opvragen, Rapporten genereren en exporteren als bestanden, Leden toevoegen, rollen instellen, versies configureren — Alles zonder een browser te openen. Dit is belangrijk voor snelheid, maar nog belangrijker voor <strong>continuïteit</strong>. Elk commando en het resultaat is zichtbaar in de chatgeschiedenis. Het is een natuurlijke audit trail.')

# ── S9 ────────────────────────────────────────────────────────────────────────
t('s9-title-1', 'The Jira Skill:', 'Le Skill Jira :', 'De Jira Skill:')
t('s9-title-2', 'Same Philosophy, Different Beast', 'Même philosophie, animal différent', 'Zelfde filosofie, ander beest')
t('s9-body', f'OpenProject is one side of my project management stack. But I also use <strong>Atlassian Jira</strong>. So I built a second skill: {LK_JIRASK}. Same architecture. Same design principles. Different API.',
  f'OpenProject est un côté de ma stack de gestion de projet. Mais j\'utilise aussi <strong>Atlassian Jira</strong>. Donc j\'ai construit un second skill : {LK_JIRASK}. Même architecture. Mêmes principes de conception. API différente.',
  f'OpenProject is één kant van mijn projectmanagement-stack. Maar ik gebruik ook <strong>Atlassian Jira</strong>. Dus bouwde ik een tweede skill: {LK_JIRASK}. Zelfde architectuur. Zelfde designprincipes. Andere API.')
t('s9-terminal-comment', '# No browser. No board. No drag-and-drop.', '# Pas de navigateur. Pas de board. Pas de glisser-déposer.', '# Geen browser. Geen board. Geen drag-and-drop.')
t('s9-body-2', '<span class="hl">What It Covers</span><br>The Jira skill gives OpenClaw full CRUD access to Jira Cloud via the REST API v3:<br>• Issues — create, read, update, delete, list, and search with JQL<br>• Comments — add, update, delete, list on any issue<br>• Attachments — upload, list, delete<br>• Workflow transitions — list available transitions and move issues through states<br><br>That last one matters more than it sounds. Workflow transitions in Jira are where tickets go to die — stuck in "In Review" because nobody clicked the button.',
  "<span class=\"hl\">Ce qu'il couvre</span><br>Le skill Jira donne à OpenClaw un accès CRUD complet à Jira Cloud via l'API REST v3 :<br>• Issues — créer, lire, modifier, supprimer, lister et rechercher avec JQL<br>• Commentaires — ajouter, modifier, supprimer, lister sur n'importe quelle issue<br>• Pièces jointes — uploader, lister, supprimer<br>• Transitions de workflow — lister les transitions disponibles et déplacer les issues<br><br>Ce dernier point est plus important qu'il n'y paraît. Les transitions de workflow dans Jira sont l'endroit où les tickets vont mourir — bloqués en \"In Review\" parce que personne n'a cliqué le bouton.",
  '<span class="hl">Wat het omvat</span><br>De Jira skill geeft OpenClaw volledige CRUD-toegang tot Jira Cloud via de REST API v3:<br>• Issues — aanmaken, lezen, bijwerken, verwijderen, lijsten en zoeken met JQL<br>• Opmerkingen — toevoegen, bijwerken, verwijderen, lijsten op elke issue<br>• Bijlagen — uploaden, lijsten, verwijderen<br>• Workflow-transities — beschikbare transities tonen en issues door statussen verplaatsen<br><br>Dat laatste is belangrijker dan het klinkt. Workflow-transities in Jira zijn waar tickets sterven — vast in "In Review" omdat niemand op de knop klikte.')
t('s9-body-3', '<span class="hl">The Same Patterns Work</span><br>Everything I described for OpenProject applies to Jira:<br>• Creating issues with full descriptions, priorities, and assignees — from a sentence<br>• Bulk operations across projects<br>• Attaching files from the chat<br>• Moving issues through workflows without opening a browser<br>• Commenting on issues as part of a conversation<br>• Add those work items into a new sprint and start the sprint !<br><br>The mental model is identical: <strong>describe what you want, the agent handles the API.</strong>',
  "<span class=\"hl\">Les mêmes modèles fonctionnent</span><br>Tout ce que j'ai décrit pour OpenProject s'applique à Jira :<br>• Créer des issues avec descriptions complètes, priorités et assignés — en une phrase<br>• Opérations en masse sur les projets<br>• Joindre des fichiers depuis le chat<br>• Déplacer les issues dans les workflows sans ouvrir un navigateur<br>• Commenter les issues dans une conversation<br>• Ajouter ces éléments dans un nouveau sprint et démarrer le sprint !<br><br>Le modèle mental est identique : <strong>décrivez ce que vous voulez, l'agent gère l'API.</strong>",
  '<span class="hl">Dezelfde patronen werken</span><br>Alles wat ik beschreef voor OpenProject geldt voor Jira:<br>• Issues aanmaken met volledige beschrijvingen, prioriteiten en toegewezenen — vanuit een zin<br>• Bulkoperaties over projecten<br>• Bestanden bijvoegen vanuit de chat<br>• Issues door workflows verplaatsen zonder browser<br>• Commentaar geven op issues als onderdeel van een gesprek<br>• Die werkitems in een nieuwe sprint plaatsen en de sprint starten!<br><br>Het mentale model is identiek: <strong>beschrijf wat je wilt, de agent handelt de API af.</strong>')
t('s9-body-4', '<span class="hl">Security: Same Standards</span><br>Both skills share the same security posture:<br>• Auth — email + API token (Basic auth, base64 encoded)<br>• No secrets to stdout — tokens never appear in logs or output<br>• Destructive operations require --confirm — no accidental deletes<br>• Rate limiting with exponential backoff — respects Atlassian\'s API limits<br>• Lazy config validation — credentials are only checked when you actually run a command<br>• Path traversal prevention — file uploads are sandboxed',
  '<span class="hl">Sécurité : Mêmes standards</span><br>Les deux skills partagent la même posture de sécurité :<br>• Auth — email + token API (Basic auth, encodé base64)<br>• Pas de secrets sur stdout — les tokens n\'apparaissent jamais dans les logs<br>• Les opérations destructives nécessitent --confirm — pas de suppressions accidentelles<br>• Rate limiting avec backoff exponentiel — respecte les limites API d\'Atlassian<br>• Validation de config « paresseuse » — les credentials sont vérifiés uniquement à l\'exécution<br>• Prévention du path traversal — les uploads de fichiers sont sandboxés',
  '<span class="hl">Beveiliging: Zelfde standaarden</span><br>Beide skills delen dezelfde beveiligingshouding:<br>• Auth — email + API-token (Basic auth, base64 gecodeerd)<br>• Geen secrets naar stdout — tokens verschijnen nooit in logs of uitvoer<br>• Destructieve operaties vereisen --confirm — geen onbedoelde verwijderingen<br>• Rate limiting met exponentiële backoff — respecteert Atlassian\'s API-limieten<br>• Lazy config validatie — credentials worden alleen gecontroleerd bij daadwerkelijk gebruik<br>• Path traversal preventie — bestandsuploads zijn gesandboxed')
t('s9-body-5', '<span class="hl">Why Two Skills Instead of One?</span> OpenProject and Jira are fundamentally different systems. Different APIs, different data models, different workflow engines. The agent layer (OpenClaw) provides the unified interface.<br><br>#bot-openproject → OpenProject skill<br>#bot-jira → Jira skill<br><br>I create Discord threads to keep the context of the projects separated:<br>#bot-openproject → mistral-ocr-mastering<br>#bot-jira → atlassian-jira-ui<br><br>Same human. Same language. Different backends.',
  '<span class="hl">Pourquoi deux Skills au lieu d\'un ?</span> OpenProject et Jira sont des systèmes fondamentalement différents. APIs différentes, modèles de données différents, moteurs de workflow différents. La couche agent (OpenClaw) fournit l\'interface unifiée.<br><br>#bot-openproject → Skill OpenProject<br>#bot-jira → Skill Jira<br><br>Je crée des threads Discord pour séparer le contexte des projets :<br>#bot-openproject → mistral-ocr-mastering<br>#bot-jira → atlassian-jira-ui<br><br>Même personne. Même langage. Backends différents.',
  '<span class="hl">Waarom twee Skills in plaats van één?</span> OpenProject en Jira zijn fundamenteel verschillende systemen. Verschillende API\'s, verschillende datamodellen, verschillende workflow-engines. De agentlaag (OpenClaw) biedt de uniforme interface.<br><br>#bot-openproject → OpenProject skill<br>#bot-jira → Jira skill<br><br>Ik maak Discord-threads aan om de context van projecten gescheiden te houden:<br>#bot-openproject → mistral-ocr-mastering<br>#bot-jira → atlassian-jira-ui<br><br>Zelfde mens. Zelfde taal. Andere backends.')

# ── S10 ───────────────────────────────────────────────────────────────────────
t('s10-title-1', 'The Skill', "L'écosystème", 'Het Skill')
t('s10-title-2', 'Ecosystem', 'de Skills', 'Ecosysteem')
t('s10-body', f'The OpenProject skill is one of many. OpenClaw\'s {LK_CH} hosts skills for:',
  f'Le skill OpenProject est un parmi d\'autres. Le {LK_CH} d\'OpenClaw héberge des skills pour :',
  f'De OpenProject skill is één van velen. OpenClaw\'s {LK_CH} host skills voor:')
t('s10-step-1-desc', 'Full CRUD, workflow transitions, JQL search', 'CRUD complet, transitions de workflow, recherche JQL', 'Volledige CRUD, workflow-transities, JQL-zoekopdrachten')
t('s10-step-2-desc', 'CRM, CMS, marketing, automation', 'CRM, CMS, marketing, automatisation', 'CRM, CMS, marketing, automatisering')
t('s10-step-3-desc', 'Issues, PRs, CI/CD, code review', 'Issues, PRs, CI/CD, revue de code', 'Issues, PRs, CI/CD, code review')
t('s10-step-4-desc', 'Documents, Todos', 'Documents, Todos', 'Documenten, Todos')
t('s10-step-5-desc', 'Gmail, Calendar, Drive, Sheets', 'Gmail, Agenda, Drive, Sheets', 'Gmail, Agenda, Drive, Sheets')
t('s10-step-6-desc', 'Pages, databases, blocks', 'Pages, bases de données, blocks', "Pagina's, databases, blokken")
t('s10-body-2', 'Each skill follows the same pattern: a Command Line Interpreter (CLI) tool that the agent knows how to use, backed by API calls with proper auth, rate limiting, and error handling.<br><br>You can also <span class="hl">build your own skills</span>. The OpenProject skill I use started as a Proof of Concept (PoC) — a Node.js CLI with Commander, dotenv, and the OpenProject API v3. OpenClaw\'s skill spec makes it straightforward to package and share.',
  'Chaque skill suit le même modèle : un outil CLI (Command Line Interpreter) que l\'agent sait utiliser, soutenu par des appels API avec authentification, limitation de débit et gestion d\'erreurs.<br><br>Vous pouvez aussi <span class="hl">construire vos propres skills</span>. Le skill OpenProject que j\'utilise a commencé comme un Proof of Concept (PoC) — un CLI Node.js avec Commander, dotenv et l\'API v3 d\'OpenProject. La spécification de skills d\'OpenClaw rend le packaging et le partage simples.',
  'Elke skill volgt hetzelfde patroon: een Command Line Interpreter (CLI) tool die de agent kan gebruiken, ondersteund door API-aanroepen met juiste authenticatie, rate limiting en foutafhandeling.<br><br>Je kunt ook <span class="hl">je eigen skills bouwen</span>. De OpenProject skill die ik gebruik begon als een Proof of Concept (PoC) — een Node.js CLI met Commander, dotenv en de OpenProject API v3. OpenClaw\'s skill-specificatie maakt het eenvoudig om te packagen en te delen.')

# ── S11 ───────────────────────────────────────────────────────────────────────
t('s11-title-1', 'What I', "Ce que j'ai", 'Wat ik heb')
t('s11-title-2', 'Learned', 'appris', 'geleerd')
t('s11-phase-1-title', 'AI never ever replace project managers. It removes the friction.', "L'IA ne remplace jamais les chefs de projet. Elle supprime la friction.", 'AI vervangt nooit projectmanagers. Het verwijdert de wrijving.')
t('s11-phase-1-desc', "The decisions are still mine: what to build, who to assign, how to prioritize. But the execution of those decisions — the clicking, the typing, the formatting, the linking — that's gone.",
  "Les décisions sont toujours les miennes : quoi construire, à qui assigner, comment prioriser. Mais l'exécution de ces décisions — les clics, la saisie, la mise en forme, les liens — c'est fini.",
  'De beslissingen zijn nog steeds van mij: wat bouwen, aan wie toewijzen, hoe prioriteren. Maar de uitvoering van die beslissingen — het klikken, het typen, het formatteren, het linken — dat is weg.')
t('s11-phase-2-title', 'Natural language is the best API client.', 'Le langage naturel est le meilleur client API.', 'Natuurlijke taal is de beste API-client.')
t('s11-phase-2-desc', "I don't need to remember Command lines flags or API endpoints like we did or do when we use the command prompts. I say what I want, and the agent figures out the how. Even the LLMs make mistakes !!! When something fails (wrong project, missing member), it tells me why and I fix it.",
  "Je n'ai pas besoin de me souvenir des flags de ligne de commande ou des endpoints API comme on le faisait ou le fait quand on utilise l'invite de commandes. Je dis ce que je veux, et l'agent trouve le comment. Même les LLMs font des erreurs !!! Quand quelque chose échoue (mauvais projet, membre manquant), il me dit pourquoi et je corrige.",
  "Ik hoef geen Command line flags of API-eindpunten te onthouden zoals we deden of doen wanneer we de opdrachtprompt gebruiken. Ik zeg wat ik wil, en de agent zoekt uit hoe. Zelfs de LLM's maken fouten !!! Wanneer iets mislukt (verkeerd project, ontbrekend lid), vertelt het me waarom en ik los het op.")
t('s11-phase-3-title', 'Quality scales when effort drops to zero.', "La qualité monte en flèche quand l'effort tombe à zéro.", 'Kwaliteit schaalt wanneer inspanning naar nul daalt.')
t('s11-phase-3-desc', "When adding a description costs nothing, every task gets one. When setting dependencies is free, every chain gets linked. The quality of project setup went up dramatically — not because I got better at it, but because the cost of doing it right became negligible.",
  "Quand ajouter une description ne coûte rien, chaque tâche en obtient une. Quand définir des dépendances est gratuit, chaque chaîne est liée. La qualité de la mise en place des projets a augmenté dramatiquement — pas parce que je suis devenu meilleur, mais parce que le coût de bien faire est devenu négligeable.",
  'Wanneer het toevoegen van een beschrijving niets kost, krijgt elke taak er een. Wanneer het instellen van afhankelijkheden gratis is, wordt elke keten gekoppeld. De kwaliteit van projectopzet ging dramatisch omhoog — niet omdat ik er beter in werd, maar omdat de kosten om het goed te doen verwaarloosbaar werden.')

# ── S12 ───────────────────────────────────────────────────────────────────────
t('s12-title-1', 'We Help Companies', 'Nous aidons les entreprises à', 'Wij helpen bedrijven')
t('s12-title-2', 'Build AI Pipelines', 'construire des pipelines IA', 'AI Pipelines bouwen')
t('s12-body', 'We help companies set up AI pipelines that create life-changing experiences — from whiteboard vision to structured project delivery, fully integrated into your existing tools.',
  'Nous aidons les entreprises à mettre en place des pipelines IA qui créent des expériences transformatrices — de la vision du tableau blanc à la livraison de projet structurée, entièrement intégrés à vos outils existants.',
  'Wij helpen bedrijven AI-pipelines op te zetten die levensveranderende ervaringen creëren — van whiteboard-visie tot gestructureerde projectoplevering, volledig geïntegreerd in uw bestaande tools.')
t('s12-col-1-title', '🔒 Private', '🔒 Privé', '🔒 Privaat')
t('s12-col-1-item', 'No internet, no cloud, no external APIs. Your data stays on your infrastructure. Period.',
  "Pas d'internet, pas de cloud, pas d'APIs externes. Vos données restent sur votre infrastructure. Point.",
  "Geen internet, geen cloud, geen externe API's. Uw data blijft op uw infrastructuur. Punt.")
t('s12-col-2-title', '🌐 Public', '🌐 Public', '🌐 Publiek')
t('s12-col-2-item', 'Leveraging cloud services: Remote drives, Mistral, Claude, Gemini, DeepSeek, Llama, and public APIs.',
  'En exploitant les services cloud : drives distants, Mistral, Claude, Gemini, DeepSeek, Llama et les APIs publiques.',
  "Gebruikmakend van clouddiensten: externe drives, Mistral, Claude, Gemini, DeepSeek, Llama en publieke API's.")
t('s12-body-2', '<span class="hl">Choose your posture. We build both.</span>',
  '<span class="hl">Choisissez votre posture. Nous construisons les deux.</span>',
  '<span class="hl">Kies uw houding. Wij bouwen beide.</span>')

# ── S13 ───────────────────────────────────────────────────────────────────────
t('s13-title-1', 'Get', 'Pour', 'Aan de')
t('s13-title-2', 'started', 'commencer', 'slag')
t('s13-cta-1', '→ <strong>OpenClaw</strong>: <a href="https://openclaw.ai" target="_blank">openclaw.ai</a> — open-source, self-hosted',
  '→ <strong>OpenClaw</strong> : <a href="https://openclaw.ai" target="_blank">openclaw.ai</a> — open source, auto-hébergé',
  '→ <strong>OpenClaw</strong>: <a href="https://openclaw.ai" target="_blank">openclaw.ai</a> — open source, zelf gehost')
t('s13-cta-2', '→ <strong>Skills</strong>: <a href="https://clawhub.ai" target="_blank">clawhub.ai</a> — browse and install',
  '→ <strong>Skills</strong> : <a href="https://clawhub.ai" target="_blank">clawhub.ai</a> — parcourir et installer',
  '→ <strong>Skills</strong>: <a href="https://clawhub.ai" target="_blank">clawhub.ai</a> — bladeren en installeren')
t('s13-cta-3', '→ <strong>Community</strong>: <a href="https://discord.com/invite/clawd" target="_blank">Discord</a> — OpenClaw Discord server',
  '→ <strong>Communauté</strong> : <a href="https://discord.com/invite/clawd" target="_blank">Discord</a> — serveur Discord OpenClaw',
  '→ <strong>Community</strong>: <a href="https://discord.com/invite/clawd" target="_blank">Discord</a> — OpenClaw Discord-server')
t('s13-cta-4', '→ <strong>Source</strong>: <a href="https://github.com/openclaw/openclaw" target="_blank">GitHub</a> — OpenClaw source code',
  '→ <strong>Source</strong> : <a href="https://github.com/openclaw/openclaw" target="_blank">GitHub</a> — code source OpenClaw',
  '→ <strong>Source</strong>: <a href="https://github.com/openclaw/openclaw" target="_blank">GitHub</a> — OpenClaw broncode')
t('s13-skills-heading', 'ALT-F1 Skills available on GitHub', 'Skills ALT-F1 disponibles sur GitHub', 'ALT-F1 Skills beschikbaar op GitHub')
t('s13-skill-1', f'<strong>SharePoint</strong> — file ops &amp; Office document intelligence <a href="{GH}/openclaw-skill-sharepoint" target="_blank">↗ repo</a>',
  f'<strong>SharePoint</strong> — opérations fichiers &amp; intelligence documentaire Office <a href="{GH}/openclaw-skill-sharepoint" target="_blank">↗ repo</a>',
  f'<strong>SharePoint</strong> — bestandsbewerkingen &amp; Office documentintelligentie <a href="{GH}/openclaw-skill-sharepoint" target="_blank">↗ repo</a>')
t('s13-skill-2', f'<strong>X/Twitter</strong> — tweets, threads, media via X API v2 <a href="{GH}/openclaw-skill-x-twitter" target="_blank">↗ repo</a>',
  f'<strong>X/Twitter</strong> — tweets, threads, médias via X API v2 <a href="{GH}/openclaw-skill-x-twitter" target="_blank">↗ repo</a>',
  f'<strong>X/Twitter</strong> — tweets, threads, media via X API v2 <a href="{GH}/openclaw-skill-x-twitter" target="_blank">↗ repo</a>')
t('s13-skill-3', f'<strong>M365 Task Manager</strong> — To Do &amp; Planner <a href="{GH}/openclaw-skill-m365-task-manager" target="_blank">↗ repo</a>',
  f'<strong>M365 Task Manager</strong> — To Do &amp; Planner <a href="{GH}/openclaw-skill-m365-task-manager" target="_blank">↗ repo</a>',
  f'<strong>M365 Task Manager</strong> — To Do &amp; Planner <a href="{GH}/openclaw-skill-m365-task-manager" target="_blank">↗ repo</a>')
t('s13-skill-4', f'<strong>Jira Cloud</strong> — issues, comments, attachments, workflows, JQL <a href="{GH}/openclaw-skill-atlassian-jira-by-altf1be" target="_blank">↗ repo</a>',
  f'<strong>Jira Cloud</strong> — issues, commentaires, pièces jointes, workflows, JQL <a href="{GH}/openclaw-skill-atlassian-jira-by-altf1be" target="_blank">↗ repo</a>',
  f'<strong>Jira Cloud</strong> — issues, opmerkingen, bijlagen, workflows, JQL <a href="{GH}/openclaw-skill-atlassian-jira-by-altf1be" target="_blank">↗ repo</a>')
t('s13-skill-5', f'<strong>OpenProject</strong> — work packages, projects, time entries, comments <a href="{GH}/openclaw-skill-openproject" target="_blank">↗ repo</a>',
  f'<strong>OpenProject</strong> — work packages, projets, saisie de temps, commentaires <a href="{GH}/openclaw-skill-openproject" target="_blank">↗ repo</a>',
  f'<strong>OpenProject</strong> — work packages, projecten, tijdregistratie, opmerkingen <a href="{GH}/openclaw-skill-openproject" target="_blank">↗ repo</a>')
t('s13-skill-6', f'<strong>HubSpot</strong> — CRM, CMS, Marketing, Conversations, Automation <a href="{GH}/openclaw-skill-hubspot-by-altf1be" target="_blank">↗ repo</a>',
  f'<strong>HubSpot</strong> — CRM, CMS, Marketing, Conversations, Automatisation <a href="{GH}/openclaw-skill-hubspot-by-altf1be" target="_blank">↗ repo</a>',
  f'<strong>HubSpot</strong> — CRM, CMS, Marketing, Gesprekken, Automatisering <a href="{GH}/openclaw-skill-hubspot-by-altf1be" target="_blank">↗ repo</a>')
t('s13-skill-7', f'<strong>Skill Template</strong> — template for creating new OpenClaw skills <a href="{GH}/openclaw-skill-template" target="_blank">↗ repo</a>',
  f'<strong>Skill Template</strong> — modèle pour créer de nouveaux skills OpenClaw <a href="{GH}/openclaw-skill-template" target="_blank">↗ repo</a>',
  f'<strong>Skill Template</strong> — sjabloon voor het aanmaken van nieuwe OpenClaw skills <a href="{GH}/openclaw-skill-template" target="_blank">↗ repo</a>')

_bio_base = '<em>{ab} is the founder of <a href="https://www.alt-f1.be" target="_blank">ALT-F1 SRL</a> and Partner at <a href="https://www.xflowdata.com" target="_blank">XFlowData</a>, based in Brussels &amp; Tunisia.</em><br><br>Abdelkrim <strong>supports your industry with SOFTWARE, DATA, ANALYTICS &amp; LEAN OPTIMISATIONS. He also yells at his AI agent in Discord.</strong><br><br><strong>Cloud, On-Premise, Digital Transformation, Digital Workplace, AI &amp; Apps</strong><br><br><strong>If you manage projects and you\'re tired of the gap between "knowing what to do" and "actually configuring it in the tool" — this is worth trying.</strong>'
t('s13-bio',
  _bio_base.format(ab=LK_AB),
  f'<em>{LK_AB} est le fondateur d\'<a href="https://www.alt-f1.be" target="_blank">ALT-F1 SRL</a> et Partenaire chez <a href="https://www.xflowdata.com" target="_blank">XFlowData</a>, basé à Bruxelles &amp; en Tunisie.</em><br><br>Abdelkrim <strong>accompagne votre industrie avec SOFTWARE, DATA, ANALYTICS &amp; LEAN OPTIMISATIONS. Il crie aussi sur son agent IA dans Discord.</strong><br><br><strong>Cloud, On-Premise, Transformation Digitale, Digital Workplace, IA &amp; Apps</strong><br><br><strong>Si vous gérez des projets et que vous en avez marre du fossé entre "savoir quoi faire" et "le configurer dans l\'outil" — ça vaut le coup d\'essayer.</strong>',
  f'<em>{LK_AB} is de oprichter van <a href="https://www.alt-f1.be" target="_blank">ALT-F1 SRL</a> en Partner bij <a href="https://www.xflowdata.com" target="_blank">XFlowData</a>, gevestigd in Brussel &amp; Tunesië.</em><br><br>Abdelkrim <strong>ondersteunt uw industrie met SOFTWARE, DATA, ANALYTICS &amp; LEAN OPTIMALISATIES. Hij schreeuwt ook tegen zijn AI-agent in Discord.</strong><br><br><strong>Cloud, On-Premise, Digitale Transformatie, Digitale Werkplek, AI &amp; Apps</strong><br><br><strong>Als u projecten beheert en moe bent van de kloof tussen "weten wat te doen" en "het daadwerkelijk configureren in de tool" — dit is het proberen waard.</strong>')

_cred_link = '<a href="https://github.com/mmaudet/last-line.dev" target="_blank" style="color:var(--green)">last-line.dev</a> by <a href="https://github.com/mmaudet" target="_blank" style="color:var(--green)">Michel-Marie Maudet</a>, <a href="https://linagora.com" target="_blank" style="color:var(--green)">Linagora</a>'
t('s13-credit', f'Inspired by {_cred_link}', f'Inspiré par {_cred_link}', f'Geïnspireerd door {_cred_link}')

# ── Menu titles ───────────────────────────────────────────────────────────────
T['menu-titles'] = {
  'en': ['Title','The Problem','An Old Idea','Several Attempts','Enter OpenClaw','The OpenProject Skill','Real Example: Part 1','Real Example: Part 2','Why This Matters','The Jira Skill','The Skill Ecosystem','What I Learned','AI Pipelines','Get Started'],
  'fr': ['Titre','Le Problème','Une vieille idée','Plusieurs tentatives','Voici OpenClaw','Le Skill OpenProject','Exemple réel : Partie 1','Exemple réel : Partie 2',"Pourquoi c'est important",'Le Skill Jira',"L'écosystème de Skills","Ce que j'ai appris",'Pipelines IA','Pour commencer'],
  'nl': ['Titel','Het Probleem','Een oud idee','Meerdere pogingen','Maak kennis met OpenClaw','De OpenProject Skill','Echt voorbeeld: Deel 1','Echt voorbeeld: Deel 2','Waarom dit belangrijk is','De Jira Skill','Het Skill Ecosysteem','Wat ik heb geleerd','AI Pipelines','Aan de slag']
}

# ─── Write JSON files ─────────────────────────────────────────────────────────
for lang in ['en', 'fr', 'nl']:
    data = {k: v[lang] for k, v in T.items()}
    with open(f'{BASE}/lang/{lang}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f'  ✓ lang/{lang}.json ({len(data)} keys)')

# ─── Copy template to language directories ────────────────────────────────────
template_path = f'{BASE}/template.html'
for lang in ['en', 'fr', 'nl']:
    shutil.copy2(template_path, f'{BASE}/{lang}/index.html')
    print(f'  ✓ {lang}/index.html')

# ─── Write root redirect ─────────────────────────────────────────────────────
root_html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Redirecting...</title>
<script>
(function(){
  var saved=localStorage.getItem('wtg-lang');
  var langs=['en','fr','nl'];
  if(saved && langs.indexOf(saved)!==-1){
    window.location.replace(saved+'/');
    return;
  }
  var nav=(navigator.language||navigator.userLanguage||'en').toLowerCase();
  if(nav.startsWith('fr'))window.location.replace('fr/');
  else if(nav.startsWith('nl'))window.location.replace('nl/');
  else window.location.replace('en/');
})();
</script>
<noscript><meta http-equiv="refresh" content="0;url=en/"></noscript>
</head>
<body></body>
</html>
'''
with open(f'{BASE}/index.html', 'w', encoding='utf-8') as f:
    f.write(root_html)
print('  ✓ index.html (root redirect)')

print('\\nDone! File structure:')
for lang in ['en', 'fr', 'nl']:
    print(f'  {lang}/index.html')
    print(f'  lang/{lang}.json')
print('  index.html (redirect)')
print('  template.html (source)')
