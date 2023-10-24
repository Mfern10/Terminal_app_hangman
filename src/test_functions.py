import pytest
from unittest.mock import patch
import functions


class TestMainMenu:
    def test_menu_user_input_play(self):
        with patch("builtins.input", return_value=1):
            user_choice = functions.main_menu()
            assert user_choice == 1

    def test_menu_user_input_exit(self):
        with patch("builtins.input", return_value = 2):
            user_choice = functions.main_menu()
            assert user_choice == 2

class TestCorrectGuess:
    def test_word_updates(self):
        result = functions.correct_guess("a", "_____", "apple")
        assert result == "a____"

    def test_word_doesnt_update(self):
        result = functions.correct_guess("z", "_____", "apple")
        assert result == "_____"
    

class TestDisplayGuessedLetters:
    def test_displays_letters_guessed_in_list(self):
        result = functions.display_guessed_letters(["a", "b", "c", "d"], "s")
        assert result == ["a", "b", "c", "d", "s"]


        






    




        