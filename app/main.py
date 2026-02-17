from fastapi import FastAPI
from .resume_parser import extract_text_from_pdf    
from .chains import get_resume_feedback

app=FastAPI()
@app.get("/")
def read_root():
    return {'Server up and running'}

@app.post("/extract-text/")
def extract_text(file_path: str):
    text = extract_text_from_pdf(file_path)
    feedback=get_resume_feedback(text)
    return {"feedback": feedback}
    


