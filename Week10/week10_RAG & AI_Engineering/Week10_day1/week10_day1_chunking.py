import re
from pathlib import Path


# ============================================================
# 1. PROJECT PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

DOCUMENTS_DIR = BASE_DIR / "documents"


# ============================================================
# 2. LOAD DOCUMENT
# ============================================================

def load_document(filepath):

    with open(
        filepath,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


# ============================================================
# 3. SPLIT INTO SENTENCES
# ============================================================

def split_sentences(text):

    return re.split(
        r'(?<=[.!?])\s+',
        text.strip()
    )


# ============================================================
# 4. CREATE CHUNKS
# ============================================================

def create_chunks(
    text,
    source,
    document_type,
    sentences_per_chunk=3,
    overlap_sentences=1
):

    sentences = split_sentences(text)

    chunks = []

    start = 0
    chunk_id = 0

    while start < len(sentences):

        end = start + sentences_per_chunk

        chunk = " ".join(
            sentences[start:end]
        )

        chunks.append({

            "chunk_id": chunk_id,

            "source": source,

            "document_type": document_type,

            "text": chunk
        })

        chunk_id += 1

        start += (
            sentences_per_chunk
            - overlap_sentences
        )

    return chunks


# ============================================================
# 5. FIND ALL TXT DOCUMENTS
# ============================================================

document_files = list(
    DOCUMENTS_DIR.glob("*.txt")
)


print("\n==============================")
print("DOCUMENT CHUNKING")
print("==============================")

print(
    "Documents folder:",
    DOCUMENTS_DIR
)

print(
    "Total documents:",
    len(document_files)
)


# ============================================================
# 6. PROCESS EVERY DOCUMENT
# ============================================================

all_chunks = []

for filepath in document_files:

    print("\n==============================")
    print("Processing:", filepath.name)
    print("==============================")

    text = load_document(filepath)

    chunks = create_chunks(

        text=text,

        source=filepath.name,

        document_type="research",

        sentences_per_chunk=3,

        overlap_sentences=1
    )

    all_chunks.extend(chunks)

    print(
        "Characters:",
        len(text)
    )

    print(
        "Chunks:",
        len(chunks)
    )


# ============================================================
# 7. DISPLAY ALL CHUNKS
# ============================================================

print("\n\n========================================")
print("ALL DOCUMENT CHUNKS")
print("========================================")

print(
    "Total chunks:",
    len(all_chunks)
)


for chunk in all_chunks:

    print("\n----------------------------------------")

    print(
        "Chunk ID:",
        chunk["chunk_id"]
    )

    print(
        "Source:",
        chunk["source"]
    )

    print(
        "Document Type:",
        chunk["document_type"]
    )

    print(
        "Text:",
        chunk["text"]
    )