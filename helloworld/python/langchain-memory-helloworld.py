# Install dependencies if not already
# pip install langchain ollama

from langchain_community.llms import Ollama
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# 1. Load the model using Ollama
# THIS LINE CAN BE REPLEACE with different AI models...
########################################################################################################
llm = Ollama(model="llama3")
# 1. llm = OpenAI(model_name="...", openai_api_key=API_KEY)
# 2. llm = HuggingFaceHub(repo_id = "..."", huggingfacehub_api_token = API_KEY)
########################################################################################################
# Replace with 'llama3' once available via `ollama pull llama3`

memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=True)

# Start chatting
response1 = conversation.predict(input="Hi, my name is Mani.")
print(response1)

response2 = conversation.predict(input="What did I just tell you?")
print(response2)