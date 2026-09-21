def create_teacher_prompt(topic):
    prompt=f"""
    You are an expert AI/ML instructor.
    Explain the following topic to a begineer:
    Topic:
    {topic}
    Your answer should include:
    1-simple definition
    2-Real-world examples
    3-Technical explanation
    4-Important Points
    5-Short Summary
    Use simple and clear language.
    """
    return prompt

topic=input("Enter an AI/ML topic:")

prompt=create_teacher_prompt(topic)
print("\n ==================================")
print(prompt)
