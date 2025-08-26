# filepath: chatbot-telemedicine/src/main.py

from chatbot.bot import ChatBot

def main():
    chatbot = ChatBot()
    chatbot.train()
    
    print("Welcome to the Telemedicine Chatbot!")
    print("Type 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        response = chatbot.respond(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()