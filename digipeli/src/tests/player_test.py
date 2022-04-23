'''Testing the Player class'''
import unittest
import os
from ..repositories.player_repository import PlayerRepository

dirname = os.path.dirname(__file__)

class TestPlayer(unittest.TestCase):
    '''Class for testing the Player class'''
    def setUp(self):
        '''Setting up a player repository'''
        player_repository = PlayerRepository(os.path.join(dirname,
        "..", "data", "players-test.csv"))

    def test_cannot_add_user_named_default_user(self):
        '''Test to see that you cannot add a username that is already in use'''
        return
