# ---------------------------------------
# CodeAlpha Internship Project
# Project: Hangman Game
# Developed by: Your Name
# ---------------------------------------

import random

# List of predefined words
WORDS = [
    "python",
    "computer",
    "science",
    "developer",
    "keyboard"
]

# Show selected word while developing
DEBUG = False


def show_welcome():
    """Display the welcome message."""
    print("=" * 50)
    print("        WELCOME TO HANGMAN GAME")
    print("=" * 50)


def choose_word():
    """Choose a random word."""
    return random.choice(WORDS)


def create_display(word):
    """Create underscores for the hidden word."""
    return ["_"] * len(word)


def get_guess():
    """Get a valid single alphabet letter from the player."""

    while True:
        guess = input("\nEnter a letter: ").lower().strip()

        if len(guess) != 1:
            print("❌ Please enter only one letter.")
            continue

        if not guess.isalpha():
            print("❌ Please enter only alphabet letters (A-Z).")
            continue

        return guess


def update_display(word, display, guess):
    """Reveal correctly guessed letters."""

    for index in range(len(word)):
        if word[index] == guess:
            display[index] = guess

def is_correct_guess(word, guess):
    """Return True if the guessed letter is in the word."""
    return guess in word


def play_game():
    """Main game logic."""

    chosen_word = choose_word()

    if DEBUG:
        print(f"\nSelected Word (Testing): {chosen_word}")

    display = create_display(chosen_word)
    attempts = 6
    guessed_letters = []

    game_over = False

    while not game_over:

        print("\n" + "=" * 50)
        print("Word:")
        print(" ".join(display))

        print(f"\nAttempts Left: {attempts}")

        print("\nGuessed Letters:")
        if guessed_letters:
            print(", ".join(guessed_letters))
        else:
            print("None")

        print("=" * 50)
        guess = get_guess()

        if guess in guessed_letters:
            print(f"⚠️ You already guessed '{guess}'. Try another letter.")
            continue
        guessed_letters.append(guess)

        if is_correct_guess(chosen_word, guess):
            update_display(chosen_word, display, guess)
        else:
            attempts -= 1
            print("❌ Wrong guess!")
        
        if attempts == 0:
             print("\n💀 Game Over!")
             print(f"The word was: {chosen_word}")
             game_over = True

        if "_" not in display:
            print("\n🎉 Congratulations!")
            print(f"You guessed the word: {chosen_word}")
            game_over = True


def main():
    """Main program loop."""

    while True:

        show_welcome()

        play_game()

        choice = input("\nDo you want to play again? (Y/N): ").lower().strip()

        if choice != "y":
            print("\nThank you for playing Hangman!")
            print("Have a great day! 😊")
            break


if __name__ == "__main__":
    main()
