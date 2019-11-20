from libraries.library_drag_and_drop import DragDrop

import pytest


@pytest.fixture
def navigate_to_page(open_browser):
    print("Navigate to the page: http://the-internet.herokuapp.com/drag_and_drop")
    driver = open_browser
    driver.get("http://the-internet.herokuapp.com/drag_and_drop")
    return driver


@pytest.mark.skip("HTML drag and drop not supported by selenium. Hence skipping.")
def test_drag_and_drop(navigate_to_page):
    driver = navigate_to_page
    class_dragdrop_instance = DragDrop(driver)
    class_dragdrop_instance.move_a_to_b()
