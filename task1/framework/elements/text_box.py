from framework.elements.base_element import BaseElement
from framework.utils.waiters import Waiters


class Textbox(BaseElement):

    def send_text(self, text):
        Waiters.wait_element_to_be_clickable(self._by, self._locator).clear()
        Waiters.wait_element_to_be_clickable(self._by, self._locator).click()
        Waiters.wait_element_to_be_clickable(self._by, self._locator)\
            .send_keys(text)
