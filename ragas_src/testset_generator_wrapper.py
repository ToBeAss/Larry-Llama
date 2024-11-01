from _ragas_wrapper import _RagasWrapper # Import the superclass
from ragas.llms import LangchainLLMWrapper
from ragas.evaluation import LangchainEmbeddingsWrapper
from ragas.testset import TestsetGenerator

class TestsetGeneratorWrapper(_RagasWrapper):
    def __init__(self, llm : LangchainLLMWrapper = None, embeddings : LangchainEmbeddingsWrapper = None):
        super().__init__(llm, embeddings)
        self.generator = TestsetGenerator(self.llm, self.embeddings)

    def generate_testset(self, documents : list, testset_size : int):
        testset = self.generator.generate_with_langchain_docs(documents, testset_size=testset_size)
        return testset.to_pandas()