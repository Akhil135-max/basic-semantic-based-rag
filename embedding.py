from embedding_api import generate_embeddings

class JinaEmbeddings:

    def embed_documents(self, texts):

        all_embeddings = []

        batch_size = 64

        for i in range(0, len(texts), batch_size):

            batch = texts[i:i + batch_size]

            vectors = generate_embeddings(
                batch,
                task="retrieval.passage"
            )

            all_embeddings.extend(vectors)

        return all_embeddings

    def embed_query(self, text):

        return generate_embeddings(
            [text],
            task="retrieval.query"
        )[0]

"""from embedding_api import generate_embeddings
class JinaEmbeddings:
    def embed_documents(self, texts):
        return generate_embeddings(texts,task="retrieval.passage")
    def embed_query(self, texts):
        return generate_embeddings([texts], task="retrieval.query")[0]"""

