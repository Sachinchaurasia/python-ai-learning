# Today we move from “What is an LLM?” to one of the most important ideas behind how LLMs process text:

# LLMs don't directly read words like humans do. They process tokens.

# This concept will become the foundation for Embeddings → Transformers → Attention → LLM applications.

# 🎯 Today's Learning Goals

# By the end of Day 3, you should understand:

# Text
#  ↓
# Tokenization
#  ↓
# Tokens
#  ↓
# Token IDs
#  ↓
# Embeddings
#  ↓
# LLM

# We'll learn:

# What is a token?
# What is tokenization?
# Word vs token
# Subword tokens
# Token IDs
# Why tokenization matters
# Context length
# Tokens and LLM cost
# Special tokens
# Practical tokenization experiment
# 🧠 STEP 1 — What Is a Token?

# A token is a piece of text that an LLM processes.

# A token can be:

# a whole word
# part of a word
# punctuation
# a space/prefix attached to a word
# sometimes other special symbols

# For example, conceptually:

# "Hello world!"

# might become something like:

# ["Hello", " world", "!"]

# The exact tokens depend on the tokenizer used by the particular model.

# ⚠️ Important: There is no universal rule that says "one word = one token."

# 🧩 STEP 2 — What Is Tokenization?

# Tokenization means:

# Converting text into tokens that a language model can process.

# Think of it like cutting a sentence into pieces.

# Original text

# "I love Python."

#         ↓

# Tokenization

# ["I", " love", " Python", "."]

# Then those tokens are converted into numbers.

# Tokens
#    ↓
# Token IDs
#    ↓
# Neural Network
# 🔥 STEP 3 — Why Can't the LLM Directly Read Text?

# Neural networks operate on numbers.

# You learned this in Week 7.

# Your neural network received numerical features:

# Study Hours = 8
# Attendance = 90
# Previous Score = 85

# It couldn't directly process:

# "Student will pass"

# without representing that information numerically.

# Similarly, an LLM needs to convert text into numerical representations.

# The simplified process is:

# Human Text
#     ↓
# Tokenizer
#     ↓
# Tokens
#     ↓
# Token IDs
#     ↓
# Model
# 🧩 STEP 4 — Word vs Token

# This is where many beginners get confused.

# You might think:

# 1 word = 1 token

# ❌ Not necessarily.

# For example, a tokenizer could represent:

# "playing"

# as:

# ["play", "ing"]

# And:

# "unbelievable"

# could be divided into multiple pieces.

# The exact split depends on the tokenizer.

# So remember:

# A token is not necessarily a complete word.

# 🧠 STEP 5 — Why Use Subword Tokens?

# Suppose we tried to create one token for every possible word.

# English alone has a huge vocabulary.

# Then consider:

# play
# plays
# played
# playing
# playfully
# player
# players
# ...

# Instead, tokenizers can break words into reusable pieces.

# For example, conceptually:

# play
# playing
# played
# player

# can share pieces related to:

# play

# This allows the model to handle a much larger variety of text without needing a separate vocabulary entry for every possible word.

# 🌍 STEP 6 — Tokens Are Not Only English Words

# Tokenizers can process:

# English
# Hindi
# Chinese
# French
# Spanish
# Java
# Python
# JSON
# SQL
# numbers
# punctuation

# For example:

# "Hello!"

# contains both:

# Hello
# !

# The punctuation can itself be represented as a token or part of a token depending on the tokenizer.

# 💻 STEP 7 — Programming Code Also Gets Tokenized

# This is especially relevant to you as a Java developer.

# Suppose you give an LLM:

# def add(a, b):
#     return a + b

# The model doesn't receive this as one giant piece of text.

# The tokenizer converts it into tokens representing pieces of the code.

# Conceptually:

# def
# add
# (
# a
# ,
# b
# )
# :
# return
# a
# +
# b

# The exact tokenization will depend on the model/tokenizer.

# So:

# Natural Language
#         ↓
#       Tokens

