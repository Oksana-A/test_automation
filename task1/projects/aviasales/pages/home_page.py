from framework.base_page.base_page import BasePage
from framework.elements.button import Button
from projects.aviasales.forms.forms import Forms


class HomePage(BasePage):
    forms = Forms()
    search_btn = \
        Button("//div[contains(@class, '--mobile-search')]")

    def find_ticket(self, departure_city, city_of_arrival,
                    start_offset_from_today,
                    end_offset_from_today, class_of_service):
        self.forms.flight_data_menu.enter_data(
            departure_city, city_of_arrival,
            start_offset_from_today, end_offset_from_today, class_of_service)
        self.search_btn.click()
