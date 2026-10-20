"""CodeAlpha Python Internship - Task 1: Hangman Game"""
import random

WORDS = ["python", "internship", "developer", "variable", "function"]
MAX_WRONG = 6

STAGES = [
    "\n  +---+\n  |   |\n      |\n      |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n      |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n  |   |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|   |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n      |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n /    |\n      |\n=========",
    "\n  +---+\n  |   |\n  O   |\n /|\\  |\n / \\  |\n      |\n=========",
]


def display_word(word, guessed):
    return " ".join(ch if ch in guessed else "_" for ch in word)


def play():
    word = random.choice(WORDS)
    guessed, wrong = set(), set()

    print("=== HANGMAN ===")
    print(f"Guess the word one letter at a time. You have {MAX_WRONG} wrong guesses.")

    while len(wrong) < MAX_WRONG:
        print(STAGES[len(wrong)])
        print("\nWord:", display_word(word, guessed))
        print("Wrong guesses:", " ".join(sorted(wrong)) or "-")
        print(f"Lives left: {MAX_WRONG - len(wrong)}")

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        if guess in guessed or guess in wrong:
            print("You already guessed that letter.")
            continue

        if guess in word:
            guessed.add(guess)
            print("Good guess!")
            if all(ch in guessed for ch in word):
                print("\nWord:", display_word(word, guessed))
                print("🎉 You won!")
                return
        else:
            wrong.add(guess)
            print("Wrong guess!")

    print(STAGES[MAX_WRONG])
    print(f"\n💀 Game over! The word was: {word}")


if __name__ == "__main__":
    while True:
        play()
        if input("\nPlay again? (y/n): ").strip().lower() != "y":
            print("Thanks for playing!")
            break
