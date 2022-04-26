'''Uniquely named wordlists for the game'''
class Wordlist:
    '''Creates a new wordlist with a unique name, an empty list and a specified
    length'''
    def __init__(self, name, length):
        '''Initialize Wordlist'''
        self._name = name
        self.wordlist = []
        self._length = length

    def get_length(self):
        '''Returns length of Wordlist'''
        return self._length

    def get_name(self):
        '''Returns name of Wordlist'''
        return self._name

    def get_list(self):
        '''Returns list of words'''
        return self.wordlist
