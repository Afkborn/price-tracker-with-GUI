from PyQt5.QtWidgets import  QMessageBox

def getBasicMB(self, title, message):
    QMessageBox.about(self, title, message)
