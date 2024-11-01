import pandas
import sys
import os

# Add the project root directory to `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import custom functions
from src.embedding import query_db
from src.chat import ask

# The class is currently Ollama spesific but will be made 
class TestsetAnswerer():
    def __init__(self, llm = None, embeddings = None):
        self.llm = llm
        self.embeddings = embeddings

    def _retrieve_contexts(self, user_input : str):
        # Query the database and retrieve documents
        retrieved_docs = query_db(user_input)
        # Extract the page_content from each Document and store as a list of strings
        return [doc.page_content for doc in retrieved_docs]
    
    def _respond(self, user_input : str, retrieved_contexts : list):
        return ask(user_input, retrieved_contexts)

    def answer_testset(self, testset : pandas.DataFrame):
        print(f"\r0/{len(testset)} questions answered", end="")

        results = []

        for idx, row in testset.iterrows():
            user_input = row['user_input']

            retrieved_contexts = self._retrieve_contexts(user_input)
            response = self._respond(user_input, retrieved_contexts)

            results.append({
                "user_input": user_input,
                "reference_contexts": row['reference_contexts'],
                "reference": row['reference'],
                "synthesizer_name": row['synthesizer_name'],
                "retrieved_contexts": retrieved_contexts,
                "response": response
            })

            # Print progress on the same line
            print(f"\r{idx+1}/{len(testset)} questions answered", end="")

        # Newline after the loop completes
        print() # Ensures the next console output starts on a new line
        return results