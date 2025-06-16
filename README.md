# 📚 AI Flashcard Generator

A lightweight tool that generates study-ready flashcards (Q&A format) from any educational content using GPT-3.5. Built for the ShelfEx AI/ML Internship (Summer/Fall 2025).

---

## ✨ Features

- ✅ Upload `.txt` or `.pdf` documents OR paste content manually
- ✅ Generates 15+ flashcards via GPT-3.5
- ✅ Supports subject input to guide prompt formatting
- ✅ Automatically falls back to mock data if API quota is exceeded
- ✅ Exports flashcards as `.csv` or `.json`
- ✅ Simple UI built in Streamlit
- ✅ Deployable on [Streamlit Cloud](https://streamlit.io/cloud)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sharon1530/flashcard-generator-ai.git
cd flashcard-generator-ai

---

## 2. Set up a virtual environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
3. Add your OpenAI API key
Create a .env file in the root directory and add your OpenAI key:

OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
Alternatively, set this as a secret in Streamlit Cloud.
▶️ Run the App Locally

streamlit run app.py
Open your browser at: http://localhost:8501

🌐 Deployment on Streamlit Cloud

The app is also deployed and accessible at:
👉 https://your-username.streamlit.app

To enable GPT-based generation in the cloud:

Go to Settings > Secrets for your app
Add:
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
Click Save and redeploy the app.

📝 Example Output

📌 Topic: Photosynthesis  
🎯 Difficulty: Easy  
Q: What is photosynthesis?  
A: It is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.

📌 Topic: Cell Structure  
🎯 Difficulty: Medium  
Q: What is the function of mitochondria?  
A: It is the powerhouse of the cell, generating ATP.
📦 Export Formats

✅ CSV
✅ JSON
Planned extensions:

Anki/Quizlet support
Multi-language flashcards
Editable flashcards before export
🎬 Demo Video

A short walkthrough is available here
(Upload your Loom or QuickTime demo here once recorded)
🛠 Tech Stack

Language: Python 3
Frontend/UI: Streamlit
LLM API: OpenAI GPT-3.5 (via openai==0.28.1)
PDF Parsing: PyMuPDF
Environment: .env + dotenv
📄 License

MIT — feel free to use, fork, and improve with attribution.

🙏 Acknowledgment

This app was built as part of the ShelfEx AI/ML Engineer Internship Task – Summer/Fall 2025.
