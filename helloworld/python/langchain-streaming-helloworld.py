# Install dependencies if not already
# pip install langchain ollama

from langchain_community.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

# 1. Load the model using Ollama
# THIS LINE CAN BE REPLEACE with different AI models...
########################################################################################################
llm = Ollama(model="llama3", callbacks=CallbackManager([StreamingStdOutCallbackHandler()]))
# 1. llm = OpenAI(model_name="...", openai_api_key=API_KEY)
# 2. llm = HuggingFaceHub(repo_id = "..."", huggingfacehub_api_token = API_KEY)
########################################################################################################
# Replace with 'llama3' once available via ollama pull llama3

# Example prompt
prompt = "What is Langchain streaming in 2 lines?"# Run the LLM
response = llm.invoke(prompt)
print(response)