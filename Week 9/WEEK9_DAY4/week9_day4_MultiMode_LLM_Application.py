# Week 9 - Day 4
# Multi-Mode LLM Application

# --------------------------------------------------
# PROMPT FUNCTIONS
# --------------------------------------------------

from http import client


def teacher_prompt(topic):
    return f"""
You are an expert teacher.

Teach the following topic to a beginner:

Topic: {topic}

Explain:
1. What it is
2. Why it is important
3. How it works
4. Give a simple example
5. Give a practical example

Use simple language.
"""


def interviewer_prompt(topic):
    return f"""
You are a technical interviewer.

Conduct an interview about:

Topic: {topic}

Ask one question at a time.

Start with a basic question.
Based on the user's answer, gradually increase the difficulty.

Do not provide the answer immediately.
"""


def coding_prompt(problem):
    return f"""
You are an expert coding assistant.

Solve the following programming problem:

Problem:
{problem}

Provide:
1. Approach
2. Explanation
3. Code
4. Example
5. Time complexity
6. Space complexity

Write clean and beginner-friendly code.
"""


# --------------------------------------------------
# LLM SERVICE
# --------------------------------------------------

def call_llm(prompt):

    # Connect your LLM API here

    response = client.models.generate_content(
        model="YOUR_MODEL_NAME",
        contents=prompt
    )

    return response.text


# --------------------------------------------------
# USER INTERFACE
# --------------------------------------------------

mode = input("""
Choose AI mode:

1. Teacher
2. Interviewer
3. Coding Assistant

Enter choice:
""")


# --------------------------------------------------
# MODE SELECTION
# --------------------------------------------------

if mode == "1":

    topic = input("Enter topic: ")

    prompt = teacher_prompt(topic)


elif mode == "2":

    topic = input("Enter interview topic: ")

    prompt = interviewer_prompt(topic)


elif mode == "3":

    problem = input("Enter coding problem: ")

    prompt = coding_prompt(problem)


else:

    print("Invalid choice")
    prompt = None


# --------------------------------------------------
# SEND TO LLM
# --------------------------------------------------

if prompt:

    response = call_llm(prompt)

    print("\n==============================")
    print("AI RESPONSE")
    print("==============================")

    print(response)