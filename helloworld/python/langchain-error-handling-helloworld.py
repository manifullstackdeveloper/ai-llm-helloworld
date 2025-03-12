# Install dependencies if not already
# pip install langchain ollama

from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate
from tenacity import retry, stop_after_attempt, wait_exponential, RetryError


# 1. Load the model using Ollama
# THIS LINE CAN BE REPLEACE with different AI models...
########################################################################################################
llm = Ollama(model="llama3")
# 1. llm = OpenAI(model_name="...", openai_api_key=API_KEY)
# 2. llm = HuggingFaceHub(repo_id = "..."", huggingfacehub_api_token = API_KEY)
########################################################################################################
# Replace with 'llama3' once available via ollama pull llama3


template = PromptTemplate.from_template("tell me a joke about {topic}.")

chain = template | llm

# Retry logic with tenacity
@retry(
    stop=stop_after_attempt(3),  # Retry up to 3 attempts
    wait=wait_exponential(multiplier=1, min=4, max=10),  # Exponential backoff with a min and max wait time
    reraise=True  # Reraise the last exception after retries
)
def stream_response_with_retry(topic):
    try:
        # Run the chain with streaming enabled
        result = chain.invoke({"topic":topic})
        print("\nComplete Response:", result)
    except Exception as e:
        print(f"Error occurred: {e}")
        raise  # Raise the exception again to trigger the retry

# Example usage
topic = "quantum mechanics"
try:
    stream_response_with_retry(topic)
except RetryError:
    print("Failed to fetch a response after multiple retries.")
