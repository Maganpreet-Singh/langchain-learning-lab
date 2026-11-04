# LangChain Prompts with Hugging Face Models

A Hugging Face-powered adaptation of the prompt-engineering examples in [campusx-official/langchain-prompts](https://github.com/campusx-official/langchain-prompts). The examples use LangChain Core prompt abstractions and Hugging Face inference/local models; **no OpenAI API key or `langchain-openai` dependency is required**.

## Model configuration

Default chat model: `HuggingFaceH4/zephyr-7b-beta` through the Hugging Face Inference API. Set `HF_MODEL` to another chat-capable model supported by your selected provider. For local CPU/GPU inference, the repo includes a Transformers `pipeline` example using a smaller instruction model.

> Hosted inference availability, provider support, quotas, and model access can change. A Hugging Face access token may be required for hosted inference. Never commit `.env` or paste tokens into code.

## Setup

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
copy .env.example .env  # Windows; on macOS/Linux use: cp .env.example .env
```

Add your Hugging Face token to `.env` as `HUGGINGFACEHUB_API_TOKEN=hf_...` if using hosted inference. Then run an example:

```bash
python prompt_template.py
python chat_prompt_template.py
python messages.py
python chatbot.py
streamlit run prompt_ui.py
```

## Files

| File | What it demonstrates |
|---|---|
| `prompt_template.py` | `PromptTemplate` piped into a Hugging Face chat model |
| `chat_prompt_template.py` | System/human `ChatPromptTemplate` messages |
| `messages.py` | Explicit `SystemMessage`, `HumanMessage`, and `AIMessage` |
| `message_placeholder.py` | `MessagesPlaceholder` with typed conversation history |
| `chatbot.py` | Terminal chatbot with in-memory conversation history |
| `temperature.py` | Model configuration and generation settings |
| `prompt_generator.py` | Research-paper prompt template saved as JSON |
| `prompt_ui.py` | Streamlit research-paper explainer UI |
| `local_transformers_chat.py` | Optional local Transformers pipeline (no hosted inference API) |
| `chat_history.txt` | Example serialized conversation transcript (loaded as messages) |
| `template.json` | Reusable prompt data |

## Hosted inference notes

`langchain_huggingface.HuggingFaceEndpoint` uses hosted inference. The model must support text generation and be served by a provider available to your account. If a provider reports that a model is unavailable, choose a currently supported model in your Hugging Face account and set `HF_MODEL` accordingly.

## Local inference notes

`local_transformers_chat.py` downloads model weights the first time and uses your machine's CPU/GPU. It can require several GB of RAM/VRAM. Change `LOCAL_MODEL` to a smaller instruction-tuned model if needed. `google/flan-t5-base` is a lightweight text-to-text fallback, but it is not a chat model.

## Security

- Keep `HUGGINGFACEHUB_API_TOKEN` in `.env` only.
- `.env` is ignored by Git.
- Do not upload model weights or virtual environments.
