from sentence_transformers import  SentenceTransformer

model=SentenceTransformer("all-MiniLM-L6-v2")
sentences=[
    "I love programming in python.",
    "Python is my favourite programming language:",
    "The Weather is very cold today"
]

embeddings=model.encode(sentences)

for sentence , embedding in zip(sentences,embeddings):
    
    print("\n Sentence")
    print(sentence)
    
    print("Embeddings Dimensions:")
    print(len(embedding))
    
    
#Calculate Similarity
from sklearn.metrics.pairwise import cosine_similarity

similarity=cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)
    
print(similarity)
