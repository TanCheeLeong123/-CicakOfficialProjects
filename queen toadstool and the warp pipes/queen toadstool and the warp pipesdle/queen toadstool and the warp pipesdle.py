import random

# This game is not working in Python. Download Visual Studio Code to run the game.
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

def is_valid_guess(guess, guesses):
    return guess in guesses

def evaluate_guess(guess, word):
    result = ""

    for i in range(5):
        if guess[i] == word[i]:
            result += "\033[32m" + guess[i]
        else:
            if guess[i] in word:
                result += "\033[33m" + guess[i]
            else:
                result += "\033[37m" + guess[i]
                
    return result + "\033[0m"

def wordle(guesses, answers):
    print("Welcome to Queen Toadstool & The Warp Pipesdle! Get 6 chances to guess a 5 letter word.")
    
    secret_word = random.choice(answers)
    attempts = 1
    max_attempts = 6

    while attempts <= max_attempts:
        guess = input(f"Enter Guess #{attempts}: ").lower()
        
        if not is_valid_guess(guess, guesses):
            print("Invalid guess.")
            continue
        
        if guess == secret_word:
            print(f"You won! You guessed the word: {secret_word} in {attempts} attempts!")
            return

        print(evaluate_guess(guess, secret_word))
        attempts += 1

    print(f"You lost! The secret word was {secret_word}")

guesses = load_dictionary("guesses.txt")
answers = load_dictionary("answers.txt")

while True:
    wordle(guesses, answers)

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break