# RAG-Based PDF Chatbot

<img width="1774" height="887" alt="ChatGPT Image May 9, 2026, 04_12_39 AM (2)" src="https://github.com/user-attachments/assets/11e40fca-8c5d-4776-93ca-016f3a49f212" />

A Retrieval-Augmented Generation (RAG) based PDF chatbot built using Python, FAISS, Sentence Transformers, and LLM APIs.

## Features

* PDF text extraction using PyPDF2
* Semantic chunk embeddings using Sentence Transformers
* FAISS vector database for similarity search
* Context-aware question answering
* Retrieval-Augmented Generation (RAG) pipeline
* Modular backend architecture

## Tech Stack

* Python
* PyPDF2
* Sentence Transformers
* FAISS
* NumPy
* OpenRouter / Gemini API

## Architecture

PDF → Text Extraction → Chunking → Embeddings → FAISS Retrieval → Context Injection → LLM Response

## Current Progress

* Basic RAG pipeline completed
* Semantic retrieval working
* LLM response generation integrated
* Modularization in progress

## Future Improvements

* Multi-PDF support
* Conversational memory
* Streamlit UI
* Persistent vector database
* Better chunking strategies
* Source/page citations

## Setup

1. Clone the repository
2. Create virtual environment
3. Install dependencies
4. Add API keys
5. Run the chatbot

## Learning Goals

This project focuses on understanding:

* Vector embeddings
* Semantic search
* Retrieval systems
* RAG architecture
* Modular backend design
* LLM integration
