from fastapi import FastAPI
from .resume_parser import extract_text_from_pdf    

app=FastAPI()
@app.get("/")
def read_root():
    return {'Server up and running'}

@app.post("/extract-text/")
def extract_text(file_path: str):
    text = extract_text_from_pdf(file_path)
    return {"extracted_text": text}

