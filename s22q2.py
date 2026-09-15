import random


responses = {
    "hello": [
        "Hello!",
        "Hi there!",
        "Greetings!",
        "Hello! How can I help you?"
    ],
    "how are you": [
        "I'm just a program, so I'm always good!",
        "I'm doing well, thank you!",
        "I'm here to assist you!"
    ],
    "what is your name": [
        "I'm a chatbot created to assist you.",
        "You can call me ChatBot!",
        "I'm your virtual assistant."
    ],
    "bye": [
        "Goodbye!",
        "See you later!",
        "Bye! Have a great day!"
    ],
    "default": [
        "I'm sorry, I didn't understand that.",
        "Can you rephrase?",
        "I'm here to help! Could you please clarify?"
    ]
}


def get_response(user_input):
    user_input = user_input.lower()

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return random.choice(responses["default"])


def chat():
    print("ChatBot: Hi! I'm here to chat with you. Type 'bye' to end the conversation.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "bye":
            print("ChatBot:", get_response("bye"))
            break

        response = get_response(user_input)
        print("ChatBot:", response)


chat()
