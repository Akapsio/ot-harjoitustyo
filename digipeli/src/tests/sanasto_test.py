import unittest
from main.sanasto import Sanasto
from typing import List

class TestSanasto(unittest.TestCase):
    def setUp(self):
        self.sanasto = Sanasto("sanasto", 50)
        
    def test_hae_sanasto_palauttaa_listan(self):
        testi_sanasto = self.sanasto.hae_sanasto("testi_sanasto.txt")
        self.assertEqual(type(testi_sanasto), List)
    
