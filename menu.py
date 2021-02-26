import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QPushButton , QWidget, QLabel
import os

class ChooseGameUI(QWidget):
    def __init__(self, parent=None):
        super(ChooseGameUI, self).__init__(parent)
        self.title = QLabel("<b> Choose game", self)
        self.title.move(145,90)
        self.title.resize(130, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.marioButton = QPushButton(self)
        self.marioButton.setText("Super Mario")
        self.marioButton.move(130,150)
        self.marioButton.resize(150, 30)
        self.marioButton.setStyleSheet("background-color : #e6a57e")
        QPushButton.setAutoDefault(self.marioButton, True)

        self.snakeButton = QPushButton(self)
        self.snakeButton.setText("Snake")
        self.snakeButton.move(130,200)
        self.snakeButton.resize(150, 30)
        self.snakeButton.setStyleSheet("background-color : #a1cdce")
        QPushButton.setAutoDefault(self.snakeButton, True)

        self.flappyBirdButton = QPushButton(self)
        self.flappyBirdButton.setText("Flappy Bird")
        self.flappyBirdButton.move(130,250)
        self.flappyBirdButton.resize(150, 30)
        self.flappyBirdButton.setStyleSheet("background-color : #beb4c5")
        QPushButton.setAutoDefault(self.flappyBirdButton, True)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,460)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff")
        QPushButton.setAutoDefault(self.goBackButton, True)
        

class changeControlsUI(QWidget):
    def __init__(self, parent=None):
        super(changeControlsUI, self).__init__(parent)
        self.title = QLabel("<b> Change controls", self)
        self.title.move(145,90)
        self.title.resize(130, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,460)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff")
        QPushButton.setAutoDefault(self.goBackButton, True)


class MainMenuUI(QWidget):
    def __init__(self, parent=None):
        super(MainMenuUI, self).__init__(parent)
        self.title = QLabel("<b> COOL TITLE", self)
        self.title.move(152,90)
        self.title.resize(120, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.gameButton = QPushButton(self)
        self.gameButton.setText("Choose game")
        self.gameButton.move(130,150)
        self.gameButton.resize(150, 30)
        self.gameButton.setStyleSheet("background-color : #F5bfd2")
        QPushButton.setAutoDefault(self.gameButton, True)

        self.extButton = QPushButton(self)
        self.extButton.setText("Use with external game")
        self.extButton.move(130,200)
        self.extButton.resize(150, 30)
        self.extButton.setStyleSheet("background-color : #a1cdce")
        QPushButton.setAutoDefault(self.extButton, True)

        self.controlButton = QPushButton(self)
        self.controlButton.setText("Change controls")
        self.controlButton.move(130,250)
        self.controlButton.resize(150, 30)
        self.controlButton.setStyleSheet("background-color : #e5db9c")
        QPushButton.setAutoDefault(self.controlButton, True)

        self.tutorialButton = QPushButton(self)
        self.tutorialButton.setText("Tutorial")
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


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        self.setFixedSize(410, 500)
        self.move(750,250)
        self.mainMenu()

    def mainMenu(self):
        self.MainMenuUI = MainMenuUI(self)
        self.setWindowTitle("Main menu")
        self.setCentralWidget(self.MainMenuUI)
        self.MainMenuUI.gameButton.clicked.connect(self.chooseGame)
        self.MainMenuUI.extButton.clicked.connect(self.useWithExt)
        self.MainMenuUI.controlButton.clicked.connect(self.controls)
        self.MainMenuUI.tutorialButton.clicked.connect(self.tutorial)
        self.MainMenuUI.closeButton.clicked.connect(self.close)
        self.show()

    def chooseGame(self):
        self.ChooseGameUI = ChooseGameUI(self)
        self.setWindowTitle("Choose game")
        self.setCentralWidget(self.ChooseGameUI)
        self.ChooseGameUI.marioButton.clicked.connect(self.startMario)
        self.ChooseGameUI.snakeButton.clicked.connect(self.startSnake)
        #self.ChooseGameUI.flappyBirdButton.clicked.connect()
        self.ChooseGameUI.goBackButton.clicked.connect(self.mainMenu)
        self.show()

    def useWithExt(self):
        return

    def controls(self):
        return

    def tutorial(self):
        return

    def startMario(self):
        os.system('cmd /c "cd ./games/super_mario/ && python main.py"')

    def startSnake(self):
        os.system('cmd /c "cd ./games/snake/ && python snake.py"')
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())




























