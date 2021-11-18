
from sys import argv
from os import getcwd
from PyQt5 import QtWidgets, uic


from PyQt5.QtCore import QTimer #timer
from PyQt5.QtTest import QTest # qsleep 


#UI
from Python.Design.UrunlerWindowUI import Ui_UrunlerWindow
from Python.AyarlarForm import AyarlarForm
from Python.HakkimdaForm import HakkımdaForm
from Python.UrunEkleForm import UrunEkleForm
from Python.UrunDetayForm import UrunDetayForm


#MODEL
from Python.Model.Product import Product


class MainWindow(QtWidgets.QMainWindow, Ui_UrunlerWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self) 
        
        self.ayarlarForm = AyarlarForm(self)
        self.urunEkleForm = UrunEkleForm(self)
        self.hakkimdaForm = HakkımdaForm(self)
        self.urunDetayForm = UrunDetayForm(self)

        self.actionAyarlar.triggered.connect(self.showSettingsWindow)
        self.actionCikis.triggered.connect(self.close)
        self.actionHakkimda.triggered.connect(self.showAboutWindow)
        self.actionYeni_Urun.triggered.connect(self.showNewProductWindow)

        myProduct = Product(id=1,isim="aaa",link="https://market.samm.com/raspberry-pi-zero-2-w",check_time_sec=600,fiyat_takip=True,stok_takip=True,fiyat=18.99,stok=True,son_kontrol_zamani=None,domain="market.samm.com")
        self.detay_button.clicked.connect(lambda: self.showProductDetailWindowWithProduct(myProduct))
        

        

    def showSettingsWindow(self):
        self.ayarlarForm.show()

    def showAboutWindow(self):
        self.hakkimdaForm.show()
    def showNewProductWindow(self):
        self.urunEkleForm.show()

    def showProductDetailWindowWithProduct(self,product:Product):
        self.urunDetayForm.show()
        self.urunDetayForm.setProduct(product)
        self.urunDetayForm.loadProduct()




