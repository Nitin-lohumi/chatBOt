class ChatBot:
    def __init__(self, intents_file):
        self.intents = self.load_intents(intents_file)
        self.responses = {}
        self.train()

    def load_intents(self, file):
        import json
        with open(file) as f:
            return json.load(f)

    def respond(self, user_input):
        for intent in self.intents['intents']:
            if user_input.lower() in intent['patterns']:
                return intent['responses'][0]
        return "I'm sorry, I don't understand that."

    def train(self):
        for intent in self.intents['intents']:
            for pattern in intent['patterns']:
                self.responses[pattern] = intent['responses']