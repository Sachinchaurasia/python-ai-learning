topic=input("What do you want to learn?")
prompt=f"""
You are an expert AI Instructor.
Explain{topic} to a beginner.
Use:
1-Simple Language.
2-One real-world example.
3-Step -by-Step explanation
4-A short summary.
"""
print("\n--- Prompt sent to LLM---")
print(prompt)

print("\n---Simulated AI Response---")

print(f" AI would now generate an explanation about{topic}")


