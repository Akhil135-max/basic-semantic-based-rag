from retrieval import search_vector_db

results = search_vector_db(
    "Give your query"
)

for document, metadata, distance in results:

    print("Document:", document)
    print("Metadata:", metadata)
    print("Distance:", distance)
    print("-" * 80)