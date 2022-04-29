'''A module for the sake of testing Wordlist class'''
import unittest
import os
from entities.wordlist import Wordlist
from tempfile import mkstemp

class TestWordlist(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestWordlist, self).__init__(*args, **kwargs)
        self.csv_path = os.path.join(mkstemp(prefix = 'wordlist-test',
                                             suffix = '.csv')[1])
        self.list_a = [ 'foo', 'bar', 'baz', 'foobar', 'pertti', 'pasanen' ]


    '''Test class for testing Wordlist class'''
    def setUp(self):
        '''Creating a specific wordlist for testing's sake'''
        self.wordlist = Wordlist("Testi", self.list_a)


    def tearDown(self):
        os.remove(self.csv_path)


    def test_initial_list_is_the_wordlist(self):
        self.assertEqual(self.wordlist.get_list(), self.list_a)