# Programming Code
#         ↓
#       Tokens

# This is why LLMs can work with programming languages as well.

# 🔢 STEP 8 — What Is a Token ID?

# The tokenizer has a vocabulary.

# Each token is associated with an integer ID.

# For example, this is only a simplified illustration:

# Token        ID
# ----------------
# Hello        1542
# world        2871
# Python       921
# !            33

# So:

# "Hello world!"

# could become:

# ["Hello", " world", "!"]

# and then:

# [1542, 2871, 33]

# ⚠️ These numbers are illustrative only. Actual IDs depend on the specific tokenizer.

# 🧠 STEP 9 — Why Token IDs?

# Because neural networks work with numerical input.

# The simplified pipeline is:

# "I love Python"
#        ↓
#    Tokenizer
#        ↓
# ["I", " love", " Python"]
#        ↓
#  Token IDs
#        ↓
# [...numbers...]
#        ↓
#    Embeddings
#        ↓
#  Neural Network

# And tomorrow we'll focus on that important middle step:

# Embeddings
# 🔥 STEP 10 — Tokenization → Embeddings

# This is the connection you need to remember.

# TEXT
#  ↓
# TOKENIZATION
#  ↓
# TOKENS
#  ↓
# TOKEN IDs
#  ↓
# EMBEDDINGS
#  ↓
# TRANSFORMER
#  ↓
# PREDICTION

# Today:

# Text → Tokens → IDs

# Tomorrow:

# Token IDs → Embeddings

# Later:

# Embeddings → Transformer → Attention
# 🧠 STEP 11 — What Is a Tokenizer?

# A tokenizer is the component that converts text into tokens/token IDs according to a particular tokenization scheme.

# Conceptually:

#                     TOKENIZER

# "I love AI"
#      ↓
# ["I", " love", " AI"]
#      ↓
# [ID1, ID2, ID3]

# Different models can use different tokenizers.

# Therefore:

# The same sentence can produce different token sequences and token counts with different tokenizers.

# 📏 STEP 12 — Why Does Token Count Matter?

# This is extremely important for LLM applications.

# LLMs have a limited context window.

# Think of the context window as the amount of tokenized information the model can consider in a single request.

# For example:

# Context Window
# ┌─────────────────────────────┐
# │ Token Token Token Token ... │
# └─────────────────────────────┘

# If your input becomes extremely large, it can exceed the model's context limit.

# That's why AI engineers care about:

# Token count
# Context length
# Prompt size
# Document size
# Output length
# 💰 STEP 13 — Tokens and API Cost

# When you eventually build LLM applications, you'll encounter pricing based partly on tokens.

# A simplified idea is:

# Input tokens
#      +
# Output tokens
#      ↓
# Total token usage

# For example:

# User prompt
#     ↓
# 100 input tokens

# Model response
#     ↓
# 300 output tokens

# Total
#     ↓
# 400 tokens

# Actual pricing depends on the specific model/provider and may distinguish input, output, cached, or other token categories.

# So an AI engineer should understand tokens not just theoretically, but also operationally.

# 🔐 STEP 14 — Special Tokens

# Some tokenization systems use special tokens to represent things such as:

# Beginning/end of a sequence
# Padding
# Unknown tokens
# Other control information

# For example, conceptually:

# <START>
# Hello
# world
# <END>

# The exact special tokens and their behavior depend on the tokenizer/model.

# Don't memorize particular token names yet.

# STEP 15 — YOUR FIRST TOKENIZATION EXPERIMENT

# Now let's make this practical.

# We're going to use a tokenizer library to see how text is actually broken down.

# Create:

# week8_day3_tokenization.py

# For this exercise, install the Hugging Face transformers library if you don't already have it:

# pip install transformers


from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
    "bert-base-uncased"
)

text = "I love Python and Machine Learning."

tokens = tokenizer.tokenize(text)

print("Text:")
print(text)

print("\nTokens:")
print(tokens)

