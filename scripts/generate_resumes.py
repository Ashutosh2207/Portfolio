#!/usr/bin/env python3
"""
Generate 4 role-specific, single-page, ATS-friendly resumes for Ashutosh Dwivedi.

Outputs (PDF, A4):
  assets/resumes/Ashutosh_Dwivedi_Software_Engineer.pdf
  assets/resumes/Ashutosh_Dwivedi_Python_Developer.pdf
  assets/resumes/Ashutosh_Dwivedi_AI_ML_Engineer.pdf
  assets/resumes/Ashutosh_Dwivedi_Internship.pdf
"""

from pathlib import Path

from fpdf import FPDF
from fpdf.enums import XPos, YPos

ROOT = Path(__file__).resolve().parent.parent
FONT_DIR = Path("/home/user/fonts")
OUT_DIR = ROOT / "assets" / "resumes"

# ---------------------------------------------------------------- palette ---
NAVY = (15, 40, 66)        # headings / name
ACCENT = (30, 84, 138)     # role title, section titles
BODY = (55, 60, 66)        # body text
MUTED = (110, 116, 122)    # dates, meta
RULE_DARK = (26, 58, 92)
RULE_LIGHT = (196, 202, 208)

PAGE_W = 210
PAGE_H = 297
MARGIN = 13
CONTENT_W = PAGE_W - 2 * MARGIN

# ------------------------------------------------------------------ data ---
COMMON = {
    "name": "ASHUTOSH DWIVEDI",
    "location": "Prayagraj, Uttar Pradesh",
    "phone": "+91 63885 69856",
    "email": "dwivediashutosh393@gmail.com",
    "linkedin": "linkedin.com/in/ashutosh2207",
    "github": "github.com/Ashutosh2207",
}

EDUCATION = {
    "degree": "B.Tech — Computer Science & Engineering",
    "college": "United Institute of Technology, Prayagraj (United University)",
    "years": "2023 – 2026 (Expected)",
}

PROJECTS = {
    "v2p": {
        "title": "Voice-to-Prescription — AI Medical Scribe",
        "tech": "Python, FastAPI, Whisper (STT), spaCy NER, Ollama LLM, Streamlit",
        "bullets": [
            "Built an end-to-end voice-to-prescription pipeline that converts a doctor's spoken dictation into structured, validated JSON prescriptions — designed to run fully local, with no cloud dependency.",
            "Integrated Whisper speech-to-text with a spaCy NER + rule-based engine to normalise medicine names, dosages, frequencies and durations; added optional Ollama (Mistral 3B) LLM for higher-accuracy extraction.",
            "Exposed FastAPI REST endpoints (CORS-enabled) for mobile clients and a Streamlit demo UI with field-level validation and confidence scores.",
        ],
        "bullets_short_idx": {0, 1},
    },
    "phish": {
        "title": "AI-Powered Phishing Detection System",
        "tech": "Python, Flask, scikit-learn (Random Forest), JavaScript, HTML, CSS",
        "bullets": [
            "Developed a web app that classifies URLs as phishing / legitimate in real time using a Random Forest model trained on lexical URL features with scikit-learn.",
            "Built the complete stack end-to-end — model training pipeline, Flask REST backend and a responsive cybersecurity-themed frontend (HTML/CSS/JS).",
        ],
        "bullets_short_idx": {0, 1},
    },
    "ocr": {
        "title": "ID-Card OCR & Information Extraction",
        "tech": "Python, OpenCV, pytesseract, Pillow, Streamlit, Flask",
        "bullets": [
            "Engineered an OCR pipeline that extracts structured fields (name, DOB, ID numbers) from Aadhaar, PAN, driving licence and voter ID images.",
            "Implemented dedicated per-document extractors with OpenCV/Pillow image pre-processing for higher recognition accuracy; exposed via Streamlit app and Flask API.",
        ],
        "bullets_short_idx": {0, 1},
    },
    "jarvis": {
        "title": "JARVIS — Personal AI Assistant",
        "tech": "Python, Flask, pywebview, SpeechRecognition, pyttsx3, psutil, OpenAI/Ollama APIs",
        "bullets": [
            "Created a JARVIS-style assistant handling voice commands, desktop automation, system monitoring (CPU/RAM via psutil) and conversational replies through OpenAI/Ollama LLM APIs.",
            "Serves a Flask web interface inside a pywebview desktop shell; packaged a standalone Windows executable using PyInstaller.",
        ],
        "bullets_short_idx": {0, 1},
    },
    "sum": {
        "title": "AI Text Summarization Web App",
        "tech": "Python, Flask, JavaScript, HTML, CSS",
        "bullets": [
            "Built a web app that condenses long text into concise summaries through a clean two-pane interface with instant Flask-powered processing.",
        ],
        "bullets_short_idx": {0},
    },
}

ACHIEVEMENTS = [
    ("Competed at Rajasthan Police Hackathon 1.0 (RAKAM), Jaipur", "Jan 2024"),
    ("Represented Team BLACKBOX 913 at HackQuest '25 — 24-hr hackathon, UIT Prayagraj", "Apr 2025"),
    ("Team Cryptoknights at HackDiwas 2024 — 24-hr hackathon, United University", "Apr 2024"),
]

