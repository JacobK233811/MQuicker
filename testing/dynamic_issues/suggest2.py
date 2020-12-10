import sys
from PyQt5 import QtCore, QtWidgets, QtWebEngineWidgets
from bs4 import BeautifulSoup


class First(QtWidgets.QMainWindow):
    closed = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QHBoxLayout(central)
        button = QtWidgets.QPushButton('Continue')
        layout.addWidget(button)
        button.clicked.connect(self.close)

    def closeEvent(self, event):
        self.closed.emit()


class Last(QtWidgets.QMainWindow):
    shouldRestart = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        layout = QtWidgets.QHBoxLayout(central)
        restartButton = QtWidgets.QPushButton('Restart')
        layout.addWidget(restartButton)
        closeButton = QtWidgets.QPushButton('Quit')
        layout.addWidget(closeButton)
        restartButton.clicked.connect(self.restart)
        closeButton.clicked.connect(self.close)

    def restart(self):
        self.exitFlag = True
        self.close()

    def showEvent(self, event):
        # ensure that the flag is always false as soon as the window is shown
        self.exitFlag = False

    def closeEvent(self, event):
        if self.exitFlag:
            self.shouldRestart.emit()


app = QtWidgets.QApplication(sys.argv)
first = First()
last = Last()
first.closed.connect(last.show)
last.shouldRestart.connect(first.show)
first.show()
sys.exit(app.exec_())
