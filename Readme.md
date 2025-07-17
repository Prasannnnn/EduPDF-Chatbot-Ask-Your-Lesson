# 📚 EduPDF Chatbot – Ask Your PDF Anything (RAG + LLM + Streamlit)

EduPDF Chatbot is a GenAI-powered question-answering system that allows users to upload any educational PDF (lessons, textbooks, handouts) and ask questions about its content. It uses **Retrieval-Augmented Generation (RAG)** with **LangChain**, **FAISS Vector Store**, and **OpenAI/Gemini LLMs** to provide precise, context-aware answers.

## 🚀 Live Demo  
[Click here to try the chatbot](https://edupdf-chatbot-ask-your-leappn-bqca6vtvpgiz2uv3mbr2tm.streamlit.app/)


---

## 🚀 Features

- 📄 Upload educational PDFs
- ❓ Ask any question from the document
- 🧠 Uses RAG (Retrieval-Augmented Generation)
- ⚡ Fast response using FAISS vector store
- 🖥️ Clean, interactive chatbot UI built with Streamlit
- 🔐 Supports `.streamlit/secrets.toml` for API key management

---

## 🧰 Tech Stack

- [LangChain](https://www.langchain.com/)
- [FAISS (Vector DB)](https://github.com/facebookresearch/faiss)
- [OpenAI API](https://platform.openai.com/) or [Gemini 1.5 Flash API](https://ai.google.dev/)
- [PyMuPDF / fitz](https://pymupdf.readthedocs.io/) (PDF reader)
- [Streamlit](https://streamlit.io/)

---

## 📦 Installation

Clone the repo and install dependencies:


## 🔐 Setup API Key
Create a .streamlit/secrets.toml file:

toml
```bash
[api_keys]
openai_api_key = "your-openai-api-key"
```
💡 Alternatively, you can use Gemini API by modifying the llm in the code.

## 📁 File Structure
```bash
edupdf-chatbot/
│
├── app.py                    # Streamlit main app
├── edupdf_chain.py          # PDF loading, vector indexing, and retrieval logic
├── requirements.txt         # Python dependencies
├── .streamlit/secrets.toml  # Your API keys (private)
└── README.md
```
▶️ Run the App
```bash
streamlit run app.py
```

## 📚 Example PDF
You can test the chatbot using this sample education lesson:

Intro to Robotics PDF

## 🧠 How It Works
PDF Loader: Parses your document using PyMuPDF

Text Splitter: Splits text into chunks for vectorization

Vector Store: Stores embeddings in FAISS

Retriever + LLM: LangChain uses RAG to combine chunked retrieval with OpenAI or Gemini for final answers

Streamlit UI: Easy chatbot interface to ask questions interactively

## 📌 Use Cases
Educational chatbots for students

Document-based tutoring

Course material Q&A

PDF knowledge extraction

## 🧑‍💻 Author
# Prasanna B – GitHub
# AI/ML Engineer | Educator | GenAI Enthusiast

## 📝 License
This project is open-source and free to use for educational and non-commercial purposes.

## 🌟 Star This Repo
If you find this project useful, please ⭐ star the repo and share it with others!

---

Let me know if you'd like to:
- Add **Gemini API** support explicitly  
- Include **Streamlit Cloud deployment instructions** in README

Ready to push to GitHub now?