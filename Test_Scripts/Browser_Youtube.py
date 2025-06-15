from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
import yaml
import os
from datetime import datetime as dt

# from runner import take_screenshot


class Browser_Youtube:
    def __init__(self):
        
        with open("App_data\\app_data.yml", "r") as f:
            self.data = yaml.safe_load(f)
            self.app_data = self.data['App_Data']
        self.curr_wd = os.getcwd()
        self.sc_dir = os.path.join(self.curr_wd,"Screenshots")
        os.makedirs(self.sc_dir,exist_ok=True)
        
        self.driver = webdriver.Edge()

    def take_screenshot(self):
        now = dt.now().strftime("%Y%m%d%H%M%S")
        sc_filepath = os.path.join(self.sc_dir,f"SC_{now}.png")
        self.driver.save_screenshot(sc_filepath)

    def browse_yt(self):
        self.driver.get(self.app_data['URL'])
        self.driver.maximize_window()

        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Trending_ele']))).click()
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Trending_ele'])))
        self.take_screenshot()
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Title_ele'])))
        self.take_screenshot()
        
        element = self.driver.find_element(By.XPATH, self.app_data['Title_ele'])
        text = element.text
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Title_ele']))).click()
        self.take_screenshot()
        WDW(self.driver,self.app_data['timeout']).until(EC.text_to_be_present_in_element((By.XPATH,self.app_data['Video_title']), text))
        self.take_screenshot()
ins1 = Browser_Youtube()
ins1.browse_yt()