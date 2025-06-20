# app.py (Streamlit frontend)
import streamlit as st
import PyPDF2
import pandas as pd
from utils import get_flashcards, parse_flashcards

st.set_page_config(page_title="AI Flashcard Generator", layout="centered")

st.title("📚 AI Flashcard Generator")
st.caption("Upload content or paste notes, and generate study flashcards with GPT.")

# Upload or paste input
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
pasted_text = st.text_area("Or paste your content here:")
subject = st.text_input("Optional: What is the subject/topic?")

# Button
if st.button("Generate Flashcards"):
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        else:
            text = uploaded_file.read().decode("utf-8")
    else:
        text = pasted_text

    if not text:
        st.warning("Please provide input.")
    else:
        with st.spinner("Generating with GPT-3.5..."):
            flashcard_text = get_flashcards(text, subject)
            flashcards = parse_flashcards(flashcard_text)

        st.success(f"✅ Generated {len(flashcards)} flashcards!")
        
        for fc in flashcards:
            st.markdown(
                f"""
                <div style='font-size: 15px; line-height: 1.6; margin-bottom: 20px'>
                <span style='color: #888'><b>Topic:</b> {fc['Topic']} | <b>Difficulty:</b> {fc['Difficulty']}</span><br><br>
                Q: {fc['Question']}<br>
                A: {fc['Answer']}
                <hr>
                </div>
                """,
                unsafe_allow_html=True
            )

        df = pd.DataFrame(flashcards)

        # Download options
        csv = df.to_csv(index=False).encode('utf-8')
        json = df.to_json(orient="records").encode('utf-8')

        st.download_button("⬇️ Download CSV", csv, file_name="flashcards.csv", mime="text/csv")
        st.download_button("⬇️ Download JSON", json, file_name="flashcards.json", mime="application/json")

# Theme and footer
st.markdown("---")
st.caption("Built with ❤️ by Sharon | Powered by OpenAI | Summer 2025 Internship Task")
