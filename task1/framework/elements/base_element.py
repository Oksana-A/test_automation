from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from framework.browser.browser import Browser
from framework.utils.waiters import Waiters


class BaseElement:

    def __init__(self, locator, by=By.XPATH):
        self._locator = locator
        self._by = by

    def _get_element(self):
        return Browser.get_inst().get_driver() \
            .find_element(self._by, self._locator)

    def get_attribute(self, name):
        return self._get_element().get_attribute(name)

    def get_text(self):
        return Waiters.wait_element_to_be_visible(self._by, self._locator).text

    def hover(self):
        element = Waiters.wait_element_to_be_clickable(self._by, self._locator)
        hov = ActionChains(Browser.get_inst().get_driver()) \
            .move_to_element(element)
        hov.perform()

    def click(self):
        Waiters.wait_element_to_be_clickable(self._by, self._locator).click()

    def get_elements_text(self, ):
        elements = Waiters.wait_all_elements_to_be_visible(
            self._by, self._locator)
        element_text_list = []
        for el in elements:
            element_text_list.append(el.text)
        return element_text_list

    def is_visible(self):
        try:
            Waiters.wait_element_to_be_visible(self._by, self._locator)
            return True
        except Exception:
            return False

    def wait_for_is_invisible(self):
        Waiters.wait_element_to_be_invisible(self._by, self._locator)
