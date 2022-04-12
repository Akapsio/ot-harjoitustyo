'''Uniquely named wordlists for the game'''
class Wordlist:
    '''Creates a new wordlist with a unique name, an empty list and a specified
    length'''
    def __init__(self, name, length):
        self.name = name
        self.wordlist = []
        self.length = length
