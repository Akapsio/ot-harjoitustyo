'''Uniquely named wordlists for the game'''
class Wordlist:
    '''Creates a new wordlist with a unique name, an empty list and a specified
    length'''
    def __init__(self, name, length):
        '''Initialize Wordlist'''
        self.name = name
        self.wordlist = []
        self.length = length

    def get_length(self):
        '''Returns length of Wordlist'''
        return self.length

    def get_name(self):
        '''Returns name of Wordlist'''
        return self.name
