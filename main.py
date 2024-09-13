#!/usr/bin/env python3
from scripts.chat import ask
from scripts.chat import addInstruction

while True:
    user_input = input("Deg: ")

    if user_input.lower() in ['/exit', '/quit', '/bye']:
        break

    ollama_response = ask(user_input)
    print("Larry Llama: " + ollama_response)