from Python.Design.UrunDisaAktarFormUI import Ui_UrunDisaAktarForm
from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QFileDialog


#MODEL
from Python.Model.Product import Product

#BUSINESS
import Python.Business.ExportProduct  as EP

import Python.MessageBox  as MB

class UrunDisaAktarForm(QtWidgets.QMainWindow,Ui_UrunDisaAktarForm):
    content = "JSON"
    selected_format = "json"
    location = ""
    isOneProduct = False
    def __init__(self,parent=None):
        super(UrunDisaAktarForm,self).__init__(parent)
        self.setupUi(self)
        self.load_supported_export_formats()
        self.kaydet_button.clicked.connect(self.export_product)
        self.iptal_button.clicked.connect(self.close_page)
        self.loc_button.clicked.connect(self.get_file_location)
        self.kayit_tipi_cb.currentTextChanged.connect(self.on_combobox_changed)

    def setProduct(self,product:Product):
        self.product = product
        self.isOneProduct = True
        self.setWindowTitle("Dışa Aktar | Ürün")
    
    def setAll(self):
        self.isOneProduct = False
        
        self.setWindowTitle("Dışa Aktar | Database")
    
    def load_supported_export_formats(self):
        supported_formats = EP.SUPPORTED_EXPORT_FORMATS
        self.kayit_tipi_cb.addItems(supported_formats)
    def close_page(self):
        self.close()
    
    def export_product(self):
        if self.content == "JSON" and self.isOneProduct:
            if self.location == EP.export_product_to_json(self.product,self.location):
                MB.getBasicMB(self,"Urun Disa Aktarıldı",f"Urun Disa Aktarıldı Location: {self.location}")
                self.close()
        elif self.content == "JSON" and not self.isOneProduct:
            if self.location == EP.export_all_products_to_json(self.location):
                MB.getBasicMB(self,"Urunler Disa Aktarıldı",f"Urunler Disa Aktarıldı Location: {self.location}")
                self.close()
                 

    
    def on_combobox_changed(self, content):
        if content == "CSV":
            self.selected_format = "csv"
        elif content == "EXCEL":
            self.selected_format = "xlsx"
        elif content == "JSON":
            self.selected_format = "json"
        self.content = content

    def get_file_location(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        if self.isOneProduct:
            product_fileName = f"product_{self.product.get_id()}.{self.selected_format}"
        else:
            product_fileName = f"database.{self.selected_format}"
        fileName, _ = QFileDialog.getSaveFileName(self,"Export Product",product_fileName,f"{self.content} (*.{self.selected_format})", options=options)
        if fileName:
            self.location = fileName
            self.loc_edit.setText(fileName)
