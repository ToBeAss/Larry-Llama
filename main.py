#!/usr/bin/env python3
import ollama

desiredModel = 'llama3.1:latest'
conversation_history = []

instruction = "Du er en AI assistent kalt Larry Llama, eller bare Larry, spesialisert i å gi veiledning om bruken av kunstig intelligens i Statens Kartverk. Gi konsise og profesjonelle svar, og svar alltid på norsk."

conversation_history.append({
    'role': 'system',
    'content': instruction,
})

def ask(question):
    conversation_history.append({
        'role': 'user',
        'content': question,
    })
    
    response = ollama.chat(model=desiredModel, messages=conversation_history)
    
    OllamaResponse = response['message']['content']
    
    conversation_history.append({
        'role': 'assistant',
        'content': OllamaResponse,
    })
    
    print("Larry Llama: " + OllamaResponse)

    #with open("data/OutputOllama.txt", "w", encoding="utf-8") as text_file:
        #text_file.write(conversation_history)
    
while True:
    user_input = input("Deg: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    
    ask(user_input)