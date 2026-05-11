# 📄 RAG-Based PDF Chatbot

<img width="1774" height="887" alt="RAG-Based PDF Chatbot Screenshot" src="https://github.com/user-attachments/assets/11e40fca-8c5d-4776-93ca-016f3a49f212" />

An end-to-end Retrieval-Augmented Generation (RAG) application that allows users to upload multiple PDF documents and ask natural language questions grounded in the document content.

---

## 🚀 Features

- 📄 Multi-PDF upload and text extraction using PyPDF2
- ✂️ Text chunking for efficient document processing
- 🧠 Semantic embeddings using Sentence Transformers
- 🔍 FAISS vector database for similarity search
- 🤖 Context-aware answer generation using OpenRouter LLM APIs
- 💬 Conversational memory for follow-up questions
- 🆕 New Chat button to reset conversation history
- ⏳ Loading spinner during response generation
- 🏗️ Modular architecture for easy extension and maintenance
- 🌐 Interactive web interface built with Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- PyPDF2
- Sentence Transformers (`all-MiniLM-L6-v2`)
- FAISS
- NumPy
- Requests
- OpenRouter API

---

## 🏗️ Architecture

```text
PDF Upload
   ↓
Text Extraction (PyPDF2)
   ↓
Text Cleaning
   ↓
Chunking
   ↓
Sentence Embeddings
   ↓
FAISS Vector Index
   ↓
Semantic Retrieval
   ↓
Prompt Construction + Chat History
   ↓
LLM Response Generation (OpenRouter)
   ↓
Streamlit Chat Interface
```

---

## 📂 Project Structure

```text
pdfchat/
├── app.py              # Streamlit user interface
├── llm.py              # Prompt creation and OpenRouter API calls
├── retriever.py        # FAISS similarity search
├── embeddings.py       # Embedding generation
├── chunker.py          # Text chunking logic
├── uploaded_pdfs.py    # PDF loading and text extraction
├── .env                # API keys
├── requirements.txt
└── README.md
```

---


