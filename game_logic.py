from ascii_art import STAGES, cinput, print_stages, print_word, game_over, success, info
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum number of mistakes allowed
MISTAKE_LIMIT = 5

def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Shows the current stage
    and the secret word with underscores for unguessed letters."""

    # Stage for the current number of mistakes
    print_stages(STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print_word(display_word)
    print("\n")


def is_single_letter(ch):
    """Helpful function to ensure a single alphabetical letter."""
    return len(ch) == 1 and ch.isalpha()


def prompt_user():
    """Asks the user to guess a letter
    and ensures that only a single alphabetical character is accepted."""

    while True:
        guess = cinput("Guess a letter: ").lower()
        if is_single_letter(guess):
            return guess
        else:
            info("Please provide a single alphabetical character")


def play_game():
    """The main game function"""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    info("Welcome to Snowman Meltdown!")
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
        success("Congrats!!! You saved the snowman!")
    else:
        game_over(secret_word)
        print_stages(STAGES[mistakes])
