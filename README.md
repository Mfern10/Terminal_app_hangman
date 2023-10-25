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
For my implentation plan I first wrote down what I thought needed to be completed to make a functioning Hangman game. I decided what features it should have and put checkpoints and set duration estimate for tasks. 

I used [Linear](https://linear.app/mitchells-workspace/project/hangman-terminal-application-492f08c73346/MIT) This was my first time using linear and was a good learning experience. 

As I developed my application I ran into extra features to be added or more things that could be done to improve my application. I tried my best to add these issues to the board.

Below I will provide some screenshots of what my Development plan looked like at the beginning, some screenshots during and what it looked like at the end.

### Linear screenshots
#### List of features to implement with set dates to the right.
This was from the start of my project and scrolls further.
![Linear](/docs/fulllist1.png)
#### Feature 1 checklist
Basic outline of what I wanted to implement and how to do it.
![Linear](/docs/feature1checklist.png)
#### Feature 2 checklist
Shows which checked features are in progress also set dates to meet.
![Linear](/docs/feature2checklist.png)
#### Feature 3 checklist
Once again shows check points of feature 3 to implement a time to finish it.
![linear](/docs/feature3checklist.png)
#### Full board 20/10/2023
Shows progress of all features on board.
![Linear](/docs/fullboard20.png)
#### Full board 21/10/2023
Shows progress from the 21st
![Linear](/docs/fullboard21.png)
#### Full board 22/10/2023
Shows progress from the 22nd
![Linear](/docs/fullboard22.png)
#### Fullboard 23/10/2023
Shows progress as of the 23rd
![Linear](/docs/fullboard23.png)
#### Full board 25/10/2023
Shows progress as of the 25th
![Linear](/docs/fullboard25.png)

This was my first time using a program like this and I learn't alot but next time I want to make it more refined and detailed... really plan well what I want my program to have as to not end up with suprises at the end. 

The main goal originally was to have 3 features and implement them in order but I ended up having some more feature ideas that were added and definitely got side tracked but it was a great learning process that I plan on improving next time.


## Help documentation
### FOR WINDOWS USERS ONLY
Currently this version of Hangman runs on MAC OS and LINUX, you can use it on your windows machine by installing WSL UBUNUTU. Please follow the guide provided [HERE](https://ubuntu.com/tutorials/install-ubuntu-on-wsl2-on-windows-10#1-overview) 

Once you have completed these steps continue to the next part of the installation.
### Prerequistes:
1. If you don't already please install python 3.10 or higher on your system. You can find a link to python [HERE](https://www.python.org/downloads/)
2. Must have Bash for running scripts(This should be available by default on MAC or Linux if you are using Windows you can use Git Bash).
### Making file and cloning repository
1. Open your terminal create a file with ```mkdir "filename"``` change directory into the new file ```cd "filename"```
2. Once in your preferred directory clone the repository using this command ```git clone https://github.com/Mfern10/Terminal_app_hangman.git```
3. All files should now be available in your directory.
### Create Virtual environment
1. In your folder create a virtual environment by running the following command for WINDOWS ```python -m venv hangman-env``` and for MACOS or LINUX ```python3 -m venv hangman-env``` This will create your virtual environment.
2. activate the virtual environment. FOR WINDOWS ONLY RUN ```hangman-env\Scripts\activate``` FOR MAC OS AND LINUX ONLY RUN ```source hangman-env/bin/activate```
### Dependencies Script
1. Check if the dependencies script is executable by running ```chmod +x install_hangman_dependencies.sh```
2. RUN DEPENDENCIED SCRIPT ```./install_hangman_dependencies.sh``` this should install all needed modules and dependencies.
### Play game scripts
1. Check to make sure game is executable by running ```chmod +x run_hangman.sh```.
2. Now make sure the script is in the current directory for where you are trying to run the game and virtual envirment is active eg: ```(.venv) mdf@Mitchells-MacBook-Pro Terminal_app_hangman %```
3. NOW RUN ```./run_hangman``` in the directory and you are ready to play hangman! 

