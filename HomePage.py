import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By

from CheckOut import chkot
class PageH:

    shop = (By.CSS_SELECTOR,"a[href*='shop']")
    def __init__(self,driver):

        self.driver = driver

    def setThings(self):

        self.driver.find_element(*PageH.shop).click()

        

        out = chkot(self.driver)

        return out 
        