# LUOKKA HENKILÖTUNNUSTEN KÄSITTELYYN
# ===================================

# KIRJASTOT JA MOODUULIT
# ----------------------

# LUOKAT
# ------

# Henkilötunuksen käsittely
class NationalSSN:
    """Various methods to access and validate Finnish Social Security Number propersties
    """
    def __init__(self, ssn: str) -> None:
        """Generates a Finnish SSN object

        Args:
            ssn (str): 11 character SSN to process
        """
        self.ssn = ssn

        # Laskemalla selviävät ominaisuudet
        self.dateOfBirth = ''
        self.number = 0
        self.gender = ''
        self.checkSum = ''

# Luokan metodit eri osien laskentaan ja järkevyystarkistuksiin
