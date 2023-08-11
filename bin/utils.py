import pandas as pd
import openpyxl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.wait import WebDriverWait

class utilClass:
    def __init__(self, driver, serialNo, name, rating, website, phoneNo, address):
        self.driver = driver
        self.timeOut = 5
        self.serialNo = serialNo
        self.name = name
        self.rating = rating
        self.website = website
        self.phoneNo = phoneNo
        self.address = address

    def linkOrButtonClicker(self, locator, locatorValue):
        linkElement = self.elementFinder(locator, locatorValue)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(linkElement).perform()
            linkElement.click()
            return True
        except Exception as e:
            print (e)
        return False
        
    def fieldValueSetter(self, locator, locatorValue, fieldValue):
        fieldElement = self.elementFinder(locator, locatorValue)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(fieldElement).perform()
            fieldElement.clear()
            fieldElement.send_keys(fieldValue)
            return True
        except Exception as e:  
            print(e)
        return False
            
    def elementFinder(self, locator, locatorValue):
        try:
            element = self.driver.find_element(locator, locatorValue)
            return element
        except Exception as e:
            print(e)
        return False

    def dropDownSetter(self, locator, locatorValue, option):
        try:
            element_present = EC.presence_of_element_located((locator, locatorValue))
            WebDriverWait(self.driver, self.timeOut).until(element_present)       
            dropDown = Select(self.driver.find_element(locator, locatorValue))
            EC.presence_of_element_located((option))
            dropDown.select_by_visible_text(option) 
        except Exception as e:
            print (e)
    
    def textInfoGraber(self, div, locator, locatorValue, infoType):
        try:
            if infoType == 1:
                return div.find_element(locator, locatorValue).text
            elif infoType == 2:
                return div.find_element(locator, locatorValue).get_attribute('href')
        except Exception as e:
            print(e)
            return ""
    
    def fileWriter(self):
        writer = pd.ExcelWriter("./files/prospect_list.xlsx", engine='openpyxl')
        print(f"File Writing in progress .......................")
        df = pd.DataFrame({"Serial No"      : self.serialNo,
                            "Institue Name"  : self.name,
                            "Ratings"        : self.rating,
                            "Website"        : self.website,
                            "Phone No"       : self.phoneNo,
                            "Address"        : self.address},
            columns=['Serial No', 'Institue Name', 'Ratings', 'Website', 'Phone No', 'Address'])
        df.to_excel(writer, index=False)
        writer.close()
        print(f"File Writing is Complete :) !! .................")