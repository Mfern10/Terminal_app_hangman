import pytest
from main import HangmanGame
from random_word import RandomWords
from unittest import TestCase
from unittest.mock import patch

# The test test the main class initalizes the correct variables before
# starting the game. It checks that the variables are initialised at the
# start of each game in order to run the game correctly.


class TestHangmanGame(TestCase):
    def test_Hangman_game_initialization(self):
        game = HangmanGame()
        assert isinstance(game.word_list, RandomWords)
        assert game.incorrect_guesses == 0
        assert game.max_incorrect_guesses == 6
        assert game. guessed_letters == []
        assert game.win_loss == 0
        assert game.selected_word == ""
        assert game.displayed_word == ""
        assert game.playing == True
