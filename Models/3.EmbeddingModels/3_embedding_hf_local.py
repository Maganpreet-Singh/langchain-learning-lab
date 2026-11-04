"""Generate local embeddings. No API key; first run downloads the model."""
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)
documents = ["Delhi is the capital of India.", "Kolkata is the capital of West Bengal.", "Paris is the capital of France."]
vectors = embedding.embed_documents(documents)
print("Number of vectors:", len(vectors))
print("Dimensions per vector:", len(vectors[0]))
print(vectors[0][:10], "...")
