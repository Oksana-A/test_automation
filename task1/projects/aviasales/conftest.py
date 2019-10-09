import pytest

from framework.browser.browser import Browser
from framework.utils.config_reader import ConfigReader


@pytest.fixture(autouse=True)
def browser_manager():
    Browser.get_inst().set_maximize_window_size()
    Browser.get_inst().enter_page(
        ConfigReader.get_inst().get_project_config().aviasales_url)
    yield
    Browser.get_inst().get_driver().quit()
