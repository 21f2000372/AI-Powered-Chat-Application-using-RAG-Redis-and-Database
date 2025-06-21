from flask import Flask, request, jsonify, render_template
from rag_engine import get_rag_answer
from db import init_db, store_message, get_messages, user_exists
from redis_cache import cache_message, get_cached_messages





app = Flask(__name__)
init_db()


@app.route("/")
def index():
    return render_template("index.html")



# @app.route("/chat", methods=["POST"])
# def chat():
#     data = request.get_json()
#     user_id = data.get("user_id")
#     message = data.get("message")

#     if not user_id or not message:
#         return jsonify({"error": "user_id and message required"}), 400

#     answer = get_rag_answer(message)
#     store_message(user_id, message, answer)

#     return jsonify({"user_id": user_id, "question": message, "answer": answer})

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_id = data.get("user_id")
    message = data.get("message")

    if not user_id or not message:
        return jsonify({"error": "user_id and message required"}), 400

    answer = get_rag_answer(message)
    store_message(user_id, message, answer)
    cache_message(user_id, message, answer)  #Redis caching

    return jsonify({"user_id": user_id, "question": message, "answer": answer})



@app.route("/cache/<user_id>", methods=["GET"])
def cache_history(user_id):
    messages = get_cached_messages(user_id)
    return jsonify(messages)












# @app.route("/history/<user_id>", methods=["GET"])
# def history(user_id):
#     messages = get_messages(user_id)
#     return jsonify(messages)



@app.route("/history/<user_id>", methods=["GET"])
def history(user_id):
    messages = get_messages(user_id)
    exists = user_exists(user_id)
    return jsonify({
        "user_exists": exists,
        "history": messages
    })












if __name__ == "__main__":
    app.run(debug=True)
