# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UrunlerWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UrunlerWindow(object):
    def setupUi(self, UrunlerWindow):
        UrunlerWindow.setObjectName("UrunlerWindow")
        UrunlerWindow.resize(800, 400)
        UrunlerWindow.setMaximumSize(QtCore.QSize(800, 400))
        self.centralwidget = QtWidgets.QWidget(UrunlerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.product_list_widget = QtWidgets.QListWidget(self.centralwidget)
        self.product_list_widget.setGeometry(QtCore.QRect(10, 10, 780, 300))
        self.product_list_widget.setMaximumSize(QtCore.QSize(780, 300))
        self.product_list_widget.setObjectName("product_list_widget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 320, 781, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.detay_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.detay_button.setObjectName("detay_button")
        self.horizontalLayout.addWidget(self.detay_button)
        self.web_start_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.web_start_button.setObjectName("web_start_button")
        self.horizontalLayout.addWidget(self.web_start_button)
        UrunlerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UrunlerWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTercihler = QtWidgets.QMenu(self.menubar)
        self.menuTercihler.setObjectName("menuTercihler")
        UrunlerWindow.setMenuBar(self.menubar)
        self.actionAyarlar = QtWidgets.QAction(UrunlerWindow)
        self.actionAyarlar.setObjectName("actionAyarlar")
        self.actionCikis = QtWidgets.QAction(UrunlerWindow)
        self.actionCikis.setObjectName("actionCikis")
        self.actionHakkimda = QtWidgets.QAction(UrunlerWindow)
        self.actionHakkimda.setObjectName("actionHakkimda")
        self.actionYeni_Urun = QtWidgets.QAction(UrunlerWindow)
        self.actionYeni_Urun.setObjectName("actionYeni_Urun")
        self.menuFile.addAction(self.actionYeni_Urun)
        self.menuTercihler.addAction(self.actionAyarlar)
        self.menuTercihler.addAction(self.actionCikis)
        self.menuTercihler.addSeparator()
        self.menuTercihler.addAction(self.actionHakkimda)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTercihler.menuAction())

        self.retranslateUi(UrunlerWindow)
        QtCore.QMetaObject.connectSlotsByName(UrunlerWindow)

    def retranslateUi(self, UrunlerWindow):
        _translate = QtCore.QCoreApplication.translate
        UrunlerWindow.setWindowTitle(_translate("UrunlerWindow", "Ürünler Listesi"))
        self.detay_button.setText(_translate("UrunlerWindow", "Detaylar"))
        self.web_start_button.setText(_translate("UrunlerWindow", "Web\'de aç"))
        self.menuFile.setTitle(_translate("UrunlerWindow", "Dosya"))
        self.menuTercihler.setTitle(_translate("UrunlerWindow", "Tercihler"))
        self.actionAyarlar.setText(_translate("UrunlerWindow", "Ayarlar"))
        self.actionAyarlar.setShortcut(_translate("UrunlerWindow", "Alt+A"))
        self.actionCikis.setText(_translate("UrunlerWindow", "Çıkış"))
        self.actionHakkimda.setText(_translate("UrunlerWindow", "Hakımda"))
        self.actionYeni_Urun.setText(_translate("UrunlerWindow", "Yeni Ürün"))
        self.actionYeni_Urun.setShortcut(_translate("UrunlerWindow", "Alt+Y"))
