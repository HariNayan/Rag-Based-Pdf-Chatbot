from sentence_transformers import SentenceTransformer
from chunker import create_chunker

def create_embeddings(uploaded_pdfs):
    chunks = create_chunker(uploaded_pdfs)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = []
    for chunk in chunks: 
        item_embedding = model.encode(chunk) 
        item = item_embedding
        item2 = {"text": chunk}
        embeddings.append(item)
    return embeddings, chunks, model