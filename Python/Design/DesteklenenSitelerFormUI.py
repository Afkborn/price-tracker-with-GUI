# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DesteklenenSitelerForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DesteklenenSitelerForm(object):
    def setupUi(self, DesteklenenSitelerForm):
        DesteklenenSitelerForm.setObjectName("DesteklenenSitelerForm")
        DesteklenenSitelerForm.resize(400, 300)
        self.desteklenen_siteler_label = QtWidgets.QLabel(DesteklenenSitelerForm)
        self.desteklenen_siteler_label.setGeometry(QtCore.QRect(10, 10, 371, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.desteklenen_siteler_label.setFont(font)
        self.desteklenen_siteler_label.setAlignment(QtCore.Qt.AlignCenter)
        self.desteklenen_siteler_label.setObjectName("desteklenen_siteler_label")
        self.label = QtWidgets.QLabel(DesteklenenSitelerForm)
        self.label.setGeometry(QtCore.QRect(10, 270, 381, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(DesteklenenSitelerForm)
        QtCore.QMetaObject.connectSlotsByName(DesteklenenSitelerForm)

    def retranslateUi(self, DesteklenenSitelerForm):
        _translate = QtCore.QCoreApplication.translate
        DesteklenenSitelerForm.setWindowTitle(_translate("DesteklenenSitelerForm", "Desteklenen Siteler"))
        self.desteklenen_siteler_label.setText(_translate("DesteklenenSitelerForm", "TEST"))
        self.label.setText(_translate("DesteklenenSitelerForm", "<html><head/><body><p>Site desteği için<span style=\" font-weight:600;\"> Tercihler-&gt;İletişim </span> menüsünden iletişime geçebilirsiniz.</p></body></html>"))
