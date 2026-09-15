

# Day 1 → Generative AI
# Day 2 → LLMs
# Day 3 → Tokens + Tokenization

# Today we move to a very important AI concept:

# How does AI represent the meaning of words and sentences as numbers?

# The answer is Embeddings.

# 🎯 Today's Learning Goals

# By the end of Day 4, you should understand:

# 1. What is an embedding?
# 2. Why do we need embeddings?
# 3. Token ID vs embedding
# 4. Vectors
# 5. Semantic meaning
# 6. Similarity
# 7. Cosine similarity
# 8. Sentence embeddings
# 9. Embeddings in search
# 10. Embeddings in RAG
# 7
# 🧠 STEP 1 — Start With What You Already Know

# From Day 3:

# Text
#  ↓
# Tokenizer
#  ↓
# Tokens
#  ↓
# Token IDs

# For example:

# "I love Python"

# might become conceptually:

# ["I", " love", " Python"]

# and then:

# [ID1, ID2, ID3]

# But there is a problem.

# ❓ Does a Token ID contain meaning?

# No.

# Suppose:

# Python → 18750
# Java   → 19999
# Dog    → 3892

# The number 18750 itself doesn't mean that Python is a programming language.

# It's simply an identifier in that tokenizer's vocabulary.

# We need something richer.

# That's where embeddings come in.

# 🔥 STEP 2 — What Is an Embedding?

# An embedding is a numerical vector that represents information in a way that captures useful relationships or semantic properties.

# In simple words:

# Embedding = meaning represented using numbers.

# For example, conceptually:

# Python
#    ↓
# [0.21, -0.73, 0.45, 0.91, ...]

# The actual vector may contain hundreds or thousands of dimensions depending on the model.

# Don't focus on the exact numbers yet.

# Focus on:

# Text
#  ↓
# Numbers representing useful meaning
# 🧩 STEP 3 — What Is a Vector?

# A vector is simply an ordered list of numbers.

# For example:

# [0.2, 0.7, -0.1, 0.9]

# That's a 4-dimensional vector.

# Another:

# [0.3, 0.8, -0.2, 0.7]

# These vectors can be compared mathematically.

# In real embedding models, vectors are often much larger:

# [0.12, -0.44, 0.81, ... many more values ...]
# 🧠 STEP 4 — Why So Many Numbers?

# Imagine we want to represent the concept:

# "Python"

# One number probably isn't enough to represent all the relationships associated with the concept.

# We might need many dimensions.

# Conceptually:

#                   Programming
#                        ↑
#                        |
#             Python ●   |   ● Java
#                        |
#                        |
#       ───────────────────────────→
#                        |
#                     Language

# This is only a visualization.

# Real embeddings usually have many dimensions, not just two.

# The model learns representations where useful relationships can emerge from the geometry of the vectors.

# 🔥 STEP 5 — Semantic Similarity

# Now consider:

# Sentence A:
# "I love programming."

# Sentence B:
# "I enjoy coding."

# Humans understand that these sentences have similar meanings.

# A good embedding model should produce vectors that are relatively close:

# "I love programming"
#         ↓
#       Vector A

# "I enjoy coding"
#         ↓
#       Vector B

# Vector A ↔ Vector B
#      relatively similar

# Now:

# "I love programming."

# versus:

# "The weather is rainy today."

# These would generally be less semantically similar.

# So:

# Similar meaning
#       ↓
# Similar vector representations

# This is the key idea.

# 🗺️ STEP 6 — Imagine an Embedding Space

# Imagine a map.

# Normally, a geographical map has:

# Delhi
# Mumbai
# London
# Paris

# and physically close places appear close on the map.

# An embedding space is different.

# It can organize information based on learned relationships.

# For example, conceptually:

# 5

# You might imagine:

#          Animals

#     Dog ●
#         ● Cat

#                  ● Tiger


# Programming

#  Python ●
#          ● Java
#                ● C++

# This is only an intuition. Real embedding spaces have many dimensions and don't necessarily form such clean human-labeled clusters.

# 🔢 STEP 7 — Token ID vs Embedding

# This distinction is extremely important.

# Token ID

# A token ID is an identifier.

# Python → 18750

# It tells the model:

# "This token corresponds to vocabulary entry 18750."

