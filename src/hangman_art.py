# Hangman Art ASCII art to create the hangman images
def print_hangman(incorrect_guesses):
    if incorrect_guesses == 0:
        print("\n")
        print("  +---+")
        print("      |")
        print("      |")
        print("      |")
        print("     ===")
    elif (incorrect_guesses == 1):
        print("\n")
        print("  +---+")
        print("  O   |")
        print("      |")
        print("      |")
        print("     ===")
    elif (incorrect_guesses == 2):
        print("\n")
        print("  +---+")
        print("  O   |")
        print("  |   |")
        print("      |")
        print("     ===")
    elif (incorrect_guesses == 3):
        print("\n")
        print("  +---+")
        print("  O   |")
        print(" /|   |")
        print("      |")
        print("     ===")
    elif (incorrect_guesses == 4):
        print("\n")
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print("      |")
        print("     ===")
    elif (incorrect_guesses == 5):
        print("\n")
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("     ===")
    else:
        print("\n")
        print("  +---+")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("     ===")