# You may see output similar to:

# Tokens:
# ['i', 'love', 'python', 'and', 'machine', 'learning', '.']

# The exact behavior comes from this tokenizer.


# STEP 16 — Get Token IDs

# Now:

token_ids = tokenizer.convert_tokens_to_ids(tokens)

print("\nToken IDs:")
print(token_ids)

# You'll get numbers such as:

# [1045, 2293, 18750, ...]

# Again, these IDs belong specifically to the tokenizer you're using.

##############################################################################
# 🧠 STEP 17 — See Both Together

# Use:

for token, token_id in zip(tokens, token_ids):
    print(token, "→", token_id)
    
#     You'll get something conceptually like:

# i → 1045
# love → 2293
# python → ...
# and → 1998
# machine → ...
# learning → ...
# . → 1012

# Now you can see the exact connection:

# Token
#   ↓
# Token ID

#################################################################################
# 🔥 STEP 18 — Try Different Sentences

# Change:

text = "I love Python and Machine Learning."

# to:

text = "Sachin is learning Generative AI."

# Then:

tokens = tokenizer.tokenize(text)

print(tokens)

# Try:

# "Spring Boot is a Java framework."

# Then:

# "Artificial Intelligence is changing software development."

# And finally:

# "I am building BioLingua AI."

# Observe how the tokenizer handles different words.

########################################################################################
# 🧪 STEP 19 — Test a Long/Unusual Word

# Try:

text = "unbelievable"
print(tokenizer.tokenize(text))

# Then:

text = "programming"
print(tokenizer.tokenize(text))

# Then:

text = "internationalization"
print(tokenizer.tokenize(text))

# You may see words split into multiple pieces.

# This demonstrates:

# Subword tokenization.

###########################################################################################
# 🧪 STEP 20 — Token Count

# You can also check the number of tokens:

text = "I am learning Generative AI and Large Language Models."

tokens = tokenizer.tokenize(text)

print("Token count:", len(tokens))
print(tokens)

# This is useful when working with:

# RAG
# Long documents
# Chatbots
# LLM APIs
# Prompt engineering

####################################################################################################
# 🧠 STEP 21 — A Very Important Example

# Consider:

# "ChatGPT is amazing!"

# Humans see:

# ChatGPT
# is
# amazing
# !

# But the tokenizer might see:

# Chat
# GPT
# is
# amazing
# !

# or another segmentation.

# The exact answer depends on the tokenizer.

# Therefore:

# Human view ≠ Tokenizer view

# This distinction is critical.

########################################################################################
# 🔥 STEP 22 — Complete Flow

# Now connect today's lesson with Day 2.

# When you type:

# "Explain Java inheritance."

# the simplified process begins:

#                  USER
#                    ↓
#        "Explain Java inheritance."
#                    ↓
#               TOKENIZER
#                    ↓
#         ┌─────────────────────┐
#         │ Tokens              │
#         │ Explain             │
#         │ Java                │
#         │ inheritance         │
#         │ .                   │
#         └─────────────────────┘
#                    ↓
#               Token IDs
#                    ↓
#               Embeddings
#                    ↓
#              Transformer
#                    ↓
#               Prediction
#                    ↓
#           Generated Response
# 
#########################################################################################

# 🧩 STEP 23 — Connect It With Your Week 7 Knowledge

# You already learned:

# Input
#  ↓
# Neurons
#  ↓
# Weights
#  ↓
# Forward Pass
#  ↓
# Prediction
#  ↓
# Loss
#  ↓
# Backpropagation
#  ↓
# Gradient
#  ↓
# Weight Update

# Now LLMs introduce a much richer input pipeline:

# Text
#  ↓
# Tokens
#  ↓
# Token IDs
#  ↓
# Embeddings
#  ↓
# Transformer
#  ↓
# Prediction

# The neural-network fundamentals you learned in Week 7 are therefore not wasted.

# They're the foundation for understanding modern LLMs.
