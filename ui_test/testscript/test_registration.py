from ui_test.testmain.pom.homepage import HomePage
from ui_test.testmain.pom.registrationpage import RegistrationPage
from ui_test.testmain.data.xlrd_read import read_data ,read_header
from pytest import mark

headers = read_header("smoke", "test_registration")
data = read_data("smoke", "test_registration")

@mark.parametrize(headers, data)
def test_registration(setup, gender, fname , lname , email, password):
    hp = HomePage(setup)
    hp.home_click_register()

    rp = RegistrationPage(setup)
    rp.reg_click_gender(gender)
    rp.reg_enter_firstname(fname)
    rp.reg_enter_lastname(lname)
    rp.reg_enter_enamil(email)
    rp.reg_enter_password(password)
    rp.reg_enter_confirm_password(password)
    rp.reg_click_register()

