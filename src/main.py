import random
import sys
import pyfiglet
import time 
import os
from Hangman_art import print_hangman
import functions



# Constants

# Functions
def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def reset(incorrect_guesses, guessed_letters, win_loss):
    # global incorrect_guesses, guessed_letters, win_loss
    incorrect_guesses = 0
    guessed_letters = []
    win_loss = 1
    return incorrect_guesses, guessed_letters, win_loss and clear_screen()

# def correct_guess(correct_letter):
#     iteration = displayed_word
#     for i in range(len(selected_word)):
#         if correct_letter == selected_word[i]:
#             lst = list(iteration)
#             lst[i] = correct_letter
#             iteration = ("".join(lst))
#     return  iteration

def incorrect_guess():
    print_hangman(incorrect_guesses)

def display_guessed_letters(list_of_guesses, guess):
    list_of_guesses.append(guess)
    return list_of_guesses

def failed_game():
    print_hangman(incorrect_guesses)
    ascii_banner = pyfiglet.figlet_format("GAME OVER!")
    print(ascii_banner)
    print(f"Nice try the word you were looking for was: {selected_word}")
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(1.5)

def won_game():
    ascii_banner = pyfiglet.figlet_format("WINNER!")
    print(ascii_banner)
    print(f"Congratulations! You have won the game! The word was: {displayed_word}")
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(1.5)

# def main_menu():
#     ascii_banner = pyfiglet.figlet_format("HANGMAN!")
#     print(ascii_banner)
#     print(""" <------Can you guess the secret word!-----> """)
#     print("1. Play")
#     print("2. Exit")
#     choice = input("Enter your choice: ")
#     return choice

# Variables
word_list = [
    "apple",
    "banana",
    "strawberry",
    "pineapple",
    "mango",
    "peach"
]
max_incorrect_guesses = 6
incorrect_guesses = 0
guessed_letters = []

# Selects random word from word_list
def select_word(word_list):
    return random.choice(word_list)

# Displays selected word as underscores
def initialize_displayed_word(word):
    return "_" * len(word)

# Main Menu Initalises game and asks user if they want to play!  
while True:
    user_choice = functions.main_menu()
    if user_choice == "1":
       selected_word = select_word(word_list)
       displayed_word = initialize_displayed_word(selected_word)
       time.sleep(1)
       print("New Game! Goodluck!")
       time.sleep(1)
    elif user_choice == "2":
        print("Thanks for playing!")
        sys.exit(0) 
    else: 
        if not user_choice == 1 or 2:
            print("Please enter number 1 or 2.")
        if not user_choice.isnumeric():
            print("Invalid choice. Please select a valid choice.")
        continue
        
    # Main game loop
    win_loss = 0
    while win_loss == 0: 
        print(displayed_word)        
        guess = input("Guess a Letter: ").lower()
        if len(guess) > 1:
            print("Please enter ONE LETTER")
            continue
        if not guess.isalpha():
            print("Please enter a LETTER.")
            continue
        if guess in guessed_letters:
            print("You guessed this letter already, try again!")
        else:
            guessed_letters = display_guessed_letters(guessed_letters, guess)
            print(guessed_letters)
            if guess in selected_word:
                displayed_word = functions.correct_guess(guess, displayed_word, selected_word) # update display word to show correct letter/ replace _ 
            else:
                incorrect_guesses += 1
                if incorrect_guesses == max_incorrect_guesses:
                    failed_game()# calls failed game function
                    incorrect_guesses, guessed_letters, win_loss = reset(incorrect_guesses, guessed_letters, win_loss) 
                else:
                    incorrect_guess() # calls incorrect guess function updates counter
            if "_" not in displayed_word:
                won_game()# calls the won game function
                incorrect_guesses, guessed_letters, win_loss = reset(incorrect_guesses, guessed_letters, win_loss) 