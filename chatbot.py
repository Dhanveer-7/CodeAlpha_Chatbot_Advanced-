import random

# Predefined responses for each intent
responses = {
    "greeting": ["Hi there!", "Hello!", "Hey!", "Nice to meet you!"],
    "how_are_you": ["I'm doing well, thank you!", "Feeling great! How about you?", "All good here!"],
    "goodbye": ["Goodbye!", "See you later!", "Take care!", "Bye!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "I didn't quite understand."]
}

# Intent keywords
intents = {
    "greeting": ["hi", "hello", "hey"],
    "how_are_you": ["how are you", "how's it going", "how do you do"],
    "goodbye": ["bye", "goodbye", "see you"],
    "thanks": ["thanks", "thank you"]
}

# Function to identify intent
def get_intent(user_input):
    user_input = user_input.lower()
    for intent, keywords in intents.items():
        for keyword in keywords:
            if keyword in user_input:
                return intent
    return "default"

# Main chatbot function
def chatbot():
    print("🤖 ChatBot: Hello! I'm here to chat with you. Type 'bye' to end the conversation.\n")
    while True:
        user_input = input("You: ").strip()
        if user_input == "":
            continue

        intent = get_intent(user_input)

        if intent == "goodbye":
            print("Bot:", random.choice(responses[intent]))
            break
        else:
            print("Bot:", random.choice(responses[intent]))

# Start the chatbot
chatbot()
