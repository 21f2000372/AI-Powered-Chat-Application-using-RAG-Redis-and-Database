from flask import Flask, request, jsonify, render_template
from rag_engine import get_rag_answer
from db import init_db, store_message, get_messages

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"error": "user_id and message required"}), 400

    answer = get_rag_answer(message)
    store_message(user_id, message, answer)

    return jsonify({"user_id": user_id, "question": message, "answer": answer})

@app.route("/history/<user_id>", methods=["GET"])
def history(user_id):
    messages = get_messages(user_id)
    return jsonify(messages)

if __name__ == "__main__":
    app.run(debug=True)
