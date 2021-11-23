import matplotlib.pyplot as plt
from datetime import datetime

#Business
from Python.Business.DatabaseProduct import DatabaseProduct

#MODELS
from Python.Model.Product import Product


class Chart:
    date = list()
    price = list()
    def __init__(self, product:Product, dateType = "epoch") -> None:
        self.product = product
        self.date.clear()
        self.price.clear()
        self.databaseProduct = DatabaseProduct()
        self.date_and_priceses_list = self.databaseProduct.get_price_and_date_from_priceses(product)

        #[(1637335334.2175646, 0), (1637335593.4976118, 0), (1637335599.9137168, 0), (1637336532.1519344, 0), (1637336673.8786097, 0), (1637337324.1453562, 0), (1637338057.8657577, 0), (1637340169.720858, 0)]
        for date_and_price in self.date_and_priceses_list:
            self.date.append(date_and_price[0])
            self.price.append(date_and_price[1])
        
        self.dateType = dateType
        if self.dateType == "epoch":
            self.convertDate()



    def convertDate(self):
        for index, i in enumerate(self.date):
            self.date[index] =  datetime.fromtimestamp(i).strftime('%H:%M:%S')
    
    def create_plot(self):
        plt.plot(self.date, self.price)
        plt.show()

    
    
