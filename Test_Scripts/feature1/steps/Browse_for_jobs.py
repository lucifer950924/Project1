from behave import *
from selenium.webdriver.support.ui import Select,WebDriverWait
from selenium import webdriver
import yaml
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from utils.Encrypt_Decrypt import Encrypt_Decrypt
from utils.take_screenshot import take_screenshot
import pandas as pd
import os

with open("App_data\\app_data.yml","r") as f:
    data_load = yaml.safe_load(f)
    app_data = data_load['App_Data']



@given('login to page')
def login_to_page(context):
    context.driver = webdriver.Edge()
    context.driver.get(app_data['Naukri_URL'])
    context.driver.maximize_window()
    WebDriverWait(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Naukri_Login_ele']))).click()
    time.sleep(2)
    context.driver.find_element(By.XPATH,app_data['Email_input_field']).send_keys(app_data['Username'])
    take_screenshot(context.driver)
    password = Encrypt_Decrypt.decrypt_pass(username=app_data['Username'])
    context.driver.find_element(By.XPATH, app_data['password_input_field']).send_keys(password)
    take_screenshot(context.driver)
    context.driver.find_element(By.XPATH,app_data['submit_btn']).click()
    take_screenshot(context.driver)
    WebDriverWait(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Login_Title'])))
    take_screenshot(context.driver)


@then('Search for something')
def search_for_something(context,something=app_data['Job_search_term']):
    take_screenshot(context.driver)
    WebDriverWait(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Job_Search']))).click()
    WebDriverWait(context.driver,app_data['timeout']).until(EC.presence_of_element_located((By.XPATH,app_data['Search_field']))).send_keys(something)
    take_screenshot(context.driver)
    context.driver.find_element(By.XPATH,app_data['Search_button']).click()
    take_screenshot(context.driver)

@then('Search is complete export data')
def search_is_complete(context):
    take_screenshot(context.driver)
    WebDriverWait(context.driver,app_data['timeout']).until(EC.presence_of_all_elements_located((By.XPATH,app_data['company_name_elements'])))
    take_screenshot(context.driver)
    list_of_comp = context.driver.find_elements(By.XPATH,app_data['company_name_elements'])
    Comp_list = [element.text for element in list_of_comp]
    list_of_ratings = context.driver.find_elements(By.XPATH,app_data['rating_element'])
    Rating_list = [element.text for element in list_of_ratings]
    list_of_job_titles = context.driver.find_elements(By.XPATH,app_data['Job_title'])
    Job_Title_list = [element.text for element in list_of_job_titles]
    data_dict = {'Company_Name': Comp_list[:5],'Job_title' : Job_Title_list[:5],'Rating':Rating_list[:5]}
    curr_wd = os.getcwd()
    export_dir=os.path.join(curr_wd,"Exports")
    os.makedirs(export_dir,exist_ok=True)
    context.filepath = os.path.join(export_dir,"Job_Export.xlsx")
    pd.DataFrame(data_dict).to_excel(context.filepath)

@then('logout')
def logout(context):
    os.path.exists(context.filepath)
    print("Job Search Successful")
    context.driver.quit()






