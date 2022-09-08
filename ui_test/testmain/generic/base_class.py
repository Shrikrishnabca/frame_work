from ui_test.testmain.generic.syn_script import _wait
from selenium.webdriver.support.select import Select

class SeleniumWrapper:
    def __init__(self, driver):
        self.driver = driver
        
    @_wait
    def element_click(self, locator):
        self.driver.find_element(*locator).click()

    @_wait
    def enter_text(self,locator,*,  value):
        self.driver.find_element(*locator).clear()
        self.driver.find_element(*locator).send_keys(value)

    @_wait
    def select_item(self,locator, *, item):
        element = self.driver.find_element(*locator)
        s = Select(element)
        if isinstance(item, str):
            s.select_by_visible_text(item)
        elif isinstance(item, int):
            s.select_by_index(item)
        else:
            raise Exception

