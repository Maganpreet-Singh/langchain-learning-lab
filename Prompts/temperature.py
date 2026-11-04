from common import get_chat_model

# Temperature controls sampling randomness; keep it in the usual 0-2 range.
model = get_chat_model(temperature=0.9, max_new_tokens=160)
response = model.invoke("Write a five-line original poem about cricket.")
print(response.content)
