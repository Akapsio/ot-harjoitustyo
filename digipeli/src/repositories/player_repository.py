'''A repository module in charge of writing, reading and creating .csv files
which contain the unique user data (username and victories).'''
from pathlib import Path

class PlayerRepository:
    '''Read players.csv-files, create a player repository: list from the players.csv
    file, and write the player repository: list into .csv file '''
    def __init__(self, file_path):
        self._file_path = file_path
        players = {}
        self._write(players)

    def find_username(self, username):
        '''Returns True if username is already in use'''

        players = self.find_all()
        for player in players:
            if player[0] == username:
                return True
        return False

    def find_all(self):
        '''Returns a list of tuples (username, victories)'''
        return self._read()

    def _read(self):
        '''KORJAA TÄMÄ FUNKTIO
        Reads the players.csv file'''
        players = {}

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                print(row)
                if row_count == 0:
                    row_count += 1
                    continue
                row = row.replace("\n", "")
                print(row)
                parts = row.split(',')
                players[parts[0]] = parts[1]
        return players

    def create(self, player):
        '''Creates a new player'''
        players = self.find_all()
        if self._ensure_username_is_free(str(player), players):
            players[player] = 0
        else:
            raise ValueError("Username is in use")
        self._write(players)

    def _write(self, players):
        '''Write to players.csv file'''
        self._ensure_file_exists()
        print("päästäänkö tänne?")

        with open(self._file_path, 'w', encoding="UTF-8") as file:
            file.write("player,victories\n")
            for player in players:
                print(players)
                row = str(player) + "," + str(players[player])
                print("Tulostetaan rivi funktiosta _write", row)
                file.write(row+"\n")

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _ensure_username_is_free(self, username_candidate, players):
        for player in players:
            # lower() varmistaa, että käyttäjä todella on uniikki
            if str(player).lower() == username_candidate.lower():
                return False
        return True
