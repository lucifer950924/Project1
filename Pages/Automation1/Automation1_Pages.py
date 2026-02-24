
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
import os, time, logging , pathlib , csv
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementClickInterceptedException
from Environment.environment import Environment
from Utils.csvReader import CSVReader

class Automation1Pages:
    
    def __init__(self):
       
        self.driver = Environment().get_driver()
        datafile = CSVReader('Automation1')
        self.data = datafile.read_csv()
        self.timeout = self.data['timeout']

    def HitURL(self):
        self.driver.get(self.data['URL'])
        self.driver.implicitly_wait(self.data['timeout'])

    def fill_text_in_fields_by_id(self,id,value):
        try:
            locator = self.driver.find_element(By.ID,id)
            locator.clear()
            locator.send_keys(value)
        except NoSuchElementException:
            print(f'Element with id {id} not found')
        except StaleElementReferenceException:
            print(f'Element with id {id} is not stable')
        except TimeoutException:
            print(f'Timeout while trying to find element with id {id}')
        except ElementClickInterceptedException:
            print(f'Element with id {id} is not clickable')
        
    def fill_text_by_id_with_Wait(self,id,value):
        try:
            locator = self.driver.find_element(By.ID,id)
            self.wait = WebDriverWait(self.driver,
                                      self.timeout,
                                      poll_frequency=self.data['polling_time'],
                                      ignored_exceptions=[NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementClickInterceptedException])
            self.wait.until(EC.presence_of_element_located((By.ID,id)))
            locator.clear()
            locator.send_keys(value)
        except NoSuchElementException:
            print(f'Element with id {id} not found')
        except StaleElementReferenceException:
            print(f'Element with id {id} is not stable')
        except TimeoutException:
            print(f'Timeout while trying to find element with id {id}')
        except ElementClickInterceptedException:
            print(f'Element with id {id} is not clickable')

    def fill_text_by_text(self,text,value):
        locator = lambda x : self.driver.find_element(By.XPATH,f'//*[text()="{x}"]//following::textarea')
        try:
            locator(text).clear()
            locator(text).send_keys(value)
        except NoSuchElementException:
            print(f'Element with text {text} not found')
        except StaleElementReferenceException:
            print(f'Element with text {text} is not stable')
        except TimeoutException:
            print(f'Timeout while trying to find element with text {text}') 
         

    def select_option_by_value(self,label,value):
        try:
            locator = lambda x : self.driver.find_element(By.XPATH,f'//label[text()="{x}"]//following::select')
            loc = Select(locator(label))
            loc.select_by_value(value)
        except NoSuchElementException:
            print(f'Element with label {label} not found')
        except StaleElementReferenceException:
            print(f'Element with label {label} is not stable')  
        except TimeoutException:
            print(f'Timeout while trying to find element with label {label}')
        
    def upload_file_byinput(self,filepath):
        try:
            locator = self.driver.find_element(By.XPATH,'//input[@type="file"]')
            actions = ActionChains(self.driver)
            actions.move_to_element(locator).perform()
            time.sleep(0.5)
            locator.send_keys(filepath)
        except FileNotFoundError:
            print(f'File at path {filepath} not found')
        except NoSuchElementException:
            print(f'File input element not found')

    def hover_element(self,text):
        try:
            loc = lambda x: self.driver.find_element(By.XPATH,f'//*[text()="{x}"]')
            locator = loc(text)
            actions = ActionChains(self.driver)
            actions.move_to_element(locator).perform()
        except NoSuchElementException:
            print(f'Element with text {text} not found')
        except StaleElementReferenceException:
            print(f'Element with text {text} is not stable')
        except TimeoutException:
            print(f'Timeout while trying to find element with text {text}') 
        
    def drag_element(self,sorce_text,target_text):
        try:
            loc = lambda x: self.driver.find_element(By.XPATH,f'//*[text()="{x}"]')
            source_locator = loc(sorce_text)
            target_locator = loc(target_text)
            actions = ActionChains(self.driver)
            actions.drag_and_drop(source_locator,target_locator).perform()
        except NoSuchElementException:
            print(f'Element with text {sorce_text} or {target_text} not found')
        except StaleElementReferenceException:
            print(f'Element with text {sorce_text} or {target_text} is not stable')
        except TimeoutException:
            print(f'Timeout while trying to find element with text {sorce_text} or {target_text}')
    def quit_browser(self):
        self.driver.quit()