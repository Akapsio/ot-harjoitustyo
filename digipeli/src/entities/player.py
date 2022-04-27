'''Unique players for the game'''
class Player:
    '''Creates a new player with specified username and 0 victories'''
    def __init__(self, username: str, victories = 0):
        self._username = username
        self._victories = victories

    def get_name(self):
        return self._username

    def get_victories(self):
        return self._victories

    def __str__(self):
        return (
            f'{{Player: '
            f'[username={self._username}, '
            f'victories={self._victories}]}}'
        )