RESUMES = {
    "swe": {
        "file": "Ashutosh_Dwivedi_Software_Engineer.pdf",
        "headline": "Aspiring Software Engineer  |  Python  ·  Flask  ·  REST APIs  ·  Full-Stack",
        "summary": (
            "Final-year B.Tech CSE student who ships complete products end-to-end — from Flask/FastAPI backends "
            "and ML services to responsive frontends. Hackathon-tested under 24-hour deadlines and comfortable "
            "across the full stack. Seeking a Software Engineer role to build reliable, user-facing systems."
        ),
        "skills": [
            ("Programming Languages", "Python, C++, JavaScript, SQL"),
            ("Web & Frameworks", "Flask, FastAPI, Streamlit, HTML, CSS, Bootstrap"),
            ("Databases", "MySQL, SQLite, SQLAlchemy"),
            ("CS Fundamentals", "Data Structures & Algorithms, OOP, DBMS, Operating Systems, Computer Networks"),
            ("Tools & Platforms", "Git/GitHub, VS Code, Postman, Linux, PyInstaller"),
        ],
        "coursework": None,
        "projects": [
            ("phish", 3),
            ("v2p", 3),
            ("jarvis", 2),
            ("ocr", 2),
        ],
    },
    "pydev": {
        "file": "Ashutosh_Dwivedi_Python_Developer.pdf",
        "headline": "Python Developer  |  Flask  ·  FastAPI  ·  Automation  ·  REST APIs",
        "summary": (
            "Python developer who builds practical tools end-to-end — voice-driven AI pipelines, OCR extractors, "
            "desktop automation and web backends in clean, testable Python. Strong grasp of OOP, REST API design "
            "and packaging. Seeking a Python Developer role to deliver production-quality code."
        ),
        "skills": [
            ("Core Python", "OOP, file & exception handling, decorators, virtual environments, packaging"),
            ("Web & APIs", "Flask, FastAPI, REST API design, Jinja2, Streamlit"),
            ("Key Libraries", "psutil, pyttsx3, SpeechRecognition, Pillow, OpenCV, pytesseract, NumPy, pandas"),
            ("Databases", "SQL, SQLite, SQLAlchemy"),
            ("Tools", "Git/GitHub, PyInstaller, VS Code, Postman, Linux"),
        ],
        "coursework": None,
        "projects": [
            ("v2p", 3),
            ("jarvis", 2),
            ("ocr", 2),
            ("phish", 2),
        ],
    },
    "aiml": {
        "file": "Ashutosh_Dwivedi_AI_ML_Engineer.pdf",
        "headline": "AI / ML Engineer  |  NLP  ·  Scikit-learn  ·  LLM Apps  ·  Model Deployment",
        "summary": (
            "AI-focused engineering student with hands-on experience across the ML lifecycle — data collection, "
            "feature engineering, training and deployment. Built NLP/GenAI systems using spaCy, Whisper, "
            "Transformers and OpenAI/Ollama LLMs. Seeking an AI/ML Engineer (or AI intern) role to turn research "
            "quality models into working products."
        ),
        "skills": [
            ("Machine Learning", "scikit-learn, Random Forest, classification, feature engineering, model evaluation"),
            ("NLP & GenAI", "spaCy NER, Hugging Face Transformers, Whisper (STT), OpenAI API, Ollama (local LLMs)"),
            ("Data Handling", "pandas, NumPy, text normalisation, feature extraction"),
            ("Deployment", "Flask, FastAPI, Streamlit, model serialisation (joblib/pickle)"),
            ("Languages & Tools", "Python, SQL, Git/GitHub, VS Code, Linux"),
        ],
        "coursework": None,
        "projects": [
            ("v2p", 3),
            ("phish", 2),
            ("ocr", 2),
            ("sum", 1),
        ],
    },
    "intern": {
        "file": "Ashutosh_Dwivedi_Internship.pdf",
        "headline": "B.Tech CSE '26  |  Software Engineering Intern",
        "summary": (
            "Motivated final-year B.Tech CSE student seeking a software engineering internship. Quick, "
            "self-driven learner with hackathon experience and four shipped projects spanning Python backends, "
            "ML applications and web frontends. Eager to contribute, learn fast and grow with a strong team."
        ),
        "skills": [
            ("Languages", "Python, C++, JavaScript, SQL"),
            ("Web", "Flask, HTML, CSS, JavaScript, Bootstrap"),
            ("ML & Data", "scikit-learn, spaCy, OpenCV, pandas, NumPy"),
            ("Tools", "Git/GitHub, VS Code, Postman, Linux"),
        ],
        "coursework": "Relevant Coursework: Data Structures & Algorithms, OOP, DBMS, Operating Systems, Computer Networks",
        "projects": [
            ("phish", 2),
            ("v2p", 2),
            ("jarvis", 2),
            ("ocr", 2),
        ],
    },
}

# --------------------------------------------------------------- renderer ---


