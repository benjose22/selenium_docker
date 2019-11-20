import pytest
from libraries.library_dynamic_controls import AddRemoveCheckbox
from libraries.library_dynamic_controls import EnableDisableTextbox


@pytest.fixture
def navigate_to_page(open_browser):
    print("Navigate to the page: http://the-internet.herokuapp.com/dynamic_controls")
    driver = open_browser
    driver.get("http://the-internet.herokuapp.com/dynamic_controls")
    return driver


# Just remove checkbox
@pytest.mark.high_priority
def test_remove_checkbox(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveCheckbox(driver)
    class_add_remove.click_remove_button()
    message = class_add_remove.verify_text()
    assert message == "It's gone!"


# Remove and then add button
def test_remove_and_add_checkbox(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveCheckbox(driver)
    class_add_remove.click_remove_button()
    message = class_add_remove.verify_text()
    assert message == "It's gone!"
    class_add_remove.click_add_button()
    assert class_add_remove.verify_checkbox_presence() == True


@pytest.mark.error
@pytest.mark.selenium_error
def test_expected_selenium_error(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveCheckbox(driver)
    message = class_add_remove.verify_text()
    assert message == "It's gone!"


@pytest.mark.error
@pytest.mark.assert_error
def test_expected_assertion_error(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveCheckbox(driver)
    class_add_remove.click_remove_button()
    message = class_add_remove.verify_text()
    assert message == "Expected error"


@pytest.mark.error
@pytest.mark.python_error
def test_expected_python_error(navigate_to_page):
    driver = navigate_to_page
    driver = driver + 1
    print(driver)


def test_enable_disable_button(navigate_to_page):
    driver = navigate_to_page
    class_enable_disable = EnableDisableTextbox(driver)
    class_enable_disable.click_enable_button()
    class_enable_disable.click_disable_button()
