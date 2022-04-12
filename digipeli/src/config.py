'''This .py file might be totally unnecessary for what I understand, so I
suppose this unnecessary comment is justified as well'''
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

PLAYERS_FILENAME = os.getenv('PLAYERS_FILENAME') or 'playes.csv'
PLAYERS_FILE_PATH = os.path.join(dirname, '..', 'data', PLAYERS_FILENAME)

WORDLISTS_FILENAME = os.getenv('WORDLISTS_FILENAME') or 'wordlists.csv'
WORDLISTS_FILE_PATH = os.path.join(dirname, '..', 'data', WORDLISTS_FILENAME)
