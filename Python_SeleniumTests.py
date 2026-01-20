from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.edge.service import Service as Eservice
from selenium.webdriver.chrome.service import Service as CService
from selenium.webdriver.firefox.service import Service as FService
from selenium.webdriver import EdgeOptions,ChromeOptions,EdgeService,ChromeService,FirefoxOptions,FirefoxService,Edge,Chrome,Firefox
from selenium.webdriver.support.ui import WebDriverWait
import csv,os,time,pathlib,tracemalloc,asyncio
from selenium.webdriver.support.select import Select

class PythonTestSelenium:
    def __init__(self):
        tracemalloc.start()
        self.currDir = os.getcwd()
        self.runTimeDataPath = os.path.join(os.getcwd(),"Data","RunTimeData.csv")
        self.sc_dir = os.path.join(self.currDir,'Screenshots',f'{int(time.time())}')
        os.makedirs(self.sc_dir,exist_ok=True)
        with open(self.runTimeDataPath,"r",encoding='utf-8') as file:
            lines = csv.reader(file)
            lines = dict(lines)
        self.timeout = int(lines['Timeout'])
        self.fileUploadPath = lines['FileUpload']
        self.multipleUploadFilePath = '\n'.join(lines['MultipleUploadFiles'].split('|'))
        if lines['Browser'] == 'Edge':
            self.driverPath = os.path.join(self.currDir,'Drivers','msedgedriver.exe')
            self.service = Eservice(self.driverPath)
            self.driver = webdriver.Edge(service = self.service)
        elif lines['Browser'] == 'Firefox':
            self.driverPath = os.path.join(self.currDir,'Drivers','geckodriver.exe')
            self.service = FService(self.driverPath)
            self.driver = webdriver.Firefox(service = self.service)
        elif lines['Browser'] == 'Chrome':
            self.driverPath = os.path.join(self.currDir,'Drivers','chromedriver.exe')
            self.service = CService(self.driverPath)
            self.driver = webdriver.Chrome(service=self.service)

    def launchAnURL(self,URL: str):

        self.driver.get(URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)
        
    def getScreenshotName(self):
        return os.path.join(self.sc_dir,f'{int(time.time())}.png')
        

    async def actOnPage(self):
        WebDriverWait(self.driver,self.timeout).until(EC.presence_of_element_located((By.ID,'singleFileInput')))
        actions = ActionChains(self.driver)
        
        upload = self.driver.find_element(By.ID,'singleFileInput')
        actions.scroll_to_element(upload)
        if pathlib.Path(self.fileUploadPath):
            upload.send_keys(self.fileUploadPath)

        sel = Select(self.driver.find_element(By.ID,"colors"))
        actions.scroll_to_element(self.driver.find_element(By.ID,"colors"))
        sel.select_by_visible_text('Yellow')
        multipleUpload = self.driver.find_element(By.ID,'multipleFilesInput')
        actions.scroll_to_element(multipleUpload)
        multipleUpload.send_keys(self.multipleUploadFilePath)
        hoverButton = self.driver.find_element(By.CLASS_NAME,'dropbtn')
        hoverMenu = self.driver.find_element(By.XPATH,'//a[text()="Mobiles"]')
        actions.scroll_to_element(hoverButton)
        actions.move_to_element(hoverButton).perform()
        self.driver.save_screenshot(self.getScreenshotName())
        parent_handle = self.driver.window_handles[0]
        self.driver.find_element(By.XPATH,"//*[text()='New Tab']").click()
        [self.driver.switch_to.window(handle) for handle in self.driver.window_handles if handle not in parent_handle ]
        assert self.driver.title == 'www.pavantestingtools.com'


        


        



async def main():
    x = PythonTestSelenium()
    x.launchAnURL('https://testautomationpractice.blogspot.com/')
    await x.actOnPage()

asyncio.run(main())


