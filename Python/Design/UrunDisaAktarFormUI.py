# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UrunDisaAktarForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UrunDisaAktarForm(object):
    def setupUi(self, UrunDisaAktarForm):
        UrunDisaAktarForm.setObjectName("UrunDisaAktarForm")
        UrunDisaAktarForm.resize(434, 150)
        UrunDisaAktarForm.setMaximumSize(QtCore.QSize(450, 150))
        font = QtGui.QFont()
        font.setPointSize(12)
        UrunDisaAktarForm.setFont(font)
        self.gridLayoutWidget = QtWidgets.QWidget(UrunDisaAktarForm)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 411, 121))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.loc_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.loc_button.setObjectName("loc_button")
        self.gridLayout.addWidget(self.loc_button, 0, 2, 1, 1)
        self.kaydet_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.kaydet_button.setObjectName("kaydet_button")
        self.gridLayout.addWidget(self.kaydet_button, 2, 1, 1, 1)
        self.loc_edit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.loc_edit.setReadOnly(True)
        self.loc_edit.setObjectName("loc_edit")
        self.gridLayout.addWidget(self.loc_edit, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setLineWidth(1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.kayit_tipi_cb = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.kayit_tipi_cb.setObjectName("kayit_tipi_cb")
        self.gridLayout.addWidget(self.kayit_tipi_cb, 1, 1, 1, 2)
        self.iptal_button = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.iptal_button.setObjectName("iptal_button")
        self.gridLayout.addWidget(self.iptal_button, 2, 0, 1, 1)

        self.retranslateUi(UrunDisaAktarForm)
        QtCore.QMetaObject.connectSlotsByName(UrunDisaAktarForm)

    def retranslateUi(self, UrunDisaAktarForm):
        _translate = QtCore.QCoreApplication.translate
        UrunDisaAktarForm.setWindowTitle(_translate("UrunDisaAktarForm", "D????a Aktar"))
        self.loc_button.setText(_translate("UrunDisaAktarForm", "..."))
        self.kaydet_button.setText(_translate("UrunDisaAktarForm", "Kaydet"))
        self.label.setText(_translate("UrunDisaAktarForm", "Konum"))
        self.label_2.setText(_translate("UrunDisaAktarForm", "Kay??t Tipi"))
        self.iptal_button.setText(_translate("UrunDisaAktarForm", "??ptal"))
