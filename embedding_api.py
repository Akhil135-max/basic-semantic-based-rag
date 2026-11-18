import os
import requests
from dotenv import load_dotenv

load_dotenv()

JINA_API_KEY = os.getenv("JINA_API_KEY")

def generate_embeddings(texts, task="retrieval.passage"):

    if not JINA_API_KEY:
        raise ValueError("JINA_API_KEY is missing")

    url = "https://api.jina.ai/v1/embeddings"

    headers = {
        "Authorization": f"Bearer {JINA_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "jina-embeddings-v3",
        "input": texts,
        "task": task,
        "dimensions": 1024
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=60
    )

    response.raise_for_status()

    result = response.json()

    return [
        item["embedding"]
        for item in sorted(result["data"], key=lambda x: x["index"])]