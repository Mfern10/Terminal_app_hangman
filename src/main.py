import sys
import time 
import functions
from random_word import RandomWords

word_list = RandomWords()

word_list.get_random_word()


# Variables

# word_list = [
#     "apple",
#     "banana",
#     "strawberry",
#     "pineapple",
#     "mango",
#     "peach"
# ]
max_incorrect_guesses = 6
incorrect_guesses = 0
guessed_letters = []


# Main Menu Initalises game and asks user if they want to play!  
while True:
    user_choice = functions.main_menu()
    if user_choice == "1":
       selected_word = functions.select_word(word_list)
       displayed_word = functions.initialize_displayed_word(selected_word)
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
            guessed_letters = functions.display_guessed_letters(guessed_letters, guess)
            print(guessed_letters)
            if guess in selected_word:
                displayed_word = functions.correct_guess(guess, displayed_word, selected_word) # update display word to show correct letter/ replace _ 
            else:
                incorrect_guesses += 1
                if incorrect_guesses == max_incorrect_guesses:
                    functions.failed_game(selected_word)# calls failed game function
                    incorrect_guesses, guessed_letters, win_loss = functions.reset(incorrect_guesses, guessed_letters, win_loss) 
                else:
                    functions.incorrect_guess(incorrect_guesses) # calls incorrect guess function updates counter
            if "_" not in displayed_word:
                functions.won_game(displayed_word)# calls the won game function
                incorrect_guesses, guessed_letters, win_loss = functions.reset(incorrect_guesses, guessed_letters, win_loss) 