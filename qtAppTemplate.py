# MALLIPOHJA QT-SOVELLUSTEN RAKENTAMISEEN PySide6-KIRJASTON AVULLA
# ================================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------

# Järjestelmäkomentojen kirjasto
import sys

# Pyside-kirjastot
from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

# LUOKKAMÄÄRITYKSET
# -----------------

# Pääikkunan luokka, joka perii QMainWindow-luokan
class MainWindow(QMainWindow):

    # Konstruktori
    def __init__(self):
        QMainWindow.__init__(self)

        # Luodaan käyttöliittymän lataaja
        windowLoader = QUiLoader()

        # Annetaan sille käyttöliittymätiedosto

        windowLoader.load('mainWindow.ui', None)
        self.setWindowTitle('Main Window')

        

if __name__ == "__main__":
    application = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(application.exec())

    
    