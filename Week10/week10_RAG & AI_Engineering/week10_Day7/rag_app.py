from pathlib import Path

import faiss
import numpy as np

from sentence_transformers import SentenceTransformer


# ==========================================
# CONFIGURATION
# ==========================================

DOCUMENTS_DIR = Path("file:///D:/download%20d/Sachin%201resume.pdf")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

TOP_K = 5
SIMILARITY_THRESHOLD = 0.30


# ==========================================
# LOAD DOCUMENTS
# ==========================================

def load_documents():

    documents = []

    for file_path in DOCUMENTS_DIR.glob("*.txt"):

        text = file_path.read_text(
            encoding="utf-8"
        )

        documents.append(
            {
                "source": file_path.name,
                "text": text
            }
        )

    return documents


# ==========================================
# CHUNKING
# ==========================================

def chunk_text(
    text,
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP
):

    chunks = []

    start = 0

    step = chunk_size - overlap

    while start < len(text):

        end = start + chunk_size

        chunk = text[start:end]

        chunks.append(chunk)

        start += step

    return chunks


def create_chunks(documents):

    all_chunks = []

    chunk_id = 0

    for document in documents:

        chunks = chunk_text(
            document["text"]
        )

        for chunk in chunks:

            all_chunks.append(
                {
                    "id": chunk_id,
                    "text": chunk,
                    "source": document["source"]
                }
            )

            chunk_id += 1

    return all_chunks


# ==========================================
# EMBEDDINGS + FAISS
# ==========================================

def build_vector_index(
    chunks,
    model
):

    texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = model.encode(
        texts
    )

    embeddings = np.array(
        embeddings
    ).astype("float32")

    faiss.normalize_L2(
        embeddings
    )

    dimension = embeddings.shape[1]

    index = faiss.IndexFlatIP(
        dimension
    )

    index.add(
        embeddings
    )

    return index


# ==========================================
# RETRIEVAL
# ==========================================

def retrieve(
    query,
    model,
    index,
    chunks,
    top_k=TOP_K,
    threshold=SIMILARITY_THRESHOLD
):

    query_embedding = model.encode(
        [query]
    )

    query_embedding = np.array(
        query_embedding
    ).astype("float32")

    faiss.normalize_L2(
        query_embedding
    )

    scores, indices = index.search(
        query_embedding,
        top_k
    )

    retrieved_chunks = []

    for score, idx in zip(
        scores[0],
        indices[0]
    ):

        if score < threshold:
            continue

        chunk = chunks[idx].copy()

        chunk["score"] = float(score)

        retrieved_chunks.append(
            chunk
        )

    return retrieved_chunks


# ==========================================
# CONTEXT
# ==========================================

def build_context(chunks):

    context_parts = []

    for i, chunk in enumerate(
        chunks,
        start=1
    ):

        context_parts.append(
            f"""
--- SOURCE {i} ---

File:
{chunk['source']}

Similarity:
{chunk['score']:.4f}

Content:
{chunk['text']}
"""
        )

    return "\n".join(
        context_parts
    )


# ==========================================
# RAG PROMPT
# ==========================================

def build_prompt(
    question,
    context
):

    return f"""
You are a helpful AI assistant.

Answer the user's question using only
the provided context.

Rules:

1. Do not invent information.
2. Do not use unsupported facts.
3. If the answer is not present in the context,
   clearly say that the information was not found.
4. Give a clear and concise answer.
5. Mention relevant sources when possible.

CONTEXT:

{context}

QUESTION:

{question}

ANSWER:
"""


# ==========================================
# MAIN
# ==========================================

def main():

    print("Loading documents...")

    documents = load_documents()

    print(
        f"Documents loaded: {len(documents)}"
    )

    chunks = create_chunks(
        documents
    )

    print(
        f"Chunks created: {len(chunks)}"
    )

    print(
        "\nLoading embedding model..."
    )

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    print(
        "Building FAISS index..."
    )

    index = build_vector_index(
        chunks,
        model
    )

    print(
        "RAG system ready."
    )

    query = input(
        "\nAsk a question: "
    )

    retrieved_chunks = retrieve(
        query,
        model,
        index,
        chunks
    )

    print(
        "\n=============================="
    )
    print(
        "RETRIEVED SOURCES"
    )
    print(
        "=============================="
    )

    for chunk in retrieved_chunks:

        print(
            f"\nSource: {chunk['source']}"
        )

        print(
            f"Score: {chunk['score']:.4f}"
        )

    if not retrieved_chunks:

        print(
            "\nNo sufficiently relevant "
            "information was retrieved."
        )

        return

    context = build_context(
        retrieved_chunks
    )

    prompt = build_prompt(
        query,
        context
    )

    print(
        "\n=============================="
    )

    print(
        "RAG PROMPT"
    )

    print(
        "=============================="
    )

    print(prompt)

    print(
        "\n=============================="
    )

    print(
        "RAG pipeline complete."
    )


if __name__ == "__main__":
    main()