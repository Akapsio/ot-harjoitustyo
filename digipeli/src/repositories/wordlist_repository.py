'''A repository module in charge of writing, reading and creating
.csv files which contain uniquely named lists of words. '''
from pathlib import Path
from entities.wordlist import Wordlist

class WordlistRepository:
    '''Read wordlists.csv-files, create a wordlist repository: dict from the
    wordlists.csv file, and write the wordlist repository: dict into wordlists.csv
    file '''
    def __init__(self, file_path):
        self._file_path = file_path
        # Kannattaako kirjoittaa valmiiksi vai mitä?
        #self._write()

    def find_wordlist(self, name):
        '''Returns the wordlist if it exists, else raises FileNotFoundError'''

    def find_all(self):
        '''Returns a dictionary with the names (string) of the worldists as
        keys and the corresponding wordlist (list) as values'''
        return self._read()

    def _read(self):
        '''Reading the wordlists.csv file'''
        wordlists = {}

        self._ensure_file_exists()

        with open(self._file_path, encoding="UTF-8") as file:
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
                name = parts[0]
                wordlist = []
                for i in range(3, len(parts) ):
                    wordlist.append(parts[i])
                wordlists[name] = wordlist

        return wordlists

    def create(self, wordlist: Wordlist):
        '''Creates a new wordlist by adding to the wordlists.csv file'''
        self._write(wordlist)

    def _write(self, wordlist: Wordlist):
        '''KORJAA
        Writing the wordlists.csv file'''
        self._ensure_file_exists()
        print("päästäänkö tänne?")
        wordlists = self.find_all()
        wordlists[wordlist.get_name()] = wordlist
        with open(self._file_path, 'w', encoding="UTF-8") as file:
            print("tänne?")
            row_count = 0
            while row_count <= 0:
                if row_count == 0:
                    file.write("player,victories\n")
                    row_count += 1
                    continue
                word = input("Anna sana:")
                file.write(word)

    def _ensure_file_exists(self):
        Path(self._file_path).touch()
