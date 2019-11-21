import pytest
import allure
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser type")
    parser.addoption("--url", action="store", default="http://the-internet.herokuapp.com", help="url")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@allure.step("Open Browser")
@pytest.fixture(scope="module")
def open_browser(request):
    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.maximize_window()

    yield driver # Teardown
    driver.close()


@pytest.fixture(autouse=True)
def allure_logs(request, open_browser):
    driver = open_browser
    yield driver
    if request.node.rep_call.failed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")
            allure.attach(driver.get_screenshot_as_png(),
                          name=request.function.__name__,
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass # just ignore
