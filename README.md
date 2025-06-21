# 📄 RAG-Powered PDF Chatbot (Flask + OpenAI)

This is a **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions from the content of a PDF file. It uses **Flask** for the backend API, **OpenAI GPT-4o** for answering questions, and stores chat history using **SQLite**.

---

## 🚀 Features

- Ask questions based on the content of a PDF
- Stores chat history per user
- Simple Flask-based API
- Ready for integration with a front-end (like Vue.js)
- Easily extendable with Redis and database of your choice

---

## 🧠 Technologies Used

- **Python 3.9+**
- **Flask**
- **OpenAI GPT-4o**
- **SQLite** (via `sqlite3`)
- **LangChain (optional)**

---

## 🗂️ Project Structure

Task1/
│
├── app.py # Main Flask app
├── rag_engine.py # Logic to extract PDF & answer using OpenAI
├── db.py # Handles database functions
├── requirements.txt # List of Python dependencies
├── .env # Contains OpenAI API Key (excluded from Git)
├── .gitignore # Prevents sensitive & unnecessary files from being pushed
│
├── data/
│ └── sample_doc.pdf # The PDF file to query from
│
├── templates/
│ └── index.html # Frontend HTML page
│
└── static/
└── style.css # Custom CSS for frontend

2. Create a virtual environment


python -m venv venv

# Activate the venv

source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows

3. Install dependencies

pip install -r requirements.txt


4. Add your OpenAI API key
Create a .env file in the root directory:


OPENAI_API_KEY=your_openai_api_key


🧪 Running the App

python app.py


🔌 API Endpoints

1. 🧠 Ask a Question

POST 
http://127.0.0.1:5000/user_id
{
  "user_id": "user12",
  "message": "Why do we need artificial intelligence?"
}

2. 🕓 Get User Chat History
GET 
[/history/<user_id>]

👨‍💻 Author
Ananya Chakraborty
Made for educational and practical use.


