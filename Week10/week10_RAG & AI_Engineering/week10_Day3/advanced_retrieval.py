from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    {
        "id": 1,
        "text": "Machine learning allows computers to learn patterns from data.",
        "topic": "machine_learning"
    },
    {
        "id": 2,
        "text": "Deep learning uses neural networks with multiple layers.",
        "topic": "deep_learning"
    },
    {
        "id": 3,
        "text": "Convolutional neural networks are commonly used for image processing.",
        "topic": "deep_learning"
    },
    {
        "id": 4,
        "text": "Transformers are widely used in natural language processing.",
        "topic": "nlp"
    },
    {
        "id": 5,
        "text": "SQL is used to store and retrieve structured relational data.",
        "topic": "database"
    }
]


model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


texts = [
    document["text"]
    for document in documents
]


document_embeddings = model.encode(
    texts
)


query = input(
    "Enter your question: "
)


query_embedding = model.encode(
    [query]
)


scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]


results = []


for document, score in zip(
    documents,
    scores
):

    results.append({
        "document": document,
        "score": float(score)
    })


results.sort(
    key=lambda x: x["score"],
    reverse=True
)


candidate_results = results[:5]


SIMILARITY_THRESHOLD = 0.40


filtered_results = [
    result
    for result in candidate_results
    if result["score"] >= SIMILARITY_THRESHOLD
]


print("\n==============================")
print("ADVANCED RETRIEVAL")
print("==============================")


for result in filtered_results:

    document = result["document"]

    print("\n------------------------------")

    print(
        "ID:",
        document["id"]
    )

    print(
        "Topic:",
        document["topic"]
    )

    print(
        "Similarity:",
        round(result["score"], 4)
    )

    print(
        "Text:",
        document["text"]
    )