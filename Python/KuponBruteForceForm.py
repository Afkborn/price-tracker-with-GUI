from Python.Design.KuponBruteForceFormUI import Ui_KuponBruteForceForm
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QInputDialog, QFileDialog

#Model
from Python.Model.Product import Product

#UI
from Python.KuponBruteForceProcessForm import KuponBruteForceProcessForm

import Python.MessageBox as MessageBox

from PyQt5.QtTest import QTest

class KuponBruteForceForm(QtWidgets.QMainWindow, Ui_KuponBruteForceForm):
    BROWSER_GELDI = False
    

    def __init__(self, parent=None):
        super(KuponBruteForceForm, self).__init__(parent)
        self.setupUi(self)

        self.kuponBruteForceProcessForm = KuponBruteForceProcessForm()


        self.kupon_liste_temizle_button.clicked.connect(self.kupon_liste_temizle)
        self.kupon_ekle_button.clicked.connect(self.kupon_ekle)
        self.kupon_sil_button.clicked.connect(self.kupon_sil)
        self.kupon_yukle_button.clicked.connect(self.kupon_yukle)
        self.kupon_liste_save_button.clicked.connect(self.kupon_liste_save)
        self.kupon_baslat_button.clicked.connect(self.kupon_baslat)
        self.kupon_liste.itemClicked.connect(self.item_activated_listener)

    def item_activated_listener(self,item):
        #print(item.text())
        pass

    def setProduct(self,product:Product):
        self.product = product
    
    def getBrowser(self,browser):
        self.browser = browser
        self.BROWSER_GELDI = True
        self.kuponBruteForceProcessForm.getBrowser(browser)


    def kupon_liste_temizle(self):
        self.kupon_liste.clear()
    
    def kupon_ekle(self):
      kupon, result = QInputDialog.getText(self, 'Kupon Ekle', 'Kupon:')
      if result:
          self.kupon_liste.addItem(kupon)


    def kupon_sil(self):
        try:
            selected_item_index = self.kupon_liste.currentRow()
            self.kupon_liste.takeItem(selected_item_index)
        except:
            MessageBox.getBasicMB(self,"Hata","Lütfen silmek istediğiniz kuponu seçiniz.")

    def read_file(self,filename):
        #TODO dosyasının boyutunu vb kontrol et 
        with open(filename, "r") as f:
            for line in f:
                line = line.replace("\n","")
                self.kupon_liste.addItem(line)

    def save_file(self,filename,kuponList):
        with open(filename, "w") as f:
            for line in kuponList:
                f.write(line + "\n")

    def kupon_yukle(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Kuponları içeren text dosyasını seçin", "","TXT Files (*.txt)", options=options)
        if fileName:
            self.read_file(fileName)

    def kupon_liste_save(self):
        kuponList = []
        for x in range(self.kupon_liste.count()):
            kuponList.append((self.kupon_liste.item(x)).text())
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Kaydetmek için konum seçin","kuponlar.txt","Text Files (*.txt)", options=options)
        if fileName:
            self.save_file(fileName,kuponList)


    def kupon_baslat(self):
        kupon_liste_txt = []
        for x in range(self.kupon_liste.count()):
            kupon_liste_txt.append((self.kupon_liste.item(x)).text())
        self.kuponBruteForceProcessForm.setProduct(self.product)
        self.kuponBruteForceProcessForm.loadProduct()

        self.kuponBruteForceProcessForm.setCouponList(kupon_liste_txt)

        self.kuponBruteForceProcessForm.show()
        QTest.qWait(200)
        self.kuponBruteForceProcessForm.start_process()
        






