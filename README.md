# HANGMAN GAME TERMINAL APPLICATION
I have chosen to make a Hangman game as my Terminal application. 

The game is simple guess a letter if its correct the letter will display in the random word. 
If incorrect you will be prompted to try again。
you will get a total number of guesses before either winning or reaching game over! 

HAVE FUN！！！！ LET'S PLAY HANGMAN!!!!

## References

## Links
[Github Repo](https://github.com/Mfern10/Terminal_app_hangman)

## Code Style Guide
For my project since I was coding in python to build my application, I used PEP 8 Style Guide.
I tried my best to adhere to the style guide in every form including spacing, line length, etc.
You can find the style guide [HERE](https://peps.python.org/pep-0008/)

## List of Features
My application in bodies many features happening as the game is played but lets just list the 3 main features that make it function.
### Feature 1: Word Selection and Display
This feature is an important part of the application as after all how can you have hangman without words or a screen to see them on.
The feature selects a word from a created word list at random utilising the **IMPORT RANDOM** module to select the word.

It then stores the word and displays it as a series of underscores representing each character in the word to be guesssed
by the player. This forms the core of the games challenge, they now know the length of the word and can start guessing.

This feature was implemented by using 2 simple functions one to define the selection of the word from the list.
The next function would display the length of the word as underscores.

### Feature 2: Guessing and Validation
This feature is where the player starts to interact with the game. It asks the player to input a letter to guess,
ofcourse handling any incorrect inputs such as numbers or strings of characters or symbols. It then validates the guesses
with if its correct guess or incorrect guess and will update the screen based on that fact.

Whether the guess is correct or incorrect the letter will append to a list that will display the players previous guesses. 

If correct the displayed word (as underscores) will be interated through and manipulate the sting to identify the position 
of the correct letter and change the underscore accordingly.

If incorrect the letter will be appened so that it is known not to use it again and the ASCII hangman images will display.

The player receives unlimited guesses but six incorrect guesses total as this will display the full hangman image.

### Feature 3: Winning and Losing Conditions
This feature determins when the game ends and when it breaks its loop. It must track the players progress such as incorrect guesses
correct guesses. 

A loss condition is when the player has  hit the max amount of incorrect guesses and Hangman has been displayed in full. 
It will exit the loop showing a game over message.

A win condition is when all the letters in the word have been displayed. All the underscores have been replaced with the correct 
letters. Upon a win the Game will show a **WINNER** message.

### Feature 4: Main Menu
This Feature was added later in my process to add more User experience. The Menu displays a Title and a choice whether to play or exit.
The feature handles for input errors so only 2 conditions can be input play or exit. 

The menu is Displayed in 3 instances. At the start of opening the application, If the player wins the screen will clear and return to 
the main menu and also if a loss occurs.



## Implementation Plan

## Help documentation
