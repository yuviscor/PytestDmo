from selenium import webdriver

import pytest


from selenium.webdriver.common.by import By


class chkot:
    
    takeout = (By.LINK_TEXT, "iphone X")
    buttonchk = (By.CSS_SELECTOR, "a[class*='nav-link btn btn-primary']")
    gett = (By.LINK_TEXT, "iphone X")

    def __init__(self, driver):
        self.driver = driver 

    def takeProduct(self):
        

        return self.driver.find_elements(*chkot.takeout)

    def clickCheckOut(self):

        

        self.driver.find_element(*chkot.buttonchk).click()

    def getText(self):

        return self.driver.find_element(*chkot.gett).text

        


        

        

