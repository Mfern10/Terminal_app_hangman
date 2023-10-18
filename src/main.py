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
random_word = random.choice(word_list)

print(random_word)

# Display empty word space with underscores
print("_ " * (len(random_word)))

#Variables needed for the game
max_tries = 6
tries = 0
guessed_letters = []   








