# So far, you learned the complete foundation:

# Generative AI
#      ↓
# LLMs
#      ↓
# Tokens
#      ↓
# Embeddings
#      ↓
# Transformers
#      ↓
# Attention
#      ↓
# PROMPT ENGINEERING
#      ↓
# FIRST LLM APP 🚀

# Today, we move from understanding AI concepts to actually building with an LLM.

# 🎯 TODAY'S GOALS

# By the end of today, you will understand:

# What is a prompt?
# What is prompt engineering?
# Why prompts matter
# System vs user instructions
# Zero-shot prompting
# Few-shot prompting
# Role prompting
# Structured prompts
# Prompt templates
# Build your first simple LLM app
# 1️⃣ WHAT IS A PROMPT?

# A prompt is the input or instruction you give to an AI model.

# Example:

# Explain machine learning.

# This is a prompt.

# Another example:

# Explain machine learning to a beginner using a real-world example.

# This is also a prompt—but it gives the model more context and instructions.

# The output can therefore be more useful.

# Basic flow
# USER
#   ↓
# PROMPT
#   ↓
# LLM
#   ↓
# GENERATED RESPONSE
# 2️⃣ WHAT IS PROMPT ENGINEERING?

# Prompt engineering means designing instructions and context so the model can produce a response that better matches your goal.

# Think of these two prompts:

# ❌ Weak prompt
# Explain Python.
# ✅ Better prompt
# You are a Python instructor.

# Explain Python to a complete beginner.

# Include:
# 1. Definition
# 2. Real-world example
# 3. Simple code example
# 4. Common beginner mistakes

# Keep the explanation under 300 words.

# The second prompt clearly specifies:

# ROLE
#  ↓
# You are a Python instructor

# TASK
#  ↓
# Explain Python

# AUDIENCE
#  ↓
# Complete beginner

# FORMAT
#  ↓
# Definition + example + code + mistakes

# CONSTRAINT
#  ↓
# Under 300 words

# This is a useful prompt structure.

# 3️⃣ THE PROMPT FORMULA YOU SHOULD REMEMBER

# For your AI Engineer learning journey, use:

# ROLE
#  +
# TASK
#  +
# CONTEXT
#  +
# FORMAT
#  +
# CONSTRAINTS

# Example:

# ROLE:
# You are an experienced Java backend developer.

# TASK:
# Explain Spring Boot dependency injection.

# CONTEXT:
# I know Java basics but I am learning Spring Boot.

# FORMAT:
# Use step-by-step explanation and a simple code example.

# CONSTRAINTS:
# Keep it beginner-friendly and under 500 words.

# This structure will be very useful for your future AI applications, including BioLingua AI and your CSIR-related projects.

# 4️⃣ ZERO-SHOT PROMPTING

# Zero-shot means asking the model to perform a task without giving it examples.

# Example:

# Classify this review as Positive, Negative, or Neutral:

# "The application is very easy to use."

# The model receives no examples. It simply performs the task.

# Flow
# Instruction
#     ↓
#     LLM
#     ↓
# Answer
# 5️⃣ FEW-SHOT PROMPTING

# Few-shot prompting means giving the model a few examples before asking it to perform the task.

# Example:

# Classify sentiment.

# Review: "This product is excellent."
# Sentiment: Positive

# Review: "I hate this product."
# Sentiment: Negative

# Review: "The product arrived yesterday."
# Sentiment:

# The examples demonstrate the expected pattern.

# Flow
# Examples
#    +
# New Input
#      ↓
#     LLM
#      ↓
# Answer following the pattern
# 6️⃣ ROLE PROMPTING

# You can tell the model what perspective or expertise to use.

# Example:

# You are an AI Engineer.

# Explain embeddings to a Java developer.

# Another:

# You are a senior Java Spring Boot developer.

# Review this backend architecture and identify potential problems.

# The role helps establish the desired perspective, but it does not guarantee expertise or correctness. You should still verify important results.

# 7️⃣ STRUCTURED PROMPTING

# You can explicitly specify the output format.

# For example:

