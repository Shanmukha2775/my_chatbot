# General Purpose Chatbot - K-Hub 2025-26

This is a **General-Purpose Chatbot Project** developed for the K-Hub 2025-26 Junior Developer Internship Selection Process.

---

## 🚀 Features:

- Google Gemini API Integration  
- Multiple Chat Sessions (each chat saved with a title like "My Chat 1")  
- WhatsApp Style Recents Menu  
- Attractive and Professional UI (Soft Gradient Colors)  
- Flask Backend + HTML, CSS, JavaScript Frontend  

---

## 📂 Folder Structure:

my_chatbot/
├── app.py -> Backend Flask Code
├── chat_sessions.json -> Chat history storage
├── templates/
│ └── index.html -> Frontend HTML
├── static/
│ └── style.css -> Frontend CSS
├── README.md -> Project documentation
├── .gitignore -> To ignore secret files like .env

---

## ⚙️ How to Run the Project:

### 1️⃣ Install Requirements:

pip install flask google-generativeai python-dotenv
2️⃣ Create .env file:
ini
Copy code
GEMINI_API_KEY=your_gemini_api_key
3️⃣ Run the App:

python app.py
Open your browser:
http://127.0.0.1:5000

📝 How It Works:
New Chat button starts a fresh chat

Send button sends messages to the Gemini API

Recents Menu (☰) shows previous chats

You can load any old chat anytime

👩‍💻 Developed By:
Devaguptapu Venkata Surya Shanmukha
3rd Year - CSM Branch

