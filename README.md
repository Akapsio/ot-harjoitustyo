# Tämän viikon muutoksista

Yritin luoda uutta haaraa, jotta voisin jatkaa siitä, mihin olen itse jäänyt. Tämän viikon muutokset masterissa ovat koodikatselmoinnista mergettyjä, enkä osaa palauttaa omaa työtäni takaisin tähän hätään. Koska koodi ei ole omaa käsialaani, en koe ansaitsevani pisteitäkään.

# Sanaselityspeli

Sovelluksen käyttäjät, eli pelaajat, voivat pelata sanaselityspeliä. Jokainen pelaaja voi luoda itselleen oman käyttäjätilin myöhempää pelaamista varten. 

Sovellus pohjautuu sanaselityspeliin, jossa pelaajat keksivät selitettävät sanat itse.

## Dokumentaatio

[Vaatimusmäärittely](./digipeli/dokumentaatio/vaatimusmaarittely.md)

[Työaikakirjanpito](./digipeli/dokumentaatio/tuntikirjanpito.md)

[Changelog](./digipeli/dokumentaatio/changelog.md)

## Asennus

Käynnistä sovellus komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit suoritetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi generoida komennolla:

```bash
poetry run invoke coverage coverage-report
```

### Pylint

Pylintin käynnistäminen tapahtuu komennolla
```bash
poetry run invoke lint
```
