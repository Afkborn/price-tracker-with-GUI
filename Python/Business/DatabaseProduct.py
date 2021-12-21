from os import getcwd
from os.path import exists

import sqlite3 as sql # sqlite3 is a module

#Models
from Python.Model.Product import Product




CREATETABLEPRODUCT = """CREATE TABLE IF NOT EXISTS products (id	INTEGER PRIMARY KEY,isim TEXT NOT NULL,link TEXT NOT NULL,check_time_sec INTEGER NOT NULL,fiyat_takip TEXT NOT NULL, stok_takip TEXT NOT NULL,fiyat INTEGER NOT NULL,stok TEXT NOT NULL,son_kontrol_zamani INTEGER NOT NULL, domain TEXT NOT NULL, birim TEXT)"""
# CREATETABLEPRICES = """CREATE TABLE IF NOT EXISTS prices (id INTEGER NOT NULL, priceTime INTEGER NOT NULL, price INTEGER NOT NULL)"""
# CREATETABLESTOCKS = """CREATE TABLE IF NOT EXISTS stocks (id INTEGER NOT NULL, stockTime INTEGER NOT NULL, stock TEXT NOT NULL)"""



class DatabaseProduct:
    __isLoaded = False
    __dbName = "database.db"
    __products = list()
    __dbLen = 0
    __dbLoc = fr"{getcwd()}\Databases\{__dbName}"

    def __init__(self):
        self.checkDB()


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
        if not exists(self.__dbLoc):
            #Konumda yoksa
            self.__create_product_table()
            

    def loadDB(self):
        """Database dosyasını yüklemeye yarar. Yüklenen değerler Product Classından bir obje olarak products listesine eklenir. """
        self.__products.clear()
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute("SELECT name FROM sqlite_master")
        tableNames = self.im.fetchall()
        newTableNames = []
        for i in tableNames:
            i = str(i).replace("(","").replace(")","").replace("'","").replace(",","")
            newTableNames.append(i)
        tableNames = newTableNames
        if "products" in tableNames : #and "prices" in tableNames and "stocks" in tableNames
            self.im.execute("SELECT * FROM products")
            allDb = self.im.fetchall()
            for i in allDb:
                
                #id,isim,link,check_time_sec,fiyat_takip,stok_takip,fiyat,stok,son_kontrol_zamani,domain
                id, isim, link, check_time_sec, fiyat_takip, stok_takip, fiyat, stok, son_kontrol_zamani, domain, birim = i

                if birim == None:
                    self.update_birim_with_id(id, "TL")

                if stok =="True":
                    stok=True
                elif stok == "False":
                    stok = False
                else:
                    stok = None

                if fiyat_takip == "True":
                    fiyat_takip = True
                else:
                    fiyat_takip = False

                if stok_takip == "True":
                    stok_takip = True
                else:
                    stok_takip = False  

                if fiyat == "None":
                    fiyat = None
                
                myProduct = Product(id,isim,link,check_time_sec,fiyat_takip,stok_takip,fiyat,stok,son_kontrol_zamani,domain,birim)

                self.__products.append(myProduct)
            self.__isLoaded = True
        else:
            self.im.execute(CREATETABLEPRODUCT)
            self.db.commit()
            self.__isLoaded = True
        self.db.close()
        return self.__products

    def __create_product_table(self):
        """kayıtlı konumda (öğrenmek için getDbLoc fonksiyonu kullanılabilir) database oluşturur. """
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(CREATETABLEPRODUCT)
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

    def create_price_list_for_product(self, product:Product):
        """Product Classından bir obje alır ve bu obje için database üzerinde fiyat listesinin tablosunu oluşturur. """
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        tableName = f"prices{product.get_id()}"
        create_table_prices = f"""CREATE TABLE IF NOT EXISTS {tableName} (time INTEGER NOT NULL, price INTEGER NOT NULL)"""
        self.im.execute(create_table_prices)
        self.db.commit()
        self.db.close()

    def addProduct(self,product:Product):
        """Database'e ürün ekler."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        # id,isim,link,check_time_sec,fiyat_takip,stok_takip,fiyat,stok,son_kontrol_zamani,domain
        # get_id get_isim get_link get_check_time_sec get_fiyat_takip get_stok_takip get_fiyat get_stok get_son_kontrol_zamani get_domain
        KEY = f"isim,link,check_time_sec,fiyat_takip,stok_takip,fiyat,stok,son_kontrol_zamani,domain,birim"
        VALUES = f"""
        '{product.get_isim()}',
        '{product.get_link()}',
        '{product.get_check_time_sec()}',
        '{product.get_fiyat_takip()}',
        '{product.get_stok_takip()}',
        '{product.get_fiyat()}',
        '{product.get_stok()}',
        '{product.get_son_kontrol_zamani()}',
        '{product.get_domain()}',
        '{product.get_birim()}'
        """
        self.im.execute(f"INSERT INTO products({KEY}) VALUES({VALUES})")
        product.set_id(self.im.lastrowid)

        self.db.commit()
        self.db.close()

        self.create_price_list_for_product(product)
        self.add_price_priceList(product)

        #create table for product prices

    def get_product_with_id(self,id:int) -> Product:
        """id ile ürünü getirir."""
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        self.im.execute(f"SELECT * FROM products WHERE id = {id}")
        product = self.im.fetchone()
        id, isim, link, check_time_sec, fiyat_takip, stok_takip, fiyat, stok, son_kontrol_zamani, domain, birim = product
        if stok =="True":
            stok=True
        elif stok == "False":
            stok = False
        else:
            stok = None

        if fiyat_takip == "True":
            fiyat_takip = True
        else:
            fiyat_takip = False

        if stok_takip == "True":
            stok_takip = True
        else:
            stok_takip = False  

        if fiyat == "None":
            fiyat = None
        myProduct = Product(id,isim,link,check_time_sec,fiyat_takip,stok_takip,fiyat,stok,son_kontrol_zamani,domain,birim)
        self.db.close()
        return myProduct

    def add_price_priceList(self,product:Product):
        try:
            self.db = sql.connect(self.__dbLoc)
            self.im = self.db.cursor()
            tableName = f"prices{product.get_id()}"
            KEY = f"time,price"
            VALUES = f"'{product.get_son_kontrol_zamani()}','{product.get_fiyat()}'"
            sql_command = f"INSERT INTO {tableName}({KEY}) VALUES({VALUES})"
            self.im.execute(sql_command)
            self.db.commit()
            self.db.close()
        except Exception as e:
            print(e)
            self.create_price_list_for_product(product)
            self.add_price_priceList(product)




    def updatePriceWithID(self,id : int, price : float):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set fiyat = {price} where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()

    def updateStockWithId(self,id : int, stock : bool):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        if stock:
            sql_update_query = f"""Update products set stok = 'True' where id = {id}"""
        else:
            sql_update_query = f"""Update products set stok = 'False' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()

    def updateSonKontrolZamaniWithId(self,id : int, son_kontrol_zamani : float):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set son_kontrol_zamani = {son_kontrol_zamani} where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()
    

     #isim url domain kontrol time fiyat_takip stok_takip
    def update_isim_with_id(self, id:int, isim : str):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set isim = '{isim}' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()
    
    def update_url_with_id(self, id:int, url : str):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set link = '{url}' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()

    def update_check_time_sec_with_id(self, id:int, check_time_sec : int):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set check_time_sec = {check_time_sec} where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()
    
    def update_fiyat_takip_with_id(self,id:int, fiyat_takip : bool):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        if fiyat_takip:
            sql_update_query = f"""Update products set fiyat_takip = 'True' where id = {id}"""
        else:
            sql_update_query = f"""Update products set fiyat_takip = 'False' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()
    
    def update_stok_takip_with_id(self,id:int, stok_takip : bool):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        if stok_takip:
            sql_update_query = f"""Update products set stok_takip = 'True' where id = {id}"""
        else:
            sql_update_query = f"""Update products set stok_takip = 'False' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()
    
    def update_birim_with_id(self,id:int, birim : str):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_update_query = f"""Update products set birim = '{birim}' where id = {id}"""
        self.im.execute(sql_update_query)
        self.db.commit()
        self.db.close()

    def delete_product_with_id(self,id:int):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        sql_delete_query = f"""Delete from products where id = {id}"""
        self.im.execute(sql_delete_query)
        self.db.commit()
        self.db.close()

    def get_price_and_date_from_priceses(self,product:Product):
        self.db = sql.connect(self.__dbLoc)
        self.im = self.db.cursor()
        tableName = f"prices{product.get_id()}"
        sql_select_query = f"SELECT * FROM {tableName}"
        self.im.execute(sql_select_query)
        result = self.im.fetchall()
        self.db.close()
        return result
