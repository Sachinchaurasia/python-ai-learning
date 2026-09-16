# TASK 4 — Modify the Python Program

# Start with:

# user_question = input("Ask your AI assistant: ")

# Modify the program so it displays:

# ===== AI APPLICATION =====

# User:
# <question>

# Prompt:
# <your dynamically created prompt>

# Status:
# Sending request to LLM API...

# Response:
# <simulated response>

# Use an f-string.
###################################################################################
# TASK 4 — LLM Application Flow

user_question = input("Ask your AI assistant: ")

# Dynamically create the prompt
prompt = f"""
You are a helpful AI assistant.
Answer the following user question clearly and simply:

{user_question}
"""

# Simulated LLM response
simulated_response = "Attention allows a Transformer to focus on the most relevant parts of the input."

print("\n===== AI APPLICATION =====")

print(f"""
User:
{user_question}

Prompt:
{prompt}

Status:
Sending request to LLM API...

Response:
{simulated_response}
""")


###################################################################
# 🧠 What makes this an f-string?

# This part:

# prompt = f"""
# You are a helpful AI assistant.
# Answer the following user question clearly and simply:

# {user_question}
# """

# The f before the string allows Python to insert the value of:

# {user_question}

# dynamically.

# For example, if the user enters:

# What is attention in Transformers?

# the generated prompt becomes:

# You are a helpful AI assistant.
# Answer the following user question clearly and simply:

# What is attention in Transformers?
# Expected output
# ===== AI APPLICATION =====

# User:
# What is attention in Transformers?

# Prompt:
# You are a helpful AI assistant.
# Answer the following user question clearly and simply:

# What is attention in Transformers?

# Status:
# Sending request to LLM API...

# Response:
# Attention allows a Transformer to focus on the most relevant parts of the input.

# Key AI Engineer concept: the prompt is fixed + user question is dynamic. This is exactly the foundation you'll use when we replace the simulated response with a real LLM API call.