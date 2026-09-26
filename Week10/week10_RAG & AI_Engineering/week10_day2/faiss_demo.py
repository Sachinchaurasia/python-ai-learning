import faiss
import numpy as np


vectors = np.array([
    [1.0, 0.0],
    [0.9, 0.1],
    [0.0, 1.0],
    [0.1, 0.9]
], dtype="float32")


dimension = vectors.shape[1]


index = faiss.IndexFlatL2(dimension)


index.add(vectors)


query = np.array([
    [0.95, 0.05]
], dtype="float32")


k = 2


distances, indices = index.search(
    query,
    k
)


print("Distances:")
print(distances)


print("\nNearest vector indices:")
print(indices)