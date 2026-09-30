# LegalEase: AI-Powered Legal Document Generator

A FastAPI web application for creating structured educational drafts of common legal-style documents.

## Features
- Simple web interface
- Multiple document types
- Structured draft generation
- FastAPI + Jinja2
- Responsive CSS

## Run
```bash
python -m venv venv
```
Windows:
```powershell
venv\Scripts\activate
```
Install:
```powershell
pip install -r requirements.txt
```
Start:
```powershell
python -m uvicorn app.main:app --reload
```
Open http://127.0.0.1:8000

## Disclaimer
LegalEase is an educational document-drafting project. Generated drafts may not satisfy the laws or procedural requirements of a particular jurisdiction. Consult a qualified legal professional before official use.
