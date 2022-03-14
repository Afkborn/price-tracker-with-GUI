
#Model
import logging
from Python.Model.Product import Product







#Business
from Python.Business.DatabaseProduct import DatabaseProduct
import json
from datetime import datetime


SUPPORTED_EXPORT_FORMATS= ["JSON"]



def get_gecmis_fiyatlar(product:Product):
    """get date and price of the product"""
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
    logging.info(f"Return old price list. Product ID and name : {product.get_id()} {product.get_isim()}")
    return returnList

def export_product_to_json(product:Product,location:str):
    """export products to json file\n product is the product object, location is the path of the file"""
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
        "birim":product.get_birim(),
        "gecmis_fiyatlar":gecmis_fiyatlar
    }
    jsonObject = json.dumps(product_json)

    with open(location, "w",encoding="utf-8") as outfile:
        outfile.write(jsonObject)
        logging.info(f"{location} is exported. Product ID and name : {product.get_id()} {product.get_isim()}")
        return location


def export_all_products_to_json(location:str):
    """export all products to json file\nlocation is the path of the file""" 
    databaseProduct = DatabaseProduct()
    all_products = databaseProduct.loadDB()

    jsonObjectList = []
    for product in all_products:
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
        "birim":product.get_birim(),
        "gecmis_fiyatlar":gecmis_fiyatlar
        }
        jsonObjectList.append(product_json)

    jsonObject = json.dumps(jsonObjectList)
    with open(location, "w",encoding="utf-8") as outfile:
        outfile.write(jsonObject)
        logging.info("All products are exported")
        return location
