from selenium import webdriver

import pytest

from HomePage import PageH
print("inside")

def pytest_addoption(parser):
    parser.addoption(

        "--browser_name", action="store"
    )


@pytest.fixture(scope="class")
def test_setup(request):

    browser_name = request.config.getoption("browser_name")

    if(browser_name=="chrome"):
        dr = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        dr.get("https://rahulshettyacademy.com/angularpractice/")
        
        

    else:

        print("do nothing")
        

    

    request.cls.driver = dr

    yield 

    dr.close()
