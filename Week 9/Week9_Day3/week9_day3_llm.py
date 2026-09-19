# question=input()
# prompt=create_prompt(question)
# response=call_llm(prompt)
# print(response)


import os
from dotenv import load_dotenv
from openai import OpenAI

#Load environment variables
load_dotenv()

#Get API Key
api_key=os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found")

#Create LLM Client
client=OpenAI(api_key=api_key)


#GEt user Input
question=input("Ask your AI assistant")

#Create prompt
prompt=f""" 
        You are a helpful AI assistant.
        Answer the following question clearly and simply.
        Question:
        {question}"""


#Send request to LLM
response=client.responses.create(
    model="gpt-5-mini",
    input=prompt
)

#Display response

print("\n ==================================")
print("AI Response")

print("=====================================")
print(response.output_text)
