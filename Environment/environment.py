from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
import os

class Environment:
    def __init__(self):
        driver_location = os.path.join(os.getcwd(),'driver','msedgedriver.exe')
        service = Service(driver_location)
        options = Options()
        options.add_argument('--start-maximized')
        self.driver = webdriver.Edge(options=options, service=service)

    def get_driver(self):
        return self.driver