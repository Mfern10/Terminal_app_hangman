import sys
import time 
import functions
from random_word import RandomWords

# creates class for the main game including initial variables etc.
class HangmanGame:
    def __init__(self):
        self.word_list = RandomWords()
        self.max_incorrect_guesses = 6
        self.incorrect_guesses = 0
        self.guessed_letters = []
        self.win_loss = 0
        self.selected_word = ""
        self.displayed_word = ""
        self.playing = True

# Main Menu Initalises game and asks user if they want to play!  
    def start_game(self):
        while self.playing:
            user_choice = functions.main_menu()
            if user_choice == "1":
                self.selected_word = functions.select_word(self.word_list)
                self.displayed_word = functions.initialize_displayed_word(self.selected_word)
                time.sleep(1)
                print("New Game! Goodluck!")
                time.sleep(1)
                self.play_game()
            elif user_choice == "2":
                print("Thanks for playing!")
                self.playing = False
                sys.exit(0) 
            else: 
                if not user_choice == 1 or 2:
                    print("Please enter number 1 or 2.")
                if not user_choice.isnumeric():
                    print("Invalid choice. Please select a valid choice.")
                
        
    # Main game loop
    def play_game(self):
        self.win_loss = 0
        while self.win_loss == 0: 
            print(self.displayed_word)        
            guess = input("Guess a Letter: ").lower()
            try:
                if len(guess) > 1:
                    raise ValueError("Please enter ONE LETTER")
                if not guess.isalpha():
                    raise ValueError("Please enter a LETTER.")
                if guess in self.guessed_letters:
                    raise ValueError("You guessed this letter already, try again!")
            except ValueError as error:
                print(error)
                continue
            self.guessed_letters = functions.display_guessed_letters(self.guessed_letters, guess)
            print(self.guessed_letters)
            if guess in self.selected_word:
                self.displayed_word = functions.correct_guess(guess, self.displayed_word, self.selected_word) # update display word to show correct letter/ replace _ 
            else:
                self.incorrect_guesses += 1
                if self.incorrect_guesses == self.max_incorrect_guesses:
                    functions.failed_game(self.selected_word)# calls failed game function
                    functions.reset(self)
                    break 
                else:
                    functions.incorrect_guess(self.incorrect_guesses) # calls incorrect guess function updates counter
            if "_" not in self.displayed_word:
                    functions.won_game(self.displayed_word)# calls the won game function
                    functions.reset(self)

#envokes the class in order of how it should function                   
if __name__ == "__main__":
    game = HangmanGame()
    while game.playing:
        game.start_game()
