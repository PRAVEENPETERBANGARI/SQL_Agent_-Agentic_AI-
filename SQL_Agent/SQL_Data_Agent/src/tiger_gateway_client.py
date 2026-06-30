import requests
from src.config import LLM_CONFIG

def call_llm(messages):
    response = requests.post(
        LLM_CONFIG["url"],
        headers={"Authorization": f"Bearer {LLM_CONFIG['api_key']}"},
        json={"model": LLM_CONFIG["model"], "messages": messages},
        timeout=60,
    )
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
