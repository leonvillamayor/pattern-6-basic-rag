# ChromaDB: filtrar por dominio y fecha antes del ANN
results = collection.query(
    query_embeddings=[query_emb],
    n_results=5,
    where={
        "$and": [
            {"domain": "finance"},
            {"published_at": {"$gte": "2024-01-01"}}
        ]
    }
)