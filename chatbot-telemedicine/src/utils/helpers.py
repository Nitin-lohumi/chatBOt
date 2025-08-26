def format_response(response):
    return response.strip().capitalize()

def validate_input(user_input):
    return isinstance(user_input, str) and len(user_input) > 0

def log_interaction(user_input, bot_response):
    with open('interaction_log.txt', 'a') as log_file:
        log_file.write(f"User: {user_input}\nBot: {bot_response}\n\n")