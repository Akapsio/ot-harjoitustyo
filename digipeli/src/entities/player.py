'''Unique players for the game'''
class Player:
    '''Creates a new player with specified username and 0 victories'''
    def __init__(self, username: str):
        self._username = username
        self._victories = 0

    def get_name(self):
        return self._username

    def get_victories(self):
        return self._victories