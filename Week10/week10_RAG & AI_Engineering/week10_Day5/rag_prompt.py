from retrieved_chunks import retrieved_chunks


def format_context(chunks):

    formatted_chunks = []

    for i, chunk in enumerate(chunks, start=1):

        formatted = f"""
--- SOURCE {i} ---

Page: {chunk['page']}
Section: {chunk['section']}
Similarity: {chunk['score']:.4f}

{chunk['text']}
"""

        formatted_chunks.append(formatted)

    return "\n".join(formatted_chunks)


def build_rag_prompt(question, chunks):

    context = format_context(chunks)

    prompt = f"""
You are an AI research assistant.

Answer the user's question using only the
retrieved context below.

Rules:

1. Do not invent information.
2. Use only the provided context.
3. If the answer is not available, say so.
4. Give a clear and concise answer.
5. Mention relevant page numbers when possible.

RETRIEVED CONTEXT:

{context}

USER QUESTION:

{question}

ANSWER:
"""

    return prompt


question = input("Enter your question: ")

prompt = build_rag_prompt(
    question,
    retrieved_chunks
)

print("\n==============================")
print("RAG PROMPT")
print("==============================")

print(prompt)