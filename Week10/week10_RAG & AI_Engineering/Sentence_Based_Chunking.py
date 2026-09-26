   #Sentence Based Chunking
import re


def split_sentences(text):

    sentences = re.split(
        r'(?<=[.!?])\s+',
        text.strip()
    )

    return sentences

#TEST IT
text = """
Machine learning is a branch of artificial intelligence.
It allows computers to learn patterns from data.
Supervised learning uses labeled data.
Deep learning uses neural networks.
"""

sentences = split_sentences(text)

for sentence in sentences:
    print(sentence)
    
    
#SENTENCE BASED CHUNKING
def sentence_chunks(
    text,
    sentences_per_chunk=3,
    overlap_sentences=1
):

    sentences = split_sentences(text)

    chunks = []

    start = 0

    while start < len(sentences):

        end = start + sentences_per_chunk

        chunk = " ".join(
            sentences[start:end]
        )

        chunks.append(chunk)

        start += (
            sentences_per_chunk
            - overlap_sentences
        )

    return chunks
