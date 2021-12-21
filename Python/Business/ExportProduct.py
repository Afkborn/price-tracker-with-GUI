from Python.Model.Product import Product
from datetime import datetime
import json


#Business
from Python.Business.DatabaseProduct import DatabaseProduct


SUPPORTED_EXPORT_FORMATS= ["JSON"]


    # id:int=None, # id
    # isim:str=None, #ürün ismi
    # link:str=None, # ürün linki
    # check_time_sec:int=None, #kontrol zamanı (saniye)
    # fiyat_takip:bool=None, #fiyat takip
    # stok_takip:bool=None, #stok takip
    # fiyat:float=None,  #ürün fiyatı
    # stok:bool=None, #stok durumu
    # son_kontrol_zamani:float=None, #son kontrol zamanı
    # domain:str=None, #domain



def get_gecmis_fiyatlar(product:Product):
    date = []
    price=[]
    databaseProduct = DatabaseProduct()
    date_and_priceses_list = databaseProduct.get_price_and_date_from_priceses(product)
    son_eklenen_fiyat = 0
    for date_and_price in date_and_priceses_list:
        if son_eklenen_fiyat == date_and_price[1]:
            continue
        else:
            date.append(date_and_price[0])
            price.append(date_and_price[1])
            son_eklenen_fiyat = date_and_price[1]
    for index, i in enumerate(date):
        date[index] =  datetime.fromtimestamp(i).strftime('%Y-%m-%d %H:%M:%S')
    
    returnList = []
    for i in range(len(date)):
        returnList.append({"date":date[i],"price":price[i]})
    return returnList

def export_product_to_json(product:Product,location:str):
    son_kontrol_zamani = datetime.utcfromtimestamp(product.get_son_kontrol_zamani()).strftime('%Y-%m-%d %H:%M:%S')

    gecmis_fiyatlar = get_gecmis_fiyatlar(product)

    product_json = {
        "id":product.get_id(),
        "isim":product.get_isim(),
        "link":product.get_link(),
        "check_time_sec":product.get_check_time_sec(),
        "fiyat_takip":product.get_fiyat_takip(),
        "stok_takip":product.get_stok_takip(),
        "fiyat":product.get_fiyat(),
        "stok":product.get_stok(),
        "son_kontrol_zamani":son_kontrol_zamani,
        "domain":product.get_domain(),
        "gecmis_fiyatlar":gecmis_fiyatlar
    }
    jsonObject = json.dumps(product_json)
    with open(location, "w") as outfile:
        outfile.write(jsonObject)
        return location


