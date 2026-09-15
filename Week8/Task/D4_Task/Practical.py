# 💻 PRACTICAL TASK

# Run this:

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

sentences = [
    "I love programming.",
    "I enjoy coding.",
    "The weather is rainy today."
]

embeddings = model.encode(sentences)

print("Embedding shape:")
print(embeddings.shape)

similarity_1 = cosine_similarity(
    [embeddings[0]],
    [embeddings[1]]
)

similarity_2 = cosine_similarity(
    [embeddings[0]],
    [embeddings[2]]
)

print("Programming vs Coding:",
      similarity_1[0][0])

print("Programming vs Weather:",
      similarity_2[0][0])

# 🎯 Your observation should be:
# Programming ↔ Coding
#         ↓
# More similar

# Programming ↔ Weather
#         ↓
# Less similar


# You may first need:

# pip install sentence-transformers scikit-learn

# Then run the code exactly as given.

# 🎯 What you should observe

# Your output should contain an embedding shape similar to:

# Embedding shape:
# (3, 384)

# 3 = three sentences.

# 384 = the size of each sentence embedding produced by all-MiniLM-L6-v2.

# Then you should see two similarity scores:

# Programming vs Coding: <score>
# Programming vs Weather: <score>

# The important observation is:

# "I love programming."
#         ↕
# "I enjoy coding."
#         ↓
# Higher similarity


# "I love programming."
#         ↕
# "The weather is rainy today."
#         ↓
# Lower similarity

# The exact numbers can vary slightly depending on the library/model environment, so send me whatever your terminal actually prints.

# 🔥 What you're demonstrating

# You're now seeing the concept we discussed earlier in practice:

# Sentence
#    ↓
# Embedding
#    ↓
# Vector
#    ↓
# Cosine Similarity
#    ↓
# Measure semantic similarity

# Paste your complete terminal output here, and I'll explain the (3, 384) shape, the embeddings, and both similarity scores step-by-step.