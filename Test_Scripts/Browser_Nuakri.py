from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
import yaml
import os
from datetime import datetime as dt
from Encrypt_Decrypt import Encrypt_Decrypt



class Browser_Nuakri:
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

    def browse_Naukri(self):
        self.driver.get(self.app_data['Naukri_URL'])
        self.driver.maximize_window()
        self.take_screenshot()
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Naukri_Login_ele']))).click()
        time.sleep(2)
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Email_input_field'])))
        self.take_screenshot()
        password = Encrypt_Decrypt.decrypt_pass(username=self.app_data['Username'])
        self.driver.find_element(By.XPATH, self.app_data['Email_input_field']).send_keys(self.app_data['Username'])
        self.driver.find_element(By.XPATH, self.app_data['password_input_field']).send_keys(password)
        self.take_screenshot()
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['submit_btn']))).click()
        WDW(self.driver,self.app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,self.app_data['Login_Title'])))
        self.take_screenshot()

ins1 = Browser_Nuakri()
ins1.browse_Naukri()

