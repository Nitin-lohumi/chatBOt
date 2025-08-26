def load_intents(file_path):
    import json
    with open(file_path, 'r') as file:
        intents = json.load(file)
    return intents

def get_intent_response(intents, user_input):
    for intent in intents['intents']:
        if user_input in intent['patterns']:
            return intent['responses']
    return ["I'm sorry, I didn't understand that."]

def add_intent(intents, intent_name, patterns, responses):
    intents['intents'].append({
        'intent': intent_name,
        'patterns': patterns,
        'responses': responses
    })
    return intents

def save_intents(file_path, intents):
    with open(file_path, 'w') as file:
        json.dump(intents, file, indent=4)