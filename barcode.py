# MODUULI VIIVAKOODIEN TUOTTAMISEEN
# =================================

# KIRJASTOT
# ---------

# ASETUKSET
# ---------

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
    text = text.strip()
    numberOfLetters = len(text)
    weightedSum = 0
    for number in range(numberOfLetters):
        letter = text[number]
        code128BValue = barCodeValue(letter)
        weightedValue = code128BValue * (number + 1)
        weightedSum = weightedSum + weightedValue
    weightedSum = weightedSum + 104
    code128BChecksum = weightedSum % 103
    return code128BChecksum

# TODO: Tee tämä loppuun ja testaa sitä Notepadissa
def createCode128B(text: str) ->str:
    """Creates a complete code128B barcode to be printed using Libre Code 128 font

    Args:
        text (str): The text fo a barcode without checksum

    Returns:
        str: String containing start, barcode, checksum and stop symbols
    """
    code128BBarCodeString = ''
    return code128BBarCodeString

if __name__ == "__main__":
    testString = '128B'
    print ('Painotetut arvot yhteensä:', calculatedCode128BChecksum(testString))

