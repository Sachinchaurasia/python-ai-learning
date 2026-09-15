# 💻 TASK 4 — BUILD THE APP FLOW

# Create:

# week8_day7_first_llm_app.py
# topic = input("What do you want to learn? ")

# prompt = f"""
# You are an AI instructor.

# Explain {topic} to a beginner.

# Include:
# 1. Definition
# 2. Real-world example
# 3. Important concepts
# 4. Summary

# Use simple English.
# """

# print("\n--- PROMPT ---")
# print(prompt)

# print("\n--- APPLICATION FLOW ---")
# print("User Input → Prompt → LLM → Response")

# print(f"\nThe application is ready to send a request about: {topic}")


####################################################################################################################
# Create a new Python file:

# week8_day7_first_llm_app.py

# Paste this code into it:

topic = input("What do you want to learn? ")

prompt = f"""
You are an AI instructor.

Explain {topic} to a beginner.

Include:
1. Definition
2. Real-world example
3. Important concepts
4. Summary

Use simple English.
"""

print("\n--- PROMPT ---")
print(prompt)

print("\n--- APPLICATION FLOW ---")
print("User Input → Prompt → LLM → Response")

print(f"\nThe application is ready to send a request about: {topic}")
# ▶️ Run it

# In your terminal:

# python week8_day7_first_llm_app.py

# When it asks:

# What do you want to learn?

# Try:

# Transformers

# You should see:

# --- PROMPT ---

# You are an AI instructor.

# Explain Transformers to a beginner.

# Include:
# 1. Definition
# 2. Real-world example
# 3. Important concepts
# 4. Summary

# Use simple English.

# Then:

# --- APPLICATION FLOW ---
# User Input → Prompt → LLM → Response

# The application is ready to send a request about: Transformers
# 🧠 Understand what you built

# Right now, your Python program does not actually call an LLM.

# It creates the first part of an LLM application:

# User
#   ↓
# Enter Topic
#   ↓
# Python Application
#   ↓
# Prompt Template
#   ↓
# Generated Prompt
#   ↓
# LLM ← 🚧 Next step
#   ↓
# AI Response
# 🔥 Important distinction

# Your previous task generated a prompt dynamically.

# This task creates the application flow around that prompt.

# The next step in a real application would replace:

# Prompt
#  ↓
# print(...)

# with:

# Prompt
#  ↓
# LLM API
#  ↓
# Response
#  ↓
# Display Response

# So you've now reached the point where you can move from "understanding LLMs" to actually connecting Python code to an LLM.