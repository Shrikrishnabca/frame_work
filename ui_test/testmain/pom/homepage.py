from time import sleep
from ui_test.testmain.generic.base_class import SeleniumWrapper
from ui_test.testmain.data.xlrd_read import read_locator
from selenium.common.exceptions import NoSuchElementException

class HomePage(SeleniumWrapper):
    
    locator = read_locator("homepage")

    def __init__(self, driver):
        super().__init__(driver)

    def home_click_login(self):
        element = HomePage.locator['lnk_login']
        self.element_click(element) 

    def home_click_register(self):
        element = HomePage.locator['lnk_register']
        self.element_click(element)

    def is_user_logged_in(self,email):
        _xpath = f"//a[text()='{email}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath", _xpath).is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue                
        return False
        
    def is_error_message_displayed(self, error_message):
        _xpath = f"//span[text()='{error_message}']"
        for _ in range(5):
            try:
                return self.driver.find_element("xpath", _xpath).is_displayed()
            except NoSuchElementException:
                sleep(1)
                continue
        return False


