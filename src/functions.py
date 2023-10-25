import pyfiglet
import os
from hangman_art import print_hangman
import time
from random_word import RandomWords

# clear screen function clears terminal state for windows or mac


def clear_screen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

# resets variable back to pre game state and clears screen for user experience


def reset(self):
    self.incorrect_guesses = 0
    self.guessed_letters = []
    self.win_loss = 1
    clear_screen()

# prints correct hangman art for incorrect guesss


def incorrect_guess(incorrect_guesses):
    print_hangman(incorrect_guesses)

# appeneds all guesses to a list to be displayed on screen showing previous guesses


def display_guessed_letters(list_of_guesses, guess):
    list_of_guesses.append(guess)
    return list_of_guesses

# displays game over message resets back to main menu


def failed_game(selected_word):
    print_hangman(incorrect_guess)
    ascii_banner = pyfiglet.figlet_format("GAME OVER!")
    print(ascii_banner)
    print(f"Nice try the word you were looking for was: {selected_word}")
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(2.5)

# displays won game message resets to main menu


def won_game(displayed_word):
    ascii_banner = pyfiglet.figlet_format("WINNER!")
    print(ascii_banner)
    print(
        f"Congratulations! You have won the game! The word was: {displayed_word}")
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(2.5)

# function selects a word from random-word


def select_word(word_list):
    return word_list.get_random_word()

# Displays selected word as underscores


def initialize_displayed_word(word):
    return "_" * len(word)

# function for main menu


def main_menu():
    ascii_banner = pyfiglet.figlet_format("HANGMAN!")
    print(ascii_banner)
    print(""" <------Can you guess the secret word!-----> """)
    print("1. Play")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

# checks for correct guess in displayed word iterates though and makes a list of the
# letters that are withn the word


def correct_guess(correct_letter, displayed_word, selected_word):
    iteration = displayed_word
    for i in range(len(selected_word)):
        if correct_letter == selected_word[i]:
            lst = list(iteration)
            lst[i] = correct_letter
            iteration = ("".join(lst))
    return iteration
