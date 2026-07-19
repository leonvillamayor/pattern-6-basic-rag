# Esqueleto mínimo con LlamaIndex
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex

docs = SimpleDirectoryReader("data/", recursive=True).load_data()
index = VectorStoreIndex.from_documents(docs)
index.storage_context.persist(persist_dir="./storage")