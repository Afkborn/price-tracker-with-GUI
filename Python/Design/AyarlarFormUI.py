# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AyarlarForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AyarlarForm(object):
    def setupUi(self, AyarlarForm):
        AyarlarForm.setObjectName("AyarlarForm")
        AyarlarForm.resize(219, 477)
        AyarlarForm.setMaximumSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setPointSize(12)
        AyarlarForm.setFont(font)
        self.groupBox = QtWidgets.QGroupBox(AyarlarForm)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 191, 111))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.headless_true_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.headless_true_rb.setObjectName("headless_true_rb")
        self.verticalLayout.addWidget(self.headless_true_rb)
        self.headless_false_rb = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.headless_false_rb.setObjectName("headless_false_rb")
        self.verticalLayout.addWidget(self.headless_false_rb)
        self.kaydet_button = QtWidgets.QPushButton(AyarlarForm)
        self.kaydet_button.setGeometry(QtCore.QRect(10, 440, 75, 25))
        self.kaydet_button.setObjectName("kaydet_button")

        self.retranslateUi(AyarlarForm)
        QtCore.QMetaObject.connectSlotsByName(AyarlarForm)

    def retranslateUi(self, AyarlarForm):
        _translate = QtCore.QCoreApplication.translate
        AyarlarForm.setWindowTitle(_translate("AyarlarForm", "Ayarlar"))
        self.groupBox.setTitle(_translate("AyarlarForm", "Headless"))
        self.headless_true_rb.setText(_translate("AyarlarForm", "True"))
        self.headless_false_rb.setText(_translate("AyarlarForm", "False"))
        self.kaydet_button.setText(_translate("AyarlarForm", "Kaydet"))
