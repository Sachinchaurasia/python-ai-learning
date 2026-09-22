from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


sentences = [
    "I love programming in Python.",
    "Python is my favorite programming language.",
    "The weather is very cold today."
]


embeddings = model.encode(sentences)


similarity_1_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)[0][0]


similarity_1_3 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)[0][0]


print("Programming vs Programming:")
print(similarity_1_2)


print("\nProgramming vs Weather:")
print(similarity_1_3)