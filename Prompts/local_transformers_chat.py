"""Optional local model example: runs with Transformers, not a hosted API."""
import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from dotenv import load_dotenv

load_dotenv()
model_id = os.getenv("LOCAL_MODEL", "TinyLlama/TinyLlama-1.1B-Chat-v1.0")
device = 0 if torch.cuda.is_available() else -1
print(f"Loading {model_id} on {'CUDA GPU' if device == 0 else 'CPU'}...")

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == 0 else torch.float32,
    device_map="auto" if device == 0 else None,
)
generator = pipeline("text-generation", model=model, tokenizer=tokenizer, device=device if device == -1 else None)

messages = [{"role": "system", "content": "You are a helpful assistant."}]
print("Local chatbot. Type 'exit' to stop.")
while True:
    query = input("You: ").strip()
    if query.lower() in {"exit", "quit"}:
        break
    messages.append({"role": "user", "content": query})
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
    output = generator(prompt, max_new_tokens=256, do_sample=True, temperature=0.7, return_full_text=False)
    answer = output[0]["generated_text"].strip()
    messages.append({"role": "assistant", "content": answer})
    print("AI:", answer, "\n")
