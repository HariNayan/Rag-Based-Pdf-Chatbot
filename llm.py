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
    Prompt = f"""
    You are a helpful AI assistant that answers questions using only the information provided in the context from one or more uploaded PDF documents.

    Conversation History:
    {conversation_history}

    Retrieved Context:
    {context}

    Current Question:
    {user_question}

    Instructions:
    1. Answer using only the information found in the retrieved context.
    2. If the answer is not present in the context, reply exactly:
    "I could not find the answer in the uploaded PDF documents."
   3. Use conversation history only to understand follow-up questions and references such as "it", "this", or "that".
   4. When multiple PDFs are uploaded, combine relevant information from all retrieved context chunks.
   5. Keep the answer clear, concise, and well-structured.
   6. Do not make up facts or use external knowledge.
   7. If the context contains conflicting information, mention the differences explicitly.

   Answer:
   """
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