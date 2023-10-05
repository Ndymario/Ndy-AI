# Ndy-AI
A proof of concept Discord Bot that can interface with an LLM.

To run the bot, you'll need:
- [Ollama AI](https://ollama.ai) on your machine with the default llama2 LLM
- A Discord bot token in a file named `token.key`
- Run `pip install -r requirements.txt` for the needed Python packages. I would recommend [using a venv](https://docs.python.org/3/library/venv.html)

## Features
Currently, this bot offers:
- `/ask`: Generates a response to a question
- `/search`: Searches DuckDuckGo for its response to a question (much slower than `/ask`!)

Note: Only one user can use the bot at a time as of now.
