from framework.browser.browser import Browser


class BasePage:

    def get_title(self):
        return Browser.get_inst().get_driver().title
