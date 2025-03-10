import json
from chromadb import PersistentClient, EmbeddingFunction, Embeddings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

MODEL_NAME = "NovaSearch/stella_en_1.5B_v5"
DB_PATH = "./chroma_db"

class QuestionAnswerPairs:
    def __init__(self, question: str, answer: str):
        self.question = question
        self.answer = answer

class CustomEmbeddingClass(EmbeddingFunction):
    def __init__(self, model_name: str):
        self.embedding_model = HuggingFaceEmbedding(model_name = MODEL_NAME)
    
    def __call__(self, input_texts: list[str]) -> Embeddings:
        return [self.embedding_model.get_text_embedding(text) for text in input_texts]

db = PersistentClient(path=DB_PATH)
custom_embedding_function = CustomEmbeddingClass(MODEL_NAME)
collection = db.get_or_create_collection(name="FAQ", embedding_function=custom_embedding_function)

# faq_file = "faq.json"
# with open(faq_file, "r") as f:
#     faq_data = json.load(f)

# collection.add(
#     documents=[QuestionAnswerPairs(question=faq["question"], answer=faq["answer"]) for faq in faq_data],
#     metadatas=[{"question": faq["question"], "answer": faq["answer"]} for faq in faq_data],
#     ids=[str(i) for i in range(len(faq_data))]
# )

def query_faq(query):
    pass
    # return collection.query(
    #     query_texts=[query],
    #     n_results=1
    # )
