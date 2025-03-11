from openai import OpenAI
import os
from dotenv import load_dotenv, dotenv_values 
load_dotenv() 

apiKey = os.getenv("apiKey")

# apiKey # use key in env variable or paste it here and run code
client = OpenAI(
    api_key= apiKey
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "What is AI ?"
        }
    ]
)

print(completion.choices[0].message)