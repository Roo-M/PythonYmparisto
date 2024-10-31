# VIIVAKOODIEN TESTIT
# ===================

# MODUULIT JA KIRJASTOT
# ---------------------

import barcode

# YKSIKKÖTESTIT
# -------------

# Testitapaus 1 Viivakoodin "128B" varmistussumma
def test_128BCheckSum():
    assert barcode.calculatedCode128BChecksum('128B') == 56

# Testitapaus 2 Viivakoodin "128B" sisältö
def test_128BString():
    assert barcode.createCode128B('128B') == 'Ì128BXÎ'
