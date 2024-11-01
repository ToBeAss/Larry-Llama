#!/usr/bin/env python3
from src.embedding import query_db
from src.chat import ask
from src.chat import addInstruction

while True:
    user_input = input("Deg: ")

    if user_input.lower() in ['/exit', '/quit', '/bye']:
        break

    retrieved_contexts = query_db(user_input)
    ollama_response = ask(user_input, retrieved_contexts)
    print("Larry Llama: " + ollama_response)