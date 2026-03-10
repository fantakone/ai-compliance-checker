# 🛡️ AI Compliance Checker

> Automated regulatory compliance assessment powered by Claude — covers EU AI Act, NIS2, GDPR, ISO 27001 and SOC 2.

---

## Overview

A full-stack web application that guides organisations through compliance self-assessments and uses Claude (Anthropic) to generate personalised gap analyses with prioritised action plans.

**Frameworks covered:**

| Framework | Focus |
|---|---|
| 🤖 **EU AI Act** | AI system risk classification, transparency, human oversight |
| 🛡️ **NIS2** | Cybersecurity governance, incident management, supply chain |
| 🔒 **GDPR** | Data processing, data subject rights, breach notification |
| 📋 **ISO 27001** | Information security management system (ISMS) |
| ✅ **SOC 2** | Availability, confidentiality, processing integrity |

---

## Features

- 🌍 **Bilingual** — Full French / English support, switchable in the UI
- 🤖 **AI-powered analysis** — Claude analyses answers and generates contextual gap reports
- 📊 **Compliance score** — 0–100 score with maturity level classification
- 🎯 **Prioritised action plan** — Ranked recommendations with suggested timelines
- ⬇️ **JSON export** — Download raw results for further processing
- 🐳 **Docker ready** — One-command deployment

---

## Quick Start

### Local (without Docker)

```bash
# Clone
git clone https://github.com/fantakone/ai-compliance-checker
cd ai-compliance-checker

# Install dependencies
pip install -r requirements.txt

# Start the server
uvicorn backend.main:app --reload --port 8000

# Open in browser
open http://localhost:8000
```

### Docker

```bash
docker build -t ai-compliance-checker .
docker run -p 8000:8000 ai-compliance-checker
```

Then open [http://localhost:8000](http://localhost:8000)

---

## Usage

1. **Enter your Anthropic API key** — get one at [console.anthropic.com](https://console.anthropic.com)
2. **Select a framework** — EU AI Act, NIS2, GDPR, ISO 27001, or SOC 2
3. **Answer the questionnaire** — Yes / Partial / No / N/A for each question
4. **Get your report** — Claude analyses your answers and generates:
   - Compliance score (0–100)
   - Identified gaps with severity levels
   - Concrete recommendations per gap
   - Prioritised action plan with timelines
5. **Export** — Download results as JSON

---

## Project Structure

```
ai-compliance-checker/
├── backend/
│   ├── main.py          # FastAPI routes
│   ├── questions.py     # Question database (FR + EN, all frameworks)
│   └── analyzer.py      # Claude API integration + prompt engineering
├── frontend/
│   └── index.html       # Single-page app (vanilla JS)
├── requirements.txt
├── Dockerfile
└── README.md
```

---

## API Reference

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/frameworks` | List all frameworks |
| GET | `/api/questions/{framework_id}` | Get questions for a framework |
| POST | `/api/assess` | Run AI compliance assessment |
| GET | `/health` | Health check |

Interactive docs at `/docs` (Swagger UI).

---

## Author

**Fanta Koné** — Cloud & Security Engineer | DevOps | AI

- 🌐 [fantakone.com](https://fantakone.com)
- 💼 [Malt](https://www.malt.fr/profile/fantadeazevedo)
