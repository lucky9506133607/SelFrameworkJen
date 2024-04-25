from selenium.webdriver.common.by import By

class Header:
    image_id = ""
    toggle_icon_xpath = ""
    Account_name_xpath = ""
    link_logout_LinkText = "Logout"
    setting_icon_xpath = ""
    setting_submit_xpath = ""


    # lets create a constructor to initiate our driver, and for that we will create our constructor which will invoke at the time of object creation.
    # what this constructor is doing is capturing the driver from the test case
    def __init__(self, driver):
        self.driver = driver

    def setImage(self, driver):
        pass