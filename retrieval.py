from embedding import JinaEmbeddings
import psycopg
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

embeddings = JinaEmbeddings()

def search_vector_db(question):

    # Generate query embedding
    query_vector = embeddings.embed_query(question)

    # Connect to PostgreSQL
    conn = psycopg.connect(DATABASE_URL)

    cur = conn.cursor()

    # Similarity search using cosine distance
    cur.execute("""
        SELECT
            document,
            cmetadata,
            embedding <=> %s::vector AS distance
        FROM langchain_pg_embedding
        WHERE collection_id = (
            SELECT uuid
            FROM langchain_pg_collection
            WHERE name = 'vr26_module'
        )
        ORDER BY embedding <=> %s::vector
        LIMIT 1;
    """, (str(query_vector), str(query_vector)))

    results = cur.fetchall()

    cur.close()
    conn.close()

    return results