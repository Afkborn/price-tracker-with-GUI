SUPPORTEDWEBSITES = ["market.samm.com"]

from typing import SupportsRound
from Python.Model.Product import Product

from os import getcwd
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

class WebPrice:
    __chromeDriverPath = getcwd() +  fr"/Driver/chromedriver.exe"
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
        


    def getPriceFromProduct(self,product :Product) -> float:
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                self.getPage(product.get_link())
                urunFiyat = (self.browser.find_element_by_css_selector("span[class='product-price']").text).replace(".","").replace(",",".")
                return float(urunFiyat)
        else:
            return -1

    def getStockFromProduct(self,product:Product) -> bool:
        if product.get_domain() in SUPPORTEDWEBSITES:
            if product.get_domain() == SUPPORTEDWEBSITES[0]:
                self.getPage(product.get_link())
                try:
                    self.browser.find_element_by_css_selector("div[class='fl col-12 mb-50 stock-durum2']")
                    return False
                except:
                    return True
        else:
            return False
    

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