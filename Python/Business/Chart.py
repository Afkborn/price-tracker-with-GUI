import matplotlib.pyplot as plt
from datetime import datetime

#logging
import logging

plt.rcParams['toolbar'] = 'None'
plt.rcParams['axes.xmargin'] = 0

#Business
from Python.Business.DatabaseProduct import DatabaseProduct
import Python.Business.Exception as Exc

#MODELS
from Python.Model.Product import Product


import mplcursors


class Chart:

    #TODO  1 fiyat varsa görünüm düzelt.

    date = list()
    price = list()
    
    def __init__(self, product:Product, dateType = "epoch") -> None:

        self.product = product
        self.para_birimi = self.product.get_birim()
        
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
                    if test == -1 or test == 0:
                        continue
                    else:
                        self.date.append(date_and_price[0])
                        self.price.append(date_and_price[1])
                        son_eklenen_fiyat = date_and_price[1]
                except:
                    pass

        self.dateType = dateType
        if self.dateType == "epoch":
            self.convertDate()
        self.clearSameDate()



    def convertDate(self):

        for index, i in enumerate(self.date):
            self.date[index] =  datetime.fromtimestamp(i).strftime('%d.%m.%Y') 
    
    def clearSameDate(self):
        son_eklenen_tarih = ""
        for index, i in enumerate(self.date,start=-1):
            if son_eklenen_tarih == i:
                del self.date[index]
                del self.price[index]

            son_eklenen_tarih = i

    
    def create_plot(self):
        # print(self.date)
        # print(self.price)
        if len(self.price) == 0 or len(self.price) == 1:
            raise Exc.MissingData

        

        # def on_mouse_move(event):
        #     if not event.inaxes:
        #         return
        #     # print('Event received:',event.x,event.y)
        #     # print("Event xdata:",event.xdata)

        #     my_xdata = int(event.xdata)
        #     myPrice = self.price[my_xdata+1]
        #     myDate = self.date[my_xdata+1]
            
        #     print(f"{myDate} : {myPrice}")

        def show_annotation(sel):
            xi = sel.target[0]
            vertical_line = plt.axvline(xi, color='red', ls=':', lw=1)
            sel.extras.append(vertical_line)
            annotation_str = f'Tarih: {self.date[int(xi)+1]}\nFiyat: {self.price[int(xi)+1]} {self.para_birimi}'
            sel.annotation.set_text(annotation_str)


        plt.figure(figsize=(9,5))

        # plt.axvline(x = 7, color = 'b') # draw line

        
        # plt.connect('motion_notify_event',on_mouse_move) #mouse move eventi atadım

        lines = plt.plot(self.date, self.price, drawstyle='steps-pre', linewidth=10, color='#ffc6c7ff') #steps-pre
        cursor = mplcursors.cursor(lines,hover=True) #Persistent  Transient
        cursor.connect('add', show_annotation)

        plt.axis('tight')
        plt.xticks(color='w')
        plt.title(f"{self.product.get_isim()}")
        plt.get_current_fig_manager().set_window_title(f"{self.product.get_isim()}")
        plt.grid(axis='y', color='0.95')
        
        plt.fill_between(self.date, self.price, step="pre", alpha=0.8,color = "#ffc6c7ff")
        plt.xlabel("Tarih")
        plt.ylabel("Fiyat")
        plt.show()
        return True

    
    
