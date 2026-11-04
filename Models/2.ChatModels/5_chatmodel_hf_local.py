"""Run TinyLlama locally. First run downloads model weights; CPU inference may be slow."""
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs={"temperature": 0.5, "max_new_tokens": 100, "do_sample": True},
)
chat_model = ChatHuggingFace(llm=llm)
print(chat_model.invoke("What is the capital of India?").content)
