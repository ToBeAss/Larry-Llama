import ollama
desiredModel='llama3.1:latest'
questionToAsk='Hva er fordelene med å bruke kunstig intelligens i Statens Kartverk?'

response = ollama.chat(model=desiredModel, messages=[
    {
        'role': 'user',
        'content': questionToAsk,
    },
])

OllamaResponse=response['message']['content']

print(OllamaResponse)

with open("OutputOllama.txt", "w", encoding="utf-8") as text_file:
    text_file.write(OllamaResponse)