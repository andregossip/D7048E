import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import QComboBox, QMessageBox, QApplication , QMainWindow , QPushButton , QWidget, QLabel
import os
from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard

class ChooseGameUI(QWidget):
    def __init__(self, parent=None):
        super(ChooseGameUI, self).__init__(parent)
        self.title = QLabel("<b> Choose game", self)
        #self.title.move(145,90)
        self.title.move(360,275)
        self.title.resize(130, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.marioButton = QPushButton(self)
        self.marioButton.setText("Super Mario")
        self.marioButton.move(345,335)
        self.marioButton.resize(150, 30)
        self.marioButton.setStyleSheet("background-color : #e6a57e; font-size: 14px;")
        self.marioButton.setFocus()
        QPushButton.setAutoDefault(self.marioButton, True)

        self.snakeButton = QPushButton(self)
        self.snakeButton.setText("Snake")
        self.snakeButton.move(345,385)
        self.snakeButton.resize(150, 30)
        self.snakeButton.setStyleSheet("background-color : #a1cdce; font-size: 14px;")
        QPushButton.setAutoDefault(self.snakeButton, True)

        self.flappyBirdButton = QPushButton(self)
        self.flappyBirdButton.setText("Flappy Bird")
        self.flappyBirdButton.move(345,435)
        self.flappyBirdButton.resize(150, 30)
        self.flappyBirdButton.setStyleSheet("background-color : #beb4c5; font-size: 14px;")
        QPushButton.setAutoDefault(self.flappyBirdButton, True)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,890)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff; font-size: 14px;")
        QPushButton.setAutoDefault(self.goBackButton, True)
        

class changeControlsUI(QWidget):
    def __init__(self, parent=None):
        super(changeControlsUI, self).__init__(parent)
        self.title = QLabel("<b> Change controls", self)
        #self.title.move(125,90)
        self.title.move(360,275)
        self.title.resize(150, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.left = QLabel("Left", self)
        self.left.move(320, 325)
        self.left.resize(100,40)
        self.left.setStyleSheet("font-size: 14px;")

        self.leftBox = QComboBox(self)
        self.leftBox.addItem("Move hand to the left")
        self.leftBox.addItem("Move head to the left")
        self.leftBox.addItem("Point to the left")
        self.leftBox.addItem("...")
        self.leftBox.addItem("...")
        self.leftBox.addItem("...")
        self.leftBox.move(370, 335)
        self.leftBox.resize(170,25)
        self.leftBox.setStyleSheet("font-size: 14px;")

        self.right = QLabel("Right", self)
        self.right.move(320, 375)
        self.right.resize(100,40)
        self.right.setStyleSheet("font-size: 14px;")

        self.rightBox = QComboBox(self)
        self.rightBox.addItem("Move hand to the right")
        self.rightBox.addItem("Move head to the right")
        self.rightBox.addItem("Point to the right")
        self.rightBox.addItem("...")
        self.rightBox.addItem("...")
        self.rightBox.addItem("...")
        self.rightBox.move(370, 385)
        self.rightBox.resize(170,25)
        self.rightBox.setStyleSheet("font-size: 14px;")

        self.up = QLabel("Up", self)
        self.up.move(320, 425)
        self.up.resize(100,40)
        self.up.setStyleSheet("font-size: 14px;")

        self.upBox = QComboBox(self)
        self.upBox.addItem("Move hand up")
        self.upBox.addItem("Move head up")
        self.upBox.addItem("Point up")
        self.upBox.addItem("...")
        self.upBox.addItem("...")
        self.upBox.addItem("...")
        self.upBox.move(370, 435)
        self.upBox.resize(170,25)
        self.upBox.setStyleSheet("font-size: 14px;")
        

        self.down = QLabel("Down", self)
        self.down.move(320, 475)
        self.down.resize(100,40)
        self.down.setStyleSheet("font-size: 14px;")

        self.downBox = QComboBox(self)
        self.downBox.addItem("Move hand down")
        self.downBox.addItem("Move head down")
        self.downBox.addItem("Point down")
        self.downBox.addItem("...")
        self.downBox.addItem("...")
        self.downBox.addItem("...")
        self.downBox.move(370, 485)
        self.downBox.resize(170,25)
        self.downBox.setStyleSheet("font-size: 14px;")

        self.esc = QLabel("Esc", self)
        self.esc.move(320, 525)
        self.esc.resize(100,40)
        self.esc.setStyleSheet("font-size: 14px;")

        self.escBox = QComboBox(self)
        self.escBox.addItem("Do peace sign")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.move(370, 535)
        self.escBox.resize(170,25)
        self.escBox.setStyleSheet("font-size: 14px;")

        self.enter = QLabel("Enter", self)
        self.enter.move(320, 575)
        self.enter.resize(100,40)
        self.enter.setStyleSheet("font-size: 14px;")

        self.enterBox = QComboBox(self)
        self.enterBox.addItem("Point index finger")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.move(370, 585)
        self.enterBox.resize(170,25)
        self.enterBox.setStyleSheet("font-size: 14px;")

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,890)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff; font-size: 14px;")
        self.goBackButton.setFocus()
        QPushButton.setAutoDefault(self.goBackButton, True)

