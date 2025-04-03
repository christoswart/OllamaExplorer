import ollama

MODEL = "gemma3:latest"

# Create a messages list array
messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

print("Sending request to Ollama API...")
response = ollama.chat(model=MODEL, messages=messages, stream=False)
print(response['message']['content'])

# The above code is a simple example of how to use the Ollama API to get a response from the Gemma model.
# You can modify the messages list to ask different questions or provide different context.
# The response is returned in JSON format, and you can access the content of the message using the key 'message'.
