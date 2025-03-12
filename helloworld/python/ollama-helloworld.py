import ollama

########################################################################################################
# This ollama running locally .. 
# Thats why you dont see any api key such as open ai, huggingface etc.,
########################################################################################################
response = ollama.chat(
    model="llama3.2:1b",
    messages=[
        {
            "role": "user",
            "content": "latest news about Ind vs Aus Cricket Match?", 
            ## This is to test and confirm that, this is not going to give latest data
        },
    ],
)
print(response["message"]["content"])