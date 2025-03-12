# ai-llm-helloworld
Only Helloworld for LLM

## Terminology

| Term      | What It Is                                                                 |
|-----------|----------------------------------------------------------------------------|
| LLaMA     | Meta's open-source language model family (LLaMA 2, LLaMA 3...)             |
| Ollama    | A local LLM runtime — makes it easy to run models like LLaMA, Mistral, etc.|
| OpenAI    | Cloud-based LLMs like GPT-3.5, GPT-4, Codex. Requires internet + API key.  |
| LangChain | A Python (or JS) framework for building LLM-powered apps (RAG, agents, chatbots, etc.) |
| LangSmith | A dev/debugging platform built by LangChain to trace and visualize LLM calls |

## What is LLM?
LLM stands for Large Language Model, a type of artificial intelligence designed to understand and generate human-like text based on vast amounts of data.

## Python
1. Install Python - [Download Python](https://www.python.org/downloads/)
2. Install OpenAI Python package - `pip install openai`
3. Set API key in environment variable - `export OPENAI_API_KEY=<your_api_key>`
4. Use OpenAI library to call OpenAI APIs

## OpenAI
OpenAI is an AI research and deployment company. Their mission is to ensure that artificial general intelligence benefits all of humanity.

1. Create an account - [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Get API key
3. Set API key based on your settings

## Virtual Environment
1. Create a virtual environment - `python -m venv venv` or `python3 -m venv venv`
2. Activate the virtual environment:
    - On Windows: `venv\Scripts\activate`
    - On macOS/Linux: `source venv/bin/activate`
3. Install the required packages - `pip install -r requirements.txt` or `pip install -r helloworld/python/requirements.txt`
4. Deactivate the virtual environment - `deactivate` if you want to exit
5. Run the Python script - `python helloworld/python/openai-helloworld.py`

## Ollama
Ollama is a platform that provides access to various versions of the Llama language model, including Llama2 and Llama3. 

- It allows users to download, install, and run these models locally or in any environment.
- Ollama simplifies the process of working with large language models by offering easy-to-use commands for pulling and running models, as well as checking available models.
- It supports both terminal-based interactions and API calls, making it versatile for different use cases.

1. Download Llama3 or Llama2 version based on your need. Some of the models are free to use and some are paid. [Llama Downloads](https://www.llama.com/llama-downloads/)
2. Choose as per your need and download the model
3. Install Llama
4. Pull the model - `ollama pull llama3:70b` or `llama3.2` or `llama2.2` or `llama3`
5. Use this command to check the models - `ollama list`
6. Run the model - `ollama run llama3`
7. You can ask in terminal: `What is the capital of India?`

### With curl
```sh
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    {
      "role": "user",
      "content": "What is the capital of India?"
    }
  ],
  "stream": false
}'
```

### With Python
1. Install the required packages - `pip install -r requirements.txt` or `pip install -r helloworld/python/requirements.txt`
2. Run - `python helloworld/python/ollama-helloworld.py`

## Langchain
1. Install the required packages - `pip install -r requirements.txt` or `pip install -r helloworld/python/requirements.txt`
2. Run - `python helloworld/python/langchain-helloworld.py` - this wrapper uses llama3

### Why Langchain
Langchain is a powerful framework designed to simplify the integration of language models into your applications. It provides a seamless interface for managing and orchestrating multiple language models, making it easier to build, deploy, and maintain complex LLM-based systems. With Langchain, you can leverage the strengths of different models, optimize their usage, and create robust, scalable solutions for various natural language processing tasks.

## Langsmith
1. Install the required packages - `pip install -r requirements.txt` or `pip install -r helloworld/python/requirements.txt`
2. Run - `python helloworld/python/langchain-helloworld.py` - this wrapper uses llama3
3. Create a free account - [Langsmith](https://www.langsmith.com/)
4. Get API key
5. Set API key based on your settings

### Why Langsmith
If you have a development background or are familiar with tools like Splunk, Dynatrace, OpenTelemetry, or New Relic, you can understand why Langsmith is important.

### Benefits of Langsmith
Langsmith provides powerful tools for monitoring and debugging your LLM applications. It offers detailed insights into model performance, helps identify bottlenecks, and ensures your applications run smoothly. With Langsmith, you can track usage, manage API keys, and optimize your LLM workflows efficiently.