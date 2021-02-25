import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("COOL TITLE")
        #self.resize(400, 500)
        self.setFixedSize(410, 500)

        
        self.title = QLabel("<b> COOL TITLE", self)
        self.title.move(152,90)
        self.title.resize(120, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.gameButton = QPushButton(self)
        self.gameButton.setText("Choose game")
        self.gameButton.clicked.connect(self.chooseGameUI)
        self.gameButton.move(130,150)
        self.gameButton.resize(150, 30)
        self.gameButton.setStyleSheet("background-color : #F5bfd2")
        QPushButton.setAutoDefault(self.gameButton, True)

        self.extButton = QPushButton(self)
        self.extButton.setText("Use with external game")
        self.extButton.clicked.connect(self.externalGameUI)
        self.extButton.move(130,200)
        self.extButton.resize(150, 30)
        self.extButton.setStyleSheet("background-color : #a1cdce")
        QPushButton.setAutoDefault(self.extButton, True)

        self.controlButton = QPushButton(self)
        self.controlButton.setText("Change controls")
        self.controlButton.clicked.connect(self.controlsUI)
        self.controlButton.move(130,250)
        self.controlButton.resize(150, 30)
        self.controlButton.setStyleSheet("background-color : #e5db9c")
        QPushButton.setAutoDefault(self.controlButton, True)

        self.tutorialButton = QPushButton(self)
        self.tutorialButton.setText("Tutorial")
        self.tutorialButton.clicked.connect(self.controlsUI)
        self.tutorialButton.move(130,300)
        self.tutorialButton.resize(150, 30)
        self.tutorialButton.setStyleSheet("background-color : #beb4c5")
        QPushButton.setAutoDefault(self.tutorialButton, True)
                
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close") 
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setShortcut('ESC')
        self.closeButton.move(130,350)
        self.closeButton.resize(150, 30)
        self.closeButton.setStyleSheet("background-color : #e6a57e")
        QPushButton.setAutoDefault(self.closeButton, True)

    def mainMenuUI(self):
        print("main menu")
        
    def chooseGameUI(self):
        print("choose game")

    def externalGameUI(self):
        print("use with external game")

    def controlsUI(self):
        print("controls")

    def tutorialUI(self):
        print("tutorial")
                                                                                                    
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
