import requests
import json
from retriever import create_retriever
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def create_llm(user_question, history, uploaded_pdfs):
    Chunks = create_retriever(user_question, uploaded_pdfs)
    context=' '.join(Chunks)
    conversation_history = '\n'.join(history)
    Prompt = f"conversation_history:{conversation_history} \n context: {context} \n Questions: {user_question} Answer only from the context."
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