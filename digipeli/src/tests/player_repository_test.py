import unittest
import os
from repositories.player_repository import PlayerRepository
from entities.player import Player

dirname = os.path.dirname(__file__)

class TestPlayerRepository(unittest.TestCase):
    '''Class for testing the Player class'''
    def setUp(self):
        '''Setting up a player repository'''
        self.player_repository = PlayerRepository(os.path.join(dirname,
        "../..", "data", "players-test.csv"))
        self.player_repository.create(Player("default"))
        
    def test_cannot_add_user_named_default(self):
        '''Test to see that you cannot add a username that is already in use'''
        self.assertRaises(ValueError, lambda: self.player_repository.create(Player("default")))

    def test_find_username_returns_True_when_looking_for_existing_player(self):
        self.assertEqual(True, self.player_repository.find_username("default"))

    def test_find_username_returns_False_when_looking_for_nonexisting_player(self):
        self.assertEqual(False, self.player_repository.find_username("anonymous"))

    def test_find_all_returns_a_dictionary(self):
        self.assertEqual(type(self.player_repository.find_all()), dict)
    
