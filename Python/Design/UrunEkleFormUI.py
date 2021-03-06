# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UrunEkleForm.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UrunEkleForm(object):
    def setupUi(self, UrunEkleForm):
        UrunEkleForm.setObjectName("UrunEkleForm")
        UrunEkleForm.resize(450, 300)
        UrunEkleForm.setMaximumSize(QtCore.QSize(450, 300))
        font = QtGui.QFont()
        font.setPointSize(12)
        UrunEkleForm.setFont(font)
        self.formLayoutWidget = QtWidgets.QWidget(UrunEkleForm)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 431, 271))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.urun_ismi_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_ismi_edit.setFont(font)
        self.urun_ismi_edit.setObjectName("urun_ismi_edit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.urun_ismi_edit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.urun_url_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.urun_url_edit.setFont(font)
        self.urun_url_edit.setObjectName("urun_url_edit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.urun_url_edit)
        self.urun_fiyat_takip_cb = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.urun_fiyat_takip_cb.setChecked(True)
        self.urun_fiyat_takip_cb.setObjectName("urun_fiyat_takip_cb")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.urun_fiyat_takip_cb)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.urun_stok_takip_cb = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.urun_stok_takip_cb.setChecked(True)
        self.urun_stok_takip_cb.setObjectName("urun_stok_takip_cb")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.urun_stok_takip_cb)
        self.urun_kontrol_suresi_time = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.urun_kontrol_suresi_time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.urun_kontrol_suresi_time.setTime(QtCore.QTime(0, 10, 0))
        self.urun_kontrol_suresi_time.setObjectName("urun_kontrol_suresi_time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.urun_kontrol_suresi_time)
        self.urun_ekle_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.urun_ekle_button.setObjectName("urun_ekle_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.urun_ekle_button)
        self.urun_temizle_button = QtWidgets.QPushButton(self.formLayoutWidget)
        self.urun_temizle_button.setObjectName("urun_temizle_button")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.urun_temizle_button)
        self.urun_domain_edit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.urun_domain_edit.setReadOnly(True)
        self.urun_domain_edit.setObjectName("urun_domain_edit")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.urun_domain_edit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.urun_otomatik_isim_cb = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.urun_otomatik_isim_cb.setCheckable(True)
        self.urun_otomatik_isim_cb.setObjectName("urun_otomatik_isim_cb")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.urun_otomatik_isim_cb)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.urun_birim_cb = QtWidgets.QComboBox(self.formLayoutWidget)
        self.urun_birim_cb.setObjectName("urun_birim_cb")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.urun_birim_cb)

        self.retranslateUi(UrunEkleForm)
        QtCore.QMetaObject.connectSlotsByName(UrunEkleForm)

    def retranslateUi(self, UrunEkleForm):
        _translate = QtCore.QCoreApplication.translate
        UrunEkleForm.setWindowTitle(_translate("UrunEkleForm", "??r??n Ekle"))
        self.label.setText(_translate("UrunEkleForm", "??sim"))
        self.label_2.setText(_translate("UrunEkleForm", "URL"))
        self.urun_fiyat_takip_cb.setText(_translate("UrunEkleForm", "Fiyat Takip Et"))
        self.label_3.setText(_translate("UrunEkleForm", "Kontrol S??resi"))
        self.urun_stok_takip_cb.setText(_translate("UrunEkleForm", "Stok Takip Et"))
        self.urun_kontrol_suresi_time.setDisplayFormat(_translate("UrunEkleForm", "HH:mm:ss"))
        self.urun_ekle_button.setText(_translate("UrunEkleForm", "Ekle"))
        self.urun_temizle_button.setText(_translate("UrunEkleForm", "Temizle"))
        self.label_4.setText(_translate("UrunEkleForm", "Domain"))
        self.urun_otomatik_isim_cb.setText(_translate("UrunEkleForm", "Otomatik ??sim"))
        self.label_5.setText(_translate("UrunEkleForm", "Birim"))
