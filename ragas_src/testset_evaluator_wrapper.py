from _ragas_wrapper import _RagasWrapper # Import the superclass
from ragas.llms import LangchainLLMWrapper
from ragas.evaluation import LangchainEmbeddingsWrapper
from ragas import EvaluationDataset
from ragas import evaluate
from ragas.metrics import LLMContextRecall, Faithfulness, FactualCorrectness, SemanticSimilarity

class TestsetEvaluatorWrapper(_RagasWrapper):
    def __init__(self, llm : LangchainLLMWrapper = None, embeddings : LangchainEmbeddingsWrapper = None):
        super().__init__(llm, embeddings)

    def _get_default_metrics(self):
        return [
            LLMContextRecall(llm=self.llm), 
            FactualCorrectness(llm=self.llm), 
            Faithfulness(llm=self.llm),
            SemanticSimilarity(embeddings=self.embeddings)
        ]
        
    def evaluate_answers(self, answers : list, metrics : list = None):
        if metrics is None:
            metrics = self._get_default_metrics()
        dataset = EvaluationDataset.from_list(answers)
        evaluation = evaluate(dataset, metrics)
        return evaluation.to_pandas()