# Built for RAGAS v0.2.3

import os
import pandas
import nest_asyncio
from langchain_community.document_loaders import PyPDFDirectoryLoader

# Import custom modules
from testset_generator_wrapper import TestsetGeneratorWrapper
from testset_answerer import TestsetAnswerer
from testset_evaluator_wrapper import TestsetEvaluatorWrapper


# Set API key
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY") # Write your API key here or 
# Set it in your terminal using:
# Windows: setx OPENAI_API_KEY "your_api_key_here"
# Mac/Linux: export OPENAI_API_KEY=your_api_key_here
if not os.environ["OPENAI_API_KEY"]:
    raise ValueError("OPENAI_API_KEY not found in environment variables")


# Set path to data variable
DATA_PATH = 'data'


def load_documents(path : str):
    loader = PyPDFDirectoryLoader(path)
    return loader.load() # Returns list of documents



def main():
    nest_asyncio.apply() # Fix APIConnectionError

    # Load documents from specified path
    documents = load_documents(DATA_PATH)

    # Generate pandas testset with custom TestsetGeneratorWrapper
    testset = TestsetGeneratorWrapper().generate_testset(documents, testset_size=3)

    # Use our RAG system to take the tests
    answers = TestsetAnswerer().answer_testset(testset)

    # Evaluate result of testset with custom TestsetEvaluatorWrapper
    evaluation = TestsetEvaluatorWrapper().evaluate_answers(answers)

    # Display/export results
    pandas.set_option('display.width', 1000)
    pandas.set_option('display.max_columns', None)
    print(evaluation)

main()