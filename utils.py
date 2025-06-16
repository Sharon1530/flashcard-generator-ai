# utils.py
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcard_prompt(text, subject=None):
    subject_line = f"The subject is {subject}." if subject else ""
    prompt = f"""
{subject_line}
From the following educational content, generate at least 15 concise flashcards in this format:

Q: <question>
A: <answer>

Text:
"""
{text}
"""
"""
    return prompt

def get_flashcards(text, subject=None):
    prompt = generate_flashcard_prompt(text, subject)
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

def parse_flashcards(raw_text):
    lines = raw_text.strip().split("\n")
    qas = []
    q, a = "", ""
    for line in lines:
        if line.startswith("Q:"):
            q = line[2:].strip()
        elif line.startswith("A:"):
            a = line[2:].strip()
            if q and a:
                qas.append({"Question": q, "Answer": a})
                q, a = "", ""
    return qas
