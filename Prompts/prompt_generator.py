from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template="""
Summarize the research paper titled: {paper_input}
Explanation style: {style_input}
Explanation length: {length_input}

Requirements:
1. Explain the research question, method, key findings, and limitations.
2. Include equations only when they are present in the supplied paper text.
3. Explain technical ideas using intuitive analogies and small code examples when useful.
4. Do not fabricate details, results, citations, or equations. If the paper text is not supplied,
   say that the title alone is insufficient to produce a reliable paper-specific summary.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True,
)
template.save("template.json")
print("Saved reusable prompt to template.json")
