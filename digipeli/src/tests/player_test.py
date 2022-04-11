import unittest
import os
from entities.player import Player
from repositories.player_repository import PlayerRepository

dirname = os.path.dirname(__file__)

class TestPlayer(unittest.TestCase):

    def setUp(self):
        player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players-test.csv"))

    def test_cannot_add_user_named_default_user(self):
        return 
    
