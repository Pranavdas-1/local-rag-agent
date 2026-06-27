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
