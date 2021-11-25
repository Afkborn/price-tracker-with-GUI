
from Python.Design.HakkimdaFormUI import Ui_HakkimdaForm
from PyQt5 import QtWidgets


class HakkimdaForm(QtWidgets.QMainWindow,Ui_HakkimdaForm):
    def __init__(self, parent=None):
        super(HakkimdaForm, self).__init__(parent)
        self.setupUi(self)