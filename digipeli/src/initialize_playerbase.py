import os
from repositories.player_repository import PlayerRepository
from entities.player import Player

dirname = os.path.dirname(__file__)

player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players.csv"))

