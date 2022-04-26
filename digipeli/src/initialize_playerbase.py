import os
from repositories.player_repository import PlayerRepository
from entities.player import Player

dirname = os.path.dirname(__file__)

player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players.csv"))

player = Player("default")

player_repository.create(player)
player_repository.create(Player("Teemu"))
player_repository.create(Player("Atte"))
player_repository.create(Player("Riia"))
player_repository.create(Player("Riku"))

while True:
    cmd = input("Pelaaja")
    if cmd == "":
        break
    player_repository.create(Player(cmd))

print(player_repository.find_all())
