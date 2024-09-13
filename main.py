#!/usr/bin/env python3
from scripts.chat import ask

while True:
    user_input = input("Deg: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    
    ollama_response = ask(user_input)
    print("Larry Llama: " + ollama_response);
    #with open("data/OutputOllama.txt", "w", encoding="utf-8") as text_file:
        #text_file.write(ollama_response)