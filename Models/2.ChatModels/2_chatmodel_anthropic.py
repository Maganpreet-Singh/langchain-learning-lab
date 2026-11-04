"""Anthropic chat example. Requires ANTHROPIC_API_KEY."""
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()
model = ChatAnthropic(model="claude-3-5-sonnet-latest", max_tokens=150)
print(model.invoke("What is the capital of India?").content)
