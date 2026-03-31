# 🦞 How I Use OpenClaw and AI Skills to Run My Projects

> **PRINCE2, PMBoK or PMI for dummies like me**
>
> *By [Abdelkrim Boujraf](https://be.linkedin.com/in/abdelkrimboujraf) — 30 March 2026*

---

## 🌐 Browse the Presentation

[![Preview](assets/preview.png)](https://alt-f1-openclaw.github.io/openclaw-for-project-managers/en/)

| Language | Link |
|----------|------|
| 🇬🇧 English | **[openclaw-for-project-managers/en/](https://alt-f1-openclaw.github.io/openclaw-for-project-managers/en/)** |
| 🇫🇷 Français | **[openclaw-for-project-managers/fr/](https://alt-f1-openclaw.github.io/openclaw-for-project-managers/fr/)** |
| 🇳🇱 Nederlands | **[openclaw-for-project-managers/nl/](https://alt-f1-openclaw.github.io/openclaw-for-project-managers/nl/)** |

Or clone the repo and open `en/index.html` locally.

---

## 💡 What is this?

A **14-slide interactive presentation** showing how [OpenClaw](https://openclaw.ai) and custom AI Skills turn project management from tedious clicking into natural language conversations.

| What | How |
|------|-----|
| 📸 Snap a whiteboard | → structured Gantt chart |
| 💬 Talk to your PM tool | → via Discord |
| 🔧 OpenProject, Jira, HubSpot | → all through conversation |
| ⚡ Set up a full project | → 45 min instead of 4-5 hours |

---

## 🎛️ Features

| Feature | Details |
|---------|---------|
| 🖥️ Design | Terminal aesthetic, JetBrains Mono, dark/light theme |
| 🌐 Languages | English, French, Dutch — dropdown selector |
| ⌨️ Navigation | Arrow keys, click, swipe, fullscreen (F) |
| 📋 Slide menu | ☰ button for quick jumping |
| 🏗️ i18n | JSON-based — `lang/en.json`, `lang/fr.json`, `lang/nl.json` |

---

## 🗂️ Architecture

```
index.html              → redirects to /en/
en/index.html           → English (loads lang/en.json)
fr/index.html           → French  (loads lang/fr.json)
nl/index.html           → Dutch   (loads lang/nl.json)
lang/
  ├── en.json           → 131 translation keys
  ├── fr.json           → 131 translation keys
  └── nl.json           → 131 translation keys
template.html           → shared HTML template
generate.py             → generates en/fr/nl from template + JSON
assets/
  ├── preview.png
  ├── discord-openproject-example.png
  ├── favicon.svg
  └── comic-prompts.md  → image generation prompts
```

---

## 🔗 Links

### OpenClaw

| Resource | URL |
|----------|-----|
| 🦞 OpenClaw | [openclaw.ai](https://openclaw.ai) — open-source, self-hosted |
| 🧩 ClawHub | [clawhub.ai](https://clawhub.ai) — browse & install skills |
| 💬 Community | [Discord](https://discord.com/invite/clawd) |
| 📦 Source | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) |

### ALT-F1 Skills on GitHub

| Skill | Description | Repo |
|-------|-------------|------|
| **OpenProject** | Work packages, projects, time entries, comments, attachments (API v3) | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-openproject) · [↗ ClawHub](https://clawhub.ai/abdelkrim/openproject-by-altf1be) |
| **Jira Cloud** | Issues, comments, attachments, workflows, JQL search (REST API v3) | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-atlassian-jira-by-altf1be) |
| **HubSpot** | CRM, CMS, Marketing, Conversations, Automation | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-hubspot-by-altf1be) |
| **SharePoint** | File ops & Office document intelligence (Graph API) | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-sharepoint) |
| **X/Twitter** | Tweets, threads, media (X API v2) | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-x-twitter) |
| **M365 Task Manager** | Microsoft 365 To Do & Planner | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-m365-task-manager) |
| **Skill Template** | Template for creating new OpenClaw skills | [↗ GitHub](https://github.com/ALT-F1-OpenClaw/openclaw-skill-template) |

### Tools & Services Referenced

| Tool | URL |
|------|-----|
| OpenProject | [openproject.org](https://www.openproject.org) |
| Atlassian Jira | [atlassian.com/software/jira](https://www.atlassian.com/software/jira) |
| Mistral AI OCR | [mistral.ai/news/mistral-ocr-3](https://mistral.ai/news/mistral-ocr-3) |
| NLTK | [nltk.org](https://www.nltk.org/) |
| Rasa | [rasa.com](https://rasa.com/) |
| LUIS | [luis.azure.us](https://luis.azure.us/) |
| Mattermost | [github.com/mattermost](https://github.com/mattermost/mattermost) |
| XFlowdata | [xflowdata.com](https://www.xflowdata.com) |
| OpenClaw User Group Belgium | [Meetup](https://www.meetup.com/openclaw-user-group-belgium/events) |

---

## 👤 Author

| | |
|---|---|
| **Name** | [Abdelkrim Boujraf](https://be.linkedin.com/in/abdelkrimboujraf) |
| **Company** | [ALT-F1 SRL](https://www.alt-f1.be) — Brussels |
| **Partner** | [XFlowData](https://xflowdata.com) |
| **Expertise** | Cloud, On-Premise, Digital Transformation, AI & Apps |

---

## 🎨 Inspired by

Design pattern from [last-line.dev](https://github.com/mmaudet/last-line.dev) by [Michel-Marie Maudet](https://github.com/mmaudet), [Linagora](https://linagora.com).

---

## 📄 License

[AGPL-3.0](LICENSE)
