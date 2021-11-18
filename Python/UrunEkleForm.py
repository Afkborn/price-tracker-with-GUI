from PyQt5 import QtWidgets
from Python.Design.UrunEkleFormUI import Ui_UrunEkleForm

class UrunEkleForm(QtWidgets.QMainWindow,Ui_UrunEkleForm):
    def __init__(self, parent=None):
        super(UrunEkleForm, self).__init__(parent)
        self.setupUi(self)
