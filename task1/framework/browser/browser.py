from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait

from framework.browser_factory.browser_factory import BrowserFactory
from framework.utils.config_reader import ConfigReader


class Browser:
    __instance = None

    def __init__(self):
        self.__driver = BrowserFactory().get_browser()
        self.__webdriver_wait = WebDriverWait(
            self.__driver,
            ConfigReader.get_inst().get_projects_config().waiting_time,
            ignored_exceptions=StaleElementReferenceException)

    @staticmethod
    def get_inst():
        if Browser.__instance is None:
            Browser.__instance = Browser()
        return Browser.__instance

    def enter_page(self, url):
        self.__driver.get(url)

    def get_current_url(self):
        return self.__driver.current_url

    def switch_to_tab(self, tab_number):
        self.__driver.switch_to_window(
            self.__driver.window_handles[tab_number])

    def set_maximize_window_size(self):
        self.__driver.maximize_window()

    def get_webdriver_wait(self):
        return self.__webdriver_wait

    def get_driver(self):
        return self.__driver
