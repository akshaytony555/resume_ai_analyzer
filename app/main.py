from fastapi import FastAPI,Form
from .resume_parser import extract_text_from_pdf    
from .chains import get_resume_feedback,get_skill_gap_analysis

app=FastAPI()
@app.get("/")
def read_root():
    return {'Server up and running'}

@app.post("/extract-text/")
def extract_text(file_path: str):
    text = extract_text_from_pdf(file_path)
    feedback=get_resume_feedback(text)
    return {"feedback": feedback}

@app.post("/skill-gap-analysis/")
def skill_gap_analysis(file_path: str, job_description: str = Form(...)):
    resume_text = extract_text_from_pdf(file_path)
    analysis = get_skill_gap_analysis(resume_text, job_description)
    return {"skill_gap_analysis": analysis}


