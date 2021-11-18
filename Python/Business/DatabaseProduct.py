from os import getcwd
from os.path import exists

import sqlite3 as sql # sqlite3 is a module

#Models
from Python.Model.Product import Product




CREATETABLEPRODUCT = """CREATE TABLE IF NOT EXISTS products (id	INTEGER PRIMARY KEY,isim TEXT NOT NULL,link TEXT NOT NULL,check_time_sec INTEGER NOT NULL,fiyat_takip TEXT NOT NULL, stok_takip TEXT NOT NULL,fiyat INTEGER NOT NULL,stok TEXT NOT NULL,son_kontrol_zamani INTEGER NOT NULL, domain TEXT NOT NULL)"""
# CREATETABLEPRICES = """CREATE TABLE IF NOT EXISTS prices (id INTEGER NOT NULL, priceTime INTEGER NOT NULL, price INTEGER NOT NULL)"""
# CREATETABLESTOCKS = """CREATE TABLE IF NOT EXISTS stocks (id INTEGER NOT NULL, stockTime INTEGER NOT NULL, stock TEXT NOT NULL)"""



class DatabaseProduct:
    __isLoaded = False
    __dbName = "database.db"
    __products = list()
    __dbLen = 0
    __dbLoc = f"{getcwd()}\Database\{__dbName}"

    def __init__(self):
        pass

    def getDbName(self) -> str:
        """Database adını döner"""
        return self.__dbName

    def getIsLoadDb(self) -> bool:
        """Database'in yüklenip yüklenmediğini döner"""
        return self.__isLoaded

    def getDbLen(self):
        """Databasede kayıtlı olan productların uzunluğunu döner"""
        return self.__dbLen

    def getProductsList(self) -> list:
        """Product listesini döner"""
        return self.__products

    def getDbLoc(self) -> str:
        return self.__dbLoc

    def setDbName(self,dbName:str):
        self.__dbName = dbName
    
    def checkDB(self):
        """Database dosyasını kontrol eder, eğer konumda database dosyası varsa yüklemeye yarayan loadDb fonksiyonu çalışır yoksa o konumda bir database dosyası oluşturmaya yarayan createDb çalışır"""
        if exists(self.__dbLoc):
            #Konumda varsa
            self.__loadDB()
        else:
            #Konumda yoksa
            self.__createDB()

    def __loadDB(self):
        """Database dosyasını yükler"""
        pass


    def __createDB(self):
        """kayıtlı konumda (öğrenmek için getDbLoc fonksiyonu kullanılabilir) database oluşturur. """
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(CREATETABLEPRODUCT)
        # self.im.execute(CREATETABLEPRICES)
        # self.im.execute(CREATETABLESTOCKS)
        self.db.commit()
        self.db.close()
        self.__isLoaded = True
        self.__dbLen = 0

    def getProductLenFromDB(self) -> int:
        """Database'de kayıtlı olan products listesinin uzunluğunu döner."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute("select last_insert_rowid() from products")
        self.__dbLen = len(self.im.fetchall())
        self.db.close() 
        return self.__dbLen 