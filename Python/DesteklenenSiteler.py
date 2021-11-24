from Python.Design.DesteklenenSitelerFormUI import Ui_DesteklenenSitelerForm
from PyQt5 import QtWidgets

from Python.Business import SupportedWebsites as SW

class DesteklenenSitelerForm(QtWidgets.QWidget, Ui_DesteklenenSitelerForm):
    def __init__(self,parent=None):
        super(DesteklenenSitelerForm, self).__init__()
        self.setupUi(self)

    def printDesteklenenSiteler(self):
        myText = ""
        for index,site in enumerate(SW.getSupportedWebsites(),1):
            myText += f"{index}) {site}\n"
        self.desteklenen_siteler_label.setText(myText)

    def updateDesteklenenSiteler(self):
        print("Desteklenen siteler güncellendi")