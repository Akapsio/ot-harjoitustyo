'''Unique players for the game'''
class Player:
    '''Creates a new player with specified username and 0 victories'''
    def __init__(self, username: str):
        self.username = username
        self.victories = 0
