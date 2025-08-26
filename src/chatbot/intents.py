# Intent detection logic (src/chatbot/intents.py)

def get_intent(message):
    # Simple rule-based intent detection
    message = message.lower()
    if any(greet in message for greet in ["hello", "hi", "namaste"]):
        return "greeting"
    if any(bye in message for bye in ["bye", "goodbye", "see you"]):
        return "goodbye"
    if any(word in message for word in ["doctor", "medicine", "appointment", "clinic", "health"]):
        return "telemedicine"
    return "unknown"