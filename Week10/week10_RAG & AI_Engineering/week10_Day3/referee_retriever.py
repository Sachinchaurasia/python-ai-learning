
import faiss
from sentence_transformers import SentenceTransformer


# --------------------------------
# 1. Referee data
# --------------------------------

referees = [
    {
        "id": 1,
        "name": "Referee A",
        "expertise": "Machine learning, computer vision",
        "domain": "AI"
    },
    {
        "id": 2,
        "name": "Referee B",
        "expertise": "Natural language processing, transformers, LLMs",
        "domain": "NLP"
    },
    {
        "id": 3,
        "name": "Referee C",
        "expertise": "Photocatalysis, photovoltaics, material chemistry",
        "domain": "Materials"
    }
]


# --------------------------------
# 2. Load embedding model
# --------------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# --------------------------------
# 3. Create expertise embeddings
# --------------------------------

expertise_texts = [
    referee["expertise"]
    for referee in referees
]

expertise_embeddings = model.encode(
    expertise_texts,
    convert_to_numpy=True
).astype("float32")


# --------------------------------
# 4. Create FAISS index
# --------------------------------

dimension = expertise_embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(expertise_embeddings)


# --------------------------------
# 5. Get proposal topic
# --------------------------------

proposal_topic = input(
    "\nEnter proposal topic: "
)


# --------------------------------
# 6. Create query embedding
# --------------------------------

query_embedding = model.encode(
    [proposal_topic],
    convert_to_numpy=True
).astype("float32")


# --------------------------------
# 7. Search
# --------------------------------

k = min(3, len(referees))

distances, indices = index.search(
    query_embedding,
    k
)


# --------------------------------
# 8. Display results
# --------------------------------

print("\n===== Matching Referees =====")

for rank, (idx, distance) in enumerate(
    zip(indices[0], distances[0]),
    start=1
):

    referee = referees[idx]

    print(f"\nRank: {rank}")
    print(f"ID: {referee['id']}")
    print(f"Name: {referee['name']}")
    print(f"Expertise: {referee['expertise']}")
    print(f"Domain: {referee['domain']}")
    print(f"Distance: {distance:.4f}")