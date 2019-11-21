import pytest
import allure
from libraries.library_add_remove_elements import AddRemoveActions


# Just confirm the functionality works
@allure.title("This test has a custom title")
@allure.description("""
Multiline test description.
That comes from the allure.description decorator.

Nothing special about it.
""")
@pytest.mark.high_priority
@pytest.mark.sanity_test
def test_add_button(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/add_remove_elements/"
    class_add_remove = AddRemoveActions(driver, url)
    class_add_remove.click_on_add_element()
    buttons = class_add_remove.count_delete_buttons()
    class_add_remove.to_delete(3)
    assert len(buttons) == 1


# Create couple of buttons and delete them
@pytest.mark.sanity_test
def test_add_two_delete_one(open_browser):
    driver = open_browser
    url = "http://the-internet.herokuapp.com/add_remove_elements/"
    class_add_remove = AddRemoveActions(driver, url)

    class_add_remove.click_on_add_element()
    class_add_remove.click_on_add_element()
    buttons = class_add_remove.count_delete_buttons()
    assert len(buttons) == 2
    class_add_remove.click_delete_button()
    buttons = class_add_remove.count_delete_buttons()
    assert len(buttons) == 1
