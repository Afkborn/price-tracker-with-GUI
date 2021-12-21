from Python.Design.UrunDisaAktarFormUI import Ui_UrunDisaAktarForm
from PyQt5 import QtWidgets


#MODEL
from Python.Model.Product import Product

class UrunDisaAktarForm(QtWidgets.QMainWindow,Ui_UrunDisaAktarForm):
    def __init__(self,parent=None):
        super(UrunDisaAktarForm,self).__init__(parent)
        self.setupUi(self)

    def setProduct(self,product:Product):
        self.product = product
        print(self.product.get_isim())