# SOVELLUKSEN PÄÄOHJELMA
# ======================

# KIRJASTOT
# ---------

# MODUULIT
# --------

from avtools import sound # Äänimerkit ja äänitiedostot
from avtools import video # Videomoduuli
import identityCheck2

# ASETUKSET
# ---------
kameraIndeksi: int = 1 # Ensimmäinen kamera on aina 0

# TODO: Tee tarkistus siitä että nimi ei voi olla tyhjä

# TODO: Rakenna funktio, jolla kysytään nimet ja muutetaan yhdysnimet isoille alkukirjaimille -> reg exp

while True:
    userGivenSsn = input('Syötä asiakkaan henkilötunnus: ')
    userGivenSsn = userGivenSsn.upper() # Varmistetaan, että tarkiste on isolla

    ssnToCheck = identityCheck2.NationalSSN(userGivenSsn)
    if ssnToCheck.isValidSsn() == True:
        try:
            ssnToCheck.getDateOfBirth()
            ssnToCheck.getGender()
            age = ssnToCheck.calculateAge()
            userGivenLastName = input('Syötä asikkaan sukunimi: ')
            userGivenLastName = userGivenLastName.capitalize()
            userGivenFirstName = input('Syötä asiakkaan etunimi: ')
            userGivenFirstName = userGivenFirstName.capitalize()
            print('Asiakkas: ', userGivenLastName, userGivenFirstName)
            print('Syntymäaika:', ssnToCheck.dateOfBirth)
            print('Ikä:', age)
            print('Sukupuoli:', ssnToCheck.gender)
        except Exception as e:
            print('Syöttämässäsi sosiaaliturvatunnuksessa oli virhe:', e)

    # Kysytään halutaanko poistua ohjelmasta
    wantExit = input('Haluatko päättää ohjelman? Vastaa k/E: ')
    # Muutetaan vastaus isoiksi kirjaimiksi ja tarkistetaan onko se K
    if wantExit.upper == 'K':
        break # Poistutaan ikuisesta silmukasta

