# 📚 AI Flashcard Generator

A lightweight tool that generates study-ready flashcards (Q&A format) from any educational content using GPT-3.5.  
Built for the **ShelfEx AI/ML Internship – Summer/Fall 2025**.

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
```

### 2. Set up a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Add your OpenAI API key

Create a `.env` file in the root directory and add:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

> Or add this as a **secret** in Streamlit Cloud.

---

## ▶️ Run the App Locally

```bash
streamlit run app.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🌐 Deployment on Streamlit Cloud

The app is also deployed and accessible at:  
👉 [https://your-username.streamlit.app
](https://flashcard-generator-ai-mpaln8fuzbn94tkvjgnu5y.streamlit.app)

To enable GPT generation:
1. Go to **Settings > Secrets**
2. Add:

```toml
OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

3. Click **Save** and **Redeploy**

---

## 📝 Example Output

```
📌 Topic: Photosynthesis  
🎯 Difficulty: Easy  
Q: What is photosynthesis?  
A: It is the process by which green plants use sunlight to synthesize food from carbon dioxide and water.

📌 Topic: Cell Structure  
🎯 Difficulty: Medium  
Q: What is the function of mitochondria?  
A: It is the powerhouse of the cell, generating ATP.
```

---

## 📦 Export Formats

- ✅ CSV  
- ✅ JSON  

**Planned extensions:**
- Anki/Quizlet support  
- Multi-language flashcards  
- Editable flashcards before export

---

## 🎬 Demo Video

> A short walkthrough is available [here](#)  
(*Upload your Loom or QuickTime demo link here once ready*)

---

## 🛠 Tech Stack

- **Language:** Python 3  
- **Frontend/UI:** Streamlit  
- **LLM API:** OpenAI GPT-3.5 (`openai==0.28.1`)  
- **PDF Parsing:** PyMuPDF  
- **Environment:** `.env` + `dotenv`

---

## 📄 License

MIT — feel free to use, fork, and improve with attribution.

---

## 🙏 Acknowledgment

This app was built as part of the **ShelfEx AI/ML Engineer Internship Task – Summer/Fall 2025**.
