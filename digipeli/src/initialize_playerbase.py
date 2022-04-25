from entities.player import Player
from repositories.player_repository import PlayerRepository

import os

dirname = os.path.dirname(__file__)

player_repository = PlayerRepository(os.path.join(dirname, "..", "data", "players.csv"))
