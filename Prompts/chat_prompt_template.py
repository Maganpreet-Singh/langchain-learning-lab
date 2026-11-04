from langchain_core.prompts import ChatPromptTemplate
from common import get_chat_model

chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful {domain} expert. Explain concepts accurately and simply."),
    ("human", "Explain {topic} in simple terms and give one practical example."),
])

prompt_value = chat_template.invoke({"domain": "cricket", "topic": "the doosra delivery"})
model = get_chat_model()
response = model.invoke(prompt_value)
print(response.content)
