

from time import strptime, time
from datetime import datetime
from urllib.parse import urlparse
from Python.Business.WebTracker import WebPrice

#UI
from Python.Design.UrunEkleFormUI import Ui_UrunEkleForm
import Python.MessageBox as MessageBox

#Business
from Python.Business.DatabaseProduct import DatabaseProduct
import Python.Business.SupportedWebsites as SupportedWebsites

#Model
from Python.Model.Product import Product


#PYQT5
from PyQt5 import QtWidgets



class UrunEkleForm(QtWidgets.QMainWindow,Ui_UrunEkleForm):
    URUN_EKLENDI_MI = False
    BROWSER_GELDI = False
    def __init__(self, parent=None):
        super(UrunEkleForm, self).__init__(parent)
        self.setupUi(self)
        self.urun_ekle_button.clicked.connect(self.btnUrunEkle_click)
        self.urun_url_edit.textChanged.connect(self.url_textChanged_listener)
        self.urun_otomatik_isim_cb.stateChanged.connect(self.urun_otomatik_isim_cb_stateChanged)
        self.databaseProduct = DatabaseProduct()
        self.urun_birim_cb.addItems(SupportedWebsites.SUPPORTEDUNIT)

    def getDomainFromURL(self,url:str) -> str:
        """Verilen str türündeki URL adresinin hangi domaine ait olduğunu döner"""
        return ".".join(urlparse(url).netloc.split('.')[0:])

    def url_textChanged_listener(self, *args):
        if len(args[0]) > 0:
            self.urun_domain_edit.setText(self.getDomainFromURL(args[0]))

    def urun_otomatik_isim_cb_stateChanged(self, state):
        #2 true 0 false
        if state == 2:
            self.urun_ismi_edit.setText("Webten getiriliyor.")
            self.urun_ismi_edit.setReadOnly(True)
        else:
            self.urun_ismi_edit.setText("")
            self.urun_ismi_edit.setReadOnly(False)

    def getBrowser(self,browser : WebPrice):
        self.browser = browser
        self.BROWSER_GELDI = True
    
    def check_relevance(self,product : Product):
        if not product.get_domain() in  SupportedWebsites.getSupportedWebsites():
            MessageBox.getBasicMB(self,"Hata","Site bilgisi şuan için desteklenmiyor. Detaylı bilgi için Tercihler->Desteklenen Siteler'e bakabilirsiniz.")
            return False
        

        return True

    def btnUrunEkle_click(self):
        urun_isim = self.urun_ismi_edit.text().strip()
        urun_url = self.urun_url_edit.text()
        urun_domain = self.getDomainFromURL(urun_url)
        kontrol_time  = self.urun_kontrol_suresi_time.time().toPyTime()
        kontrol_time_sec = kontrol_time.hour * 3600 + kontrol_time.minute * 60 + kontrol_time.second
        urun_fiyat_takip = self.urun_fiyat_takip_cb.isChecked()
        urun_stok_takip = self.urun_stok_takip_cb.isChecked()
        urun_birim = self.urun_birim_cb.currentText()

        
        self.urun_domain_edit.setText(self.getDomainFromURL(self.urun_url_edit.text()))

        myProduct = Product(isim=urun_isim,link=urun_url,check_time_sec=kontrol_time_sec,fiyat_takip=urun_fiyat_takip,stok_takip=urun_stok_takip,domain=urun_domain,birim=urun_birim)
        #TODO ürünün değerlerini kontrol et
        if self.check_relevance(myProduct):

            if self.BROWSER_GELDI:

                if self.urun_otomatik_isim_cb.isChecked():
                    #get name from web if url support
                    try:
                        productName = self.browser.getProductName(myProduct)
                        self.urun_ismi_edit.setText(productName)
                        myProduct.set_isim(productName)
                    except Exception as e:
                        print(f"Error {e}")
                        MessageBox.getBasicMB(self,"Hata","Ürün ismi webten alınamadı.")
                        self.urun_otomatik_isim_cb.setCheckable(False)
                        self.urun_ismi_edit.setReadOnly(False)
                        return
                
                price = self.browser.getPriceFromProduct(myProduct)
                stock = self.browser.getStockFromProduct(myProduct)
                myProduct.set_fiyat(price)
                myProduct.set_stok(stock)
                myProduct.set_son_kontrol_zamani(time())


                self.databaseProduct.addProduct(myProduct)
                self.URUN_EKLENDI_MI = True
                MessageBox.getBasicMB(self,"Ürün Eklendi","Ürün başarıyla eklendi")

                #inputları temizle
                self.urun_ismi_edit.setText("")
                self.urun_url_edit.setText("")
                self.urun_domain_edit.setText("")
                self.urun_otomatik_isim_cb.setChecked(False)
                
                self.close()
            else:
                print("Browser gelmedi.")
                MessageBox.getBasicMB(self,"Hata","Lütfen durumu bildirin (Browser)")
            
            