class ResumePDF(FPDF):
    def __init__(self):
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_auto_page_break(auto=False)
        self.set_margins(MARGIN, MARGIN, MARGIN)
        self.set_title("Ashutosh Dwivedi — Resume")
        self.set_author("Ashutosh Dwivedi")
        self.set_creator("Ashutosh Dwivedi")

        self.add_font("Poppins", "", str(FONT_DIR / "Poppins-Regular.ttf"))
        self.add_font("Poppins", "B", str(FONT_DIR / "Poppins-Bold.ttf"))
        self.add_font("Poppins", "I", str(FONT_DIR / "Poppins-Italic.ttf"))
        self.add_font("Poppins", "BI", str(FONT_DIR / "Poppins-SemiBold.ttf"))

    # -- helpers ------------------------------------------------------------
    def _style(self, style: str, size: float, color=tuple, scroll=True):
        self.set_font("Poppins", style, size)
        self.set_text_color(*color)

    def section(self, title: str):
        self.ln(2.0)
        self._style("BI", 10.3, ACCENT)
        self.set_text_color(*ACCENT)
        self.cell(0, 5.2, title.upper(), new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y = self.get_y()
        self.set_draw_color(*RULE_DARK)
        self.set_line_width(0.45)
        self.line(MARGIN, y + 0.6, MARGIN + CONTENT_W, y + 0.6)
        self.ln(2.6)

    def entry_row(self, left: str, right: str, size=9.6):
        self._style("BI", size, NAVY)
        self.cell(CONTENT_W * 0.80, 5.2, left, align="L")
        self._style("", 8.4, MUTED)
        self.cell(CONTENT_W * 0.20, 5.2, right, align="R", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def muted_line(self, text: str, size=8.5):
        self._style("I", size, MUTED)
        self.multi_cell(0, 4.2, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    def bullet(self, text: str, size=9.0):
        self._style("", size, BODY)
        x0 = self.get_x()
        y0 = self.get_y()
        indent = 4.6
        self.set_x(x0 + indent)
        self.multi_cell(CONTENT_W - indent, 4.35, text, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        # bullet dot — aligned with the FIRST line of the bullet
        self.set_fill_color(*ACCENT)
        self.rect(x0 + 1.7, y0 + 1.55, 1.1, 1.1, "F")

    def skill_row(self, label: str, value: str):
        self._style("BI", 9.0, NAVY)
        self.cell(42, 4.7, label)
        self._style("", 8.9, BODY)
        self.multi_cell(0, 4.7, value, new_x=XPos.LMARGIN, new_y=YPos.NEXT)

    # -- build ---------------------------------------------------------------
    def build(self, cfg: dict):
        self.add_page()

        # Header
        self._style("B", 20, NAVY)
        self.cell(0, 9, COMMON["name"], align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self._style("BI", 9.6, ACCENT)
        self.cell(0, 5.2, cfg["headline"], align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        self._style("", 8.2, MUTED)
        contact = "  •  ".join([
            COMMON["location"],
            COMMON["phone"],
            COMMON["email"],
            COMMON["linkedin"],
            COMMON["github"],
        ])
        self.cell(0, 4.6, contact, align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)
        y = self.get_y()
        self.set_draw_color(*RULE_DARK)
        self.set_line_width(0.55)
        self.line(MARGIN, y + 1.2, MARGIN + CONTENT_W, y + 1.2)
        self.ln(3.4)

        # Summary
        self._style("", 9.0, BODY)
        self.multi_cell(0, 4.5, cfg["summary"], align="C", new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Education
        self.section("Education")
        self.entry_row(EDUCATION["degree"], EDUCATION["years"])
        self.muted_line(EDUCATION["college"])
        if cfg["coursework"]:
            self._style("", 8.8, BODY)
            self.multi_cell(0, 4.2, cfg["coursework"], new_x=XPos.LMARGIN, new_y=YPos.NEXT)

        # Skills
        self.section("Technical Skills")
        for label, value in cfg["skills"]:
            self.skill_row(label, value)

        # Projects
        self.section("Projects")
        for pid, n_bullets in cfg["projects"]:
            p = PROJECTS[pid]
            self.entry_row(p["title"], "", size=9.7)
            self.muted_line("Tech: " + p["tech"], size=8.4)
            bullets = p["bullets"][:n_bullets]
            for b in bullets:
                self.bullet(b)
            self.ln(1.8)

        # Achievements
        self.section("Achievements & Certifications")
        for text, date in ACHIEVEMENTS:
            self.bullet(f"{text}  ({date})", size=9.0)

        return self


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for key, cfg in RESUMES.items():
        pdf = ResumePDF().build(cfg)
        out = OUT_DIR / cfg["file"]
        pdf.output(str(out))
        # sanity: verify single page
        import re
        raw = out.read_bytes()
        pages = len(re.findall(rb"/Type\s*/Page[^s]", raw))
        print(f"{out.name:48s} pages={pages} size={out.stat().st_size/1024:.1f} KB")
        if pages != 1:
            raise SystemExit(f"ERROR: {out.name} has {pages} pages, expected 1")


if __name__ == "__main__":
    main()
