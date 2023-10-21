# Hangman Art 
def print_hangman(incorrect_guesses):
    if incorrect_guesses == 0:
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 1):
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
    elif(incorrect_guesses == 3):
        print("\n+---+")
        print(" O   |")
        print("/|   |")
        print("     |")
        print("    ===")
    elif(incorrect_guesses == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    elif(incorrect_guesses == 5):
        print("\n+---+")
        print("  O   |")
        print(" /|\  |")
        print(" /    |")
        print("     ===")
    elif(incorrect_guesses == 6):
        print("\n+---+")
        print("  O   |")
        print(" /|\  |")
        print(" / \  |")
        print("     ===")
    