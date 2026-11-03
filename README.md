<!--
  LANGCHAIN LEARNING LAB
  A practical, evolving learning workspace for LangChain and LLM application engineering.
-->

<div align="center">

# 🧠 LangChain Learning Lab

### From language models to real-world LLM applications — one experiment at a time.

<p>
  <a href="https://github.com/Maganpreet-Singh/langchain-learning-lab">
    <img src="https://img.shields.io/badge/Repository-LangChain%20Learning%20Lab-1f6feb?style=for-the-badge&logo=github&logoColor=white" alt="Repository">
  </a>
  <img src="https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Framework-LangChain-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/Focus-LLM%20Engineering-8A2BE2?style=for-the-badge" alt="LLM Engineering">
  <img src="https://img.shields.io/badge/Status-Learning%20in%20Progress-orange?style=for-the-badge" alt="Learning in progress">
</p>

<p><em>A hands-on, code-first repository for understanding how modern language-model applications are built, connected, evaluated, and improved.</em></p>

[Explore the repository](https://github.com/Maganpreet-Singh/langchain-learning-lab) · [Report an issue](https://github.com/Maganpreet-Singh/langchain-learning-lab/issues) · [View the learning roadmap](#-learning-roadmap)

</div>

---

## 📌 Table of Contents

- [🌟 About the Project](#-about-the-project)
- [🎯 Learning Objectives](#-learning-objectives)
- [🧰 Technology Stack](#-technology-stack)
- [🗂️ Repository Structure](#️-repository-structure)
- [🚀 Getting Started](#-getting-started)
- [🔐 API Key Configuration](#-api-key-configuration)
- [▶️ Running the Examples](#️-running-the-examples)
- [📚 Learning Modules](#-learning-modules)
  - [1. LLMs](#1-large-language-models)
  - [2. Chat Models](#2-chat-models)
  - [3. Embedding Models](#3-embedding-models)
- [🧠 Core Concepts](#-core-concepts)
- [🧪 Practice and Experimentation](#-practice-and-experimentation)
- [🛠️ Troubleshooting](#️-troubleshooting)
- [🔒 Security and Responsible Usage](#-security-and-responsible-usage)
- [🗺️ Learning Roadmap](#️-learning-roadmap)
- [📈 Project Development Plan](#-project-development-plan)
- [🤝 Contributing](#-contributing)
- [📖 Useful Resources](#-useful-resources)
- [❓ Frequently Asked Questions](#-frequently-asked-questions)
- [👨‍💻 Author](#-author)
- [📄 License](#-license)

---

## 🌟 About the Project

**LangChain Learning Lab** is a practical Python learning repository focused on the building blocks of applications powered by large language models (LLMs).

The goal is to move beyond simply calling a model API. This repository is intended to help learners understand the components behind an LLM application:

- How a language model receives a prompt and generates a response.
- How chat models work with conversational messages.
- How to connect different model providers through consistent interfaces.
- How to generate numerical vector representations of text.
- How to compare documents by semantic similarity.
- How to run selected Hugging Face models locally instead of relying on a hosted API.
- How to organize experiments into reusable, understandable Python scripts.

The repository begins with model integrations and embedding fundamentals. It is designed to grow into a structured learning lab covering prompt engineering, chains, retrieval-augmented generation (RAG), vector databases, tools, agents, evaluation, and deployment as those modules are implemented.

> **Project philosophy:** Learn the primitive, understand the abstraction, inspect the output, and only then build a larger system.

### Why this repository?

LangChain provides abstractions for working with language models and connecting them to other software components. Those abstractions are powerful, but they are easier to use well when their underlying behavior is understood.

This lab emphasizes:

1. **First principles** — understand inputs, outputs, model calls, tokens, vectors, and similarity.
2. **Practical code** — each concept should lead to an experiment that can be executed.
3. **Provider awareness** — compare hosted APIs and local open-source models.
4. **Reproducibility** — use a virtual environment, dependency file, and environment variables.
5. **Incremental engineering** — build from small scripts toward complete AI applications.

---

## 🎯 Learning Objectives

By working through this repository, the learner should develop the ability to:

| Area | Learning outcome |
|---|---|
| Python environment | Create and manage an isolated Python environment |
| LangChain fundamentals | Understand model integrations and the LangChain package ecosystem |
| LLMs | Invoke completion-style language models |
| Chat models | Send instructions and messages to conversational model interfaces |
| Provider integrations | Connect OpenAI, Anthropic, Google Gemini, and Hugging Face examples |
| Local inference | Load a compatible Hugging Face model on a local machine |
| Embeddings | Convert text into numerical vector representations |
| Document embeddings | Encode multiple text documents |
| Similarity search | Rank text documents using cosine similarity |
| Debugging | Diagnose dependency, interpreter, credential, and model-access errors |
| Engineering habits | Keep secrets out of source code and document experiments clearly |

### Expected prerequisites

You do not need to be an expert in machine learning to start. Familiarity with the following will make the examples easier:

- Python variables, functions, imports, and lists.
- Installing packages with `pip`.
- Running Python scripts from a terminal.
- Basic ideas about APIs and JSON.
- Basic linear algebra concepts are useful for understanding embeddings and cosine similarity.

---

## 🧰 Technology Stack

The repository uses a Python-based stack. Exact installed versions are resolved by the package installer when dependencies are installed; this repository does not claim that every provider or model identifier will remain available forever.

| Technology | Role in this repository |
|---|---|
| Python | Main programming language |
| LangChain | Common interfaces and application framework |
| LangChain Core | Shared message, prompt, and runnable abstractions |
| langchain-openai | OpenAI model and embedding integration |
| langchain-anthropic | Anthropic chat model integration |
| langchain-google-genai | Google Gemini integration |
| langchain-huggingface | Hugging Face model and embedding integration |
| Hugging Face Hub | Model repositories and hosted inference access |
| Transformers | Model and pipeline support |
| Sentence Transformers | Local sentence embedding models |
| NumPy | Numerical computing foundation |
| scikit-learn | Cosine similarity calculation |
| python-dotenv | Load local environment variables from a `.env` file |

### Supported learning environments

- Windows 10 / Windows 11
- macOS
- Linux
- Visual Studio Code
- Other Python IDEs and editors

**Recommended Python version:** Python 3.11 or 3.12 for a straightforward compatibility baseline with common machine-learning packages. Always check the compatibility of the specific packages and model backend you install.

---

## 🗂️ Repository Structure

The repository is organized by learning topic. The following layout represents the current model-and-embedding examples and the setup files maintained for this learning track.

```text
langchain-learning-lab/
│
├── 1.LLMs/
│   └── 1_llm_demo.py
│
├── 2.ChatModels/
│   ├── 1_chatmodel_openai.py
│   ├── 2_chatmodel_anthropic.py
│   ├── 3_chatmodel_google.py
│   ├── 4_chatmodel_hf_api.py
│   └── 5_chatmodel_hf_local.py
│
├── 3.EmbeddingModels/
│   ├── 1_embedding_openai_query.py
│   ├── 2_embedding_openai_docs.py
│   ├── 3_embedding_hf_local.py
│   └── 4_document_similarity.py
│
├── .env.example
├── .gitignore
├── requirements.txt
├── test.py
└── README.md
```

> The directory list above documents the intended learning-track layout. A file is runnable only after it exists in the checked-out branch. New sections will be added as their implementations are committed.

### Naming convention

The numeric prefixes indicate a suggested study order, not a package version or execution requirement. Run each script individually from the repository root.

---

## 🚀 Getting Started

Follow these steps to set up the project locally.

### 1. Install Python

Install Python 3.11 or 3.12 from the official Python downloads page:

https://www.python.org/downloads/

During installation on Windows, enable the option to add Python to PATH when available.

Verify the installation:

```powershell
python --version
py --version
```

If multiple versions are installed, you can check the Python launcher:

```powershell
py -0p
```

### 2. Clone the repository

Open PowerShell, Windows Terminal, or the VS Code terminal:

```bash
git clone https://github.com/Maganpreet-Singh/langchain-learning-lab.git
cd langchain-learning-lab
```

### 3. Create a virtual environment

A virtual environment isolates this project's packages from other Python projects.

**Windows PowerShell:**

```powershell
py -3.12 -m venv .venv
`.\.venv\Scripts\Activate.ps1`
```

If PowerShell blocks script activation in the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

**Windows Command Prompt:**

```bat
py -3.12 -m venv .venv
.venv\Scripts\activate.bat
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

When active, the environment name (usually `.venv`) appears at the start of the terminal prompt.

### 4. Upgrade pip

```bash
python -m pip install --upgrade pip
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

For a local Hugging Face embedding workflow, make sure the Hugging Face integration and Sentence Transformers are installed:

```bash
python -m pip install -U langchain-huggingface sentence-transformers
```

For local text-generation pipelines, PyTorch may also be needed by the selected Transformers backend. Install a PyTorch build appropriate for your operating system and hardware from:

https://pytorch.org/get-started/locally/

### 6. Open in VS Code

From the project directory:

```bash
code .
```

In VS Code:

1. Open the Command Palette with `Ctrl + Shift + P`.
2. Search for **Python: Select Interpreter**.
3. Select the interpreter inside this project's `.venv` directory.
4. Open a new integrated terminal.
5. Confirm that the terminal is using the same environment.

Check the selected interpreter:

```bash
python -c "import sys; print(sys.executable)"
```

### 7. Verify installation

```bash
python test.py
```

If this command prints a LangChain version, the basic LangChain import is working.

---

## 🔐 API Key Configuration

Some examples call hosted model providers. These providers generally require an account, an API key, and billing or usage access according to their own terms.

### 1. Create a local environment file

Copy `.env.example` to a new file named `.env` in the repository root.

**PowerShell:**

```powershell
Copy-Item .env.example .env
```

**Command Prompt:**

```bat
copy .env.example .env
```

**macOS / Linux:**

```bash
cp .env.example .env
```

### 2. Add the keys you actually use

Open `.env` and fill in the relevant values:

```dotenv
OPENAI_API_KEY=your_openai_api_key
ANTHROPIC_API_KEY=your_anthropic_api_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token
```

These are placeholders. Replace them with valid credentials from the corresponding provider. Do not include quotation marks unless the value requires them.

### 3. Provider key reference

| Provider | Environment variable | Official site |
|---|---|---|
| OpenAI | `OPENAI_API_KEY` | https://platform.openai.com/ |
| Anthropic | `ANTHROPIC_API_KEY` | https://console.anthropic.com/ |
| Google AI | `GOOGLE_API_KEY` | https://aistudio.google.com/ |
| Hugging Face | `HUGGINGFACEHUB_API_TOKEN` | https://huggingface.co/settings/tokens |

### 4. Which examples need credentials?

| Example | Credential requirement |
|---|---|
| `1.LLMs/1_llm_demo.py` | OpenAI API key |
| `2.ChatModels/1_chatmodel_openai.py` | OpenAI API key |
| `2.ChatModels/2_chatmodel_anthropic.py` | Anthropic API key |
| `2.ChatModels/3_chatmodel_google.py` | Google API key |
| `2.ChatModels/4_chatmodel_hf_api.py` | Hugging Face token and eligible hosted inference access |
| `2.ChatModels/5_chatmodel_hf_local.py` | No provider API key; local model download required |
| `3.EmbeddingModels/1_embedding_openai_query.py` | OpenAI API key |
| `3.EmbeddingModels/2_embedding_openai_docs.py` | OpenAI API key |
| `3.EmbeddingModels/3_embedding_hf_local.py` | No provider API key; model download required |
| `3.EmbeddingModels/4_document_similarity.py` | No provider API key; model download required |

**Important:** No API key does not mean no cost or no resource usage in every situation. Local inference uses your own hardware, electricity, RAM, disk space, and download bandwidth. Hosted API calls may incur provider charges.

---

## ▶️ Running the Examples

Run commands from the **repository root**, with the virtual environment active.

### Check LangChain

```bash
python test.py
```

### Run the LLM example

```bash
python 1.LLMs/1_llm_demo.py
```

### Run chat model examples

```bash
python 2.ChatModels/1_chatmodel_openai.py
python 2.ChatModels/2_chatmodel_anthropic.py
python 2.ChatModels/3_chatmodel_google.py
python 2.ChatModels/4_chatmodel_hf_api.py
python 2.ChatModels/5_chatmodel_hf_local.py
```

Only run a hosted provider example after setting its matching API key and confirming that the model is available to your account.

### Run embedding examples

```bash
python 3.EmbeddingModels/1_embedding_openai_query.py
python 3.EmbeddingModels/2_embedding_openai_docs.py
python 3.EmbeddingModels/3_embedding_hf_local.py
python 3.EmbeddingModels/4_document_similarity.py
```

### Recommended first run

For a low-friction introduction that does not require a paid model API:

```bash
python 3.EmbeddingModels/3_embedding_hf_local.py
python 3.EmbeddingModels/4_document_similarity.py
```

The first run may download the embedding model. Later runs can reuse the local model cache.

---

## 📚 Learning Modules

The current learning track begins with three essential areas: language models, chat models, and embedding models.

## 1. Large Language Models

**Folder:** `1.LLMs/`

Large Language Models are machine-learning models trained to process and generate natural language. An LLM receives a sequence of input tokens and generates an output sequence based on the model's learned parameters and the supplied context.

### What to understand

- What an LLM is and what it is not.
- The difference between text completion and conversational interfaces.
- How prompts influence generated results.
- Tokens, context windows, and output limits.
- Model identifiers and provider-specific capabilities.
- Latency, rate limits, reliability, and cost.
- Why generated responses should be validated rather than blindly trusted.

### Example: basic LLM invocation

The basic workflow is:

```python
from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=100)
response = llm.invoke("What is the capital of India?")

print(response)
```

### Execution flow

```text
Python script
     |
     v
Load environment variables
     |
     v
Initialize provider integration
     |
     v
Create a prompt
     |
     v
Send request to the model provider
     |
     v
Receive generated text
     |
     v
Inspect and print the response
```

### Experiments to try

1. Ask the model the same question in multiple ways.
2. Compare a factual question with an open-ended creative prompt.
3. Change the output token limit.
4. Ask for structured output and inspect whether the response follows the format.
5. Compare response length, latency, and quality across available models.

**Learning checkpoint:** You should be able to explain the model invocation lifecycle and identify which parts of the workflow depend on the provider.

## 2. Chat Models

**Folder:** `2.ChatModels/`

Chat models use conversational message structures. Rather than treating every input as an isolated string completion, the interface is designed around roles and messages, such as system instructions, user messages, and assistant responses.

### What to understand

- Chat message roles.
- System instructions and user prompts.
- Conversation history and context.
- Temperature and output token controls.
- Provider-specific model names and options.
- Differences between hosted inference and local inference.
- Why a model's behavior can vary across providers.

### Provider examples

| File | Integration | What it demonstrates |
|---|---|---|
| `1_chatmodel_openai.py` | OpenAI | Calling an OpenAI chat model |
| `2_chatmodel_anthropic.py` | Anthropic | Calling a Claude chat model |
| `3_chatmodel_google.py` | Google Gemini | Calling a Gemini model |
| `4_chatmodel_hf_api.py` | Hugging Face hosted inference | Using a hosted Hugging Face endpoint |
| `5_chatmodel_hf_local.py` | Hugging Face local pipeline | Running a model on local hardware |

### Example: chat model invocation

```python
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    max_tokens=100
)

response = model.invoke("Write a five-line poem about cricket.")
print(response.content)
```

### Understanding the response

A chat model invocation commonly returns an AI message object. The generated text is available through:

```python
response.content
```

The message object can contain additional metadata, depending on the integration and provider.

### Hosted inference vs. local inference

| Hosted inference | Local inference |
|---|---|
| Request is sent to an external provider | Model executes on your machine |
| Usually needs an API key or account | Usually downloads model weights |
| Provider operates the model infrastructure | You manage local compute and dependencies |
| May have per-request charges | Uses local hardware resources |
| Model availability depends on provider | Model compatibility depends on local setup |

### Local model considerations

A local model is not automatically lightweight. Model size, quantization, sequence length, hardware acceleration, and framework support all affect performance.

Before downloading a model, consider:

- Available RAM and GPU memory.
- Disk space for model weights and caches.
- Whether the model supports your intended task.
- Whether the license permits your intended use.
- Whether your installed PyTorch and Transformers versions are compatible.

**Learning checkpoint:** You should be able to invoke at least one chat model and explain the difference between remote and local inference.

## 3. Embedding Models

**Folder:** `3.EmbeddingModels/`

An embedding model maps text into a numerical vector. These vectors are designed to represent useful properties of the input, often including semantic relationships.

Embeddings are a foundation for semantic search, clustering, recommendation, deduplication, and retrieval-augmented generation.

### What to understand

- What a vector embedding represents.
- How text is transformed into a numerical vector.
- Query embeddings vs. document embeddings.
- Embedding dimensions.
- Similarity and distance measures.
- Why documents and queries in a retrieval system should use compatible embedding spaces.
- How normalization and preprocessing influence similarity results.

### 3.1 Query embedding

A query embedding represents a single input text.

```python
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")
vector = embedding.embed_query("Delhi is the capital of India")

print("Dimensions:", len(vector))
print(vector)
```

The result is a vector of floating-point values. Its dimensionality is determined by the selected model and configuration.

### 3.2 Document embeddings

A document embedding workflow transforms multiple text inputs into vectors.

```python
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-small")

documents = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France."
]

vectors = embedding.embed_documents(documents)

print("Documents:", len(vectors))
print("Dimensions:", len(vectors[0]))
```

### 3.3 Local Hugging Face embeddings

Local sentence embedding models make it possible to experiment without sending every text input to a hosted embedding API.

```python
from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

documents = [
    "Delhi is the capital of India.",
    "Kolkata is the capital of West Bengal.",
    "Paris is the capital of France."
]

vectors = embedding.embed_documents(documents)

print("Documents:", len(vectors))
print("Dimensions:", len(vectors[0]))
```

The first execution downloads model files from Hugging Face if they are not already cached.

### 3.4 Document similarity

Semantic similarity compares vector representations rather than relying only on exact keyword matches.

This learning example uses cosine similarity to compare a query vector against document vectors.

```python
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"device": "cpu"},
    encode_kwargs={"normalize_embeddings": True}
)

documents = [
    "Virat Kohli is an Indian cricketer known for aggressive batting.",
    "MS Dhoni is a former Indian captain famous for calm leadership.",
    "Sachin Tendulkar is a legendary Indian batter.",
    "Rohit Sharma is known for elegant batting.",
    "Jasprit Bumrah is an Indian fast bowler known for yorkers."
]

query = "Tell me about Bumrah"

document_vectors = embedding.embed_documents(documents)
query_vector = embedding.embed_query(query)

scores = cosine_similarity([query_vector], document_vectors)[0]
best_index = scores.argmax()

print("Query:", query)
print("Best match:", documents[best_index])
print("Similarity:", float(scores[best_index]))
```

### Cosine similarity intuition

For vectors (A) and (B), cosine similarity is:

[
\operatorname{cosine\_similarity}(A,B)
=
\frac{A\cdot B}{\|A\|\,\|B\|}
]

It measures the cosine of the angle between two non-zero vectors. In many embedding applications, a higher score suggests greater similarity, but the score should not be treated as a universal probability or confidence measure.

### Important embedding design considerations

- Use the same embedding model for queries and indexed documents, unless the model explicitly supports a paired query/document design.
- Preserve a mapping between every vector and its original document.
- Chunk long documents thoughtfully before embedding.
- Keep track of model name and version when building a persistent index.
- Consider metadata filters in addition to vector similarity.
- Evaluate retrieval with representative questions, not only a few convenient examples.

**Learning checkpoint:** You should be able to generate vectors, explain their dimensions, and retrieve the closest document using a similarity measure.

---

## 🧠 Core Concepts

This section is a conceptual reference for the ideas that connect the examples.

### 1. LLM

A large language model predicts or generates token sequences based on its training and the context provided at inference time.

It can be useful for summarization, transformation, question answering, drafting, classification, and many other language tasks. It can also make errors, invent details, or fail to follow constraints.

### 2. Tokens

Tokens are the units processed by a language model. A token may represent a whole word, part of a word, punctuation, or another text fragment.

Input and output limits are usually expressed in tokens, not characters or words.

### 3. Prompt

A prompt is the input context supplied to a model. It can include instructions, examples, user content, and formatting constraints.

A good prompt should clearly specify the task, relevant context, expected output, and restrictions.

### 4. Chat messages

Chat interfaces commonly represent input as a sequence of messages with roles. Roles help distinguish instructions, user requests, and model responses.

### 5. Embedding

An embedding is a numerical representation of an input. Similarity between embedding vectors can be used to identify semantically related content.

### 6. Vector similarity

Similarity metrics compare vectors. Cosine similarity is a common choice for text embeddings, but retrieval quality depends on the model, data, chunking, and evaluation process.

### 7. Inference

Inference is the process of using a trained model to generate a result for a new input. Inference can happen remotely through an API or locally on a machine.

### 8. Context window

A context window is the amount of token context a model can process for a request. The exact limit varies by model and can change over time.

### 9. Temperature

Temperature influences the sampling behavior of models that support it. Lower settings generally produce more focused or less varied outputs; higher settings generally increase variation. It is not a direct accuracy control.

### 10. RAG

Retrieval-Augmented Generation combines retrieval from an external knowledge source with a language model's generation process.

A typical pipeline is:

```text
Knowledge sources
      |
      v
Document loading
      |
      v
Text splitting / chunking
      |
      v
Embedding generation
      |
      v
Vector index
      |
      v
User query --> Query embedding
      |               |
      +-------> Retrieval
                      |
                      v
              Context selection
                      |
                      v
                LLM prompt
                      |
                      v
                Generated answer
```

RAG is a future learning area for this repository; the diagram explains the concept and does not imply that a complete RAG implementation is already included.

---

## 🧪 Practice and Experimentation

Reading code is only the beginning. The most useful learning happens when you change inputs, observe outputs, and record what happened.

### Beginner exercises

| # | Exercise | What to observe |
|---:|---|---|
| 1 | Change the LLM question | How prompt wording changes output |
| 2 | Try a summarization task | Whether important details are retained |
| 3 | Change chat temperature | Variation in generated responses |
| 4 | Compare two available providers | Differences in format, behavior, and latency |
| 5 | Print the chat response object | Message content and metadata |
| 6 | Generate a query embedding | Vector length and numeric values |
| 7 | Embed five related documents | Consistency of vector dimensions |
| 8 | Change the semantic search query | Which document ranks first |
| 9 | Add an unrelated document | How retrieval ranking changes |
| 10 | Compare local and hosted embeddings | Differences in results and resource use |

### Intermediate exercises

1. Create a list of ten documents on one topic and build a simple semantic search function.
2. Return the top three documents instead of only the best match.
3. Add source IDs and metadata to each document.
4. Compare cosine similarity with another appropriate distance metric.
5. Test multiple queries that mean similar things but use different words.
6. Test ambiguous queries and note where retrieval becomes unreliable.
7. Add error handling for missing environment variables.
8. Record latency and model details for repeatable comparisons.
9. Separate model initialization from the main application logic.
10. Write small tests for text preprocessing and similarity ranking.

### Suggested experiment log

For every experiment, record:

| Field | Example |
|---|---|
| Experiment ID | EMB-001 |
| Date | YYYY-MM-DD |
| Concept | Local sentence embeddings |
| Model | all-MiniLM-L6-v2 |
| Input | Example query |
| Expected behavior | Semantically related document ranks highly |
| Actual behavior | Observed result |
| Notes | What changed and why |
| Next step | Test more queries |

A small experiment log makes it easier to understand why a model behaves differently after code, data, or dependency changes.

---

## 🛠️ Troubleshooting

Python ML environments can fail for reasons unrelated to the code itself. Start by checking the interpreter and package environment before changing the script.

### 1. ModuleNotFoundError: No module named 'langchain_huggingface'

The import uses an underscore, but the package is installed with a hyphen.

Install it using:

```bash
python -m pip install -U langchain-huggingface
```

For local sentence embeddings, also install:

```bash
python -m pip install -U sentence-transformers
```

Verify:

```bash
python -c "from langchain_huggingface import HuggingFaceEmbeddings; print('Import successful')"
```

### 2. Package installed, but Python still cannot import it

This commonly happens when VS Code uses a different Python interpreter from the one where the package was installed.

Check the interpreter:

```bash
python -c "import sys; print(sys.executable)"
python -m pip --version
```

Check the package:

```bash
python -m pip show langchain-huggingface
```

Select the correct `.venv` interpreter in VS Code and open a new terminal.

### 3. Missing API key

Check that:

- A `.env` file exists in the repository root.
- The environment variable name is spelled correctly.
- The key is valid and enabled at the provider.
- The script is executed from the repository root.
- `load_dotenv()` is called before initializing the provider client.

Never paste an API key into an issue, commit, notebook output, or public chat.

### 4. Hugging Face model download fails

Possible causes include:

- Network connection problems.
- Hugging Face rate limits.
- A private or gated model requiring access approval.
- A model repository that has moved or changed availability.
- Insufficient local disk space.
- An interrupted download or cache problem.

Check that the model repository is accessible in a browser and retry after resolving the underlying issue.

### 5. Local inference is slow

Local generation can be slow on CPU, especially for larger models.

Possible improvements:

- Use a smaller model.
- Reduce `max_new_tokens`.
- Use an appropriate GPU-enabled backend where available.
- Close resource-intensive applications.
- Consider a compatible quantized model and runtime.
- Start with embeddings before attempting larger local generation models.

### 6. PyTorch or Transformers installation conflict

Create a fresh environment rather than repeatedly changing a broken one.

```powershell
deactivate
py -3.12 -m venv .venv-clean
.\.venv-clean\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install a compatible PyTorch build from the official installation selector if required.

### 7. Provider model not found or not available

Model names, endpoints, account permissions, and provider catalogs change. A script can be structurally correct while the selected model identifier is no longer available to the account.

Check the provider's current model documentation and use a model enabled for your account. Avoid assuming that a model name in an older tutorial will remain available indefinitely.

### 8. Environment activation is blocked in PowerShell

For the current PowerShell process only:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt activation.

### 9. Dependency resolver reports conflicts

First check the active interpreter and installed versions:

```bash
python --version
python -m pip list
python -m pip check
```

Prefer a fresh environment and a compatible set of package versions. For a reproducible production project, pin tested dependency versions rather than relying indefinitely on unbounded latest-version installs.

---

## 🔒 Security and Responsible Usage

This repository is intended for learning and experimentation. Safe handling of credentials and data is essential.

### Protect API credentials

- Never commit `.env`.
- Never hardcode secrets in Python scripts.
- Use `.env.example` only for variable names and placeholder values.
- Rotate a key immediately if it is accidentally exposed.
- Use separate credentials for development and production.
- Apply provider-side usage and spending limits when available.

### Protect user data

Before sending data to an external model provider:

- Understand the provider's data handling and retention policies.
- Avoid uploading personal, confidential, regulated, or proprietary information without authorization.
- Remove unnecessary identifiers from test data.
- Do not assume that an API request is private merely because it is sent through code.

### Use AI outputs responsibly

- Verify important factual claims.
- Treat model output as generated content, not guaranteed truth.
- Validate structured output before using it in another system.
- Test for prompt injection and unsafe tool use before building agent workflows.
- Respect model licenses, dataset licenses, and provider terms.
- Clearly disclose AI-generated content where appropriate.

---

## 🗺️ Learning Roadmap

This roadmap describes a suggested progression for extending the current model-and-embedding foundations into broader LLM engineering.

| Stage | Topic | Key outcome | Status |
|---:|---|---|---|
| 1 | Environment and LangChain setup | Reproducible local Python setup | Starter material |
| 2 | LLM integrations | Invoke language models | Examples included |
| 3 | Chat model integrations | Work with conversational interfaces | Examples included |
| 4 | Embedding models | Generate and inspect vectors | Examples included |
| 5 | Similarity search | Rank documents semantically | Example included |
| 6 | Prompt engineering | Design and evaluate prompts | Planned |
| 7 | Prompt templates and parsers | Build reusable prompt workflows | Planned |
| 8 | Chains and runnables | Compose multi-step model workflows | Planned |
| 9 | Document loaders and splitters | Ingest and chunk external content | Planned |
| 10 | Vector databases | Store and retrieve embeddings | Planned |
| 11 | Retrieval-Augmented Generation | Ground model responses in retrieved data | Planned |
| 12 | Tools and function calling | Connect models with controlled functions | Planned |
| 13 | Agents | Explore model-directed workflows | Planned |
| 14 | Memory and conversation state | Manage conversational context | Planned |
| 15 | Evaluation and testing | Measure quality and reliability | Planned |
| 16 | API development | Expose model workflows through services | Planned |
| 17 | Deployment and monitoring | Operate an AI application responsibly | Planned |

### Suggested order of study

**Foundation:** Python environment → LangChain packages → LLM invocation → chat models.

**Representation:** Query embeddings → document embeddings → local embeddings → similarity search.

**Application building:** Prompt templates → structured output → chains → document ingestion.

**Knowledge systems:** Vector stores → retrievers → RAG → retrieval evaluation.

**Advanced workflows:** Tools → function calling → agents → orchestration.

**Engineering:** Testing → API development → deployment → monitoring → security.

This is a learning plan, not a claim that all stages have already been implemented in this repository.

---

## 📈 Project Development Plan

The long-term direction is to evolve this repository from a collection of short scripts into a practical, well-documented LLM engineering portfolio.

### Planned engineering improvements

| Area | Planned improvement |
|---|---|
| Project organization | Consistent module structure and naming |
| Dependencies | Tested version constraints and optional dependency groups |
| Configuration | Centralized environment and settings management |
| Logging | Useful logs without leaking secrets |
| Error handling | Clear messages for API, model, and input failures |
| Testing | Unit tests for deterministic helper functions |
| Documentation | Setup instructions and runnable examples per module |
| Evaluation | Small, repeatable test datasets and quality measurements |
| Applications | A collection of progressively more complete LLM applications |
| Deployment | Documented local and hosted deployment patterns |

### Potential future projects

These are possible directions, not currently claimed as completed features.

1. **Semantic Document Search** — search a local collection of notes using embeddings.
2. **PDF Knowledge Assistant** — retrieve relevant passages from uploaded documents.
3. **RAG Question Answering** — generate answers grounded in retrieved source chunks.
4. **Research Paper Assistant** — organize and query technical papers.
5. **Multi-Provider Model Playground** — compare provider responses and performance.
6. **Structured Information Extractor** — convert unstructured text into validated schemas.
7. **Tool-Calling Assistant** — allow a model to use a controlled set of functions.
8. **LLM Evaluation Workbench** — compare outputs across prompts and models.

### Quality principles

As the project grows, each new example should aim to be:

- Runnable from a documented environment.
- Focused on one principal concept.
- Clear about API keys and external services.
- Safe with credentials and user data.
- Reproducible where practical.
- Accompanied by expected behavior and troubleshooting guidance.

---

## 🤝 Contributing

Learning repositories improve when experiments are shared, reviewed, and refined.

Contributions, corrections, and suggestions are welcome.

### Contribution ideas

- Correct an outdated API or model identifier.
- Add a provider integration with clear setup instructions.
- Improve error handling.
- Add a small experiment around embeddings or retrieval.
- Add tests for helper functions.
- Improve documentation or explain a confusing concept.
- Add a new learning module with a focused example.

### Suggested contribution workflow

1. Fork the repository.
2. Create a feature branch.
3. Make a focused change.
4. Run the affected example or tests.
5. Update the documentation.
6. Open a pull request explaining the change.

Example:

```bash
git checkout -b feature/add-new-example
git add .
git commit -m "Add a focused LangChain example"
git push origin feature/add-new-example
```

Then open a pull request on GitHub.

### Contribution guidelines

- Keep examples small and readable.
- Do not commit API keys, private data, or local model files.
- Mention external requirements clearly.
- Include installation instructions for any new dependency.
- Avoid claiming an example has been tested on environments where it has not been tested.
- Keep changes relevant to the learning objective.

---

## 📖 Useful Resources

The following official documentation and learning resources are useful references. Provider APIs and library interfaces evolve, so consult current documentation when code examples behave differently.

### LangChain

- [LangChain documentation](https://python.langchain.com/docs/introduction/)
- [LangChain Python API reference](https://python.langchain.com/api_reference/)
- [LangChain integrations](https://python.langchain.com/docs/integrations/)
- [LangChain tutorials](https://python.langchain.com/docs/tutorials/)

### Model providers

- [OpenAI API documentation](https://platform.openai.com/docs/)
- [Anthropic documentation](https://docs.anthropic.com/)
- [Google AI for Developers](https://ai.google.dev/gemini-api/docs)
- [Hugging Face documentation](https://huggingface.co/docs)
- [Hugging Face Hub](https://huggingface.co/models)

### Embeddings and machine learning

- [Sentence Transformers documentation](https://www.sbert.net/)
- [scikit-learn documentation](https://scikit-learn.org/stable/)
- [NumPy documentation](https://numpy.org/doc/)
- [PyTorch documentation](https://pytorch.org/docs/stable/index.html)

### Developer tools

- [Python documentation](https://docs.python.org/3/)
- [Python virtual environments](https://docs.python.org/3/library/venv.html)
- [pip documentation](https://pip.pypa.io/en/stable/)
- [Git documentation](https://git-scm.com/doc)
- [Visual Studio Code Python guide](https://code.visualstudio.com/docs/python/python-tutorial)

---

## ❓ Frequently Asked Questions

<details>
<summary><strong>1. Is this repository suitable for beginners?</strong></summary>

Yes. The first modules focus on model invocation, chat interfaces, and embeddings. Basic Python knowledge and comfort with a terminal are recommended.
</details>

<details>
<summary><strong>2. Do I need an OpenAI API key to study LangChain?</strong></summary>

No. The local Hugging Face embedding examples and local chat-model example are designed to run without an OpenAI key. They still require local dependencies and model downloads.
</details>

<details>
<summary><strong>3. Can I run the examples on CPU?</strong></summary>

The embedding examples can be configured for CPU execution. Local text generation may be slow depending on the model size and available hardware.
</details>

<details>
<summary><strong>4. Why does Python use an underscore in the import name while pip uses a hyphen?</strong></summary>

Python import names and distribution package names follow different naming conventions. For example, install `langchain-huggingface` and import from `langchain_huggingface`.
</details>

<details>
<summary><strong>5. Why does the first Hugging Face run take longer?</strong></summary>

The model files may need to be downloaded and cached locally. Download time depends on model size and network speed. Later runs can reuse the cache.
</details>

<details>
<summary><strong>6. Does a higher cosine similarity score guarantee a correct answer?</strong></summary>

No. Similarity is a ranking signal, not a factual correctness score. Retrieval results should be evaluated against representative queries and source material.
</details>

<details>
<summary><strong>7. Are all model names permanent?</strong></summary>

No. Provider model catalogs, access requirements, and endpoint behavior can change. Always check the current provider documentation and account permissions.
</details>

<details>
<summary><strong>8. Does this repository already include a full RAG application?</strong></summary>

The current introductory track documents LLMs, chat models, embeddings, and semantic similarity. RAG is included in the roadmap as a future extension, not represented as an already completed implementation.
</details>

<details>
<summary><strong>9. How should I report an error?</strong></summary>

Open a GitHub issue and include the relevant script, Python version, operating system, package information, full error traceback, and steps to reproduce. Remove API keys and private information before posting.
</details>

<details>
<summary><strong>10. Can I use this repository for portfolio learning?</strong></summary>

Yes. Use it as a record of experiments and concepts you genuinely understand. For a portfolio, add your own projects, tests, explanations, and evaluation results rather than presenting planned modules as completed work.
</details>

---

## 👨‍💻 Author

<div align="center">

### Maganpreet Singh

**Computer Science & Engineering Student | AI/ML & LLM Engineering Learner**

Interested in building practical applications with Python, machine learning, deep learning, and modern language-model tools.

<p>
  <a href="https://github.com/Maganpreet-Singh">
    <img src="https://img.shields.io/badge/GitHub-Maganpreet--Singh-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub profile">
  </a>
</p>

</div>

This repository is part of an ongoing learning journey. The objective is simple: understand the fundamentals deeply, build useful systems, and improve the engineering behind them with every iteration.

---

## 📄 License

No license has been specified for this repository in this README. Before reusing, distributing, or modifying the repository's code, check whether a license file is present and review the applicable terms. If you intend to make the project open source, add an explicit license that reflects your choice.

---

<div align="center">

### ⭐ Learn. Build. Test. Improve. Repeat.

*The best way to understand an AI system is to build one, inspect its behavior, and keep asking better questions.*

[⬆ Back to Top](#-langchain-learning-lab)

</div>
