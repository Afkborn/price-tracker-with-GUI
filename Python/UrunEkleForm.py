from PyQt5 import QtWidgets
from Python.Design.UrunEkleFormUI import Ui_UrunEkleForm
from Python.Model.Product import Product
from time import strptime, time
from datetime import datetime
from urllib.parse import urlparse
from Python.Business.DatabaseProduct import DatabaseProduct

class UrunEkleForm(QtWidgets.QMainWindow,Ui_UrunEkleForm):
    URUN_EKLENDI_MI = False
    BROWSER_GELDI = False
    def __init__(self, parent=None):
        super(UrunEkleForm, self).__init__(parent)
        self.setupUi(self)
        self.urun_ekle_button.clicked.connect(self.btnUrunEkle_click)
        self.urun_url_edit.textChanged.connect(self.url_textChanged_listener)
        self.databaseProduct = DatabaseProduct()

    def getDomainFromURL(self,url:str) -> str:
        """Verilen str türündeki URL adresinin hangi domaine ait olduğunu döner"""
        return ".".join(urlparse(url).netloc.split('.')[0:])

    def url_textChanged_listener(self, *args):
        if len(args[0]) > 0:
            self.urun_domain_edit.setText(self.getDomainFromURL(args[0]))

    def getBrowser(self,browser):
        self.browser = browser
        self.BROWSER_GELDI = True
    


    def btnUrunEkle_click(self):
        urun_isim = self.urun_ismi_edit.text().strip()
        urun_url = self.urun_url_edit.text()
        urun_domain = self.getDomainFromURL(urun_url)
        kontrol_time  = self.urun_kontrol_suresi_time.time().toPyTime()
        kontrol_time_sec = kontrol_time.hour * 3600 + kontrol_time.minute * 60 + kontrol_time.second
        urun_fiyat_takip = self.urun_fiyat_takip_cb.isChecked()
        urun_stok_takip = self.urun_stok_takip_cb.isChecked()
        #TODO ürünün değerlerini kontrol et
        
        self.urun_domain_edit.setText(self.getDomainFromURL(self.urun_url_edit.text()))
        myProduct = Product(isim=urun_isim,link=urun_url,check_time_sec=kontrol_time_sec,fiyat_takip=urun_fiyat_takip,stok_takip=urun_stok_takip,domain=urun_domain)
        
        if self.BROWSER_GELDI:
            price = self.browser.getPriceFromProduct(myProduct)
            stock = self.browser.getStockFromProduct(myProduct)
            myProduct.set_fiyat(price)
            myProduct.set_stok(stock)
            myProduct.set_son_kontrol_zamani(time())



        self.databaseProduct.addProduct(myProduct)
        self.URUN_EKLENDI_MI = True
        
        self.close()

