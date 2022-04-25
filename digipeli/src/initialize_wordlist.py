import os

from repositories.wordlist_repository import WordlistRepository

dirname = os.path.dirname(__file__)

wordlist_repository = WordlistRepository(os.path.join(dirname, "..", "data",
"wordlists.csv"))

print(wordlist_repository.find_all())
