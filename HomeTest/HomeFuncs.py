from tkinter.tix import Select
from selenium import webdriver

import pytest

import time 

from selenium.webdriver.common.by import By


class that_contains_imp:


    nameis = (By.NAME,"name")

    emailis = (By.NAME,"email")

    passwordis = (By.ID,"exampleInputPassword1")

    checkbox=(By.XPATH, "//input[@id='exampleCheck1']")

    radiocheck = (By.XPATH, "//input[@id='inlineRadio1']")

    submitt = (By.CSS_SELECTOR, "input[class*='btn btn-success']")

    textSuccess = (By.XPATH ,
                   "//div[@class='alert alert-success alert-dismissible']/strong")

    # selectMorF = (
    #     By.ID, "driver.find_element_by_id('exampleFormControlSelect1')")
    
    def __init__(self,driver):

        self.driver = driver
        

    def getName(self):

        return self.driver.find_element(*that_contains_imp.nameis)

    def getEmail(self):

        return self.driver.find_element(*that_contains_imp.emailis)

    def getPassw(self):

        return self.driver.find_element(*that_contains_imp.passwordis)

    def selectice(self):

        return self.driver.find_element(*that_contains_imp.checkbox)

    def selectcheck(self):

        return self.driver.find_element(*that_contains_imp.radiocheck)

    def getSubmit(self):

        return self.driver.find_element(*that_contains_imp.submitt)

    def gettextplease(self):

        return self.driver.find_element(*that_contains_imp.textSuccess)

    
















