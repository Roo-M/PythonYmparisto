# VIIVAKOODIEN TESTIT
# ===================

# MODUULIT JA KIRJASTOT
# ---------------------

import barcode
import pytest # Tarvitaan virheiden generointiin

# YKSIKKÖTESTIT
# -------------

# Testitapaus 1 Viivakoodin "128B" varmistussumma 
def test_128BCheckSum():
    assert barcode.calculateCode128BChecksum('128B') == 56

# Testitapaus 2 Viivakoodin "128B" sisältö
def test_128BString():
    assert barcode.createCode128B('128B') == 'Ì128BXÎ'

# Luokan Code128B testit Common-variantille
# ----------------------

text1 = '128B'
barcode1 = barcode.Code128B(text1, 'Common')
def test_Common128B():
    assert barcode1.text == '128B'
    assert barcode1.variant == 'Common'

def test_Common128BValid():
    assert barcode1.checkValidityOfText() == True

text2 = '128Ö'
barcode2 = barcode.Code128B(text2, 'Common')
def test_invalidCharacterCommon():
    with pytest.raises(ValueError) as errorMessage:
        barcode2.checkValidityOfText()

    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

text3 = '128B'
variant = 'A'
barcode3 = barcode.Code128B(text3, variant)

def test_invalidVariant():
    with pytest.raises(ValueError) as errorMessage:
        barcode3.checkValidityOfText()

    assert str(errorMessage.value) == 'Invalid variant (A): Common, Uncommon and BarcodeSoft supported'

# Testit Uncommon-variantille
barcode4 = barcode.Code128B(text1, 'Uncommon')
def test_Uncommon128B():
    assert barcode1.text == '128B'
    assert barcode4.variant == 'Uncommon'

def test_Uncommon128BValid():
    assert barcode4.checkValidityOfText() == True

barcode5 = barcode.Code128B(text2, 'Uncommon')
def test_invalidCharacterUncommon():
    with pytest.raises(ValueError) as errorMessage:
        barcode5.checkValidityOfText()

    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

# Testit BarcodeSoft-variantille
barcode6 = barcode.Code128B(text1, 'BarcodeSoft')
def test_BarcodeSoft128B():
    assert barcode6.text == '128B'
    assert barcode6.variant == 'BarcodeSoft'

def test_BarcodeSoft128BValid():
    assert barcode6.checkValidityOfText() == True

barcode7 = barcode.Code128B(text2, 'BarcodeSoft')
def test_invalidCharacterBarcodeSoft():
    with pytest.raises(ValueError) as errorMessage:
        barcode7.checkValidityOfText()

    assert str(errorMessage.value) == 'Text string contains invalid characters (Ö)'

# Erikoismerkkitestit 

text4 = '128Â'
def test_commonSpecial1():
    barcode8 = barcode.Code128B(text4, 'Common')
    assert barcode8.checkValidityOfText() == True

text5 = '128Ï'
def test_commonSpecial2():
    barcode9 = barcode.Code128B(text5, 'Common')
    assert barcode9.checkValidityOfText() == True

text6 = '128 '
def test_commonSpace():
    barcode10 = barcode.Code128B(text6, 'Common')
    assert barcode10.checkValidityOfText() == True

text7 = '128Ô'
def test_unCommonNormal():
    barcode10 = barcode.Code128B(text7, 'Uncommon')
    assert barcode10.checkValidityOfText() == True

text8 = '128ü'
def test_barcodeSoftNormal():
    barcode10 = barcode.Code128B(text8, 'BarcodeSoft')
    assert barcode10.checkValidityOfText() == True

# Testataan oletusvariantin toiminta
def test_defaultVariant():
    barcode11 = barcode.Code128B(text1)
    assert barcode11.checkValidityOfText() == True

# Testataan oikein muodostetun viivakoodin syntyminen
def test_validBarcode():
    assert barcode1.buildBarcode() == 'Ì128BXÎ'

