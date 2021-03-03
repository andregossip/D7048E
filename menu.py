import sys
from PyQt5.QtWidgets import QComboBox, QMessageBox, QApplication , QMainWindow , QPushButton , QWidget, QLabel
import os
from pynput.keyboard import Key, Controller, Listener
from pynput import keyboard

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
        self.marioButton.setFocus()
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
        self.title.move(125,90)
        self.title.resize(150, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.left = QLabel("Left", self)
        self.left.move(100, 140)
        self.left.resize(100,40)

        self.leftBox = QComboBox(self)
        self.leftBox.addItem("Move hand to the left")
        self.leftBox.addItem("Move head to the left")
        self.leftBox.addItem("Point to the left")
        self.leftBox.addItem("...")
        self.leftBox.addItem("...")
        self.leftBox.addItem("...")
        self.leftBox.move(150, 150)
        self.leftBox.resize(150,20)

        self.right = QLabel("Right", self)
        self.right.move(100, 170)
        self.right.resize(100,40)

        self.rightBox = QComboBox(self)
        self.rightBox.addItem("Move hand to the right")
        self.rightBox.addItem("Move head to the right")
        self.rightBox.addItem("Point to the right")
        self.rightBox.addItem("...")
        self.rightBox.addItem("...")
        self.rightBox.addItem("...")
        self.rightBox.move(150, 180)
        self.rightBox.resize(150,20)

        self.up = QLabel("Up", self)
        self.up.move(100, 200)
        self.up.resize(100,40)

        self.upBox = QComboBox(self)
        self.upBox.addItem("Move hand up")
        self.upBox.addItem("Move head up")
        self.upBox.addItem("Point up")
        self.upBox.addItem("...")
        self.upBox.addItem("...")
        self.upBox.addItem("...")
        self.upBox.move(150, 210)
        self.upBox.resize(150,20)

        self.down = QLabel("Down", self)
        self.down.move(100, 230)
        self.down.resize(100,40)

        self.downBox = QComboBox(self)
        self.downBox.addItem("Move hand down")
        self.downBox.addItem("Move head down")
        self.downBox.addItem("Point down")
        self.downBox.addItem("...")
        self.downBox.addItem("...")
        self.downBox.addItem("...")
        self.downBox.move(150, 240)
        self.downBox.resize(150,20)

        self.esc = QLabel("Esc", self)
        self.esc.move(100, 260)
        self.esc.resize(100,40)

        self.escBox = QComboBox(self)
        self.escBox.addItem("Do peace sign")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.addItem("...")
        self.escBox.move(150, 270)
        self.escBox.resize(150,20)

        self.enter = QLabel("Enter", self)
        self.enter.move(100, 290)
        self.enter.resize(100,40)

        self.enterBox = QComboBox(self)
        self.enterBox.addItem("Point index finger")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.addItem("...")
        self.enterBox.move(150, 300)
        self.enterBox.resize(150,20)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,460)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff")
        self.goBackButton.setFocus()
        QPushButton.setAutoDefault(self.goBackButton, True)


class tutorialUI(QWidget):
    def __init__(self, parent=None):
        super(tutorialUI, self).__init__(parent)
        self.title = QLabel("<b> Tutorial", self)
        self.title.move(165,90)
        self.title.resize(150, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,460)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff")
        self.goBackButton.setFocus()
        QPushButton.setAutoDefault(self.goBackButton, True)

class useWithExtUI(QWidget):
    def __init__(self, parent=None):
        super(useWithExtUI, self).__init__(parent)
        self.title = QLabel("<b> Use with external game", self)
        self.title.move(95,90)
        self.title.resize(250, 60) 
        self.title.setStyleSheet("font-size: 18px;")

        self.launchButton = QPushButton(self)
        self.launchButton.setText("Launch")
        self.launchButton.move(130,150)
        self.launchButton.resize(150, 30)
        self.launchButton.setStyleSheet("background-color : #F5bfd2")
        QPushButton.setAutoDefault(self.launchButton, True)

        self.goBackButton = QPushButton(self)
        self.goBackButton.setText("Go back")
        self.goBackButton.move(10,460)
        self.goBackButton.resize(100, 30)
        self.goBackButton.setStyleSheet("background-color : #ffffff")
        self.goBackButton.setFocus()
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
        self.gameButton.setFocus()
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
        self.MainMenuUI.controlButton.clicked.connect(self.changeControls)
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
        self.useWithExtUI.launchButton.clicked.connect(self.minimizeWindow)
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
        os.system('cmd /c "cd ./games/super_mario/ && python main.py"')
        #os.system('cmd /c "cd ./games/super_mario/"')
    def startSnake(self):
        #os.system('cmd /c "cd ./games/snake/ && python snake.py"')
        os.system('cmd /c "cd ./games/snake/"')
    def minimizeWindow(self):
        self.showMinimized()
if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = MainWindow()

    sys.exit(app.exec_())
