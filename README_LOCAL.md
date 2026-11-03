# LangChain Models — Local Setup

A cleaned local-learning copy of the CampusX examples, covering LLMs, chat models, and embeddings.

## Requirements
- Windows 10/11 and VS Code with the Python extension
- Python 3.11 or 3.12 recommended (avoid Python 3.14 for this stack)
- Internet connection for package/model downloads

## 1. Create the environment (VS Code PowerShell terminal)

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

If activation is blocked in the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

For Command Prompt, activate with `.venv\Scripts\activate.bat`.

## 2. API keys (hosted models only)
Copy `.env.example` to `.env` and fill in only the provider key you use. Do not commit `.env`.
- OpenAI: `OPENAI_API_KEY`
- Anthropic: `ANTHROPIC_API_KEY`
- Gemini: `GOOGLE_API_KEY`
- Hugging Face hosted inference: `HUGGINGFACEHUB_API_TOKEN`

The local Hugging Face embedding examples and TinyLlama local chat example do not need API keys. They download model weights at first run.

## 3. Run from the project root

```powershell
python test.py
python 3.EmbeddingModels/3_embedding_hf_local.py
python 3.EmbeddingModels/4_document_similarity.py
python 2.ChatModels/5_chatmodel_hf_local.py
```

Hosted provider examples (run only after setting the matching key):

```powershell
python 2.ChatModels/1_chatmodel_openai.py
python 2.ChatModels/2_chatmodel_anthropic.py
python 2.ChatModels/3_chatmodel_google.py
python 2.ChatModels/4_chatmodel_hf_api.py
python 3.EmbeddingModels/1_embedding_openai_query.py
python 3.EmbeddingModels/2_embedding_openai_docs.py
```

## Notes
- Always run scripts from the project root so `load_dotenv()` finds `.env`.
- Local model downloads can be large; CPU inference may be slow and requires adequate RAM.
- Provider model IDs and hosted access can change. If a provider rejects a model ID, check its current model catalogue and account access.
- Never hard-code API keys in source files.
