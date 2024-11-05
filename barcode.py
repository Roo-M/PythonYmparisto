# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

# FUNKTIOT
# --------

def barCodeValue(character: str) ->int:
    """Calculates a value of character used in Code128B barcode generation

    Args:
        character (str): a single character to convert

    Returns:
        int: Code128B value for calculating the checksum
    """
    asciiValue = ord(character)
    code128BValue = asciiValue - 32
    return code128BValue

def calculatedCode128BChecksum(text: str) ->int:
    """Calculates a checksum for a given string

    Args:
        text (str): text string to use in a barcode

    Returns:
        int: Modulo 103 checksum of weighted values
    """
    text = text.strip() # Poistetaan ylimääräiset tyhjät alusta ja lopusta
    numberOfLetters = len(text)
    weightedSum = 0 # Alustetaan tyhjäksi

    # Käydään teksti kirjaimittain läpi
    for number in range(numberOfLetters):
        letter = text[number]

        # Kutsutaan funktiota, joka palauttaa 128-koodin arvon
        code128BValue = barCodeValue(letter)

        # Lasketaan sijainnilla painotettu arvo
        weightedValue = code128BValue * (number + 1)

        # Lisätään se summaan
        weightedSum = weightedSum + weightedValue
    
    # Lisätään alkumerkin arvo silmukan jälkeen
    weightedSum = weightedSum + 104

    # Lasketaan jakojäännös mod 103
    code128BChecksum = weightedSum % 103
    return code128BChecksum

def createCode128B(text: str) ->str:
    """Creates a complete code128B barcode to be printed using Libre Code128 font

    Args:
        text (str): The text fo a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BBarCodeString = ''
    startChar = chr(204)
    stopChar = chr(206)
    checkSum = calculatedCode128BChecksum(text)
    checkSumSymbol = chr(checkSum +32)
    code128BBarCodeString = startChar + text + checkSumSymbol + stopChar
    return code128BBarCodeString

# LUOKKA VIIVAKOODEILLE
# =====================

class Viivakoodi:
    pass
    if __name__ == "__main__":
        testString = '128B'
        print ('Painotetut arvot yhteensä:', calculatedCode128BChecksum(testString))
        print('Koko viivakoodi on', createCode128B('128B'))

