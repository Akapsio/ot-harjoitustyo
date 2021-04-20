# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä pystyy pelaamaan tuttua pasianssipeliä ilman mitään ylimääräistä. Tavoitteena on saada 
kaikki kortit maittain omiin pinoihinsa pienimmästä suurimpaan järjestyksessä. Kortteja on neljää
eri maata, joista kaksi on punaisia (Hearts (Hertta) ja Diamond (Ruutu)) ja kaksi mustia (Spade 
(Pata) ja Club (Risti)). Jokaista maata on edustaa 13 korttia.  

## Käyttäjät

Peliin on mahdollista rekisteröityä. Tällöin huipputulokset taltioidaan automaattisesti.

## Käyttöliittymä

Sovellus koostuu neljästä eri näkymästä:
1. Kirjatumisnäkymä
2. Käyttäjätunnuksen luomisnäkymä
3. Pasianssi-näkymä
4. TOP 10 tulokset -näkymä
Erilaisten näkymien toiminnallisuuksia avataan paremmin alempana

### Kirjautumisnäkymä

Käyttäjä voi kirjautua sisään omalla käyttäjätunnuksellaan ja sitä vastaavalla salasanalla.
Kirjautuneen käyttäjän pisteet taltioidaan järjestelmään, mikäli käyttäjä yltää kymmenen parhaan 
joukkoon. Käyttäjä voi halutessaan aloittaa pikapelin, jolloin pelaamaan pääsee nopeammin, mutta
pisteitä ei tallenneta siinäkään tapauksessa, että pisteet yltäisivät kymmenen parhaan joukkoon.

### Käyttäjätunnuksen luomisnäkymä

Klikkaamalla luo uusi käyttäjätunnus pelaaja voi luoda itselleen uuden uniikin käyttäjätunnuksen. 
Salasanavaatimusta ei ole.

### Pasianssi-näkymä

Pasianssinäkymä voidaan jakaa kolmeen eri osioon, jotka sijaitsevat vasemmalla ylhäällä, oikealla 
ylhäällä ja alhaalla. Nämä alanäkymät ovat nimeltään Deck (pakka), AceStack (ÄssäPino) ja FieldStack
(KenttäPino). 

#### Deck (Pakka)

Pakkaa klikkaamalla pelaaja nostaa uusia kortteja peliin. Pakan päälimmäinen kortti on ainoa, joka 
on pelattavissa kerrallaan. Pakkaa ei sekoiteta missään vaiheessa, joten järjestys tulee olemaan 
sama alusta loppuun asti. 

#### FieldStack (KenttäPino)

Varsinainen pelialusta. Alussa kentälle jaetaan kortteja seitsemään pinoon siten, ensimmäisessä 
pinossa (vasemmalta alkaen) on yksi kortti, seuraavassa toinen aina edelleen siten, että oikean-
puolimmaisessa pinossa on seitsemän korttia. Pinojen päälimmäinen kortti on alussa näkyvä. Näkyvän 
kortin päälle voidaan asettaa yhtä lukuarvoa pienempi eri värinen kortti.  Mikäli 
päälimmäisen kortin saa siirrettyä pois, sen alla ollut kortti voidaan "avata", eli saattaa 
näkyväksi. Kun pinosta on siirretty kaikki kortit pois, tyhjälle paikalle voidaan asettaa K, eli 
suurin kortti. 

#### AceStack (ÄssäPino)

Päämääränä on saada kaikki kortit tälle alueelle omiin pinoihinsa suuruusjärjestykseen maittain. 

## Pelimoodit

Pelissä on mahdollisuus valita kahdesta moodista mieleinen.

### Nosta-kolme-korttia

Klassinen pasianssi. Pakasta nostetaan kolme korttia kerrallaan, jotka asetetaan pinoon. Pinon 
korteista vain päälimmäinen on käytettävissä. 

### Nosta-yksi-kortti

Helpotettu versio. Peli etenee muuten samalla tavalla, mutta kolmen kortin sijaan nostetaan vain
yksi kortti.

## Jatkokehitysideoita

Pelattavia pelejä voisi olla enemmän.  
