from PyQt5 import QtWidgets
from Python.Design.UrunGuncelleniyorFormUI import Ui_UrunGuncelleniyorForm

class UrunGuncelleniyorForm(QtWidgets.QMainWindow,Ui_UrunGuncelleniyorForm):
    def __init__(self, parent=None):
        super(UrunGuncelleniyorForm, self).__init__(parent)
        self.setupUi(self)

    def changeLabelText(self,text:str):
        text = f"{text} güncelleniyor."
        self.urun_guncelleniyor_label.setText(text)