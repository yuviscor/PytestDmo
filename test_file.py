from selenium import webdriver

import pytest



@pytest.fixture()

def setup():


    drive = webdriver.Chrome("C:\\chromedriver.exe")

    drive.get("https://rahulshettyacademy.com/angularpractice/")
    return drive
    


@pytest.mark.usefixtures("setup")

def test_first(setup):
    drive = setup
    assert drive.title == "ProtoCommerce"
