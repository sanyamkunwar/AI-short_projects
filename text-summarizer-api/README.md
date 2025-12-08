# Text Summarizer API (FastAPI + Transformers)

A lightweight API that generates summaries using `facebook/bart-large-cnn`.

## 🚀 Run the API
pip install -r requirements.txt

uvicorn app:app --reload


## 📝 Endpoint
**POST /summarize**
```json
{
  "text": "Your long paragraph here..."
}

Response:

{ "summary": "..." }


---
