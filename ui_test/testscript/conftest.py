from selenium import webdriver
from ui_test.testmain.generic.config import Config
from pytest import fixture
import random


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="browser type chrome/edge")


@fixture
def setup(request):
    browser_type = request.config.getoption("--browser")
    if browser_type.lower() == "chrome":
        driver = webdriver.Chrome(r"E:\_selenium\framework\ui_test\testscript\drivers\chromedriver.exe")
    elif browser_type.lower() == "edge":
        driver = webdriver.Edge(r"E:\_selenium\framework\ui_test\testscript\drivers\msedgedriver.exe")
    else:
        raise NameError("Unknown Browser")
    driver.get(Config.URL)
    driver.maximize_window()
    yield driver
    n = random.randint(0, 1122)
    driver.save_screenshot(f"E:\_selenium\\framework\\ui_test\\testoutput\screenshots\\{n}screenshot.png")
    driver.close()
