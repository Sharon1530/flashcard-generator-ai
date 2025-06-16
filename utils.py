# utils.py
import openai
import os
from dotenv import load_dotenv
from openai.error import RateLimitError

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcard_prompt(text, subject=None):
    subject_line = f"The subject is {subject}." if subject else ""
    prompt = (
        f"{subject_line}\n"
        "From the following educational content, generate at least 15 concise flashcards in this format:\n\n"
        "Q: <question>\n"
        "A: <answer>\n\n"
        "Text:\n"
        f"""\n{text}\n"""
    )
    return prompt

def get_flashcards(text, subject=None):
    prompt = generate_flashcard_prompt(text, subject)
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response['choices'][0]['message']['content']
    except RateLimitError:
        # Fallback mock response for demo/testing if quota exceeded
        return """
Q: What is photosynthesis?
A: Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.

Q: Where does photosynthesis occur?
A: Photosynthesis occurs in the chloroplasts of plant cells.

Q: What pigment is responsible for absorbing sunlight in plants?
A: Chlorophyll is the pigment that absorbs sunlight.

Q: What are the main reactants of photosynthesis?
A: The main reactants are carbon dioxide and water.

Q: What are the products of photosynthesis?
A: The products are glucose and oxygen.
(Note: Displaying mock flashcards because OpenAI quota was exceeded.)
"""

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
