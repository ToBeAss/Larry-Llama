import ollama

desiredModel = 'llama3.1:latest'
conversation_history = []

def addInstruction(instruction):
    conversation_history.append({
        'role': 'system',
        'content': instruction,
    })
    return "Instruksjon mottatt."

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

# Add instructions here:
addInstruction("Du er en AI assistent kalt Larry Llama, eller bare Larry, som skal hjelpe med å løse oppgaver og finne svar på spørsmål. Gi profesjonelle, korte og konsise svar, og svar alltid på norsk, med mindre annet blir oppgitt.")