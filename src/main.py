import random
import sys
import pyfiglet
import time 
from Hangman_art import print_hangman
# Create Word List for the games words
word_list = [
    "apple",
    "banana",
    "strawberry",
    "pineapple",
    "mango",
    "peach"
]

# Variables need for the game
max_incorrect_guesses = 6
incorrect_guesses = 0
guessed_letters = []

# Select a random word from the List
def select_word(word_list):
    return random.choice(word_list)

selected_word = select_word(word_list)

# Display the selected word as undercores
def initialize_displayed_word(word):
    return "_" * len(word)

displayed_word = initialize_displayed_word(selected_word)

# call this function when the player fails
def failed_game():
    print_hangman(incorrect_guesses)
    ascii_banner = pyfiglet.figlet_format("GAME OVER!")
    print(ascii_banner)
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(1.5)
    sys.exit(1)


# Call this function when the player wins
def won_game():
    ascii_banner = pyfiglet.figlet_format("WINNER!")
    print(ascii_banner)
    print("Congratulations! You have won the game!")
    print("PlEASE WAIT... LOADING MENU...")
    time.sleep(1.5)

# This function is checking that the guess is within the selected word, 
# if correct saving it to local iteration variable then returning the iteration variable once all letters are found
def correct_guess(correct_letter):
    iteration = displayed_word
    for i in range(len(selected_word)):
        if correct_letter == selected_word[i]:
            lst = list(iteration)
            lst[i] = correct_letter
            iteration = ("".join(lst))
    return  iteration
   
# Checks if guess is incorrect and not in guessed letter list will append list
# and display guessed letters guessed on screen
def incorrect_guess(wrong_letter):
    print_hangman(incorrect_guesses)
    guessed_letters.append(wrong_letter)
    print(f"These are your previous guesses! {guessed_letters}")

# Inital screen to display if user would like to play or exit
def main_menu():
    ascii_banner = pyfiglet.figlet_format("HANGMAN!")
    print(ascii_banner)
    print(""" <------Can you guess the secret word!-----> """)
    print("1. Play")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

# Main Menu Initalises game and asks user if they want to play!  
while True:
    user_choice = main_menu()
    if user_choice == "1":
       selected_word = select_word(word_list)
       displayed_word = initialize_displayed_word(selected_word)
       time.sleep(1)
       print("New Game! Goodluck!")
       time.sleep(1)
       print(displayed_word)
    elif user_choice == "2":
        print("Thanks for playing!")
        sys.exit(0) 
    else: 
        print("Invalid choice. Please select a valid choice.")
        
    # Main game loop runs only if user asked to play, uses conditions and above functions for how to win or lose
    
    while True:        
        guess = input("Guess a Letter: ")
        if guess in guessed_letters:
            print("You guessed this letter already, try again!", end = " ")
        else:
            if guess in selected_word:
                incorrect_guesses -= 1
                displayed_word = correct_guess(guess) # update display word to show correct letter/ replace _ 
                print(displayed_word)
            if "_" not in displayed_word:
                won_game()# calls the won game function
            else:
                if incorrect_guesses == max_incorrect_guesses:
                    failed_game()# calls failed game function
                else:
                    incorrect_guesses += 1
                    incorrect_guess(guess) # calls incorrect guess function updates counter