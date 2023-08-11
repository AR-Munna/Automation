from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from utils import utilClass

class mainClass:
    def __init__(self):  
        self.timeOut = 10
        self.serialNo = []
        self.name = []
        self.rating = []
        self.website = []
        self.phoneNo = []
        self.address = []
        self.textTypeInfo = 1
        self.hrefTypeInfo = 2
        try:
            service = Service(executable_path="./resource/chromedriver.exe")
            options = webdriver.ChromeOptions()
            options.add_experimental_option("detach", True)
            self.driver = webdriver.Chrome(service=service, options=options)
            self.utilClassObj = utilClass(self.driver, self.serialNo, self.name, self.rating, self.website, self.phoneNo, self.address)

        except Exception as e:
            print("Sorry! Driver can not be loaded")
            print(e)
         
    def driverFunction(self):
        self.driver.get("https://trustanalytica.com/us/art-studios")
        self.driver.implicitly_wait(self.timeOut) 
       
        self.utilClassObj.dropDownSetter(By.ID, "filterState", "Alabama")       
        self.utilClassObj.dropDownSetter(By.ID, "filterCity", "Birmingham") 
        self.utilClassObj.linkOrButtonClicker(By.CLASS_NAME, "search-top-page-filters")
       
        divArray = []
        divArray = self.driver.find_elements(By.CLASS_NAME, "sr-item")
        for div in divArray:
            self.serialNo.append(self.utilClassObj.textInfoGraber(div, By.CLASS_NAME, "sr-counter-label", self.textTypeInfo))
            self.name.append(self.utilClassObj.textInfoGraber(div, By.XPATH, ".//*[@class='sr-item-details-info']/span/h3", self.textTypeInfo))
            self.rating.append(self.utilClassObj.textInfoGraber(div, By.XPATH, ".//*[@class='sr-item-details-info-rating']/span", self.textTypeInfo))
            self.website.append(self.utilClassObj.textInfoGraber(div, By.XPATH, ".//.//.//*[@class='sr-ci-text']/a", self.hrefTypeInfo))
            self.phoneNo.append(self.utilClassObj.textInfoGraber(div, By.XPATH, ".//.//.//*[@class='sr-ci-text']/strong", self.textTypeInfo))
            self.address.append(self.utilClassObj.textInfoGraber(div, By.XPATH, ".//.//.//*[@class='sr-ci-text']/span", self.textTypeInfo))
        
        self.utilClassObj.fileWriter()
        # self.driver.quit()

if __name__ == "__main__":
    obj = mainClass()
    obj.driverFunction()
      