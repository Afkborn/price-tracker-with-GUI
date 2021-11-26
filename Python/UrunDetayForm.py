
from time import gmtime, strftime , time
from urllib.parse import urlparse


#MODEL
from Python.Model.Product import Product

#SUPPORTED WEBSITES
import Python.Business.SupportedWebsites as SW

#PyQT5
from PyQt5.QtCore import QTime
from PyQt5 import QtWidgets

#Business
from Python.Business.DatabaseProduct import DatabaseProduct
from Python.Business.Chart import Chart


#UI
from Python.Design.UrunDetayFormUI import Ui_UrunDetayForm
from Python.KuponBruteForceForm import KuponBruteForceForm

import Python.MessageBox as MessageBox

class UrunDetayForm(QtWidgets.QMainWindow, Ui_UrunDetayForm):
    URUN_GUNCELLENDI_MI = False
    BROWSER_GELDI = False
    def __init__(self,parent=None):
        super(UrunDetayForm, self).__init__(parent)
        self.setupUi(self)
            #DATABASE
        
        self.SW_brute_force = SW.getSupportedWebsitesForBruteForce()

        self.databaseProduct = DatabaseProduct()
        
        self.kuponBruteForceForm = KuponBruteForceForm()
        
        self.urun_guncelle_button.clicked.connect(self.update_product_price_and_stock)
        self.urun_kaydet_button.clicked.connect(self.update_product)
        self.urun_sil_button.clicked.connect(self.delete_product)
        self.urun_grafik_goster_button.clicked.connect(self.show_product_price_chart)

        self.urun_kupon_bruteforce_button.clicked.connect(self.show_kupon_brute_force_form)


    def setProduct(self,product:Product):
        self.product = product
    
    def getBrowser(self,browser):
        self.browser = browser
        self.BROWSER_GELDI = True
        self.kuponBruteForceForm.getBrowser(browser)


    def show_kupon_brute_force_form(self):
        if self.product.get_domain() in self.SW_brute_force:

            #TODO check kuponlar.txt eğer varsa yükle.
            try:
                self.kuponBruteForceForm.kupon_liste_temizle()
                self.kuponBruteForceForm.read_file("kuponlar.txt")
            except:
                pass
            self.kuponBruteForceForm.setProduct(self.product)
            self.kuponBruteForceForm.show()
        else:
            MessageBox.getBasicMB(self,"Hata","Bu site şuan için bruteforce için desteklenmiyor.")


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
    
    def update_product_price_and_stock(self):
        if self.BROWSER_GELDI:
                print(f"{self.product.get_isim()} güncelleniyor.")
                #TODO GÜNCELLEMESİ YAP
                price = self.browser.getPriceFromProduct(self.product)
                stock = self.browser.getStockFromProduct(self.product)
                self.product.set_fiyat(price)
                self.product.set_stok(stock)
                self.product.set_son_kontrol_zamani(time())


                #TODO DATABASE PRODUCT UPDATE FONKSİYONU YAZ
                self.databaseProduct.updatePriceWithID(self.product.get_id(),self.product.get_fiyat())
                self.databaseProduct.updateStockWithId(self.product.get_id(),self.product.get_stok())
                self.databaseProduct.updateSonKontrolZamaniWithId(self.product.get_id(),self.product.get_son_kontrol_zamani())
                self.databaseProduct.add_price_priceList(self.product)

                self.product = self.databaseProduct.get_product_with_id(self.product.get_id())
                self.loadProduct()
                self.URUN_GUNCELLENDI_MI = True
                MessageBox.getBasicMB(self,"Başarılı","Fiyat ve stok bilgisi güncellendi.")


    def getDomainFromURL(self,url:str) -> str:
        """Verilen str türündeki URL adresinin hangi domaine ait olduğunu döner"""
        return ".".join(urlparse(url).netloc.split('.')[0:])

    def update_product(self):
        urun_isim = self.urun_ismi_edit.text().strip()
        urun_url = self.urun_url_edit.text()
        urun_domain = self.getDomainFromURL(urun_url)

        kontrol_time  = self.urun_kontrol_suresi_time.time().toPyTime()
        kontrol_time_sec = kontrol_time.hour * 3600 + kontrol_time.minute * 60 + kontrol_time.second
        urun_fiyat_takip = self.urun_fiyat_takip_cb.isChecked()
        urun_stok_takip = self.urun_stok_takip_cb.isChecked()  
        
       
        if urun_isim != self.product.get_isim():
            #update isim
            self.databaseProduct.update_isim_with_id(self.product.get_id(),urun_isim)
        if urun_url != self.product.get_link():
            #update url
            self.databaseProduct.update_url_with_id(self.product.get_id(),urun_url)
        if urun_domain != self.product.get_domain():
            #update domain
            self.databaseProduct.update_domain_with_id(self.product.get_id(),urun_domain)
        if kontrol_time_sec != self.product.get_check_time_sec():
            #update kontrol_time
            self.databaseProduct.update_check_time_sec_with_id(self.product.get_id(),kontrol_time_sec)
        if urun_fiyat_takip != self.product.get_fiyat_takip():
            #update fiyat_takip
            self.databaseProduct.update_fiyat_takip_with_id(self.product.get_id(),urun_fiyat_takip)

        if urun_stok_takip != self.product.get_stok_takip():
            #update stok_takip
            self.databaseProduct.update_stok_takip_with_id(self.product.get_id(),urun_stok_takip)
        self.URUN_GUNCELLENDI_MI = True
        MessageBox.getBasicMB(self,"Başarılı","Ürün başarıyla güncellendi.")
        self.close()




    def delete_product(self):
        self.databaseProduct.delete_product_with_id(self.product.get_id())
        self.URUN_GUNCELLENDI_MI = True
        MessageBox.getBasicMB(self,"Başarılı","Ürün başarıyla silindi.")
        self.close()

    def show_product_price_chart(self):
        myChart = Chart(self.product)
        myChart.create_plot()





