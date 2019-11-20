from libraries.locators import Locators


class AddRemoveActions(object):

    def __init__(self, driver):
        self.driver = driver

    def click_on_add_element(self):
        self.driver.find_element_by_xpath(Locators.xpath_add_element_button).click()

    def count_delete_buttons(self):
        elements = self.driver.find_elements_by_xpath(Locators.xpath_delete_button_list)
        return elements

    def click_delete_button(self):
        delete_button = self.driver.find_element_by_xpath(Locators.xpath_first_delete_button)
        delete_button.click()