# Explain Neural Networks.

# Return the answer in this format:

# Definition:
# ...

# Real-world example:
# ...

# Important components:
# ...

# Summary:
# ...

# This is useful when building applications because predictable output is easier for software to process.

# For example:

# User Input
#     ↓
# Prompt Template
#     ↓
# LLM
#     ↓
# Structured Response
#     ↓
# Your Application
# 8️⃣ PROMPT TEMPLATE

# A prompt template contains fixed instructions plus dynamic user input.

# Example:

# You are an AI teacher.

# Explain the following topic to a beginner:

# Topic: {topic}

# Include:
# 1. Definition
# 2. Example
# 3. Key concepts

# If:

# topic = "Embeddings"

# Your application effectively sends:

# You are an AI teacher.

# Explain the following topic to a beginner:

# Topic: Embeddings

# Include:
# 1. Definition
# 2. Example
# 3. Key concepts

# This is important for AI Engineering.

# FIXED PROMPT
#       +
# USER INPUT
#       ↓
# FINAL PROMPT
#       ↓
# LLM
#       ↓
# RESPONSE
# 9️⃣ WHY PROMPTS MATTER

# Suppose you ask:

# Tell me about Java.

# The request is broad.

# Now:

# You are a Java instructor.

# Explain Java Collections to a beginner who already understands
# arrays.

# Compare List, Set, and Map.

# Give one Java example for each.

# End with a comparison table.

# This gives the model:

# Clear task
# Audience
# Context
# Expected output
# Structure

# Usually, a well-specified request makes it easier for the model to provide a relevant answer.

# 🔟 YOUR FIRST PROMPT TEMPLATE IN PYTHON

# Create a file:

# week8_day7_prompt.py

# Write:

topic = input("Enter a topic: ")

prompt = f"""
You are an AI instructor.

Explain {topic} to a beginner.

Include:
1. Simple definition
2. Real-world example
3. Important concepts
4. Short summary

Keep the answer easy to understand.
"""

print(prompt)

# Run it:

# python week8_day7_prompt.py

# Try:

# Enter a topic: Machine Learning

# This program does not call an LLM yet.

# It teaches you the first AI Engineering concept:

# Your Python application can dynamically construct prompts.

# 1️⃣1️⃣ NOW: BUILD YOUR FIRST LLM APP

# The architecture is:

# USER
#   ↓
# Python Application
#   ↓
# Prompt
#   ↓
# LLM
#   ↓
# Response
#   ↓
# Display Result

# Your first app will ask:

# What do you want to learn?

# Then send the topic to an LLM and display an AI-generated explanation.

# 1️⃣2️⃣ CREATE THE PROJECT FOLDER

# Since you previously mentioned using:

# C:\Users\HP\Desktop\AI Engineer

# create this folder:

# C:\Users\HP\Desktop\AI Engineer\Week8_GenAI

# Inside it, create:

# week8_day7_first_llm_app.py
# 1️⃣3️⃣ OPTION A — FIRST LLM APP USING AN API

# A typical production-style architecture looks like:

# Python App
#     ↓
# Environment Variable
#     ↓
# API Key
#     ↓
# LLM API
#     ↓
# AI Response

# Important security rule:

# NEVER put your secret API key directly into GitHub code.

# Use environment variables instead.

# A generic Python pattern is:

# import os

# api_key = os.getenv("YOUR_API_KEY_NAME")

# Your actual code depends on the LLM provider and SDK you choose.

# 1️⃣4️⃣ SIMPLE FIRST LLM APP WITHOUT AN API

# Before connecting a real provider, let's understand the application flow.

# Create:

# topic = input("What do you want to learn? ")

# prompt = f"""
# You are an expert AI instructor.

# Explain {topic} to a beginner.

# Use:
# 1. Simple language
# 2. One real-world example
# 3. Step-by-step explanation
# 4. A short summary
# """

# print("\n--- PROMPT SENT TO LLM ---")
# print(prompt)

# print("\n--- SIMULATED AI RESPONSE ---")
# print(f"AI would now generate an explanation about: {topic}")

