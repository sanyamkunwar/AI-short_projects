from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/summarize")
def summarize(data: dict):
    text = data["text"]
    result = summarizer(
        text,
        max_length=60,
        min_length=20,
        do_sample=False
    )
    return {"summary": result[0]["summary_text"]}
