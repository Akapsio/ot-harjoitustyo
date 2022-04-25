import os

from repositories.player_repository import PlayerRepository

dirname = os.path.dirname(__file__)

player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players.csv"))
