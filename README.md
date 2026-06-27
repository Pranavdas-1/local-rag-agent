# Local RAG Agent — Restaurant Review Q&A

A local Retrieval-Augmented Generation (RAG) system that answers natural language 
questions about a pizza restaurant using real customer reviews — no external APIs, 
runs entirely on your machine.

## How It Works

1. Restaurant reviews are loaded from a CSV file and converted into LangChain Documents
2. Each review is embedded using `mxbai-embed-large` via Ollama
3. Embeddings are stored in a persistent ChromaDB vector database
4. User queries are embedded and matched against stored reviews using semantic search
5. The top 5 most relevant reviews are retrieved and passed as context to Llama 3.2
6. Llama 3.2 generates a grounded answer based only on the retrieved context

## Tech Stack

| Component | Tool |
|---|---|
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | mxbai-embed-large (via Ollama) |
| LLM | Llama 3.2 (via Ollama) |
| Data | Pandas |
| Language | Python |

## Project Structure
├── main.py          # CLI loop, prompt chain, LLM inference

├── vector.py        # Embedding, ChromaDB setup, retriever

├── realistic_restaurant_reviews.csv

└── chroma_langchain_db/   # Auto-generated on first run

## Setup

### Prerequisites
- [Ollama](https://ollama.com/) installed and running
- Python 3.9+

### Install dependencies

```bash
pip install langchain langchain-ollama langchain-chroma chromadb pandas
```

### Pull required Ollama models

```bash
ollama pull llama3.2
ollama pull mxbai-embed-large
```

### Run

```bash
python main.py
```

On first run, the vector database is built automatically from the CSV. 
Subsequent runs load the existing database — no re-embedding needed.

## Example
Ask your question: What do people say about the pizza dough?
Customers consistently praised the pizza dough for being well-fermented

and crispy on the outside while remaining chewy inside...

## Key Concepts Demonstrated

- End-to-end RAG pipeline implementation
- Local LLM inference with no external API dependency
- Persistent vector storage with ChromaDB
- Semantic retrieval using cosine similarity
- Prompt design with hallucination guardrails
