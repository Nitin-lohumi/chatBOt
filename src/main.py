# Main entry point for the chatbot web API (src/main.py)

from flask import Flask, request, jsonify
from chatbot.bot import get_bot_response  # Import chatbot logic from chatbot/bot.py

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    # Receives user message and returns chatbot response
    user_message = request.json.get('message')
    response = get_bot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)