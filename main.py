"""
main.py — FastAPI backend for AI Compliance Checker
"""

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import os

from questions import FRAMEWORKS, QUESTIONS
from analyzer import analyze_compliance

app = FastAPI(
    title="AI Compliance Checker",
    description="Automated compliance assessment for EU AI Act, NIS2, GDPR, ISO 27001, SOC 2",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")


# ─────────────────────────────────────────
# MODELS
# ─────────────────────────────────────────

class AssessmentRequest(BaseModel):
    framework_id: str
    answers: dict          # {question_id: "oui"|"non"|"partiel"|"na"}
    lang: str = "fr"       # "fr" or "en"
    api_key: str


class HealthResponse(BaseModel):
    status: str
    version: str


# ─────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def root():
    index_path = os.path.join(frontend_path, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return HTMLResponse("<h1>AI Compliance Checker API</h1><p>Visit /docs for API documentation.</p>")


@app.get("/health", response_model=HealthResponse)
async def health():
    return {"status": "ok", "version": "1.0.0"}


@app.get("/api/frameworks")
async def get_frameworks(lang: str = "fr"):
    """Return all available compliance frameworks."""
    result = []
    for fw_id, fw_data in FRAMEWORKS.items():
        questions = QUESTIONS[fw_id]
        result.append({
            "id": fw_id,
            "name": fw_data["name_fr"] if lang == "fr" else fw_data["name_en"],
            "icon": fw_data["icon"],
            "question_count": len(questions),
        })
    return result


@app.get("/api/questions/{framework_id}")
async def get_questions(framework_id: str, lang: str = "fr"):
    """Return questions for a specific framework."""
    if framework_id not in QUESTIONS:
        raise HTTPException(status_code=404, detail=f"Framework '{framework_id}' not found")

    questions = QUESTIONS[framework_id]
    result = []
    for q in questions:
        result.append({
            "id": q["id"],
            "text": q["text_fr"] if lang == "fr" else q["text_en"],
            "category": q["category_fr"] if lang == "fr" else q["category_en"],
            "weight": q["weight"],
        })
    return {
        "framework_id": framework_id,
        "framework_name": FRAMEWORKS[framework_id]["name_fr" if lang == "fr" else "name_en"],
        "questions": result
    }


@app.post("/api/assess")
async def assess(request: AssessmentRequest):
    """
    Run AI-powered compliance assessment.
    Calls Claude API and returns structured gap analysis.
    """
    if request.framework_id not in QUESTIONS:
        raise HTTPException(status_code=404, detail=f"Framework '{request.framework_id}' not found")

    if not request.api_key:
        raise HTTPException(status_code=400, detail="Anthropic API key is required")

    if request.lang not in ["fr", "en"]:
        raise HTTPException(status_code=400, detail="Language must be 'fr' or 'en'")

    try:
        result = analyze_compliance(
            framework_id=request.framework_id,
            answers=request.answers,
            lang=request.lang,
            api_key=request.api_key
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")
