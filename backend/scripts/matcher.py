import spacy
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

nlp = spacy.load("en_core_web_lg")

def compute_similarity(text1, text2):
    """
    Computes cosine similarity between two texts using spaCy vector embeddings.
    """
    doc1 = nlp(text1)
    doc2 = nlp(text2)

    # spaCy warns if vector is empty (bad text). Handle that:
    if not doc1.vector_norm or not doc2.vector_norm:
        print("[WARN] One of the texts has no vector representation.")
        return 0.0

    # Convert to 2D arrays for sklearn
    vec1 = doc1.vector.reshape(1, -1)
    vec2 = doc2.vector.reshape(1, -1)

    similarity = cosine_similarity(vec1, vec2)[0][0]
    return round(similarity, 4)
