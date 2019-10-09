from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from framework.utils.config_reader import ConfigReader


class BrowserFactory:
    _browser = None
    projects_config = ConfigReader.get_inst().get_projects_config()
    framework_config = ConfigReader.get_inst().get_framework_config()

    def get_browser(self):
        if self.projects_config.browser_name.lower()\
                in self.framework_config.chrome_names:
            self._create_chrome_browser()
        elif self.projects_config.browser_name.lower()\
                in self.framework_config.firefox_name:
            self._create_ff_browser()
        else:
            self._create_chrome_browser()
        return self._browser

    def _create_chrome_browser(self):
        self._browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install())

    def _create_ff_browser(self):
        self._browser = webdriver.Firefox(
            executable_path=GeckoDriverManager().install())
