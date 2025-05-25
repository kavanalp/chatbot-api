# app.py
from flask import Flask, request, jsonify
from openai import OpenAI

import sys


if len(sys.argv) < 2:
    print("Usage: python app.py <id>")
    sys.exit(1)

ape  = sys.argv[1]
print(f"ape: {ape}")



model="ft:gpt-4o-2024-08-06:personal::B3HrC6W4"

client = OpenAI(api_key=ape)

app = Flask(__name__)

@app.route("/")
def home():
    return "Chatbot API is running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_prompt = request.json.get("prompt", "")
    if not user_prompt:
        return jsonify({"error": "Prompt is required"}), 400

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": user_prompt}],
            temperature=0.7
        )
        answer = response.choices[0].message.content
        return jsonify({"response": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
