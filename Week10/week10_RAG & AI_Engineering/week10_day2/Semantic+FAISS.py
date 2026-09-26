from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


documents = [
    "Python is widely used for machine learning.",
    "Java is commonly used for enterprise applications.",
    "Deep learning uses neural networks.",
    "SQL is used for relational databases.",
    "Natural language processing deals with human language."
]


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


embeddings = model.encode(
    documents
)


embeddings = np.array(
    embeddings,
    dtype="float32"
)


dimension = embeddings.shape[1]


index = faiss.IndexFlatL2(
    dimension
)


index.add(embeddings)


print("Total vectors:", index.ntotal)


question = input(
    "\nEnter your question: "
)


query_embedding = model.encode(
    [question]
)


query_embedding = np.array(
    query_embedding,
    dtype="float32"
)


k = 3


distances, indices = index.search(
    query_embedding,
    k
)


print("\n==============================")
print("SEARCH RESULTS")
print("==============================")


for rank, (distance, index_id) in enumerate(
    zip(distances[0], indices[0]),
    start=1
):

    print(f"\nRank: {rank}")

    print(
        "Document:",
        documents[index_id]
    )

    print(
        "L2 Distance:",
        round(float(distance), 4)
    )