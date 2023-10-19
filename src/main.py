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
    return "_ " * len(word)

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

while True:
    guess = input("Guess a Letter: ")
    current_tries += 1
    if current_tries == max_incorrect_guesses:
        failed_game()

    




    

    

  








