import random
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
max_incorrect_guesses = 6
current_tries = 0
guessed_letters = []

# Start game loop using while loop
def failed_game():
    print("GAME OVER!")
    exit(1)

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
   
            

    
def incorrect_guess():
    pass
#     if guess not in selected_word:
#         guessed_letters.append(guessed)
#         print(guessed_letters)
#     else:
#         for guess in guessed_letters:
#              current_tries += 1

    

while True:
    guess = input("Guess a Letter: ")
    if guess in guessed_letters:
        print("You guessed this letter already, try again!")
    else:
        if guess in selected_word:
            displayed_word = correct_guess(guess) # update display word to show correct letter/ replace _ 
            print(displayed_word)
        else:
            incorrect_guess() # calls incorrect guess function updates counter

 

    




    

    

  








