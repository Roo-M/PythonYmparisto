# TESTATAAN MODUULIN identityCheck2.py LUOKKIEN TOIMINTAA

import identityCheck2 # Module to be tested
import pytest # Needed to rise simulated exceptions

# Testeissä käytettävät henkilötunnukset
# --------------------------------------
testSsnOK = identityCheck2.NationalSSN('130728-478N')
testSsnShort = identityCheck2.NationalSSN('130728-78N')
testSsnLong = identityCheck2.NationalSSN('1300728-478N')
testSsnWrongDay = identityCheck2.NationalSSN('120728-478N')
testSsnWrongMonth = identityCheck2.NationalSSN('130628-478N')
testSsnWrongYear = identityCheck2.NationalSSN('130722-478N')
testSsnWrongCentury = identityCheck2.NationalSSN('130728x478N')
testSsnWrongNumber = identityCheck2.NationalSSN('130728-477N')
testSsnWrongCheckSum = identityCheck2.NationalSSN('130728-478A')
testSsnWrongCenturySymbol = identityCheck2.NationalSSN('130728x478N')

# Testitapaukset palautusarvojen ja ominaisuuksien päivittymisen testaamiseen
# ---------------------------------------------------------------------------

# Testitapaus 1: HeTu:n pituus on oikein -> True
def test_checkSsnLengthOK():
    assert testSsnOK.checkSsnLengthOk() == True

# Testitapaus 2: Henkilötunnuksen varmistussumma on oikein
def test_isValidSSN():
    assert testSsnOK.isValidSsn() == True

# Testitapaus 3: Henkilötunnuksen syntymäaika väärin -> False
def test_birthdayWrong():
    assert testSsnWrongDay.isValidSsn() == False
    assert testSsnWrongMonth.isValidSsn() == False
    assert testSsnWrongYear.isValidSsn() == False

# Testitapaus 4: Vuosisatamerkki väärin -> True (vuosisataa ei tarkisteta modulo 31)
def test_centuryWrong():
    assert testSsnWrongCentury.isValidSsn() == True

# Testitapaus 5: Iän laskenta, huom korjattava vuosittain testin tulos
def test_age():
    assert testSsnOK.calculateAge() == 96

# Testitapaus 6: Sukupuolen selvittäminen
def test_gender():
    testSsnOK.getGender()
    assert testSsnOK.gender == 'Nainen'

# Virhetilannetestit
# ------------------

# Testitapaus 7: Liian lyhyen HeTu:n virheilmoitus, huom! assert ei saa olla with:n sisällä
def test_tooShortError():
    with pytest.raises(ValueError) as exceptionMessage:
        testSsnShort.checkSsnLengthOk()
    assert str(exceptionMessage.value) == 'Henkilötunnuksesta puuttuu merkkejä'

# Testitapaus 8: Liian pitkän HeTu:n virheilmoitus
def test_tooLongError():
    with pytest.raises(ValueError) as exceptionMessage:
        testSsnLong.checkSsnLengthOk()
    assert str(exceptionMessage.value) == 'Henkilötunnuksessa ylimääräisiä merkkejä'

# Testitapaus 9: Väärän vuosisatamerkin virheilmoitus, muutoin oikea oikea HeTu
def test_wrongCenturySymbolError():
    with pytest.raises(ValueError) as exceptionMessage:
        testSsnWrongCenturySymbol.getDateOfBirth()
    assert str(exceptionMessage.value) == 'Vuosisatamerkki virheellinen'

# Muita testitapauksia
# --------------------

# Testitapaus 10: Henkilötunnuksen pilkkominen, oikea pituus
def test_splitSsn():
    parts = testSsnOK.splitSsn()
    assert parts == {'days': '13',
                    'months': '07',
                    'years': '28',
                    'century': '-',
                    'number': '478',
                    'checksum': 'N'
                    }

# Testitapaus 11: Syntymäaikaominaisuus ISO-päivämäärä
def test_getDateOfBirth():
    testSsnOK.getDateOfBirth()
    assert testSsnOK.dateOfBirth == '1928-07-13'
