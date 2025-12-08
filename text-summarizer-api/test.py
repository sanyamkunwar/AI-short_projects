import requests

data = {
    "text": "Artificial intelligence is transforming the world through automation, analytics, and optimization."
}

res = requests.post("http://127.0.0.1:8000/summarize", json=data)
print(res.json())
