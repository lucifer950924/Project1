from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import time
from selenium.webdriver.support.ui import WebDriverWait as WDW
import yaml
import os
from datetime import datetime as dt
from utils.take_screenshot import take_screenshot
from behave import *




with open("App_data\\app_data.yml", "r") as f:
    data = yaml.safe_load(f)
    app_data = data['App_Data']
    curr_wd = os.getcwd()
    sc_dir = os.path.join(curr_wd,"Screenshots")
    os.makedirs(sc_dir,exist_ok=True)
        
    

@given('login to Youtube')
def browse_yt(context):
    curr_wd = os.getcwd()
    driver_dir = os.path.join(curr_wd,"Drivers\\msedgedriver.exe")
    service =Service(driver_dir)
    edgeoptions = Options()
    edgeoptions.add_argument("--start-maximized")
    edgeoptions.add_argument("--inprivate")
    context.driver = webdriver.Edge(options=edgeoptions,service=service)
    context.driver.get(app_data['URL'])
    # context.driver.maximize_window()

    
@then('Navigate to the Trending Video')
def navigate_YT(context):
    WDW(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Trending_ele']))).click()
    WDW(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Trending_ele'])))
    take_screenshot(context.driver)
    WDW(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Title_ele'])))
    take_screenshot(context.driver)
        
    element = context.driver.find_element(By.XPATH, app_data['Title_ele'])
    text = element.text
    WDW(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Title_ele']))).click()
    take_screenshot(context.driver)
    WDW(context.driver,app_data['timeout']).until(EC.text_to_be_present_in_element((By.XPATH,app_data['Video_title']), text))
    take_screenshot(context.driver)

@then('Logout')
def logout_from_yt(context):
    context.driver.quit()
