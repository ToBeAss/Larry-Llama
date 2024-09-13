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
    
    result = ollama.chat(model=desiredModel, messages=conversation_history)
    
    response = result['message']['content']
    
    conversation_history.append({
        'role': 'assistant',
        'content': response,
    })
    
    return response