'''A module for the sake of testing Wordlist class'''
import unittest
import os
from entities.wordlist import Wordlist

class TestWordlist(unittest.TestCase):
    '''Test class for testing Wordlist class'''
    def setUp(self):
        '''Creating a specific wordlist for testing's sake'''
        self.wordlist = Wordlist("Testi", 50)
