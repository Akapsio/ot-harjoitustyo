'''This is a repository module in charge of writing, reading and creating
.csv files which contain uniquely named lists of words. '''
from pathlib import Path
from entities.wordlist import Wordlist

class WordlistRepository:
    '''Read .csv-files, create a player repository: list from the .csv file,
    and write the player repository: list into .csv file '''
    def __init__(self, file_path):
        self._file_path = file_path
        self._write

    def find_wordlist(self, name):
        '''Returns True if such wordlist exists'''

    def find_all(self):
        print("Etsitään ")
        '''Returns a dictionary with the names (string) of the worldists as 
        keys and the corresponding wordlist (list) as values'''
        return self._read()

    def _read(self):
        print("Luetaan")
        '''Reads the wordlists.csv file'''
        wordlists = {}

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                #print(row)
                #if row_count == 0:
                #    file.write("name,wordlist")
                #    row_count += 1
                #    continue
                row = row.replace("\n", "")
                parts = row.split(",")
                if len(parts) == 2:
                    continue
                print("length of parts", len(parts))
                name = parts[0]
                wordlist = []
                for i in range(3, len(parts) ):
                    wordlist.append(parts[i])
                wordlists[name] = wordlist
        
        return wordlists

    def create(self, wordlist: dict):
        '''Create a new wordlist'''
        print("Luodaan")
        self._write(wordlist)

    def _write(self, wordlist):
        print("kirjoitetaan")
        '''Write a .csv file'''
        self._ensure_file_exists()
        print("päästäänkö tänne?")
        name = wordlist.get_name()
        length = wordlist.get_length()

        with open(self._file_path, 'w', encoding="UTF-8") as file:
            print("tänne?")
            row_count = 0
            while row_count <= length:
                if row_count == 0:
                    file.write("player,victories\n")
                    row_count += 1
                    continue
                word = input("Anna sana:")
                file.write(word)

    def _ensure_file_exists(self):
        Path(self._file_path).touch()
