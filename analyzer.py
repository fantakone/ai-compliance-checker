"""
analyzer.py — Calls Claude API to analyze compliance answers
and generate gap analysis with recommendations.
"""

import anthropic
import json
from questions import FRAMEWORKS, QUESTIONS


def build_prompt(framework_id: str, answers: dict, lang: str) -> str:
    """Build the analysis prompt from answers."""
    fw = FRAMEWORKS[framework_id]
    questions = QUESTIONS[framework_id]
    fw_name = fw["name_fr"] if lang == "fr" else fw["name_en"]

    lines = []
    for q in questions:
        qid = q["id"]
        text = q["text_fr"] if lang == "fr" else q["text_en"]
        cat  = q["category_fr"] if lang == "fr" else q["category_en"]
        ans  = answers.get(qid, "non_repondu")
        lines.append(f"[{cat}] {text} → Réponse: {ans}")

    answers_text = "\n".join(lines)

    if lang == "fr":
        return f"""Tu es un expert en conformité réglementaire spécialisé dans le référentiel {fw_name}.

Voici les réponses d'une organisation à un questionnaire d'auto-évaluation {fw_name} :

{answers_text}

Analyse ces réponses et fournis une évaluation structurée en JSON avec exactement ce format :

{{
  "score": <nombre entre 0 et 100>,
  "niveau": "<Conforme|Partiellement conforme|Non conforme>",
  "resume": "<2-3 phrases résumant la situation globale>",
  "points_forts": ["<point fort 1>", "<point fort 2>"],
  "gaps": [
    {{
      "titre": "<titre court du gap>",
      "severite": "<Critique|Élevée|Moyenne|Faible>",
      "description": "<description du problème>",
      "recommandation": "<action corrective concrète>",
      "delai": "<Court terme (< 3 mois)|Moyen terme (3-6 mois)|Long terme (> 6 mois)>"
    }}
  ],
  "plan_action": [
    {{
      "priorite": <1 à 5>,
      "action": "<action concrète>",
      "delai": "<délai recommandé>"
    }}
  ]
}}

Réponds UNIQUEMENT avec le JSON, sans texte avant ou après."""

    else:
        return f"""You are a compliance expert specialised in the {fw_name} framework.

Below are an organisation's answers to a {fw_name} self-assessment questionnaire:

{answers_text}

Analyse these answers and provide a structured assessment in JSON with exactly this format:

{{
  "score": <number between 0 and 100>,
  "niveau": "<Compliant|Partially compliant|Non-compliant>",
  "resume": "<2-3 sentences summarising the overall situation>",
  "points_forts": ["<strength 1>", "<strength 2>"],
  "gaps": [
    {{
      "titre": "<short gap title>",
      "severite": "<Critical|High|Medium|Low>",
      "description": "<description of the issue>",
      "recommandation": "<concrete corrective action>",
      "delai": "<Short term (< 3 months)|Medium term (3-6 months)|Long term (> 6 months)>"
    }}
  ],
  "plan_action": [
    {{
      "priorite": <1 to 5>,
      "action": "<concrete action>",
      "delai": "<recommended timeframe>"
    }}
  ]
}}

Reply ONLY with JSON, no text before or after."""


def analyze_compliance(
    framework_id: str,
    answers: dict,
    lang: str,
    api_key: str
) -> dict:
    """
    Call Claude to analyze compliance answers.
    Returns parsed JSON result.
    """
    client = anthropic.Anthropic(api_key=api_key)

    prompt = build_prompt(framework_id, answers, lang)

    message = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}]
    )

    raw = message.content[0].text.strip()

    # Strip markdown fences if present
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    result = json.loads(raw)
    result["framework_id"] = framework_id
    result["framework_name"] = FRAMEWORKS[framework_id]["name_fr" if lang == "fr" else "name_en"]
    result["lang"] = lang

    return result
