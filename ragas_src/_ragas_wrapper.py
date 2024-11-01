from ragas.llms import LangchainLLMWrapper
from ragas.evaluation import LangchainEmbeddingsWrapper
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

class _RagasWrapper():
    @staticmethod
    def _get_openai_llm(model : str = "gpt-4o-mini"):
        return LangchainLLMWrapper(ChatOpenAI(model=model))

    @staticmethod
    def _get_openai_embeddings():
        return LangchainEmbeddingsWrapper(OpenAIEmbeddings())
    
    def __init__(self, llm : LangchainLLMWrapper = None, embeddings : LangchainEmbeddingsWrapper = None):
        self.llm = llm if llm is not None else self._get_openai_llm()
        self.embeddings = embeddings if embeddings is not None else self._get_openai_embeddings()