from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
text="Python is a Programming language."
embedding=model.encode(text)
print("Embedding:")
print(embedding)

print("\n Embedding type")
print(type(embedding))

print("\n Embedding dimensions")
print(len(embedding))

