'''A repository module in charge of writing, reading and creating .csv files
which contain the unique user data (username and victories).'''
from pathlib import Path
from entities.player import Player
import os

class PlayerRepository:
    '''
    Read players.csv-files, create a player repository: list from the players.csv
    file, and write the player repository: list into players.csv file '''
    def __init__(self, file_path):
        self._file_path = file_path
        self._players = {}

        self._read()


    def find_username(self, username):
        '''Returns True if username is already in use'''
        return username in self._players.keys()


    def find_all(self):
        '''Returns a dictionary: str, int of players'''
        return self._players


    def _read(self):
        '''
        Read a CVS file containing player object instance representations,
        and update the internal player list to reflect the file contents.

        Raises:
            Whatever open() might toss at you.

        Returns:
            A dictionary of player victories indexed by their names.
        '''
        if not os.path.exists(self._file_path):
            return {}

        with open(self._file_path, encoding="UTF-8") as file:
            for row in file:
                name, victories = row.split(',')

                try:
                    victories = int(victories)
                except ValueError:
                    continue

                if name == 'player' and 'victories' == 0:
                    continue

                self._players[name] = victories


    def create(self, player: Player):
        '''Creating a new player'''
        if player.get_name().lower() in self._players.keys():
            raise ValueError

        if player.get_name != "" and len(player.get_name()) <= 16:
            self._players[player.get_name()] = 0

        self._write()


    def _write(self):
        '''
        Write out the current player (victories) list into a CSV file.
        '''
        with open(self._file_path, 'w', encoding="UTF-8") as file:
            file.write("player,victories\n")
            for name, victories in self._players.items():
                row = f'{name},{victories}\n'
                file.write(row)


    def _ensure_file_exists(self):
        '''Making sure the file exists'''
        Path(self._file_path).touch()

    def _ensure_username_is_free(self, player_candidate: Player, players: dict):
        '''Checking to see if requested username is available'''
        for player in players.keys():
            # lower() varmistaa, että käyttäjä todella on uniikki
            if player.lower() == player_candidate.lower():
                return False
        return True
