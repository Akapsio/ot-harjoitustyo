import os
from entities.player import Player
from repositories.player_repository import PlayerRepository

dirname = os.path.dirname(__file__)

todo_repository = PlayerRepository(os.path.join(dirname, "..", "data", "todos.csv"))

todo_repository.create(Player("Learn the repository pattern"))

todos = todo_repository.find_all()

print(todos)
