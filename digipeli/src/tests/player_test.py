import unittest
import csv
from entities.player import Player

class TestPlayer(unittest.TestCase):

    def setUp(self):
        with open("players.csv", "w") as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow("default,0")

    def test_cannot_add_user_named_default_user(self):
        with open("players.csv", 'r') as f:
            csv_reader = csv.read(f)
            line_count = 0
            for row in csv_reader:
                if line_count == 0:
                    continue
                
        self.assertEquals(Player("default_user"), "Nimi on jo käytössä")
    

    
