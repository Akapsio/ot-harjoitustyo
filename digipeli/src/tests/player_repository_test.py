import unittest
import os
from repositories.player_repository import PlayerRepository
from entities.player import Player
from tempfile import mkstemp

dirname = os.path.dirname(__file__)

class TestPlayerRepository(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPlayerRepository, self).__init__(*args, **kwargs)
        self.csv_path = os.path.join(mkstemp(prefix = 'digipeli',
                                             suffix = '.csv')[1])


    '''Class for testing the Player class'''
    def setUp(self):
        '''Setting up a player repository'''
        self.player_repository = PlayerRepository(self.csv_path)
        self.player_repository.create(Player("default"))

    def tearDown(self):
        os.remove(self.csv_path)

    def test_cannot_add_user_named_default(self):
        '''Test to see that you cannot add a username that is already in use'''
        self.assertRaises(ValueError, lambda: self.player_repository.create(Player("default")))

    def test_find_username_returns_True_when_looking_for_existing_player(self):
        self.assertTrue(self.player_repository.find_username("default"))

    def test_find_username_returns_False_when_looking_for_nonexisting_player(self):
        self.assertFalse(self.player_repository.find_username("anonymous"))

    def test_find_all_returns_a_dictionary(self):
        self.assertEqual(type(self.player_repository.find_all()), dict)
    
