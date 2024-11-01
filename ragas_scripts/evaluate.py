import os
import pandas
import nest_asyncio
from ragas.llms import LangchainLLMWrapper
from ragas.embeddings import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI, AzureChatOpenAI # Vurder å hoste OpenAI gjennom Azure
from langchain_openai import OpenAIEmbeddings
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness, SemanticSimilarity
from ragas import EvaluationDataset
from ragas import evaluate


# Set API key
os.environ["OPENAI_API_KEY"] = os.environ.get("OPENAI_API_KEY")
if not os.environ["OPENAI_API_KEY"]:
    raise ValueError("OPENAI_API_KEY not found in environment variables")


# Create Evaluator Class
class Evaluator:
    def __init__(self, evaluator_llm: LangchainLLMWrapper, evaluator_embeddings: LangchainEmbeddingsWrapper):
        self.evaluator_llm = evaluator_llm
        self.evaluator_embeddings = evaluator_embeddings

    def get_metrics(self):
        return [
            LLMContextRecall(llm=self.evaluator_llm), 
            FactualCorrectness(llm=self.evaluator_llm), 
            Faithfulness(llm=self.evaluator_llm),
            SemanticSimilarity(embeddings=self.evaluator_embeddings)
        ]

    def evaluate(self, dataset: EvaluationDataset):
        metrics = self.get_metrics()
        return evaluate(dataset=dataset, metrics=metrics)
        

def get_evaluator_llm(model: str):
    return LangchainLLMWrapper(ChatOpenAI(model=model))

def get_evaluator_embeddings():
    return LangchainEmbeddingsWrapper(OpenAIEmbeddings())

def get_evaluator(evaluator_llm: LangchainLLMWrapper, evaluator_embeddings: LangchainEmbeddingsWrapper):
    return Evaluator(evaluator_llm, evaluator_embeddings)