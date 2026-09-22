from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model=SentenceTransformer("all-MiniLM-L6-v2")

documents=[
    "Python is widely used for machine learning",
    "java is commonly used for enterprise backend systems",
    "Deep learning is useful for image recognition",
    "SQL is used to manage relational databases",
    "Natural language Processing deals with human language"
]

query=input("Enter your search query:")

document_embeddings=model.encode(documents)
query_embedding=model.encode([query])

similarities=cosine_similarity(
    query_embedding,
    document_embeddings
)[0]

results=list(zip(documents,similarities))
results.sort(
    key=lambda x:x[1],
    reverse=True
    
)


print("\n=================================")
print("SEMANTIC SEARCH RESULTS")

print("====================================")


for document,score in results:
    print("\n Document:")
    print(document)
    
    print("Similarity")
    print(round(score,4))
    