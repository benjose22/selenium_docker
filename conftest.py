import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://the-internet.herokuapp.com", help="url")


@pytest.fixture(scope="module")
def open_browser(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.close()




