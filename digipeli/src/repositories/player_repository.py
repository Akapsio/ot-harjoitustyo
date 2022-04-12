'''This is a repository module in charge of writing, reading and creating
.csv files which contain the unique user data (username and victories). One can also
find out if a username is already in use and return a list of players'''
from pathlib import Path

class PlayerRepository:
    '''Read .csv-files, create a player repository: list from the .csv file,
    and write the player repository: list into .csv file '''
    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        '''Returns a player repository'''
        return self._read()

    def find_username(self, username):
        '''Returns True if username exists in file'''
        players = self.find_all()
        for player in players:
            if player[0] == username:
                return True
        return False

    def create(self, player):
        '''Create a new player'''
        players = self.find_all()
        if not self._ensure_username_is_free:
            raise ValueError("Username is in use")
        players.append(player)

        self._write(players)

    def _read(self):
        '''Read .csv file'''
        players = []

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                if row_count == 0:
                    row_count += 1
                    continue
                row = row.replace("\n", "")
                parts = row.split(',')
                players.append(parts[0], parts[1])
        return players

    def _write(self, players):
        '''Write a .csv file'''
        self._ensure_file_exists()

        with open(self._file_path, 'w', encoding="UTF-8") as file:
            row_count = 0
            for player in players:
                if row_count == 0:
                    file.write("players,victories\n")
                    continue
                row = f"{player[0]},{player[1]}"
                file.write(row+"\n")

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _ensure_username_is_free(self, username_candidate):
        players = self.find_all
        for player in players:
            if player[0] == username_candidate:
                return False
        return True
