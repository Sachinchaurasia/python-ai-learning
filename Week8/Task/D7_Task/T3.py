# 💻 TASK 3 — PRACTICAL PYTHON TASK

# Create and run:

# week8_day7_prompt.py
topic = input("Enter a topic: ")

prompt = f"""
ROLE:
You are an expert AI instructor.

TASK:
Explain the given topic.

CONTEXT:
The student is a beginner in AI Engineering.

TOPIC:
{topic}

OUTPUT FORMAT:
1. Definition
2. Real-world example
3. Key concepts
4. Summary

CONSTRAINTS:
Use simple English.
Keep the explanation beginner-friendly.
"""

print("\n--- GENERATED PROMPT ---")
print(prompt)

# Try these topics:

# Embeddings
# Transformers
# Attention Mechanism
# Machine Learning

####################################################################################################################
# Then put this code inside it:
    
    

topic = input("Enter a topic: ")

prompt = f"""
ROLE:
You are an expert AI instructor.

TASK:
Explain the given topic.

CONTEXT:
The student is a beginner in AI Engineering.

TOPIC:
{topic}

OUTPUT FORMAT:
1. Definition
2. Real-world example
3. Key concepts
4. Summary

CONSTRAINTS:
Use simple English.
Keep the explanation beginner-friendly.
"""

print("\n--- GENERATED PROMPT ---")
print(prompt)
# ▶️ Run the program

# Open your terminal in the folder containing the file and run:

# python week8_day7_prompt.py

# For example, enter:

# Embeddings

# You should get something similar to:

# Enter a topic: Embeddings

# --- GENERATED PROMPT ---

# ROLE:
# You are an expert AI instructor.

# TASK:
# Explain the given topic.

# CONTEXT:
# The student is a beginner in AI Engineering.

# TOPIC:
# Embeddings

# OUTPUT FORMAT:
# 1. Definition
# 2. Real-world example
# 3. Key concepts
# 4. Summary

# CONSTRAINTS:
# Use simple English.
# Keep the explanation beginner-friendly.
# 🧠 What did you learn?

# The important part is:

# topic = input("Enter a topic: ")

# The user provides the topic.

# Then:

# {topic}

# dynamically inserts that topic into the prompt.

# So one Python program can generate prompts for:

# Embeddings
# Transformers
# Attention Mechanism
# Machine Learning
# 🔥 AI Engineering connection

# You just built a very small prompt-generation system:

# User Input
#     ↓
# Python
#     ↓
# Prompt Template
#     ↓
# Dynamic Prompt
#     ↓
# LLM (future step)
#     ↓
# AI Response

# This is an important transition from learning prompts to building applications that generate/use prompts dynamically.