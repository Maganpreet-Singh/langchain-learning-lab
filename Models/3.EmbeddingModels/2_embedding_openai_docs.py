"""Create document embeddings with OpenAI. Requires OPENAI_API_KEY."""
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
embedding = OpenAIEmbeddings(model="text-embedding-3-small")
documents = ["Delhi is the capital of India.", "Kolkata is the capital of West Bengal.", "Paris is the capital of France."]
vectors = embedding.embed_documents(documents)
print("Number of vectors:", len(vectors))
print("Dimensions per vector:", len(vectors[0]))
