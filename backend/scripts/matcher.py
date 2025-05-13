from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L32-v2')  

def compute_similarity(doc1, doc2):
    
    embedding1 = model.encode(doc1, convert_to_tensor=True)
    embedding2 = model.encode(doc2, convert_to_tensor=True)
    score = util.pytorch_cos_sim(embedding1, embedding2)
    return float(score[0])
