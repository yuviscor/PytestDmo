
from selenium import webdriver

from selenium import webdriver

from selenium.webdriver.support.ui import Select

import pytest

import time
from BaseLog import BaseLogClass
from DataClass import DcData

from HomeTest.HomeFuncs import that_contains_imp

import logging
@pytest.mark.usefixtures("test_setup")
@pytest.mark.usefixtures("GetData")
class Test_Of_Home(BaseLogClass):

    def test_firstPageCheck(self,GetData):

        lg=self.LOGGINGdemo()

        lg.setLevel(logging.DEBUG)

        obj = that_contains_imp(self.driver)

        c=obj.getName()

        lg.info("Sending the name"+GetData["name"])
     

        c.send_keys(GetData["name"])

        time.sleep(10)

        lg.info("Sending the email"+GetData["email"])

        obj.getEmail().send_keys(GetData["email"])

        obj.getPassw().send_keys("some text")

        obj.selectice().click()

        

        obj.selectcheck().click()

        obj.getSubmit().click()

        textp = obj.gettextplease().text

        

        sel = Select(self.driver.find_element_by_id(
            'exampleFormControlSelect1'))


        

        lg.info("Sending the gender"+GetData["gender"])

        c = sel.select_by_visible_text(GetData["gender"])

        time.sleep(10)
        assert textp == "Success!"

        self.driver.refresh()

@pytest.fixture(params=DcData.GetDataM())
def GetData(request):
    print(DcData.GetDataM())
    return request.param






    