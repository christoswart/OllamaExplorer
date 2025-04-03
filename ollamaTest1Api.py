import requests
from bs4 import BeautifulSoup
from IPython.display import Markdown, display


OLLAMA_API = "http://localhost:11434/api/chat"
HEADERS = {"Content-Type": "application/json"}
MODEL = "gemma3:latest"

# Create a messages list using the same format that we used for OpenAI

messages = [
    {"role": "user", "content": "Describe some of the business applications of Generative AI"}
]

payload = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

print("Sending request to Ollama API...")
response = requests.post(OLLAMA_API, json=payload, headers=HEADERS)
print(response.json()['message']['content'])

#display(Markdown(response.json()['message']['content']))
# The above code is a simple example of how to use the Ollama API to get a response from the Gemma model.
# You can modify the messages list to ask different questions or provide different context.
# The response is returned in JSON format, and you can access the content of the message using the key 'message'.
# You can also use the display function from IPython to display the response in a more readable format.