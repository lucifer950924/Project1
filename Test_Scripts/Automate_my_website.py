
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
# from Generate_Report import generate_report

class OpenMyWebsite:
    def __init__(self,url="https://mhkplb0zog60wttz-89780912500.shopifypreview.com/"):
        self.url=url
        self.driver = webdriver.Chrome()
    def Open_the_Url(self):
        self.driver.get(self.url)
        self.ele = lambda x:"//*[contains(text(),'" + x + "')]"
        self.add_to_cart = self.ele("Add to cart") + "//parent::button"
        
        try:
            
            WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@alt='My Store']")))
            self.driver.maximize_window()
            time.sleep(2)
        except:
            print("Webpage is not loading properly")
        
        

    def buy_an_item(self,item):
        
        
        item_ele = lambda x:"//a[contains(@aria-labelledby,'CardLink-template') and contains(text(),'" + x + "')]"
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,item_ele(item)))).click()
        time.sleep(2)
        
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.add_to_cart))).click()
        time.sleep(3)
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.ele("View cart")))).click()
        time.sleep(2)
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,'//button[@id="checkout"]'))).click()
        time.sleep(1)
        WDW(self.driver,10).until(EC.presence_of_element_located((By.XPATH,self.ele("Return to home page")))).click()
        time.sleep(1)
    
    def search_for_an_item(self,item):
        self.search_icon = '(//*[@class="icon icon-search"])[3]'
        self.searchbox = '(//input[@type="search"])[2]'
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.search_icon))).click()
        time.sleep(1)
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.searchbox))).send_keys("Shirt")
        time.sleep(2)
        search_ele = lambda x: '//p[contains(text(),"' + x +'")]'
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,search_ele(item)))).click()
        WDW(self.driver,20).until(EC.presence_of_element_located((By.XPATH,self.add_to_cart)))
        time.sleep(1)




ins1 = OpenMyWebsite()
ins1.Open_the_Url()
ins1.buy_an_item("Guitar")
ins2 = OpenMyWebsite()
ins2.Open_the_Url()
ins2.buy_an_item("Shirt")
ins3 = OpenMyWebsite()
ins3.Open_the_Url()
ins3.search_for_an_item("Shirt")
