from ascii_art import STAGES, cinput, print_stages, print_word, game_over, success, info
import random

# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]

# Maximum number of mistakes allowed
MISTAKE_LIMIT = len(STAGES) - 1  # last index is the final melted stage

def get_random_word():
    """Selects a random word from the list."""
    return random.choice(WORDS)


def display_game_state(mistakes, secret_word, guessed_letters, wrong_guesses):
    """Shows the current stage
    and the secret word with underscores for unguessed letters."""

    print_stages(STAGES[mistakes])

    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in secret_word)
    print_word(display_word)

    if wrong_guesses:
        info(f"Wrong guesses: {' '.join(sorted(wrong_guesses))}")
    print()


def is_single_letter(ch):
    """Helpful function to ensure a single alphabetical letter."""
    return len(ch) == 1 and ch.isalpha()


def prompt_user(guessed_letters, wrong_guesses):
    """Asks the user to guess a letter
    and ensures that only a single alphabetical character is accepted.
    We don't punish the user for entering the same letter again"""

    while True:
        guess = cinput("Guess a letter: ").strip().lower()

        if not is_single_letter(guess):
            info("Please provide exactly one letter.")
            continue

        if guess in guessed_letters or guess in wrong_guesses:
            info("You already guessed that letter.")
            continue

        return guess


def play_game():
    """The main game function."""

    secret_word = get_random_word()
    secret_letters = set(secret_word)
    guessed_letters = set()
    wrong_guesses = set()
    mistakes = 0

    info("Welcome to Snowman Meltdown!")
    # Display the initial game state.
    display_game_state(mistakes, secret_word, guessed_letters, wrong_guesses)

    # Continue prompting the user until either they win or they exceed the mistake limit.
    while mistakes < MISTAKE_LIMIT and not secret_letters.issubset(guessed_letters):
        guess = prompt_user(guessed_letters, wrong_guesses)
        if guess in secret_letters:
            guessed_letters.add(guess)
        else:
            wrong_guesses.add(guess)
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters, wrong_guesses)

    if secret_letters.issubset(guessed_letters):
        success("Congrats!!! You saved the snowman!")
    else:
        game_over(secret_word)
        print_stages(STAGES[mistakes])
