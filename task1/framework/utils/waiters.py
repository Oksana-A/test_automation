from selenium.webdriver.support.expected_conditions import \
    element_to_be_clickable, invisibility_of_element_located, \
    visibility_of_element_located, visibility_of_all_elements_located

from framework.browser.browser import Browser
from framework.utils.config_reader import ConfigReader


class Waiters:

    @staticmethod
    def wait_element_to_be_clickable(by, locator):
        return Browser.get_inst().get_webdriver_wait() \
            .until(element_to_be_clickable((by, locator)))

    @staticmethod
    def wait_element_to_be_visible(by, locator):
        return Browser.get_inst().get_webdriver_wait() \
            .until(visibility_of_element_located((by, locator)))

    @staticmethod
    def wait_all_elements_to_be_visible(by, locator):
        return Browser.get_inst().get_webdriver_wait() \
            .until(visibility_of_all_elements_located((by, locator)))

    @staticmethod
    def wait_element_to_be_invisible(by, locator):
        Browser.get_inst().get_webdriver_wait() \
            .until(invisibility_of_element_located((by, locator)))

    @staticmethod
    def implicitly_wait():
        Browser.get_inst().get_driver().implicitly_wait(
            ConfigReader.get_inst().get_projects_config().implicitly_wait)
