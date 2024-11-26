# PYSIDE6-MALLI SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# ==============================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

import sys

from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtUiTools import QUiLoader

# LUOKKAMÄÄRITYKSET
# -----------------

# Luodaan käyttöliittymätiedoston lataajaobjekti QUiLoader-luokasta
loader = QUiLoader()

# Määritellään sovellusobjekti
app = QtWidgets.QApplication(sys.argv)

# Luodaan pääikkunan objekti ui-tiedoston perusteella, pääikkunalla ei ole isäntäobjektia
window = loader.load('mainWindow.ui', None)

# Asetetaan pääikkunan nimi
window.setWindowTitle('PÄÄIKKUNA')
label = window.findChild(QtWidgets.QLabel, 'label')

statusBar = window.findChild(QtWidgets.QStatusBar, 'statusbar')
if statusBar != None:
    statusBar.showMessage('Kaikki hyvin', -1)

if label != None:
    label.setText('Muutettu tekstiä')

else:
    if statusBar != None:
        statusBar.showMessage('Pielen meni', 5000)

# Määritellään ikkuna näkyväksi
window.show()

# Ajetaan sovellus
app.exec()
