from langchain_core.messages import SystemMessage, HumanMessage
from common import get_chat_model

model = get_chat_model()
messages = [
    SystemMessage(content="You are a helpful assistant who teaches LangChain."),
    HumanMessage(content="What is LangChain? Explain its main components."),
]
response = model.invoke(messages)
messages.append(response)
print("Assistant:", response.content)
print("\nMessage history:", messages)
