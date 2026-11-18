import os
from dotenv import load_dotenv
from langchain_postgres import PGVector
from embedding import JinaEmbeddings

load_dotenv()

CONNECTION_STRING = os.getenv("DATABASE_URL")

def store_chunks(chunks):

    embeddings = JinaEmbeddings()

    vector_store = PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="vr26_module",
        connection=CONNECTION_STRING,
        use_jsonb=True
    )

    return vector_store