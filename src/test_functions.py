import pytest
from unittest.mock import patch
import functions
from random_word import RandomWords

# This tests my main menu is allowing correct input selection


class TestMainMenu:
    def test_menu_user_input_play(self):
        with patch("builtins.input", return_value=1):
            user_choice = functions.main_menu()
            assert user_choice == 1

    def test_menu_user_input_exit(self):
        with patch("builtins.input", return_value=2):
            user_choice = functions.main_menu()
            assert user_choice == 2

# This tests that the correct guess is changing the _ to the letter
# also that showing and incorrect result as well


class TestCorrectGuess:
    def test_word_updates(self):
        result = functions.correct_guess("a", "_____", "apple")
        assert result == "a____"

    def test_word_doesnt_update(self):
        result = functions.correct_guess("z", "_____", "apple")
        assert result == "_____"

# This test checks that guesses are being appended correctly to the 
# list and displayed


class TestDisplayGuessedLetters:
    def test_displays_letters_guessed_in_list(self):
        result = functions.display_guessed_letters(["a", "b", "c", "d"], "s")
        assert result == ["a", "b", "c", "d", "s"]
