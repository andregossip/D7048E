import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("COOL TITLE")
        self.resize(400, 500)
        #self.centralWidget = QLabel("Hello, World")
        #self.centralWidget.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        #self.setCentralWidget(self.centralWidget)

        self.playButton = QPushButton(self)
        self.playButton.setText("Choose game")
        self.playButton.move(130,150)
        self.playButton.resize(150, 30)

        self.extButton = QPushButton(self)
        self.extButton.setText("Use with external game")
        self.extButton.move(130,200)
        self.extButton.resize(150, 30)

        self.controlButton = QPushButton(self)
        self.controlButton.setText("Change controls")
        self.controlButton.move(130,250)
        self.controlButton.resize(150, 30)
                
        self.closeButton = QPushButton(self)
        self.closeButton.setText("Close") 
        self.closeButton.clicked.connect(self.close)
        self.closeButton.setShortcut('ESC')
        self.closeButton.move(130,300)
        self.closeButton.resize(150, 30)
                                                                                                    
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
