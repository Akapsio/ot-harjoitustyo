from entities.player import Player
from repositories.player_repository import PlayerRepository

import os

dirname = os.path.dirname(__file__)

player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players.csv"))

player_repository.create(Player("Akapsio"))

player_repository.create(Player("Teemu"))

players = player_repository.find_all()
for player in players:
    print(player)

new_player = Player("Teemu")
print(new_player)

print(players)
