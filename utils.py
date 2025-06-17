# utils.py
import openai
import os
from dotenv import load_dotenv
from openai import OpenAIError

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_flashcard_prompt(text, subject=None):
    subject_line = f"The subject is {subject}." if subject else ""
    prompt = (
        f"{subject_line}\n"
        "Based on the following content, generate at least 15 flashcards grouped by topic.\n"
        "Each flashcard should include:\n"
        "- A topic heading\n"
        "- A difficulty tag (Easy, Medium, Hard)\n"
        "- Q: <question>\n"
        "- A: <answer>\n\n"
        "Use the following format:\n"
        "### Topic Title\n"
        "[Difficulty]\n"
        "Q: ...\n"
        "A: ...\n\n"
        "Text:\n"
        f"\"\"\"\n{text}\n\"\"\""
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
    except OpenAIError:
        # Fallback mock content
        return """
### Photosynthesis
[Easy]
Q: What is photosynthesis?
A: It is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.

[Medium]
Q: What are the main reactants of photosynthesis?
A: Carbon dioxide and water.

### Cell Structure
[Medium]
Q: What is the function of mitochondria?
A: It is the powerhouse of the cell, generating ATP.

[Hard]
Q: What is the role of the Golgi apparatus?
A: It modifies, sorts, and packages proteins and lipids for secretion or delivery to other organelles.

(Note: Displaying mock flashcards because OpenAI quota was exceeded.)
"""

def parse_flashcards(raw_text):
    lines = raw_text.strip().split("\n")
    qas = []
    topic = ""
    difficulty = ""
    q, a = "", ""

    for line in lines:
        line = line.strip()
        if line.startswith("###"):
            topic = line.replace("###", "").strip()
        elif line.startswith("[") and line.endswith("]"):
            difficulty = line.strip("[]")
        elif line.startswith("Q:"):
            q = line[2:].strip()
        elif line.startswith("A:"):
            a = line[2:].strip()
            if q and a:
                qas.append({
                    "Topic": topic or "General",
                    "Question": q,
                    "Answer": a,
                    "Difficulty": difficulty or "Medium"
                })
                q, a, difficulty = "", "", ""
        elif line.startswith("(") and line.endswith(")"):
            qas.append({"Topic": "Note", "Question": "None", "Answer": line, "Difficulty": "None"})
    return qas
