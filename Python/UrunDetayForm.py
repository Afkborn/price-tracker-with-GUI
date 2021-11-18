from Python.Design.UrunDetayFormUI import Ui_UrunDetayForm
from PyQt5 import QtWidgets
from time import gmtime, strftime 
from Python.Model.Product import Product
from PyQt5.QtCore import QTime
class UrunDetayForm(QtWidgets.QMainWindow, Ui_UrunDetayForm):
    def __init__(self,parent=None):
        super(UrunDetayForm, self).__init__(parent)
        self.setupUi(self)

    def setProduct(self,product:Product):
        self.product = product
    
    def loadProduct(self):
        self.urun_id_edit.setText(str(self.product.get_id()))
        self.urun_domain_edit.setText(self.product.get_domain())
        self.urun_ismi_edit.setText(self.product.get_isim())
        self.urun_url_edit.setText(self.product.get_link())


        myTime = strftime('%H:%M:%S', gmtime(self.product.get_check_time_sec())) # second to hour:minute:second
        myTime = QTime.fromString(str(myTime), 'hh:mm:ss') # string to QTime
        self.urun_kontrol_suresi_time.setTime(myTime) # set QTime to QTimeEdit

        self.urun_fiyat_edit.setText(str(self.product.get_fiyat()))
        if self.product.get_stok():
            self.urun_stok_edit.setText("VAR")
        else:
            self.urun_stok_edit.setText("YOK")

        if self.product.get_fiyat_takip():
            self.urun_fiyat_takip_cb.setChecked(True)
        if self.product.get_stok_takip():
            self.urun_stok_takip_cb.setChecked(True)
        
