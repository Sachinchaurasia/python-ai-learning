def create_chunks(
    text,
    source,
    chunk_size=50,
    overlap=10
):

    words = text.split()

    chunks = []

    start = 0

    chunk_id = 0

    while start < len(words):

        end = start + chunk_size

        chunk_text = " ".join(
            words[start:end]
        )

        chunks.append({
            "chunk_id": chunk_id,
            "source": source,
            "text": chunk_text
        })

        chunk_id += 1

        start += chunk_size - overlap

    return chunks