# Run:

# python week8_day7_first_llm_app.py

# Example:

# What do you want to learn? Embeddings

# Flow:

# User enters:
# Embeddings
#        ↓
# Python creates prompt
#        ↓
# Prompt is sent to an LLM
#        ↓
# LLM generates response
#        ↓
# Application displays response
# 1️⃣5️⃣ REAL APPLICATION FLOW

# When we connect a real LLM later, your application will conceptually work like this:

# ┌──────────────┐
# │ User Input   │
# └──────┬───────┘
#        ↓
# ┌──────────────┐
# │ Python App   │
# └──────┬───────┘
#        ↓
# ┌──────────────┐
# │ Prompt Build │
# └──────┬───────┘
#        ↓
# ┌──────────────┐
# │ LLM API      │
# └──────┬───────┘
#        ↓
# ┌──────────────┐
# │ AI Response  │
# └──────┬───────┘
#        ↓
# ┌──────────────┐
# │ Display      │
# └──────────────┘

# This basic pattern appears again and again in AI Engineering.

# 1️⃣6️⃣ YOUR BIO LINGUA AI CONNECTION 🐦🐕

# Your future flagship project BioLingua AI can eventually follow a more advanced architecture:

# Animal / Bird Sound
#         ↓
# Audio Processing
#         ↓
# AI Model
#         ↓
# Sound Classification
#         ↓
# Pattern Analysis
#         ↓
# Context / Behaviour Information
#         ↓
# AI Interpretation
#         ↓
# Human-Readable Output

# LLMs may help with explanations, interaction, reasoning over retrieved context, and presenting model outputs, but they alone would not automatically translate animal language.

# This is an example of how your roadmap is gradually preparing you for larger AI systems.

# 1️⃣7️⃣ YOUR CSIR / FTR PROJECT CONNECTION

# Imagine a future FTR AI assistant:

# User:
# "Show delayed projects with low publication output."
#            ↓
#       User Question
#            ↓
#        Prompt / Query
#            ↓
# Database + Retrieval
#            ↓
# Relevant FTR Data
#            ↓
# LLM
#            ↓
# Answer:
# "Here are the relevant projects..."

# Later, when you learn RAG, you'll be able to build this more realistically using:

# Documents / Database
#        ↓
# Embeddings
#        ↓
# Vector Search / Retrieval
#        ↓
# Relevant Context
#        ↓
# Prompt
#        ↓
# LLM
#        ↓
# Answer
# 1️⃣8️⃣ PROMPT ENGINEERING BEST PRACTICES
# ✅ Be clear

# Instead of:

# Explain AI.

# Use:

# Explain supervised machine learning to a beginner.
# Use a student-exam example.
# Keep it under 300 words.
# ✅ Provide context
# I am a Java backend developer learning AI Engineering.
# Explain APIs used in LLM applications.
# ✅ Specify the format
# Return the answer with:

# 1. Definition
# 2. Example
# 3. Code
# 4. Common mistakes
# ✅ Specify constraints
# Use simple English.
# Do not use advanced mathematics.
# Keep the answer under 500 words.
# 1️⃣9️⃣ A STRONG PROMPT TEMPLATE

# Save this template:

# ROLE:
# You are a/an [ROLE].

# TASK:
# [What should the model do?]

# CONTEXT:
# [Relevant background information]

# INPUT:
# [User data/question]

# OUTPUT FORMAT:
# [How should the answer be structured?]

# CONSTRAINTS:
# [Rules, limits, tone, length]

# Example:

# ROLE:
# You are an AI Engineering instructor.

# TASK:
# Explain embeddings.

# CONTEXT:
# The student has learned Python, Machine Learning,
# Deep Learning, Tokens, and LLM basics.

# INPUT:
# Explain how embeddings are used in semantic search.

# OUTPUT FORMAT:
# 1. Definition
# 2. Step-by-step flow
# 3. Real-world example
# 4. Python example
# 5. Summary

# CONSTRAINTS:
# Use beginner-friendly English.
# Explain technical terms simply.