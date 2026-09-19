import os
from dotenv import load_dotenv
from google import genai

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

print("API key loaded:", bool(api_key))

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create an interaction
interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input="How many r's are in the word 'strawberry'?"
)

# Print response
print("\nGemini Response:")
print(interaction.output_text)