'''Uniquely named wordlists for the game'''
from queue import Empty


class Wordlist:
    '''
    A representation of a named wordlist, possibly with a unique name,
    and an empty list or a list with initial seed of words.
    '''
    def __init__(self, name, contents):
        '''Initialize Wordlist'''
        self._name = name
        if contents is Empty:
            self.worldlist = []
        else:
            self._wordlist = contents


    def get_length(self):
        '''
        Returns length of this Wordlist instance.
        '''
        return len(self._wordlist)


    def get_name(self):
        '''
        Returns name of this Wordlist instance.
        '''
        return self._name


    def get_list(self):
        '''
        Returns list of words stored in this wordlist.

        It might be a good idea not to return the list itself, but
        a deep copy in case someone gets any ideas about modifying
        what has been returned (this would reveal the innards of this
        to the caller, though in Python that happens anyway).
        '''
        return self._wordlist


    # Always nice to have one for debugging purposes.
    def __str__(self):
        return (
            f'{{WordList: '
            f'[name={self.get_name()}, '
            f'lenght={self.get_length()}}}'
        )
