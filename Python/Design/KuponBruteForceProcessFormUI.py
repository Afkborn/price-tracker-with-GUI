# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'KuponBruteForceProcessForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KuponBruteForceProcessForm(object):
    def setupUi(self, KuponBruteForceProcessForm):
        KuponBruteForceProcessForm.setObjectName("KuponBruteForceProcessForm")
        KuponBruteForceProcessForm.resize(820, 237)
        font = QtGui.QFont()
        font.setPointSize(12)
        KuponBruteForceProcessForm.setFont(font)
        self.progressBar = QtWidgets.QProgressBar(KuponBruteForceProcessForm)
        self.progressBar.setGeometry(QtCore.QRect(10, 160, 800, 25))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progress_label = QtWidgets.QLabel(KuponBruteForceProcessForm)
        self.progress_label.setGeometry(QtCore.QRect(10, 190, 800, 25))
        self.progress_label.setAlignment(QtCore.Qt.AlignCenter)
        self.progress_label.setObjectName("progress_label")
        self.durdur_button = QtWidgets.QPushButton(KuponBruteForceProcessForm)
        self.durdur_button.setGeometry(QtCore.QRect(10, 190, 100, 30))
        self.durdur_button.setObjectName("durdur_button")
        self.formLayoutWidget = QtWidgets.QWidget(KuponBruteForceProcessForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 581, 101))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.urun_ismi_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.urun_ismi_edit.setReadOnly(True)
        self.urun_ismi_edit.setObjectName("urun_ismi_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.urun_ismi_edit)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.urun_url_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.urun_url_edit.setReadOnly(True)
        self.urun_url_edit.setObjectName("urun_url_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.urun_url_edit)
        self.urun_domain_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.urun_domain_edit.setReadOnly(True)
        self.urun_domain_edit.setObjectName("urun_domain_edit")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.urun_domain_edit)
        self.formLayoutWidget_2 = QtWidgets.QWidget(KuponBruteForceProcessForm)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(600, 10, 201, 101))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.gecen_sure_time_edit = QtWidgets.QTimeEdit(self.formLayoutWidget_2)
        self.gecen_sure_time_edit.setReadOnly(True)
        self.gecen_sure_time_edit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.gecen_sure_time_edit.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.gecen_sure_time_edit.setObjectName("gecen_sure_time_edit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.gecen_sure_time_edit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.urun_fiyat_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.urun_fiyat_edit.setReadOnly(True)
        self.urun_fiyat_edit.setObjectName("urun_fiyat_edit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.urun_fiyat_edit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.urun_stok_edit = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.urun_stok_edit.setObjectName("urun_stok_edit")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.urun_stok_edit)
        self.formLayoutWidget_3 = QtWidgets.QWidget(KuponBruteForceProcessForm)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(159, 120, 491, 31))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_7.setObjectName("label_7")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.aktif_kupon_edit = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.aktif_kupon_edit.setReadOnly(True)
        self.aktif_kupon_edit.setObjectName("aktif_kupon_edit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aktif_kupon_edit)

        self.retranslateUi(KuponBruteForceProcessForm)
        QtCore.QMetaObject.connectSlotsByName(KuponBruteForceProcessForm)

    def retranslateUi(self, KuponBruteForceProcessForm):
        _translate = QtCore.QCoreApplication.translate
        KuponBruteForceProcessForm.setWindowTitle(_translate("KuponBruteForceProcessForm", "Kupon Brute Force"))
        self.progress_label.setText(_translate("KuponBruteForceProcessForm", "... of ..."))
        self.durdur_button.setText(_translate("KuponBruteForceProcessForm", "Durdur"))
        self.label_2.setText(_translate("KuponBruteForceProcessForm", "İsim"))
        self.label_3.setText(_translate("KuponBruteForceProcessForm", "URL"))
        self.label_5.setText(_translate("KuponBruteForceProcessForm", "Domain"))
        self.label_6.setText(_translate("KuponBruteForceProcessForm", "Geçen Süre"))
        self.gecen_sure_time_edit.setDisplayFormat(_translate("KuponBruteForceProcessForm", "HH:mm:ss"))
        self.label_4.setText(_translate("KuponBruteForceProcessForm", "Fiyat"))
        self.label.setText(_translate("KuponBruteForceProcessForm", "Stok"))
        self.label_7.setText(_translate("KuponBruteForceProcessForm", "Şuan Denenen Kupon:"))
