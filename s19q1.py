import random


def hangman():
    secret_word = random.choice([
        "python",
        "hangman",
        "programming",
        "computer",
        "science",
        "algorithm"
    ])

    guessed_letters = {secret_word[0]}
    attempts = 6

    while attempts > 0 and not set(secret_word).issubset(guessed_letters):
        print(
            "Current word:",
            ''.join(
                letter if letter in guessed_letters else '_'
                for letter in secret_word
            )
        )

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("Letter already guessed!")
            print()
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            attempts -= 1

        print("Attempts left:", attempts)
        print()

    if set(secret_word).issubset(guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print("Sorry, you ran out of attempts.")
        print("The word was:", secret_word)


if __name__ == "__main__":
    hangman()
