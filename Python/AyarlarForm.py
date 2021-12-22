from Python.Design.AyarlarFormUI import Ui_AyarlarForm
from PyQt5 import QtWidgets

#BUSINESS
from Python.Business.Config import Config

#UI
import Python.MessageBox as MessageBox
from Python.UrunDisaAktarForm import UrunDisaAktarForm

class AyarlarForm(QtWidgets.QMainWindow, Ui_AyarlarForm):
    def __init__(self, parent=None):
        super(AyarlarForm, self).__init__(parent)
        self.setupUi(self) 
        self.myConfig = Config("config.ini")
        if self.myConfig.get_config('DEFAULT', 'headless') == 'True':
            self.headless = True
            self.headless_true_rb.setChecked(True)
        else:
            self.headless = False
            self.headless_false_rb.setChecked(True)


        self.urunDisaAktarForm = UrunDisaAktarForm()
        self.export_database_button.clicked.connect(self.export_database_button_fun)
        self.import_database_button.clicked.connect(self.import_database_button_fun)
        self.kaydet_button.clicked.connect(self.ayarlari_kaydet)

    def ayarlari_kaydet(self):

        if self.headless_true_rb.isChecked():
            self.myConfig.set_config('DEFAULT', 'headless', 'True')
        else:
            self.myConfig.set_config('DEFAULT', 'headless', 'False')
            
        self.myConfig.save_config()
        MessageBox.getBasicMB(self, "Ayarlar Kaydedildi", "Ayarlarınız başarıyla kaydedildi. Ayarların çalışması için uygulamayı yeniden başlatın.")
    def export_database_button_fun(self):
        self.urunDisaAktarForm.setAll()
        self.urunDisaAktarForm.show()
    def import_database_button_fun(self):
        pass
