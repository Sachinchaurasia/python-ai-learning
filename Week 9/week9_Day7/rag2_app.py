import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI


# ==========================================
# 1. Load API configuration
# ==========================================

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)


# ==========================================
# 2. Load documents
# ==========================================

def load_documents(folder):

    documents = []

    for filename in os.listdir(folder):

        filepath = os.path.join(folder, filename)

        if filename.endswith(".txt"):

            with open(filepath, "r", encoding="utf-8") as file:

                text = file.read()

                documents.append({
                    "filename": filename,
                    "text": text
                })

    return documents


# ==========================================
# 3. Chunk documents
# ==========================================

def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i + chunk_size]

        chunks.append(chunk)

    return chunks


# ==========================================
# 4. Load + chunk
# ==========================================

documents = load_documents("documents")

chunks = []

for document in documents:

    document_chunks = chunk_text(document["text"])

    for chunk in document_chunks:

        chunks.append({
            "filename": document["filename"],
            "text": chunk
        })


print("Documents loaded:", len(documents))
print("Chunks created:", len(chunks))


# ==========================================
# 5. Create embedding model
# ==========================================

embedding_model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


# ==========================================
# 6. Generate chunk embeddings
# ==========================================

chunk_texts = [
    chunk["text"]
    for chunk in chunks
]

chunk_embeddings = embedding_model.encode(
    chunk_texts
)


# ==========================================
# 7. User question
# ==========================================

question = input("\nAsk a question: ")


# ==========================================
# 8. Question embedding
# ==========================================

question_embedding = embedding_model.encode(
    [question]
)


# ==========================================
# 9. Semantic search
# ==========================================

similarities = cosine_similarity(
    question_embedding,
    chunk_embeddings
)[0]


results = list(
    zip(chunks, similarities)
)

results.sort(
    key=lambda x: x[1],
    reverse=True
)


top_results = results[:3]


# ==========================================
# 10. Build context
# ==========================================

context = "\n\n".join(
    result[0]["text"]
    for result in top_results
)


# ==========================================
# 11. Build RAG prompt
# ==========================================

prompt = f"""
You are a helpful AI assistant.

Answer the user's question using ONLY
the provided context.

If the answer cannot be found in the
context, say:

"The information is not available
in the provided documents."

Context:

{context}

Question:

{question}
"""


# ==========================================
# 12. Call LLM
# ==========================================

response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)


# ==========================================
# 13. Display result
# ==========================================

print("\n==============================")
print("RAG ANSWER")
print("==============================")

print(response.output_text)