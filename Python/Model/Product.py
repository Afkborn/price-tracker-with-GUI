class Product:
    def __init__(self,
    id:int=None, # id
    isim:str=None, #ürün ismi
    link:str=None, # ürün linki
    check_time_sec:int=None, #kontrol zamanı (saniye)
    fiyat_takip:bool=None, #fiyat takip
    stok_takip:bool=None, #stok takip
    fiyat:float=None,  #ürün fiyatı
    stok:bool=None, #stok durumu
    son_kontrol_zamani:float=None, #son kontrol zamanı
    domain:str=None, #domain

    ) -> None:
        self.__id = id
        self.__isim = isim
        self.__link = link
        self.__check_time_sec = check_time_sec
        self.__fiyat_takip = fiyat_takip
        self.__stok_takip = stok_takip
        self.__fiyat = fiyat
        self.__stok = stok
        self.__son_kontrol_zamani = son_kontrol_zamani
        self.__domain = domain

 
    def __str__(self) -> str:
        return f"Product(id={self.__id},isim={self.__isim},link={self.__link},check_time_sec={self.__check_time_sec},fiyat_takip={self.__fiyat_takip},stok_takip={self.__stok_takip},fiyat={self.__fiyat},stok={self.__stok},son_kontrol_zamani={self.__son_kontrol_zamani},domain={self.__domain})"

    def get_id(self):
        return self.__id
    def get_isim(self):
        return self.__isim
    def get_link(self):
        return self.__link
    def get_check_time_sec(self):
        return self.__check_time_sec
    def get_fiyat_takip(self):
        return self.__fiyat_takip
    def get_stok_takip(self):
        return self.__stok_takip
    def get_fiyat(self):
        return self.__fiyat
    def get_stok(self):
        return self.__stok
    def get_son_kontrol_zamani(self):
        return self.__son_kontrol_zamani
    def get_domain(self):
        return self.__domain

    def set_id(self,id):
        self.__id = id
    def set_isim(self,isim):
        self.__isim = isim
    def set_link(self,link):
        self.__link = link
    def set_check_time_sec(self,check_time_sec):
        self.__check_time_sec = check_time_sec
    def set_fiyat_takip(self,fiyat_takip):
        self.__fiyat_takip = fiyat_takip
    def set_stok_takip(self,stok_takip):
        self.__stok_takip = stok_takip
    def set_fiyat(self,fiyat):
        self.__fiyat = fiyat
    def set_stok(self,stok):
        self.__stok = stok
    def set_son_kontrol_zamani(self,son_kontrol_zamani):
        self.__son_kontrol_zamani = son_kontrol_zamani
    def set_domain(self,domain):
        self.__domain = domain


        
