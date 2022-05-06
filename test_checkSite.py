from selenium import webdriver

import pytest

from HomePage import PageH


# @pytest.fixture(scope="class")
# def test_setup(request):
#     dr = webdriver.Chrome(executable_path="C:\\chromedriver.exe")

#     dr.get("https://rahulshettyacademy.com/angularpractice/shop")

#     request.cls.driver = dr

#     yield

#     dr.close()


@pytest.mark.usefixtures("test_setup")

class Test_websitecheck:
    def test_sitecheck(self):
        

        

        h = PageH(self.driver)

        out=h.setThings()

        Text=self.driver.find_element_by_link_text("iphone X").text

        assert Text=="iphone X"

        bucket=out.takeProduct()

        for i in bucket:

            if(i.text=="iphone X"):
                i.find_element_by_xpath("//button[@class='btn btn-info']").click()
                break

        print("successfull")

        # self.driver.find_element_by_css_selector("a[class*='nav-link btn btn-primary']").click()
        
        out.clickCheckOut()
        # Text2=self.driver.find_element_by_link_text("iphone X").text

        Text2=out.getText()

        assert Text2=="iphone X"






