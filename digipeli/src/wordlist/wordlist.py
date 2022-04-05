path_to_names_of_wordlists = '/home/tee/Desktop/ot-harjoitustyo/digipeli/src/sanastojen_nimet.txt'
path_to_test_wordlist = '/home/tee/Desktop/ot-harjoitustyo/digipeli/src/sanastot/testi_sanasto.txt'

class Wordlist:
    
    def __init__(self, name, length):
        self.name = name
        self.wordlist = []
        self.length = length

    def get_wordlist(self):
        return self.wordlist
       
    def add_word(self, word):
        if len(self.wordlist) < self.length:
            self.wordlist.append(word)
            self.length += 1
        else:
            print("Sanasto on täynnä")
    
    def save_wordlist(self):
            with open(self.name, "w") as file:
                for word in self.wordlist:
                    file.write(f"{word}, ")
            with open(path_to_names_of_wordlists, "w") as wordlist:
                wordlist.write(", {self.nimi}")
	    

