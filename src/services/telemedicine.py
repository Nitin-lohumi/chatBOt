# Telemedicine-specific response logic (src/services/telemedicine.py)

import json
import os

def handle_telemedicine_intent(message):
    # Load telemedicine FAQs from data/faq.json
    faq_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'faq.json')
    with open(faq_path, 'r', encoding='utf-8') as f:
        faqs = json.load(f)
    # Match user message to FAQ keywords
    for faq in faqs:
        if any(keyword in message.lower() for keyword in faq['keywords']):
            return faq['answer']
    # Default response if no FAQ matches
    return "For telemedicine services, you can book an appointment with a doctor, ask about medicines, or get health advice. How can I help you?"