import pytest
from libraries.library_add_remove_elements import AddRemoveActions


@pytest.fixture
def navigate_to_page(open_browser):
    print("Navigate to the page: http://the-internet.herokuapp.com/add_remove_elements/")
    driver = open_browser
    driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
    return driver


# Just confirm the functionality works
@pytest.mark.high_priority
@pytest.mark.sanity_test
def test_add_button(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveActions(driver)
    class_add_remove.click_on_add_element()
    buttons = class_add_remove.count_delete_buttons()
    assert len(buttons) == 1


# Create couple of buttons and delete them
@pytest.mark.sanity_test
def test_add_two_delete_one(navigate_to_page):
    driver = navigate_to_page
    class_add_remove = AddRemoveActions(driver)

    class_add_remove.click_on_add_element()
    class_add_remove.click_on_add_element()
    buttons = class_add_remove.count_delete_buttons()
    assert len(buttons) == 2
    class_add_remove.click_delete_button()
    buttons = class_add_remove.count_delete_buttons()
    assert len(buttons) == 1
