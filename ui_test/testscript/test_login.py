from ui_test.testmain.pom.homepage import HomePage
from ui_test.testmain.pom.loginpage import LoginPage
from ui_test.testmain.data.xlrd_read import read_data, read_header
from pytest import mark

headers = read_header("smoke", "test_login_positive")
data = read_data("smoke", "test_login_positive")


@mark.parametrize(headers, data)
def test_login_positive(setup, email, password):
    hp = HomePage(setup)
    hp.home_click_login()

    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    # if lp.login_is_user_logged_in():
    #     print("user sucessfully logged in")
    # else:
    #     print("user not logged in")
    assert hp.is_user_logged_in(email) == True



headers = read_header("smoke", "test_login_negative")
data = read_data("smoke", "test_login_negative")


@mark.parametrize(headers, data)
def test_login_negative(setup, email, password, error_message):
    hp = HomePage(setup)
    hp.home_click_login()

    lp = LoginPage(setup)
    lp.login_enter_email(email)
    lp.login_enter_password(password)
    lp.login_click_login()
    # if hp.is_user_logged_in():
    #     print("user sucessfully logged in")
    # else:
    #     print("user not logged in")
    assert hp.is_error_message_displayed(error_message) == True