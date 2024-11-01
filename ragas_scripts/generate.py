import os
import pandas
import nest_asyncio
from langchain_community.document_loaders import PyPDFDirectoryLoader
from ragas.llms import LangchainLLMWrapper
from ragas.evaluation import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from ragas.testset import TestsetGenerator

# Set API key
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
if not os.environ["OPENAI_API_KEY"]:
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# Set path to data variable
DATA_PATH = 'data'


def load_documents(path: str):
    loader = PyPDFDirectoryLoader(path)
    return loader.load() # Returns list of documents


def get_generator_llm(model: str):
    return LangchainLLMWrapper(ChatOpenAI(model=model))

def get_generator_embeddings():
    return LangchainEmbeddingsWrapper(OpenAIEmbeddings())

def get_generator(generator_llm: LangchainLLMWrapper, generator_embeddings: LangchainEmbeddingsWrapper):
    return TestsetGenerator(llm=generator_llm, embedding_model=generator_embeddings)