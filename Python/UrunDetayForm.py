from Python.Design.UrunDetayFormUI import Ui_UrunDetayForm
from PyQt5 import QtWidgets

from Python.Model.Product import Product

class UrunDetayForm(QtWidgets.QMainWindow, Ui_UrunDetayForm):
    def __init__(self,parent=None):
        super(UrunDetayForm, self).__init__(parent)
        self.setupUi(self)

    def setProduct(self,product:Product):
        self.product = product
        self.product.kendiniTanit()
        
