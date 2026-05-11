import faiss
import numpy as np

from embeddings import create_embeddings

def create_retriever(user_question, uploaded_pdfs):
    embeddings, chunks, model = create_embeddings(uploaded_pdfs)
    dimensions = len(embeddings [0])
    index = faiss.IndexFlatIP(dimensions)
    vectors = np.array(embeddings).astype(np.float32)
    index.add(vectors)
    K=8
    query_embedding = model.encode(user_question)
    query_vector = np.array(query_embedding).astype(np.float32)
    collection = [query_vector]
    collection = np.array(collection).astype(np.float32)
    distance, indices=index.search(collection, K)
    Chunks=[]
    for i in indices[0]:
        Chunks.append(chunks[i])
    return Chunks