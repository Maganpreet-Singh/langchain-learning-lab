"""Hugging Face hosted inference example. Requires HUGGINGFACEHUB_API_TOKEN and access to this model/provider."""
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()
llm = HuggingFaceEndpoint(
    repo_id="HuggingFaceH4/zephyr-7b-beta",
    task="text-generation",
    max_new_tokens=128,
    temperature=0.5,
)
chat_model = ChatHuggingFace(llm=llm)
print(chat_model.invoke("What is the capital of India?").content)
