import streamlit as st
from langchain_core.prompts import load_prompt
from common import get_chat_model

st.set_page_config(page_title="Research Paper Explainer", page_icon="📚", layout="centered")
st.title("📚 Research Paper Explainer")
st.caption("LangChain prompts + Hugging Face inference. No OpenAI API used.")

paper_input = st.text_input("Research paper title", "Attention Is All You Need")
style_input = st.selectbox("Explanation style", ["Beginner-friendly", "Technical", "Code-oriented", "Mathematical"])
length_input = st.selectbox("Explanation length", ["Short (1–2 paragraphs)", "Medium (3–5 paragraphs)", "Long (detailed)"])
paper_text = st.text_area("Optional: paste the abstract or paper text", height=180, placeholder="Paste source text here for a grounded summary.")

if st.button("Generate explanation", type="primary", use_container_width=True):
    if not paper_input.strip():
        st.warning("Enter a paper title first.")
    else:
        try:
            with st.spinner("Generating with Hugging Face..."):
                model = get_chat_model(temperature=0.3, max_new_tokens=900)
                prompt = load_prompt("template.json")
                chain = prompt | model
                source = paper_input.strip()
                if paper_text.strip():
                    source += "\n\nProvided paper text / abstract:\n" + paper_text.strip()
                result = chain.invoke({
                    "paper_input": source,
                    "style_input": style_input,
                    "length_input": length_input,
                })
            st.markdown(result.content)
        except Exception as exc:
            st.error(f"Generation failed: {exc}")
            st.info("Check your token, model ID, provider availability, and installed package versions.")
