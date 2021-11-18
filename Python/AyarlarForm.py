from Python.Design.AyarlarFormUI import Ui_AyarlarForm
from PyQt5 import QtWidgets

class AyarlarForm(QtWidgets.QMainWindow, Ui_AyarlarForm):
    def __init__(self, parent=None):
        super(AyarlarForm, self).__init__(parent)
        self.setupUi(self) 