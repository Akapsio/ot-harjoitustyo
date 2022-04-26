'''A repository module in charge of writing, reading and creating
.csv files which contain uniquely named lists of words. '''
from pathlib import Path
from entities.wordlist import Wordlist

class WordlistRepository:
    '''Read wordlists.csv-files, create a Wordlists: dict from the
    wordlists.csv file, and write the wordlists: dict into wordlists.csv
    file'''
    def __init__(self, file_path):
        self._file_path = file_path
        wordlists = self.find_all()
        self._write(wordlists)

    def find_wordlist(self, name):
        '''Returns the wordlist if it exists, else raises FileNotFoundError'''
        for wordlist in self.find_all():
            if wordlist == name:
                return wordlist[name]
        raise FileNotFoundError

    def find_all(self):
        '''Returns a dictionary with the names: string of the worldists as
        keys and the corresponding wordlist: list as values'''
        return self._read()

    def _read(self):
        '''Reading the wordlists.csv file'''
        wordlists = {}

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
            row_count = 0
            for row in file:
                if row_count == 0:
                    row_count += 1
                    continue
                row = row.replace("\n", "")
                parts = row.split(",")
                if len(parts) == 2:
                    continue
                name = parts[0]
                wordlist = []
                for i in range(1, len(parts) ):
                    wordlist.append(parts[i])
                wordlists[name] = wordlist
        return wordlists

    def create(self, new_wordlist: Wordlist):
        '''Creates a new wordlist by adding to the wordlists.csv file'''
        wordlists = self.find_all()

        if self._ensure_name_is_free(new_wordlist, wordlists):
            wordlists[new_wordlist.get_name] = new_wordlist.get_list()
        else:
            raise ValueError
        print(wordlists)
        self._write(wordlists)

    def _write(self, wordlists: dict):
        '''Writing to wordlists.csv file'''

        self._ensure_file_exists()

        print("päästäänkö tänne?")
        with open(self._file_path, "w", encoding="UTF-8") as file:
            file.write("name,words\n")
            for wordlist in wordlists:
                file.write(f"{wordlist},")
                iterated_list = self.find_wordlist(wordlist)
                for i in len(iterated_list):
                    if i == len(iterated_list) - 1:
                        file.write(f"{wordlist[wordlist][i]}\n")
                    file.write(f"{wordlist[wordlist][i]},")

    def _ensure_file_exists(self):
        Path(self._file_path).touch()

    def _ensure_name_is_free(self, new_wordlist: Wordlist, wordlists: dict):
        for wordlist in wordlists:
            if wordlist == new_wordlist.get_name():
                return False
        return True
