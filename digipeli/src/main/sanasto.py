class Sanasto:
    
    def __init__(self, nimi, pituus):
        if tarkista_sanaston_nimen_saatavuus(nimi):
            self.nimi = nimi
        self.sanasto = []
        self.pituus = pituus

    def hae_sanasto(self, nimi):
        try:
            with open(nimi) as tiedosto:
                sanasto = tiedosto.split(",")
                return sanasto
        except ValueError:
            print(f"{nimi} nimistä tiedostoa ei löytynyt")
   
    def tarkista_sanaston_nimen_saatavuus(self, nimi: str):
        with open("sanastojen_nimet.txt") as tiedosto:
            mjono = tiedosto.read()
            sanastojen_nimet = mjono.split(",")
            for sanasto in sanastojen_nimet:
                if sanasto != nimi:
                    return True
                else:
                    raise ValueError("Nimi on jo käytössä")
        return False
           
    def lisaa_sana(self, sana):
        if len(self.sanasto) < self.pituus:
            self.sanasto.append(sana)
        else:
            raise ValueError("Sanasto on täynnä")
    
    def tallenna_sanasto(self):
        with open(self.nimi, "w") as tiedosto:
            for sana in self.sanasto:
                tiedosto.write(f"{sana}, ")
        with open("Sanastot") as tiedosto:
            tiedosto.write(", {self.nimi}")
	    
