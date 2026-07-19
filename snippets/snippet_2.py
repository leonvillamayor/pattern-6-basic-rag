from llama_index.core import Document

doc = Document(
    text="Alexander met Diogenes in Corinth...",
    metadata={"source": "gutenberg", "author": "Plutarch", "date": "2024-01-15"},
    doc_id="plutarch-alexander-001",
)