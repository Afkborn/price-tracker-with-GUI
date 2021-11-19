
from sys import argv
from os import getcwd
from time import strftime,time
from datetime import date, datetime


#PyQT5
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QTime, QTimer #timer
from PyQt5.QtTest import QTest # qsleep 
from PyQt5.QtWidgets import QErrorMessage, QMessageBox

#UI
from Python.Design.UrunlerWindowUI import Ui_UrunlerWindow
from Python.AyarlarForm import AyarlarForm
from Python.HakkimdaForm import HakkımdaForm
from Python.UrunEkleForm import UrunEkleForm
from Python.UrunDetayForm import UrunDetayForm

#Business
from Python.Business.DatabaseProduct import DatabaseProduct
from Python.Business.WebTracker import WebPrice

#MODEL
from Python.Model.Product import Product


class MainWindow(QtWidgets.QMainWindow, Ui_UrunlerWindow):
    __productList = list()

    #isim fiyat_takip stok_takip fiyat stok son_kontrol_zamani link
    __table_widget_name = ["İsim","Fiyat Takip","Stok Takip","Fiyat","Stok Durumu","Son Kontrol Zamanı","Link"]

    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self) 

        #NOTIFY PRODUCT LIST CHANGED TIMER
        self.notify_product_list_changed_timer = QTimer()
        self.notify_product_list_changed_timer.timeout.connect(self.notify_product_list_changed)
        self.notify_product_list_changed_timer.start(1000)

        #kontrol zamanı gelip gelmediğpini kontrol eden timer
        self.kontrol_zamanı_timer = QTimer()
        self.kontrol_zamanı_timer.timeout.connect(self.kontrol_zamani_kontrol_et)
        self.kontrol_zamanı_timer.start(1000)


        #DATABASE
        self.databaseProduct = DatabaseProduct()

        #WEB
        self.web_browser = WebPrice("profile1")


        #FORMS
        self.ayarlarForm = AyarlarForm(self)
        self.urunEkleForm = UrunEkleForm(self)
        self.urunEkleForm.getBrowser(self.web_browser)

        self.hakkimdaForm = HakkımdaForm(self)
        
        self.urunDetayForm = UrunDetayForm(self)
        self.urunDetayForm.getBrowser(self.web_browser)


        self.actionAyarlar.triggered.connect(self.showSettingsWindow)
        self.actionCikis.triggered.connect(self.close)
        self.actionHakkimda.triggered.connect(self.showAboutWindow)
        self.actionYeni_Urun.triggered.connect(self.showNewProductWindow)
        
        self.load_products_from_sqlite()
        self.load_product_table_attributes()
        self.load_product_from_product_list()



        self.detay_button.clicked.connect(self.showProductDetailWindowWithProduct)
        

        

    def showSettingsWindow(self):
        self.ayarlarForm.show()

    def showAboutWindow(self):
        self.hakkimdaForm.show()
    def showNewProductWindow(self):
        self.urunEkleForm.show()

    def showProductDetailWindowWithProduct(self):
        selected = self.product_table_widget.currentRow()
        if not selected == -1:
            self.urunDetayForm.show()
            self.urunDetayForm.setProduct(self.__productList[selected])
            self.urunDetayForm.loadProduct()
        else:
            QMessageBox.about(self, "Error", "Before click detail button select one product from list.")
            

    def createTestProduct(self) -> Product:
        myProduct = Product(id=1,isim="aaa",link="https://market.samm.com/raspberry-pi-zero-2-w",check_time_sec=600,fiyat_takip=True,stok_takip=True,fiyat=18.99,stok=True,son_kontrol_zamani=1637312657.6746655,domain="market.samm.com")
        # self.__productList.append(myProduct)
        return myProduct

    def load_product_table_attributes(self):
        self.product_table_widget.setRowCount(len(self.__productList))

        self.product_table_widget.setColumnCount(len(self.__table_widget_name))
        self.product_table_widget.setHorizontalHeaderLabels(self.__table_widget_name)

        self.product_table_widget.horizontalHeader().setStretchLastSection(True)
        self.product_table_widget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Interactive)

    def load_products_from_sqlite(self):
        """SQLite'den ürünleri çek"""
        self.__productList.clear()
        self.product_table_widget.clear()
        self.__productList = self.databaseProduct.loadDB()

    def notify_product_list_changed(self, control = False):
        if self.urunEkleForm.URUN_EKLENDI_MI:
            self.load_products_from_sqlite()
            self.load_product_table_attributes()
            self.load_product_from_product_list()
            self.urunEkleForm.URUN_EKLENDI_MI = False
        elif control:
            self.load_products_from_sqlite()
            self.load_product_table_attributes()
            self.load_product_from_product_list()
        if self.urunDetayForm.URUN_GUNCELLENDI_MI:
            self.load_products_from_sqlite()
            self.load_product_table_attributes()
            self.load_product_from_product_list()
            self.urunDetayForm.URUN_GUNCELLENDI_MI = False

    def kontrol_zamani_kontrol_et(self):
        for index,product in enumerate(self.__productList):
            guncelTime = time()
            if product.get_son_kontrol_zamani() + product.get_check_time_sec() < guncelTime:
                print(f"{product.get_isim()} güncelleniyor.")
                
                #TODO GÜNCELLEMESİ YAP
                price = self.web_browser.getPriceFromProduct(product)
                stock = self.web_browser.getStockFromProduct(product)
                product.set_fiyat(price)
                product.set_stok(stock)
                product.set_son_kontrol_zamani(time())


                #TODO DATABASE PRODUCT UPDATE FONKSİYONU YAZ
                self.databaseProduct.updatePriceWithID(product.get_id(),product.get_fiyat())
                self.databaseProduct.updateStockWithId(product.get_id(),product.get_stok())
                self.databaseProduct.add_price_priceList(product)
                self.databaseProduct.updateSonKontrolZamaniWithId(product.get_id(),product.get_son_kontrol_zamani())
                
                self.notify_product_list_changed(control=True)





        

    def printTest(self,test):
        print(test)

    def load_product_from_product_list(self):
        """Productları table widget'a yükle"""
        for index,product in enumerate(self.__productList):
            #isim fiyat_takip stok_takip fiyat stok son_kontrol_zamani link
            self.product_table_widget.setItem(index,0,QtWidgets.QTableWidgetItem(product.get_isim()))
            if product.get_fiyat_takip():
                self.product_table_widget.setItem(index,1,QtWidgets.QTableWidgetItem("Evet"))
            else:
                self.product_table_widget.setItem(index,1,QtWidgets.QTableWidgetItem("Hayır"))
            if product.get_stok_takip():
                self.product_table_widget.setItem(index,2,QtWidgets.QTableWidgetItem("Evet"))
            else:
                self.product_table_widget.setItem(index,2,QtWidgets.QTableWidgetItem("Hayır"))


            if product.get_fiyat() == None:
                self.product_table_widget.setItem(index,3,QtWidgets.QTableWidgetItem("None"))
            else:
                self.product_table_widget.setItem(index,3,QtWidgets.QTableWidgetItem(str(product.get_fiyat())))


            if product.get_stok():
                self.product_table_widget.setItem(index,4,QtWidgets.QTableWidgetItem("Var"))
            elif product.get_stok() == False:
                self.product_table_widget.setItem(index,4,QtWidgets.QTableWidgetItem("Yok"))
            else:
                self.product_table_widget.setItem(index,4,QtWidgets.QTableWidgetItem("None"))

            my_time = datetime.fromtimestamp(product.get_son_kontrol_zamani()).strftime(' %H:%M:%S %Y-%m-%d')

            self.product_table_widget.setItem(index,5,QtWidgets.QTableWidgetItem(my_time))
            self.product_table_widget.setItem(index,6,QtWidgets.QTableWidgetItem(product.get_link()))

