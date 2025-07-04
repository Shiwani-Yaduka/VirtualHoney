from flask import Flask, request, jsonify
from flask_cors import CORS
from chat_model import ai_bf_response
from utils import extract_messages

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  # ✅ Allow all origins

# Load chat context
context = " ".join(extract_messages("data/whatsapp_chat.txt"))

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message")
    reply = ai_bf_response(user_msg, context)
    return jsonify({"response": reply})

@app.route("/")
def home():
    return "AI Boyfriend Backend is Running 💖"

if __name__ == "__main__":
    app.run(debug=True)
