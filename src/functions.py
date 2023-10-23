import pyfiglet

def main_menu():
    ascii_banner = pyfiglet.figlet_format("HANGMAN!")
    print(ascii_banner)
    print(""" <------Can you guess the secret word!-----> """)
    print("1. Play")
    print("2. Exit")
    choice = input("Enter your choice: ")
    return choice

def correct_guess(correct_letter, displayed_word, selected_word):
    iteration = displayed_word
    for i in range(len(selected_word)):
        if correct_letter == selected_word[i]:
            lst = list(iteration)
            lst[i] = correct_letter
            iteration = ("".join(lst))
    return  iteration