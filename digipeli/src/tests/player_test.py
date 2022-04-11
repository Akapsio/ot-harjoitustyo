import unittest
from player.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        Player("tester")

    def test_cannot_add_user_named_default_user(self):
        self.assertEquals(Player("default_user"), "Nimi on jo käytössä")
    
    
    