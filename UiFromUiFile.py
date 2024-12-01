# PYSIDE6-MALLI SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# ==============================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

import os # Tarvitaan mm. hakemistopolkujen käsittelyyn
import sys # Tarvitaan sovelluksen argumenttien käsittelyyn
from PySide6 import QtCore, QtGui, QtWidgets # Tärkeimmät Qt:n moduulit
from PySide6.QtUiTools import QUiLoader # Tarvitaan käyttöliittymätiedoston lataamiseen

# KÄYTTÖLIITTYMÄN LUOMINEN
# ------------------------

# Luodaan käyttöliittymätiedoston lataajaobjekti QUiLoader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perusteella, pääikkunalla ei ole isäntäobjektia
window = loader.load('mainWindow.ui', None)

# Asetetaan pääikkunan nimi
window.setWindowTitle('PÄÄIKKUNA')

# Luodaan osoitin (pointer), joka viittaa käyttöliittymän elementtiin label
label = window.findChild(QtWidgets.QLabel, 'label')

# Muutetaan label-elementin sisältö
label.setText('Muutettu tekstiä')

# Luodaan osoitin sovelluksen tilariville
statusBar = window.findChild(QtWidgets.QStatusBar, 'statusbar')

# Kirjoitetaan teksti tilariville ja pidetään se näkyvissä koko ajan (-1)
statusBar.showMessage('Kaikki hyvin', -1)

# Määritellään ikkuna näkyväksi, oletuksena kaikki ikkunat ovat piilotettuja
window.show()

# Ajetaan sovellus, tämä luo tapahtuman käsittelijän (event loop)
# Python 2 sovelluksissa komento on app.exec_(), tuettu edelleen
app.exec()
