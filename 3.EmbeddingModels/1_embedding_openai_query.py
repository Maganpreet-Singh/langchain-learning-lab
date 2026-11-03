"""Create one embedding vector with OpenAI. Requires OPENAI_API_KEY."""
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
embedding = OpenAIEmbeddings(model="text-embedding-3-small")
vector = embedding.embed_query("Delhi is the capital of India")
print("Vector dimensions:", len(vector))
print(vector)
