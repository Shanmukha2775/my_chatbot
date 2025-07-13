from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import json
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.5-flash")

SESSIONS_FILE = "chat_sessions.json"

def load_sessions():
    if not os.path.exists(SESSIONS_FILE):
        return []
    with open(SESSIONS_FILE, "r") as f:
        try:
            return json.load(f)
        except:
            return []

def save_sessions(sessions):
    with open(SESSIONS_FILE, "w") as f:
        json.dump(sessions, f, indent=2)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/new_chat", methods=["POST"])
def new_chat():
    sessions = load_sessions()
    chat_number = len(sessions) + 1
    session = {
        "session_id": f"chat{chat_number}",
        "title": f"My Chat {chat_number}",
        "messages": []
    }
    sessions.append(session)
    save_sessions(sessions)
    return jsonify({"session_id": session["session_id"]})

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    message = data["message"]
    session_id = data["session_id"]

    try:
        response = model.generate_content(message)
        bot_reply = response.text or "No response from Gemini."
    except Exception as e:
        bot_reply = f"❌ Error: {str(e)}"

    sessions = load_sessions()
    for s in sessions:
        if s["session_id"] == session_id:
            s["messages"].append({"user": message, "bot": bot_reply})
            break
    save_sessions(sessions)

    return jsonify({"reply": bot_reply})

@app.route("/recents")
def recents():
    sessions = load_sessions()
    return jsonify([{"session_id": s["session_id"], "title": s["title"]} for s in sessions])

@app.route("/load_session/<session_id>")
def load_session(session_id):
    sessions = load_sessions()
    for s in sessions:
        if s["session_id"] == session_id:
            return jsonify(s["messages"])
    return jsonify([])

if __name__ == "__main__":
    app.run(debug=True)
