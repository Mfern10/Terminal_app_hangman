import pytest
from main import HangmanGame
from random_word import RandomWords
from unittest import TestCase
from unittest.mock import patch


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
