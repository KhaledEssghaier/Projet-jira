import os
import requests

def generate_summary(description: str) -> str:
    """
    Calls an LLM API (e.g., OpenAI) to generate a summary for the book description.
    """
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        return "No API key provided."
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that summarizes book descriptions."},
            {"role": "user", "content": f"Résumé du livre : {description}"}
        ],
        "max_tokens": 100
    }
    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers=headers,
        json=data
    )
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"].strip()
    return "Résumé non disponible."