# Embedding

# An embedding is a vector representation.

# Python
#  ↓
# [0.12, -0.54, 0.81, ...]

# It contains numerical information useful for computation and representation.

# So:

# Token ID
#     ↓
# identifier

# Embedding
#     ↓
# vector representation
# 🔥 Remember

# Token ID is not the same thing as an embedding.

# STEP 8 — How Do Token IDs Become Vectors?

# At a simplified level:

# Token
#  ↓
# Token ID
#  ↓
# Embedding lookup
#  ↓
# Vector

# Imagine an embedding table:

# Token ID       Vector

# 1001       →   [0.2, 0.5, -0.1, ...]

# 1002       →   [0.7, 0.1,  0.8, ...]

# 1003       →   [-0.2, 0.9, 0.4, ...]

# The model uses the ID to retrieve the corresponding learned vector.

# This is often called an embedding matrix/table.

# 🧠 STEP 9 — Embeddings Are Learned

# This is another important idea.

# The numbers aren't manually assigned by programmers like:

# Python = programming = 10
# Java = programming = 11
# Dog = animal = 20

# Instead, the representations are learned during model training.

# Through training, the model learns useful relationships from the data.

# Conceptually:

# Training Data
#       ↓
# Neural Network
#       ↓
# Learned parameters
#       ↓
# Useful representations
#       ↓
# Embeddings
# 🔥 STEP 10 — Sentence Embeddings

# Embeddings aren't limited to individual words/tokens.

# We can also create embeddings for:

# Words
# "Python"
# Sentences
# "Python is easy to learn."
# Paragraphs
# "Python is widely used in machine learning..."
# Documents
# Research paper

# Then we can compare their vector representations.

# 🔍 STEP 11 — Semantic Search

# This is where embeddings become extremely useful for AI Engineering.

# Traditional keyword search might look for:

# "Java backend"

# and find documents containing those exact words.

# Semantic search tries to find content with similar meaning, even when the exact words differ.

# Suppose your document contains:

# "Spring Boot is commonly used to build server-side applications."

# User searches:

# "Java backend development"

# Even though the exact phrase might not appear, an embedding-based system can recognize semantic similarity.

# Conceptually:

# User Query
#     ↓
# Embedding
#     ↓
# Vector
#     ↓
# Compare with document vectors
#     ↓
# Most similar documents
# 5
# 🚀 STEP 12 — Embeddings + Vector Database

# Now we're approaching one of the most important AI Engineering concepts.

# Suppose you have:

# 10,000 documents

# You can create embeddings:

# Document 1 → Vector 1
# Document 2 → Vector 2
# Document 3 → Vector 3
# ...
# Document 10000 → Vector 10000

# Store them in a vector database/index.

# Then:

# User Question
#       ↓
# Create query embedding
#       ↓
# Search vector database
#       ↓
# Find similar vectors
#       ↓
# Retrieve relevant documents

# This is a major building block of RAG.

# 🔥 STEP 13 — RAG Connection

# You will learn RAG later in your roadmap, but understand the basic idea now.

# RAG = Retrieval-Augmented Generation

# Simplified:

#              USER
#                ↓
#           Question
#                ↓
#           Embedding
#                ↓
#        Vector Search
#                ↓
#       Relevant Documents
#                ↓
#              LLM
#                ↓
#         Final Answer

# This allows an AI application to retrieve relevant information before generating an answer.

# 5
# 🧠 STEP 14 — How Do We Compare Embeddings?

# Suppose:

# Vector A
# =
# [0.2, 0.8, 0.4]

# Vector B
# =
# [0.3, 0.7, 0.5]

# We want to know:

# How similar are these vectors?

# One popular measure is:

# Cosine Similarity

# The formula is:

# You don't need to memorize the mathematics today.

# The intuition is:

# Vectors pointing in similar directions
#           ↓
#       high similarity

# Vectors pointing in different directions
#           ↓
#       low similarity
# 🧭 STEP 15 — Visualizing Cosine Similarity

# Imagine two arrows:

# Vector A
#    ↗

# Vector B
#    ↗

# They're pointing in nearly the same direction.

# Therefore:

# High similarity

# Now:

# Vector A
#    ↗

# Vector B
#    ↘

