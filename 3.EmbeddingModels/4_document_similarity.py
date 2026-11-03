"""Semantic document similarity using local embeddings; no API key needed."""
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True},
)
documents = [
    "Virat Kohli is an Indian cricketer known for aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for calm leadership and finishing.",
    "Sachin Tendulkar is a legendary Indian batter who holds many records.",
    "Rohit Sharma is known for elegant batting and double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for yorkers and his unusual action.",
]
query = "Tell me about Bumrah"
doc_vectors = embedding.embed_documents(documents)
query_vector = embedding.embed_query(query)
scores = cosine_similarity([query_vector], doc_vectors)[0]
best_index = scores.argmax()
print("Query:", query)
print("Best match:", documents[best_index])
print("Similarity score:", round(float(scores[best_index]), 4))
