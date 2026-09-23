import os

from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI


load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found.")

client = OpenAI(api_key=api_key)

def load_documents(folder):

    documents = []

    for filename in os.listdir(folder):

        filepath = os.path.join(folder, filename)

        if filename.endswith(".txt"):

            with open(filepath, "r", encoding="utf-8") as file:

                text = file.read()

                documents.append({
                    "filename": filename,
                    "text": text
                })

    return documents

documents = load_documents("documents")

print("Documents loaded:", len(documents))

