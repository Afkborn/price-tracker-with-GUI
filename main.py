from sys import argv
from PyQt5 import QtWidgets
from Python.UrunlerWindow import MainWindow

def main():
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__":
    main()
