from langchain_core.messages import SystemMessage, HumanMessage
from common import get_chat_model

model = get_chat_model(temperature=0.5, max_new_tokens=400)
chat_history = [SystemMessage(content="You are a friendly, concise AI assistant.")]
print("Hugging Face LangChain chatbot. Type 'exit' to stop.\n")

while True:
    user_input = input("You: ").strip()
    if user_input.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break
    if not user_input:
        continue
    chat_history.append(HumanMessage(content=user_input))
    try:
        response = model.invoke(chat_history)
        chat_history.append(response)
        print(f"AI: {response.content}\n")
    except Exception as exc:
        chat_history.pop()  # Do not leave an unanswered user turn in the history.
        print(f"Model request failed: {exc}\n")
