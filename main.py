#!/usr/bin/env python3
from scripts.embedding import query_db
from scripts.chat import ask
from scripts.chat import addInstruction

while True:
    user_input = input("Deg: ")

    if user_input.lower() in ['/exit', '/quit', '/bye']:
        break

    retrieved_contexts = query_db(user_input)
    ollama_response = ask(user_input, retrieved_contexts)
    print("Larry Llama: " + ollama_response)