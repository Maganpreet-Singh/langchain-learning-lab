"""OpenAI chat example. Requires OPENAI_API_KEY."""
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=100)
print(model.invoke("Write a five-line poem about cricket.").content)
