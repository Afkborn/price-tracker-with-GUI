from PyQt5 import QtWidgets
from Python.Design.UrunEkleFormUI import Ui_UrunEkleForm
from Python.Model.Product import Product
from time import strptime
from datetime import datetime
from urllib.parse import urlparse

class UrunEkleForm(QtWidgets.QMainWindow,Ui_UrunEkleForm):
    def __init__(self, parent=None):
        super(UrunEkleForm, self).__init__(parent)
        self.setupUi(self)
        self.urun_ekle_button.clicked.connect(self.btnUrunEkle_click)
        self.urun_url_edit.textChanged.connect(self.url_textChanged_listener)

    def getDomainFromURL(self,url:str) -> str:
        """Verilen str türündeki URL adresinin hangi domaine ait olduğunu döner"""
        return ".".join(urlparse(url).netloc.split('.')[0:])

    def url_textChanged_listener(self, *args):
        if len(args[0]) > 0:
            self.urun_domain_edit.setText(self.getDomainFromURL(args[0]))


    def btnUrunEkle_click(self):
        urun_isim = self.urun_ismi_edit.text()
        urun_url = self.urun_url_edit.text()
        urun_domain = self.getDomainFromURL(urun_url)
        kontrol_time  = self.urun_kontrol_suresi_time.time().toPyTime()
        kontrol_time_sec = kontrol_time.hour * 3600 + kontrol_time.minute * 60 + kontrol_time.second
        urun_fiyat_takip = self.urun_fiyat_takip_cb.isChecked()
        urun_stok_takip = self.urun_stok_takip_cb.isChecked()
        # ürünün değerlerini kontrol et
        self.urun_domain_edit.setText(self.getDomainFromURL(self.urun_url_edit.text()))
        myProduct = Product(isim=urun_isim,link=urun_url,check_time_sec=kontrol_time_sec,fiyat_takip=urun_fiyat_takip,stok_takip=urun_stok_takip,domain=urun_domain)
        print(myProduct)
        #TODO ürün verilerini internetten kontrol et
        #TODO ürünün veritabanına kaydedilmesi
        #TODO ürün ekleme formu kapansın
        #TODO ürünler listesine yeni ürünü ekle

