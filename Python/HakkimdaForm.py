
from Python.Design.HakkimdaFormUI import Ui_HakkimdaForm
from PyQt5 import QtWidgets


class HakkımdaForm(QtWidgets.QMainWindow,Ui_HakkimdaForm):
    def __init__(self, parent=None):
        super(HakkımdaForm, self).__init__(parent)
        self.setupUi(self)