class tutorialUI(QWidget):
    def __init__(self, parent=None):
        super(tutorialUI, self).__init__(parent)
        self.title = QLabel("<b> Tutorial", self)
        self.title.move(380,90)
        self.title.resize(150, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.upGifLabel = QLabel("", self)
        self.upGifLabel.move(100,160)
        self.upGif = QMovie("gifs/Tutorial_Up.gif")
        self.upGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.upGif.start()
        self.upGifLabel.setMovie(self.upGif)
        self.upGifText = QLabel("some text", self)
        self.upGifText.setStyleSheet("font-size: 14px;")
        self.upGifText.move(195,240)
        self.upGifText.resize(120, 200)

        self.downGifLabel = QLabel("", self)
        self.downGifLabel.move(100,370)
        self.downGif = QMovie("gifs/Tutorial_Down.gif")
        self.downGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.downGif.start()
        self.downGifLabel.setMovie(self.downGif)
        self.downGifText = QLabel("some text", self)
        self.downGifText.setStyleSheet("font-size: 14px;")
        self.downGifText.move(190,450)
        self.downGifText.resize(120, 200)

        self.enterGifLabel = QLabel("", self)
        self.enterGifLabel.move(100,580)
        self.enterGif = QMovie("gifs/One_Finger.gif")
        self.enterGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.enterGif.start()
        self.enterGifLabel.setMovie(self.enterGif)
        self.enterGifText = QLabel("Click the selected button", self)
        self.enterGifText.setStyleSheet("font-size: 14px;")
        self.enterGifText.move(182,660)
        self.enterGifText.resize(120, 200)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,890)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff; font-size: 14px;")
        self.goBackButton.setFocus()
        QPushButton.setAutoDefault(self.goBackButton, True)

class useWithExtUI(QWidget):
    def __init__(self, parent=None):
        super(useWithExtUI, self).__init__(parent)
        self.title = QLabel("<b> Use with external game", self)
        self.title.move(322,275)
        self.title.resize(250, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.minimizeButton = QPushButton(self)
        self.minimizeButton.setText("Minimize UI")
        self.minimizeButton.move(350,335)
        self.minimizeButton.resize(150, 30)
        self.minimizeButton.setStyleSheet("background-color : #F5bfd2; font-size: 14px;")
        self.minimizeButton.setFocus()
        QPushButton.setAutoDefault(self.minimizeButton, True)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,890)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff; font-size: 14px;")
        QPushButton.setAutoDefault(self.goBackButton, True)
        

