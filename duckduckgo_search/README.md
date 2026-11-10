# Ollama + duckduckgo Search Integration

Tested example :  
[GitHub](https://github.com/alby13/ollama-internet-search-tool/blob/main/ddgsearch.py)

Single-script Python demo: web search results (via the `ddgs` package) fed
as system context to a local Ollama chat model (`gemma3`) 4.9GB, with the AI
response to the terminal.

## Running

- Use the repo-local venv (Python 3.12).
- No requirements file exists — the venv is the source of truth for deps.
  Recreate: `python3 -m venv venv && ./venv/bin/pip install ddgs ollama`

## Prerequisites

- A local Ollama server must be running with the model pulled:
  `ollama serve` + `ollama pull gemma3:latest` (model name is hardcoded in main.py).


---
