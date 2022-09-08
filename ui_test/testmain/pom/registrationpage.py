from ui_test.testmain.data.xlrd_read import read_locator
from ui_test.testmain.pom.homepage import HomePage

class RegistrationPage(HomePage):
    locator = read_locator("registrationpage")

    def __init__(self, driver):
        super().__init__(driver)

    def reg_click_gender(self,value):
        if value == "male":
            element = RegistrationPage.locator["rdo_male"]
            self.element_click(element)
        elif value == "female":
            element = RegistrationPage.locator["rdo_female"]
            self.element_click(element)            

    def reg_enter_firstname(self, firstname):
        element = RegistrationPage.locator["txt_fname"]
        self.enter_text(element, value=firstname)

    def reg_enter_lastname(self, lastname):
        element = RegistrationPage.locator["txt_lname"]
        self.enter_text(element, value=lastname)

    def reg_enter_enamil(self, email):
        element = RegistrationPage.locator["txt_email"]
        self.enter_text(element, value=email)

    def reg_enter_password(self, password):
        element = RegistrationPage.locator["txt_password"]
        self.enter_text(element, value=password)

    def reg_enter_confirm_password(self, confirm_password):
        element = RegistrationPage.locator["txt_confirm_password"]
        self.enter_text(element, value=confirm_password)

    def reg_click_register(self):
        element = RegistrationPage.locator["btn_register"]
        self.element_click(element)