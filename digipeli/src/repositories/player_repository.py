'''A repository module in charge of writing, reading and creating .csv files
which contain the unique user data (username and victories).'''
from pathlib import Path
from entities.player import Player

class PlayerRepository:
    '''Read players.csv-files, create a player repository: list from the players.csv
    file, and write the player repository: list into players.csv file '''
    def __init__(self, file_path):
        self._file_path = file_path
        players = self.find_all()
        self._write(players)

    def find_username(self, username):
        '''Returns True if username is already in use'''
        players = self.find_all()
        for player in players:
            if  player.get_name() == username:
                return True
        return False

    def find_all(self):
        '''Returns a dictionary: str, int of players'''
        return self._read()

    def _read(self):
        '''Reading the players.csv file'''
        players = {}

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                if row_count == 0:
                    row_count += 1
                    continue
                row = row.replace("\n", "")
                parts = row.split(',')
                players[parts[0]] = parts[1]
        return players

    def create(self, player: Player):
        '''Creating a new player'''
        players = self.find_all()
        if self._ensure_username_is_free(player.get_name(), players):
            if player.get_name != "" and len(player.get_name()) <= 16:
                players[player.get_name()] = 0
        else:
            raise ValueError
        self._write(players)

    def _write(self, players: dict):
        '''Writing to players.csv file'''

        self._ensure_file_exists()

        with open(self._file_path, 'w', encoding="UTF-8") as file:
            file.write("player,victories\n")
            for player in players:
                row = player + "," + str(players[player])
                file.write(row+"\n")

    def _ensure_file_exists(self):
        '''Making sure the file exists'''
        Path(self._file_path).touch()

    def _ensure_username_is_free(self, player_candidate: Player, players: dict):
        '''Checking to see if requested username is available'''
        for player in players:
            # lower() varmistaa, että käyttäjä todella on uniikki
            if player.lower() == player_candidate.lower():
                return False
        return True
