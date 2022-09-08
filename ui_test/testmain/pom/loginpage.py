from time import sleep
from ui_test.testmain.generic.base_class import SeleniumWrapper
from ui_test.testmain.data.xlrd_read import read_locator
from selenium.common.exceptions import NoSuchElementException


class LoginPage(SeleniumWrapper):
    locators = read_locator("loginpage")

    def __init__(self, driver):
        super().__init__(driver)

    def login_enter_email(self, email):
        element = LoginPage.locators['txt_email']
        super().enter_text(element, value=email)

    def login_enter_password(self, password):
        element = LoginPage.locators['txt_password']
        super().enter_text(element, value=password)

    def login_click_login(self):
        element = LoginPage.locators['btn_login']
        super().element_click(element)
