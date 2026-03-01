from ascii_art import STAGES
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum number of mistakes allowed
MISTAKE_LIMIT = 3

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows the current stage
    and the secret word with underscores for unguessed letters."""

    # Stage for the current number of mistakes
    print(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def is_single_letter(ch):
    """Helpful function to ensure a single alphabetical letter."""
    return len(ch) == 1 and ch.isalpha()


def prompt_user():
    """Asks the user to guess a letter
    and ensures that only a single alphabetical character is accepted."""

    while True:
        guess = input("Guess a letter: ").lower()
        if is_single_letter(guess):
            return guess
        else:
            print("Please provide a single alphabetical character")


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    # Display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters)

    # Continue prompting the user until either they win or they exceed the mistake limit.
    while mistakes < MISTAKE_LIMIT and len(guessed_letters) < len(secret_word):
        guess = prompt_user()
        if guess not in secret_word:
            mistakes += 1
        else:
            guessed_letters.append(guess)
        display_game_state(mistakes, secret_word, guessed_letters)

    if mistakes < MISTAKE_LIMIT:
        print("Congrats!!! You saved the snowman!")
    else:
        print("Game Over! The word was:", secret_word)
        print(STAGES[mistakes])
