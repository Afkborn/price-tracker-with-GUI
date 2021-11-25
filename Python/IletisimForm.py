from Python.Design.IletisimFormUI import Ui_IletisimForm
from PyQt5 import QtWidgets

class IletisimForm(QtWidgets.QMainWindow, Ui_IletisimForm):
    def __init__(self,parent=None):
        super(IletisimForm,self).__init__(parent)
        self.setupUi(self)