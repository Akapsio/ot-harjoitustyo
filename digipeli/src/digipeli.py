class Joukkue:
    
    def __init(self, pelaaja1, pelaaja2):
        self.joukkue = (pelaaja1, pelaaja2)

class Pelaaja:
    
    def __init__(self, nimi):
        self.nimi = nimi

class Sanasto:

    def __init__(self, nimi):
        self.nimi = nimi
        self.sanasto = []

    def hae_sanasto(self, nimi):
        return self.sanasto

    def lisaa_sana(self, sana):
        if len(self.sanasto) < 50:
            self.sanasto.append(sana)
        else:
            raise ValueError("Sanasto on täynnä")
    
    def tallenna_sanasto(self):
        with open(self.nimi, "w") as tiedosto:
            for sana in self.sanasto:
                tiedosto.write(f"{sana}, ")
        