class MainMenuUI(QWidget):
    def __init__(self, parent=None):
        super(MainMenuUI, self).__init__(parent)
        self.title = QLabel("<b> COOL TITLE", self)
        #self.title.move(152,90)
        self.title.move(152,275)
        self.title.resize(120, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.gameButton = QPushButton(self)
        self.gameButton.setText("Choose game")
        #self.gameButton.move(130,150)
        self.gameButton.move(130,335)
        self.gameButton.resize(150, 30)
        self.gameButton.setStyleSheet("background-color : #F5bfd2; font-size: 14px;")
        self.gameButton.setFocus()
        QPushButton.setAutoDefault(self.gameButton, True)

        self.extButton = QPushButton(self)
        self.extButton.setText("Use with external game")
        #self.extButton.move(130,200)
        self.extButton.move(130,385)
        self.extButton.resize(150, 30)
        self.extButton.setStyleSheet("background-color : #a1cdce; font-size: 14px;")
        QPushButton.setAutoDefault(self.extButton, True)

        self.controlButton = QPushButton(self)
        self.controlButton.setText("Change controls")
        #self.controlButton.move(130,250)
        self.controlButton.move(130,435)
        self.controlButton.resize(150, 30)
        self.controlButton.setStyleSheet("background-color : #e5db9c; font-size: 14px;")
        QPushButton.setAutoDefault(self.controlButton, True)

        self.tutorialButton = QPushButton(self)
        self.tutorialButton.setText("Tutorial")
        #self.tutorialButton.move(130,300)
        self.tutorialButton.move(130,485)
        self.tutorialButton.resize(150, 30)
        self.tutorialButton.setStyleSheet("background-color : #beb4c5; font-size: 14px;")
        QPushButton.setAutoDefault(self.tutorialButton, True)
                
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close")
        self.closeButton.setShortcut('ESC')
        #self.closeButton.move(130,350)
        self.closeButton.move(130,535)
        self.closeButton.resize(150, 30)
        self.closeButton.setStyleSheet("background-color : #e6a57e; font-size: 14px;")
        QPushButton.setAutoDefault(self.closeButton, True)

        self.upGifLabel = QLabel("", self)
        self.upGifLabel.move(440,80)
        self.upGif = QMovie("gifs/Tutorial_Up.gif")
        self.upGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.upGif.start()
        self.upGifLabel.setMovie(self.upGif)
        self.upGifText = QLabel("Go up in the menu", self)
        self.upGifText.setStyleSheet("font-size: 14px;")
        self.upGifText.move(523,160)
        self.upGifText.resize(120, 200)

        self.downGifLabel = QLabel("", self)
        self.downGifLabel.move(440,360)
        self.downGif = QMovie("gifs/Tutorial_Down.gif")
        self.downGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.downGif.start()
        self.downGifLabel.setMovie(self.downGif)
        self.downGifText = QLabel("Go down in the menu", self)
        self.downGifText.setStyleSheet("font-size: 14px;")
        self.downGifText.move(515,440)
        self.downGifText.resize(150, 200)

        self.enterGifLabel = QLabel("", self)
        self.enterGifLabel.move(440,640)
        self.enterGif = QMovie("gifs/One_Finger.gif")
        self.enterGif.setScaledSize(QtCore.QSize().scaled(280, 160, QtCore.Qt.IgnoreAspectRatio))
        self.enterGif.start()
        self.enterGifLabel.setMovie(self.enterGif)
        self.enterGifText = QLabel("Click the selected button", self)
        self.enterGifText.setStyleSheet("font-size: 14px;")
        self.enterGifText.move(507,720)
        self.enterGifText.resize(150, 200)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setGeometry(50, 50, 400, 450)
        #self.setFixedSize(410, 600)
        self.setFixedSize(872, 930)
        self.move(20,20)
        self.mainMenu()

    def mainMenu(self):
        self.MainMenuUI = MainMenuUI(self)
        self.setWindowTitle("Main menu")
        self.setCentralWidget(self.MainMenuUI)
        self.MainMenuUI.gameButton.clicked.connect(self.chooseGame)
        self.MainMenuUI.extButton.clicked.connect(self.useWithExt)
        #self.MainMenuUI.controlButton.clicked.connect(self.changeControls)
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
        #keyboard.press(Key.tab)
        #keyboard.release(Key.tab)
        #self.doInput()

    def useWithExt(self):
        self.useWithExtUI = useWithExtUI(self)
        self.setWindowTitle("Use with external game")
        self.setCentralWidget(self.useWithExtUI)
        self.useWithExtUI.minimizeButton.clicked.connect(self.minimizeWindow)
        self.useWithExtUI.goBackButton.clicked.connect(self.mainMenu)
        self.show()

    def changeControls(self):
        self.changeControlsUI = changeControlsUI(self)
        self.setWindowTitle("Change controls")
        self.setCentralWidget(self.changeControlsUI)
        self.changeControlsUI.goBackButton.clicked.connect(self.mainMenu)
        self.show()

    def tutorial(self):
        self.tutorialUI = tutorialUI(self)
        self.setWindowTitle("Tutorial")
        self.setCentralWidget(self.tutorialUI)
        self.tutorialUI.goBackButton.clicked.connect(self.mainMenu)
        self.show()

    def startMario(self):
        #os.system('cmd /c "cd ./games/super_mario/ && python main.py"')
        os.system('cmd /c "cd ./games/super_mario/"')

    def startSnake(self):
        #os.system('cmd /c "cd ./games/snake/ && python snake.py"')
        os.system('cmd /c "cd ./games/snake/"')
        
    def minimizeWindow(self):
        self.showMinimized()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
