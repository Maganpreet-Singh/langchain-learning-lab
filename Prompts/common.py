"""Shared Hugging Face model construction for the examples."""
import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

load_dotenv()

def get_chat_model(temperature: float = 0.7, max_new_tokens: int = 512):
    """Create a hosted Hugging Face chat model using an environment token."""
    token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
    model_id = os.getenv("HF_MODEL", "HuggingFaceH4/zephyr-7b-beta")
    if not token:
        raise RuntimeError(
            "HUGGINGFACEHUB_API_TOKEN is missing. Add it to your .env file. "
            "See .env.example and README.md."
        )
    endpoint = HuggingFaceEndpoint(
        repo_id=model_id,
        task="text-generation",
        max_new_tokens=max_new_tokens,
        do_sample=temperature > 0,
        temperature=max(0.01, temperature),
        huggingfacehub_api_token=token,
    )
    return ChatHuggingFace(llm=endpoint)
