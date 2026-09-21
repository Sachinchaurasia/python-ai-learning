import os
import json

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)


topic = input("Enter an AI/ML topic: ")


prompt = f"""
Analyze the following AI/ML topic:

{topic}

Return the answer ONLY as valid JSON.

Use exactly this structure:

{{
    "topic": "string",
    "difficulty": "string",
    "definition": "string",
    "use_cases": [
        "string",
        "string",
        "string"
    ]
}}
"""


response = client.responses.create(
    model="gpt-5-mini",
    input=prompt
)


print("\n==============================")
print("RAW AI RESPONSE")
print("==============================")

print(response.output_text)