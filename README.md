# Sanaselityspeli

Sovelluksen käyttäjät, eli pelaajat, voivat pelata sanaselityspeliä. Jokainen pelaaja voi luoda itselleen oman käyttäjätilin myöhempää pelaamista varten. 

Sovellus pohjautuu sanaselityspeliin, jossa pelaajat keksivät selitettävät sanat itse.

## Dokumentaatio

[Vaatimusmäärittely](.dokumentaatio/vaatimusmaarittely.md)
[Työaikakirjanpito](.dokumentaatio/tuntikirjanpito.md)
[Changelog](.dokumentaatio/changelog.md)

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
poetry run invoke coverage-report
