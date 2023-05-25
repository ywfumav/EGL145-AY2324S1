import random

def play_game():
    words = ["python", "programming", "hangman", "openai", "game"]
    word = random.choice(words).lower()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")
    print("_ " * len(word))

    while attempts > 0:
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
        else:
            print("Correct guess!")

        word_progress = ""
        for letter in word:
            if letter in guessed_letters:
                word_progress += letter + " "
            else:
                word_progress += "_ "

        print(word_progress)

        if "_" not in word_progress:
            print("Congratulations! You guessed the word.")
            break

    if attempts == 0:
        print(f"Game over! The word was '{word}'.")

def play_again():
    while True:
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes":
            return True
        elif choice.lower() == "no":
            return False
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

print("=== Hangman Game ===")

while True:
    play_game()
    if not play_again():
        break

print("Thank you for playing! Goodbye!")
