from evaluation_dataset import evaluation_dataset


def precision_at_k(retrieved_ids, relevant_ids, k):

    retrieved = retrieved_ids[:k]

    if not retrieved:
        return 0.0

    relevant_count = sum(
        1
        for doc_id in retrieved
        if doc_id in relevant_ids
    )

    return relevant_count / len(retrieved)


def recall_at_k(retrieved_ids, relevant_ids, k):

    if not relevant_ids:
        return 0.0

    retrieved = retrieved_ids[:k]

    relevant_count = sum(
        1
        for doc_id in retrieved
        if doc_id in relevant_ids
    )

    return relevant_count / len(relevant_ids)


retrieval_results = {
    "What is machine learning?": [2, 3, 1],
    "What is Python used for?": [1, 2, 4],
    "What is natural language processing?": [5, 3, 2]
}


for item in evaluation_dataset:

    question = item["question"]
    relevant_ids = item["relevant_ids"]

    retrieved_ids = retrieval_results[question]

    precision = precision_at_k(
        retrieved_ids,
        relevant_ids,
        3
    )

    recall = recall_at_k(
        retrieved_ids,
        relevant_ids,
        3
    )

    print("\nQuestion:", question)
    print("Precision@3:", round(precision, 3))
    print("Recall@3:", round(recall, 3))