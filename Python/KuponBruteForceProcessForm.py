from Python.Design.KuponBruteForceProcessFormUI import Ui_KuponBruteForceProcessForm
from PyQt5 import QtWidgets

#Model
from Python.Model.Product import Product

from PyQt5.QtCore import QTimer #timer
from PyQt5.QtCore import QTime
from time import gmtime, strftime , time
import Python.MessageBox as MessageBox

from PyQt5.QtTest import QTest

class KuponBruteForceProcessForm(QtWidgets.QMainWindow, Ui_KuponBruteForceProcessForm):
    ISLEM_BASLADI_MI = False
    BROWSER_GELDI = False
    time_counter_sec = 0
    len_couponList = 0
    active_coupon_index = 0
    basarili_sayisi = 0
    basarisiz_sayisi = 0
    basarili_kupon_list = []
    def __init__(self, parent=None):
        super(KuponBruteForceProcessForm, self).__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.time_counter)
        self.durdur_button.clicked.connect(self.durdur)
        

    def setProduct(self,product:Product):
        self.product = product

    def loadProduct(self):
        self.urun_domain_edit.setText(self.product.get_domain())
        self.urun_ismi_edit.setText(self.product.get_isim())
        self.urun_url_edit.setText(self.product.get_link())
        self.urun_fiyat_edit.setText(str(self.product.get_fiyat()))

        if self.product.get_stok():
            self.urun_stok_edit.setText("VAR")
        else:
            self.urun_stok_edit.setText("YOK")


    def time_counter(self):
        self.time_counter_sec += 1
        myTime = strftime('%H:%M:%S', gmtime(self.time_counter_sec)) # second to hour:minute:second
        myTime = QTime.fromString(str(myTime), 'hh:mm:ss') # string to QTime
        self.gecen_sure_time_edit.setTime(myTime) # set QTime to QTimeEdit

        self.progress_label.setText(f"{self.active_coupon_index} of {self.len_couponList} (Başarılı: {self.basarili_sayisi}, Başarısız: {self.basarisiz_sayisi})")

        #progress bar 
        self.progressBar.setValue(self.active_coupon_index)

        if self.active_coupon_index == self.len_couponList:
            self.timer.stop()
            self.ISLEM_BASLADI_MI = False
            if self.basarili_sayisi > 0:
                MessageBox.getBasicMB(self,"Bitti",f"İşlem başarıyla tamamlandı. Başarılı kupon sayısı: {self.basarili_sayisi}")
            else:
                MessageBox.getBasicMB(self,"Bitti","İşlem başarısız.")
            self.close()




    def setCouponList(self,couponList):
        self.couponList = couponList
        self.len_couponList = len(couponList)
        self.progressBar.setMaximum(self.len_couponList)
        self.progress_label.setText(f"{self.active_coupon_index} of {self.len_couponList} (Başarılı: {self.basarili_sayisi}, Başarısız: {self.basarisiz_sayisi})")

        #progress bar 
        self.progressBar.setValue(self.active_coupon_index)


    def durdur(self):
        self.ISLEM_BASLADI_MI = False
        self.close()
        MessageBox.getBasicMB(self,"Durdur","İşlem durduruldu.")

        

    def getBrowser(self,browser):
        self.browser = browser
        self.BROWSER_GELDI = True
    
    def start_process(self):
        if self.BROWSER_GELDI:
            self.ISLEM_BASLADI_MI = True
            self.timer.start(1000)
            if self.browser.add_product_to_basket(self.product):
                
                self.browser.get_basket(self.product)
                for coupon in self.couponList:
                    self.aktif_kupon_edit.setText(coupon)
                    result = self.browser.try_coupon(self.product,coupon)
                    if result:
                        self.basarili_sayisi += 1
                        self.basarili_kupon_list.append(coupon)

                    else:
                        self.basarisiz_sayisi += 1
                    self.active_coupon_index += 1
                    QTest.qWait(200)
                

            else:
                print("ürün eklenmedi.")



