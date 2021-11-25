from sys import argv
from PyQt5 import QtWidgets
from Python.UrunlerWindow import MainWindow
from os import path, makedirs

folder_names = ["Profile","Python","Databases","Driver"]
def create_folder_if_not_exists(folder_names):
    for folder_name in folder_names:
        if not path.exists(folder_name):
            makedirs(folder_name)



#TODO config file olustur
#TODO config file oku
#TODO chrome yüklü mu kontrol et
#TODO chrome versiyonu kontrol et
#TODO chrome driver kontrol et yoksa indir
#TODO ayarlara chrome headless ayarını ekle


def main():
    create_folder_if_not_exists(folder_names)
    app = QtWidgets.QApplication(argv)
    window = MainWindow()
    window.show()
    app.exec()



if __name__ == "__main__":
    main()
