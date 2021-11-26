

#SUPPORTED WEBSITE
import Python.Business.SupportedWebsites as SW


SUPPORTEDWEBSITES =  SW.getSupportedWebsites()

from time import sleep

from Python.Model.Product import Product

from os import getcwd
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class WebPrice:
    __chromeDriverPath = getcwd() +  fr"/Driver/chromedriver.exe"
    # TODO CHECK EXISTS CHROME DRIVER
    def __init__(self, profileName="profile1",headless = False):

        self.options = ChromeOptions()
        self.__profileName = profileName
        self.__profileLoc = getcwd() + fr"/Profile/{self.__profileName}"
        self.options.add_argument(f"user-data-dir={self.__profileLoc}")
        self.options.add_argument("--lang=tr")
        self.options.add_argument("--log-level=3")
        self.options.headless = headless

        self.__startBrowser()

    def close(self):
        self.browser.close()
        
    def str_price_to_float(self,price : str) -> float:
        """string fiyatını float'a çevirme"""
        price = price.replace(".","")
        price = price.replace(",",".")
        price = price.replace("TL","")
        return price

    def getPriceFromProduct(self,product :Product) -> float:
        if product.get_domain() in SUPPORTEDWEBSITES:

            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                self.getPage(product.get_link())
                urunFiyat = (self.browser.find_element_by_css_selector("span[class='product-price']").text)
                return self.str_price_to_float(urunFiyat)
            elif product.get_domain() == SUPPORTEDWEBSITES[1]:
                #AMAZON
                try:
                    self.getPage(product.get_link())
                    urunFiyat = (self.browser.find_element_by_css_selector("span[class='a-price a-text-price a-size-medium']").text)
                    return self.str_price_to_float(urunFiyat)
                except:
                    return 0.0
            elif product.get_domain() == SUPPORTEDWEBSITES[2]:
                #TRENDYOL
                self.getPage(product.get_link())
                urunDiv = self.browser.find_element_by_css_selector("div[class='product-detail-container']")
                urunFiyatDsc = urunDiv.find_element_by_css_selector("span[class='prc-dsc']").text
                urunFiyatSlg = urunDiv.find_element_by_css_selector("span[class='prc-slg']").text
                if urunFiyatDsc == "":
                    return self.str_price_to_float(urunFiyatSlg)
                else:
                    return self.str_price_to_float(urunFiyatDsc)
            elif product.get_domain() == SUPPORTEDWEBSITES[3]:
                #HEPSİBURADA
                self.getPage(product.get_link())

                try:
                    urunSpan = self.browser.find_element_by_css_selector("span[id='offering-price']").get_attribute('content')
                    return float(urunSpan)
                except Exception as e :
                    print(f"Error {e}")
                    return 0.0
        else:
            return -1

    def getStockFromProduct(self,product:Product) -> bool:
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                self.getPage(product.get_link())
                try:
                    self.browser.find_element_by_css_selector("div[class='fl col-12 mb-50 stock-durum2']")
                    return False
                except:
                    return True
            elif product.get_domain() == SUPPORTEDWEBSITES[1]:
                #AMAZON
                self.getPage(product.get_link())
                try:
                    self.browser.find_element_by_css_selector("span[class='a-color-price a-text-bold']")
                    return False
                except:
                    return True
            elif product.get_domain() == SUPPORTEDWEBSITES[2]:
                #TRENDYOL
                self.getPage(product.get_link())
                try:
                    self.browser.find_element_by_css_selector("button[class='add-to-basket sold-out']")
                    return True
                except:
                    return False
            elif product.get_domain() == SUPPORTEDWEBSITES[3]:
                #HEPSİBURADA
                self.getPage(product.get_link())
                try:
                    self.browser.find_element_by_css_selector("button[id='addToCart']")
                    return True
                except:
                    return False
        else:
            return False

    def getProductName(self,product:Product) -> str:
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                self.getPage(product.get_link())    
                return (self.browser.find_element_by_css_selector("h1[id='productName']").text).strip()
            elif product.get_domain() == SUPPORTEDWEBSITES[1]:
                #AMAZON
                self.getPage(product.get_link())
                return (self.browser.find_element_by_css_selector("span[id='productTitle']").text).strip()
            elif product.get_domain() == SUPPORTEDWEBSITES[2]:
                #TRENDYOL
                self.getPage(product.get_link())
                return self.browser.title.strip()
            elif product.get_domain() == SUPPORTEDWEBSITES[3]:
                #HEPSİBURADA
                self.getPage(product.get_link())
                return (self.browser.find_element_by_css_selector("h1[id='product-name']").text).strip()


    def add_product_to_basket(self,product:Product):
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                self.getPage(product.get_link())
                button = self.browser.find_element_by_css_selector("a[id='addCartBtn']")
                button.click()
                # yarım saniye kadar bekle
                sleep(0.3)
                # basketSuccess var mı kontrol et varsa true dön
                try:
                    self.browser.find_element_by_css_selector("span[class='basketSuccess']")
                    return True
                except:
                    return False

    def get_basket(self,product:Product):
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                self.getPage("https://market.samm.com/sepet") #TODO OTOMATİKLEŞTİR

    def try_coupon(self,product:Product,coupon:str):
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                #SAMM MARKET
                indirim_kupon_side = self.browser.find_element_by_css_selector("input[id='indirimkuponu']")
                indirim_kupon_side.send_keys(coupon)
                indirim_uygula_button = self.browser.find_element_by_css_selector("a[id='indirim']")
                indirim_uygula_button.click()
                #row oh
                sleep(0.5)
                try:
                    self.browser.find_element_by_css_selector("div[class='row oh']")
                    self.browser.find_element_by_css_selector("div[class='pClose close']").click()
                    return False
                except:
                    return True

    def __startBrowser(self):
        self.browser = Chrome(executable_path=self.__chromeDriverPath,options=self.options)
        self.browser.set_window_position(0,0)
        #WEB 1008X635 PX
        self.browser.set_window_size(1024,768)

    def getPage(self,URL : str):
        if self.browser.current_url == URL:
            pass
        else:
            self.browser.get(URL)

    
    def __clickXY(self,x,y):
        """tarayıcıda istenilen yere tıklamak için kullanılıyor"""
        action = ActionChains(self.browser)
        action.move_by_offset(x,y)
        action.click()
        action.perform()
        action.reset_actions()

    def __getSS(self,name):
        """test amaçlı ekran görüntüsü almak için"""
        self.browser.save_screenshot(f"{name}.png")