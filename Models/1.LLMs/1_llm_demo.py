"""Basic completion-style OpenAI example. Requires OPENAI_API_KEY in .env."""
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()
llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=100)
print(llm.invoke("What is the capital of India?"))
