'''Testing the Player class'''
import unittest
import os
from entities.player import Player

class TestPlayer(unittest.TestCase):
    '''Class for testing the Player class'''
    def setUp(self):
        self.player = Player("default")

    def test_player_name_is_default(self):
        self.assertEqual(self.player.get_name(), "default")

    def test_player_has_zero_victories(self):
        self.assertEqual(self.player.get_victories(), 0)