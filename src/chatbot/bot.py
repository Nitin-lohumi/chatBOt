# Core chatbot logic (src/chatbot/bot.py)

from .intents import get_intent  # Import intent detection from chatbot/intents.py
from ..services.telemedicine import handle_telemedicine_intent # Import telemedicine handler

def get_bot_response(message):
    # Determine user intent and generate appropriate response
    intent = get_intent(message)
    if intent == "telemedicine":
        return handle_telemedicine_intent(message)
    elif intent == "greeting":
        return "Hello! How can I assist you with your health today?"
    elif intent == "goodbye":
        return "Take care! If you have more questions, feel free to ask."
    else:
        return "Sorry, I didn't understand that. Can you please rephrase?"