# Very different directions:

# Low similarity

# The magnitude and exact similarity behavior depend on the vectors and metric, but direction is the key intuition behind cosine similarity.

# 💻 STEP 16 — Your First Embedding Experiment

# Now let's actually create embeddings.

# We'll use the Hugging Face ecosystem.

# Install:

# pip install sentence-transformers

# Create:

# week8_day4_embeddings.py

# Then:

# from sentence_transformers import SentenceTransformer

# model = SentenceTransformer(
#     "all-MiniLM-L6-v2"
# )

# sentences = [
#     "I love programming.",
#     "I enjoy coding.",
#     "The weather is rainy today."
# ]

# embeddings = model.encode(sentences)

# print(embeddings)

# You will get numerical vectors.

# 🔢 STEP 17 — Check Their Shape

# Add:

# print(
#     "Embedding shape:",
#     embeddings.shape
# )

# For this particular model, you should see something like:

# (3, 384)

# Meaning:

# 3 sentences
# ×
# 384-dimensional embedding

# The exact dimensions depend on the embedding model.

# 🧠 STEP 18 — Print One Embedding
# print(embeddings[0])

# You'll see many numbers:

# [ 0.034...
#  -0.092...
#   0.117...
#  ...
# ]

# Don't try to interpret each individual number.

# The important thing is:

# Sentence
#    ↓
# 384-dimensional vector

# for this particular model.

# 🔥 STEP 19 — Calculate Similarity

# Now:

# from sklearn.metrics.pairwise import cosine_similarity

# similarity = cosine_similarity(
#     [embeddings[0]],
#     [embeddings[1]]
# )

# print(
#     "Similarity:",
#     similarity[0][0]
# )

# This compares:

# "I love programming."

#         VS

# "I enjoy coding."

# Now compare:

# similarity2 = cosine_similarity(
#     [embeddings[0]],
#     [embeddings[2]]
# )

# print(
#     "Similarity 2:",
#     similarity2[0][0]
# )

# This compares:

# "I love programming."

#         VS

# "The weather is rainy today."

# You should generally expect the first pair to have higher semantic similarity than the second.

# The exact numerical values can vary by model/version/environment.

# 🧪 STEP 20 — Your Own Experiment

# Try:

# sentences = [
#     "Java is a programming language.",
#     "Python is a programming language.",
#     "Spring Boot is used for backend development.",
#     "I went to the market to buy vegetables.",
#     "The weather is very pleasant today."
# ]

# Generate embeddings.

# Then compare:

# Java ↔ Python
# Java ↔ Spring Boot
# Java ↔ vegetables
# Java ↔ weather

# Think about which pairs you expect to be closest.

# 🔥 STEP 21 — Your Java/Spring Boot Connection

# This is where your previous experience becomes useful.

# Imagine you build a Spring Boot application containing:

# 1000 CSIR research documents

# You could create:

# Document
#    ↓
# Embedding
#    ↓
# Vector Database

# Then a researcher asks:

# "Find research related to machine learning
# for biological applications."

# The application can:

# Question
#    ↓
# Embedding
#    ↓
# Vector Search
#    ↓
# Relevant CSIR documents
#    ↓
# LLM
#    ↓
# Answer

# Eventually, you'll learn how to implement architectures like this.

# 🧠 STEP 22 — The Complete Picture So Far

# You now have:

#                 USER TEXT
#                     ↓
#                TOKENIZATION
#                     ↓
#                   TOKENS
#                     ↓
#                 TOKEN IDs
#                     ↓
#                EMBEDDINGS
#                     ↓
#              TRANSFORMER
#                     ↓
#                 ATTENTION
#                     ↓
#               LLM OUTPUT

# Today we focused on:

# TOKEN IDs
#     ↓
# EMBEDDINGS
#     ↓
# VECTOR REPRESENTATION
# ⚠️ VERY IMPORTANT DISTINCTION

# Don't confuse these three:

# 1️⃣ Token

# Piece of text.

# "Python"
# 2️⃣ Token ID

# Integer identifier.

# 18750
# 3️⃣ Embedding

# Vector representation.

# [0.12, -0.54, 0.81, ...]

# Remember:

# Token
#  ↓
# Token ID
#  ↓
# Embedding