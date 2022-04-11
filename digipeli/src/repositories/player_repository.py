import csv
import os
from pathlib import Path

class PlayerRepository:

    def __init__(self, file_path):
        self._file_path = file_path

    def find_all(self):
        return self._read()

    def find_username(self, username):
        players = self.find_all()
        for player in players:
            if player[0] == username:
                return True
        return False

    def create(self, player):
        players = self._find_all()
        if not self._ensure_username_is_free:
            raise ValueError("Username is in use")
        else:
            players.append(player)

            self._write(players)

    def _read(self):
        players = []

        self._ensure_file_exists()

        with open(self._file_path) as file:
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
        self._ensure_file_exists()

        with open(self._file_path, "w") as file:
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