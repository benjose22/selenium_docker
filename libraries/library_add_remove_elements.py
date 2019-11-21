from libraries.locators import Locators
import allure


class AddRemoveActions(object):

    def __init__(self, driver, url):
        self.driver = driver
        driver.get(url)

    @allure.title("click_on_add_element")
    def click_on_add_element(self):
        self.driver.find_element_by_xpath(Locators.xpath_add_element_button).click()

    @allure.feature("count_delete_buttons")
    def count_delete_buttons(self):
        elements = self.driver.find_elements_by_xpath(Locators.xpath_delete_button_list)
        return elements

    @allure.story("click_delete_button")
    def click_delete_button(self):
        delete_button = self.driver.find_element_by_xpath(Locators.xpath_first_delete_button)
        delete_button.click()
