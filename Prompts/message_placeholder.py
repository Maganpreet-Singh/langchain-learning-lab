from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from common import get_chat_model

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer-support agent. Never invent order status."),
    MessagesPlaceholder(variable_name="chat_history", optional=True),
    ("human", "{query}"),
])

# Typed messages are important: do not pass raw lines from a text file as chat messages.
chat_history = [
    HumanMessage(content="I want to request a refund for order #12345."),
    AIMessage(content="I can help you understand the refund process. Please check the store's official policy."),
]
prompt = chat_template.invoke({"chat_history": chat_history, "query": "What information do you need from me?"})
response = get_chat_model().invoke(prompt)
print(response.content)
