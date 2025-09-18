from flask import Blueprint, request, jsonify
from app.utils.gpt_engine import ask_gpt

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/", methods=["POST"])
def chat():
    data = request.json
    question = data.get("question", "")
    response = ask_gpt(question)
    return jsonify({"response": response})
