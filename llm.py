import requests
import json
from retriever import create_retriever
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")
Chunks, query = create_retriever()

def create_llm():
    context=' '.join(Chunks)
    Prompt = f"context: {context} Questions: {query} Answer only from the context."
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
          headers={
              "Authorization": f"Bearer {api_key}",
              "Content-Type": "application/json"
              },
              data=json.dumps({
                  "model": "z-ai/glm-4.5-air:free",
                  "messages": [
                      {
                          "role": "user",
                          "content": Prompt
                }
            ]
        })
   )
    result = response.json()
    answer = result["choices"][0]["message"]["content"]
    return answer