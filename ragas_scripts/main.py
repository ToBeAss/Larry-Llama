import pandas
import nest_asyncio
import sys
import os
from ragas import EvaluationDataset

# Add the project root directory to `sys.path`
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import generate
from scripts.embedding import query_db
from scripts.chat import ask
import evaluate


DATA_PATH = 'data'
LLM_MODEL = 'gpt-4o-mini'


def print_pandas(dataset):
    pandas.set_option('display.width', 1000)
    pandas.set_option('display.max_columns', None)
    df = dataset.to_pandas()
    print(df)


def main():
    nest_asyncio.apply() # Fix APIConnectionError

    # Generate testset
    docs = generate.load_documents(DATA_PATH)
    llm = generate.get_generator_llm(model=LLM_MODEL)
    embeddings = generate.get_generator_embeddings()

    generator = generate.get_generator(llm, embeddings)
    testset = generator.generate_with_langchain_docs(docs, testset_size=3)
    testset = testset.to_pandas()


    # Answer testset
    results = []

    for idx, row in testset.iterrows():
        user_input = row['user_input']

        # Query the database and retrieve documents
        retrieved_docs = query_db(user_input)

        # Extract the page_content from each Document and store as a list of strings
        retrieved_contexts = [doc.page_content for doc in retrieved_docs]

        response = ask(user_input, retrieved_contexts)

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
    print()  # Ensures the next console output starts on a new line
    print("The testset has been answered")


    # Evaluate answers
    dataset = EvaluationDataset.from_list(results)
    llm = evaluate.get_evaluator_llm(LLM_MODEL)
    embeddings = evaluate.get_evaluator_embeddings()

    evaluator = evaluate.get_evaluator(llm, embeddings)
    evaluation = evaluator.evaluate(dataset)
    df = evaluation.to_pandas()

    # Display/export results
    # Set the display option to show all columns side by side
    pandas.set_option('display.width', 1000)
    pandas.set_option('display.max_columns', None)
    print(df)


main()