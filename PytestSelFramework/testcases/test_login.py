import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pageObjects.LoginPage import LoginPage
from utilites.readProperities import ReadConfig
from utilites.customlogger import LogGen


class Test_01_login:
    baseUrl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

    #@pytest.mark.sanity
    def test_homepageTitle(self, setup):

        self.logger.info("********************************** Testing homepage title ***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepageTitle.png")
            self.driver.close()
            assert False
        self.logger.info("********************************** Test case1 close ***********************************")

    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********************************** Testing test_login Page ***********************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.driver.maximize_window()
        act_title = self.driver.title
        self.logger.info(act_title)
        self.lp = LoginPage(self.driver)
        self.lp.setUsername(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickOnLogin()
        assert "Dashboard / nopCommerce administration" in self.driver.page_source
        if "Dashboard / nopCommerce administration" in self.driver.page_source:
            assert True
            #self.driver.close()
        else:
            self.logger.info("********************************** Else condition fail and saving screenshot of the failure ***********************************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
        self.logger.info("********************************** Test case2 close ***********************************")


    def test_check(self, setup):
        self.logger.info("********************************** Test check ***********************************")
        print("test check function call")
        self.logger.info("********************************** Test case3 close ***********************************")
        pass
