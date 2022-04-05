import os

path_to_names_of_wordlists = '/home/tee/Desktop/ot-harjoitustyo/digipeli/src/sanastojen_nimet.txt'
path_to_test_wordlist = '/home/tee/Desktop/ot-harjoitustyo/digipeli/src/sanastot/testi_sanasto.txt'
name_of_test_worldist = "testi_sanasto.txt"
complete_name = os.path.join(path_to_test_wordlist, name_of_test_worldist)

class Wordlist:
    
    def __init__(self, name, length):
        self.name = name
        self.wordlist = []
        self.length = length

    def get_wordlist(self):
        return self.wordlist

    def make_list_from_textfile(self):
        with open(path_to_test_wordlist, "r") as filu:
            textfile = filu.read()
            wordfile = textfile.split(",")
        for w in wordfile:
            self.wordlist.append(w)
       
    def add_word(self, word):
        if len(self.wordlist) < self.length:
            self.wordlist.append(word)
            self.length += 1
        else:
            raise ValueError("Sanasto on täynnä")
    
    def save_wordlist(self):
            with open(self.name, "w") as file:
                for word in self.wordlist:
                    file.write(f"{word}, ")
            with open(path_to_names_of_wordlists, "w") as wordlist:
                wordlist.write(", {self.nimi}")
