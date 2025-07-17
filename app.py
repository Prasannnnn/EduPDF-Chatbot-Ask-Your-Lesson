import streamlit as st
import fitz  # PyMuPDF
import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai

# --------------- SETUP ----------------
st.set_page_config(page_title="EduPDF Chatbot", layout="centered")
st.title("📚 EduPDF Chatbot – Ask Your Lesson")

# --------------- GEMINI API SETUP ----------------
api_key = st.secrets["GEMINI_API_KEY"] if "GEMINI_API_KEY" in st.secrets else st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("models/gemini-1.5-flash")

# --------------- PDF UPLOAD ----------------
uploaded_file = st.file_uploader("📄 Upload a Lesson PDF", type=["pdf"])
if uploaded_file:
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        full_text = ""
        for page in doc:
            full_text += page.get_text()

    st.success("✅ Text extracted from PDF successfully!")

    # --------------- TEXT CHUNKING ----------------
    def chunk_text(text, chunk_size=500):
        words = text.split()
        return [" ".join(words[i:i + chunk_size]) for i in range(0, len(words), chunk_size)]

    chunks = chunk_text(full_text)

    # --------------- EMBEDDING & FAISS ----------------
    st.info("🔍 Embedding and indexing content...")
    embedder = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = embedder.encode(chunks)

    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(embeddings))

    st.success("✅ Embeddings indexed with FAISS!")

    # --------------- CHATBOT UI ----------------
    st.markdown("### 💬 Ask a Question About the Lesson")
    user_question = st.text_input("Your question:", placeholder="e.g., What is photosynthesis?")

    if user_question:
        query_embedding = embedder.encode([user_question])
        distances, indices = index.search(np.array(query_embedding), k=5)
        relevant_chunks = [chunks[i] for i in indices[0]]
        context = "\n".join(relevant_chunks)

        prompt = f"""
        You are an education assistant helping a student.
        Use the following context to answer the question as clearly and accurately as possible.

        Context:
        {context}

        Question:
        {user_question}
        """

        with st.spinner("Thinking... 🤔"):
            response = model.generate_content(prompt)
            st.markdown("### 🤖 Answer:")
            st.markdown(response.text)
