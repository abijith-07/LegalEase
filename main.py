from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from .legal_service import generate_document

app = FastAPI(title="LegalEase: AI-Powered Legal Document Generator")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={})

@app.post("/generate", response_class=HTMLResponse)
def generate(request: Request, document_type: str = Form(...), name: str = Form(...), details: str = Form(...)):
    document = generate_document(document_type, name, details)
    return templates.TemplateResponse(
        request=request, name="result.html",
        context={"document_type": document_type, "name": name, "document": document}
    )

@app.get("/health")
def health():
    return {"status": "ok", "project": "LegalEase AI Legal Document Generator"}
