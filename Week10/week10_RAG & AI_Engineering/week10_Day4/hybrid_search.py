from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    {
        "id": 1,
        "text": "Machine learning is used for image classification.",
        "domain": "AI",
        "status": "active"
    },

    {
        "id": 2,
        "text": "Natural language processing uses transformers and language models.",
        "domain": "NLP",
        "status": "active"
    },

    {
        "id": 3,
        "text": "Photocatalysis and photovoltaics are important areas of material chemistry.",
        "domain": "Materials",
        "status": "active"
    },

    {
        "id": 4,
        "text": "Deep learning uses neural networks for many AI applications.",
        "domain": "AI",
        "status": "inactive"
    }
]


def calculate_keyword_score(
    query,
    text
):

    query_words = set(
        query.lower().split()
    )

    text_words = set(
        text.lower().split()
    )

    if not query_words:
        return 0.0

    common_words = (
        query_words.intersection(
            text_words
        )
    )

    return (
        len(common_words)
        / len(query_words)
    )


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
    "Enter your search query: "
)


query_embedding = model.encode(
    [query]
)


semantic_scores = cosine_similarity(
    query_embedding,
    document_embeddings
)[0]


SEMANTIC_WEIGHT = 0.7
KEYWORD_WEIGHT = 0.3


results = []


for document, semantic_score in zip(
    documents,
    semantic_scores
):

    keyword_score = calculate_keyword_score(
        query,
        document["text"]
    )

    final_score = (
        SEMANTIC_WEIGHT * float(
            semantic_score
        )
        +
        KEYWORD_WEIGHT * keyword_score
    )

    results.append({
        "document": document,
        "semantic_score": float(
            semantic_score
        ),
        "keyword_score": keyword_score,
        "final_score": final_score
    })


results.sort(
    key=lambda x: x["final_score"],
    reverse=True
)


print("\n==============================")
print("HYBRID SEARCH RESULTS")
print("==============================")


for result in results:

    document = result["document"]

    print("\n------------------------------")

    print(
        "ID:",
        document["id"]
    )

    print(
        "Domain:",
        document["domain"]
    )

    print(
        "Status:",
        document["status"]
    )

    print(
        "Semantic Score:",
        round(
            result["semantic_score"],
            4
        )
    )

    print(
        "Keyword Score:",
        round(
            result["keyword_score"],
            4
        )
    )

    print(
        "Final Score:",
        round(
            result["final_score"],
            4
        )
    )

    print(
        "Text:",
        document["text"]
    )