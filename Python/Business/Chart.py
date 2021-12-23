import matplotlib.pyplot as plt
from datetime import datetime

#Business
from Python.Business.DatabaseProduct import DatabaseProduct

#MODELS
from Python.Model.Product import Product


class Chart:

    #TODO  1 fiyat varsa görünüm düzelt.
    
    date = list()
    price = list()
    def __init__(self, product:Product, dateType = "epoch") -> None:

        self.product = product


        self.date.clear()
        self.price.clear()
        self.databaseProduct = DatabaseProduct()
        self.date_and_priceses_list = self.databaseProduct.get_price_and_date_from_priceses(product)


        son_eklenen_fiyat = 0
        for date_and_price in self.date_and_priceses_list:
            if son_eklenen_fiyat == date_and_price[1]:
                continue
            else:
                try:
                    test = int(date_and_price[1])
                    self.date.append(date_and_price[0])
                    self.price.append(date_and_price[1])
                    son_eklenen_fiyat = date_and_price[1]
                except:
                    pass

        self.dateType = dateType
        if self.dateType == "epoch":
            self.convertDate()

    def on_mouse_move(self,event):
        print('Event received:',event.x,event.y)

    def convertDate(self):

        for index, i in enumerate(self.date):
            self.date[index] =  datetime.fromtimestamp(i).strftime('%d.%m.%Y') #
    
    def create_plot(self):

        plt.plot(self.date, self.price, drawstyle='steps-pre', linewidth=2, color='#ffc6c7ff')
        plt.axis('tight')
        plt.title(f"{self.product.get_isim()}")

        plt.grid(axis='y', color='0.95')
        plt.connect('motion_notify_event',self.on_mouse_move)
        plt.fill_between(self.date, self.price, step="pre", alpha=0.8,color = "#ffc6c7ff")
        plt.xlabel("Tarih")
        plt.ylabel("Fiyat")
        plt.show()

    
    
