import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

from selenium.webdriver.support.expected_conditions import element_to_be_clickable

from pageObjects.LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from testcases import test_login

class Test_01_Header:
    baseUrl = ReadConfig.getApplicationUrl()
    logger = LogGen.loggen()
    image_xpath = "//img[@class='brand-image-xl logo-xl']"
    toggle_icon_xpath = ""
    Account_name_xpath = ""
    link_logout_LinkText = "Logout"
    setting_icon_xpath = ""
    setting_submit_xpath = ""

    @pytest.mark.regression
    def test_logo(self, setup):
        self.logger.info("********************************** Test logo ***********************************")
        self.obj_login = test_login.Test_01_login()
        self.obj_login.test_login(setup)
        self.logger.info("********************************** Tsdfsdfsdf ***********************************")
        self.driver = setup
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.image_xpath)))
        self.driver.save_screenshot(".//Screenshots//" + "test_homepageTitle.png")
        self.logger.info(element)
        self.driver.close()
        self.logger.info("********************************** Test case 4 close ***********************************")


    def test_check2(self, setup):
        self.logger.info("********************************** Test check2 ***********************************")
        pass
