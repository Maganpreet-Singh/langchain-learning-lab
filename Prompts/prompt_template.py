from langchain_core.prompts import PromptTemplate
from common import get_chat_model

model = get_chat_model(temperature=0.7)

template = PromptTemplate(
    template="Greet this person in five languages. Their name is {name}.",
    input_variables=["name"],
)

prompt = template.invoke({"name": "Maganpreet"})
response = model.invoke(prompt)
print(response.content)
