from sys import argv
from PyQt5 import QtWidgets
from Python.UrunlerWindow import MainWindow
from os import path, makedirs
import logging

from Python.Business import Compatibility
from datetime import datetime

def get_time_log_config():
    return datetime.now().strftime("%H_%M_%S_%d_%m_%Y")

def set_logging():
    logging.basicConfig(filename=fr'Log/log_{get_time_log_config()}.log', level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')
    logging.info("Logging is set")

def main(): 
    Compatibility.check_folder()
    set_logging()
    if Compatibility.check_compatibility():
        app = QtWidgets.QApplication(argv)
        window = MainWindow()
        window.show()
        app.exec()
    else:
        print("Your computer is not compatible with this program")
        logging.error("Your computer is not compatible with this program")



if __name__ == "__main__":
    main()
