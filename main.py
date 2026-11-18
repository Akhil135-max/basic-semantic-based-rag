from ingestion import pdf_loader
from chunking import chunking
from vector_db import store_chunks

# Step 1: Load PDF
docs = pdf_loader(
    "give pdf"
)

print("Total documents:", len(docs))

# Step 2: Chunk documents
chunks = chunking(docs)

print("Total chunks:", len(chunks))

# Step 3: Generate embeddings and store in PostgreSQL
vector_store = store_chunks(chunks)

print("Successfully stored chunks and embeddings!")
    
    