import random
import sys
# Create Word List for the games words
word_list = [
    "apple",
    "banana",
    "strawberry",
    "pineapple",
    "mango",
    "peach"
]

# Select a random word from the List
def select_word(word_list):
    return random.choice(word_list)

selected_word = select_word(word_list)

print(selected_word)

# Display the selected word as undercores
def initialize_displayed_word(word):
    return "_" * len(word)

displayed_word = initialize_displayed_word(selected_word)
print(displayed_word)

# Variables need for the game
max_incorrect_guesses = 5
incorrect_guesses = 0
guessed_letters = []

# Start game loop using while loop
def failed_game():
    print("GAME OVER!")
    sys.exit(1)

def won_game():
    print("GOOD JOB!")
    sys.exit(0)

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
    guessed_letters.append(wrong_letter)
    print(guessed_letters)
    

# while loop runs main function of game asks user to guess and checks correct or incorrect and calls correct functions 
while True:
    guess = input("Guess a Letter: ")
    if guess in guessed_letters:
        print("You guessed this letter already, try again!")
    else:
        if guess in selected_word:
            incorrect_guesses -= 1
            displayed_word = correct_guess(guess) # update display word to show correct letter/ replace _ 
            print(displayed_word)
        if "_" not in displayed_word:
                won_game()
        else:
            if incorrect_guesses == max_incorrect_guesses:
                failed_game()
            else:
                incorrect_guesses += 1
                incorrect_guess(guess) # calls incorrect guess function updates counter
                