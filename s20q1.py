#defficult to run bohot kuch install krna pdta hai

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

college_bot = ChatBot("CollegeBot")

trainer = ChatterBotCorpusTrainer(college_bot)
trainer.train("chatterbot.corpus.english")


def chat_with_college_bot():
    print("College Bot: Hi! I'm your College Bot. Ask me anything about college.")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("College Bot: Goodbye!")
            break

        response = college_bot.get_response(user_input)
        print("College Bot:", response)


if __name__ == "__main__":
    chat_with_college_bot()
