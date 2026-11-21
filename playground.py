from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer("BAAI/bge-small-en-v1.5")

sentences = [
    "How many days of paid leave do employees get?",
    "Employees are entitled to 24 days of annual vacation.",
    "The API returns a 429 status code when rate limits are exceeded.",
    "What is the capital of France?",
]

vectors = model.encode(sentences, normalize_embeddings=True)
print("Shape:", vectors.shape) 
# vectors.shape: the dimensions of that array. (4, 384) means 4 sentences, each with 384 numbers.

#vectors @ vectors.T: @ is matrix multiplication and .T flips the matrix. A (4×384) matrix times a (384×4) matrix gives a (4×4) table where row i, column j is the similarity between sentence i and sentence j. One line compares every pair.
similarity = vectors @ vectors.T
print(np.round(similarity, 2))