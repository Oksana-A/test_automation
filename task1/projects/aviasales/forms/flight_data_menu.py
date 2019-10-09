from framework.elements.button import Button
from framework.elements.text_box import Textbox
from framework.elements.label import Label
from framework.utils.date_utils import DateUtils
from framework.utils.config_reader import ConfigReader


class FlightDataMenu:
    departure_city_txtbox = Textbox("//input[@id='origin']")
    city_of_arrival_txtbox = Textbox("//input[@id='destination']")
    departure_date_btn = Button("//div[contains(@class, '--depart')]")
    class_of_service_btn = Button("//div[@class='additional-fields__label']")
    switch_month_btn = Button("//span[contains(@class, '--next')]")
    day_xpath = "//div[contains(@class, 'daypicker__day-wrap')][text()='%s']"
    class_variation_xpath = \
        "//div[@class='custom-radio__caption'][text()='%s']"
    month_and_year_label = Label("//div[@class='daypicker__caption']")

    def enter_data(self, departure_city, city_of_arrival,
                   start_offset_from_today, end_offset_from_today,
                   class_of_service):
        self.__choose_city(departure_city, self.departure_city_txtbox)
        self.__choose_city(city_of_arrival, self.city_of_arrival_txtbox)
        self.departure_date_btn.click()
        current_date = self.__get_current_date()
        departure_data = DateUtils.get_new_date_from_today(
            start_offset_from_today)
        arrival_data = DateUtils.get_new_date_from_today(end_offset_from_today)
        self.__choose_date(current_date, departure_data)
        self.__choose_date(departure_data, arrival_data)
        self.__choose_class_of_service(class_of_service)

    def __choose_city(self, city, element):
        element.send_text(city)
        element.hover()
        element.click()

    def __choose_date(self, current_date, required_date):
        number_of_switches = 0
        number_of_years = int(required_date.year) - int(current_date.year)
        if number_of_years == 0:
            number_of_switches = \
                int(required_date.month) - int(current_date.month)
        if number_of_years >= 1:
            number_of_switches = 12*number_of_years - int(current_date.month) \
                                 + int(required_date.month)
        self.__switch_month(number_of_switches)
        el_xpath = self.day_xpath % required_date.day
        btn = Button(el_xpath)
        btn.hover()
        btn.click()

    def __switch_month(self, amount):
        while amount > 0:
            self.switch_month_btn.click()
            amount -= 1

    def __choose_class_of_service(self, class_of_service):
        self.class_of_service_btn.click()
        el_xpath = self.class_variation_xpath % class_of_service
        Button(el_xpath).click()

    def __get_current_date(self):
        month_and_year = self.month_and_year_label.get_text().split()
        month = month_and_year[0].lower()
        year = int(month_and_year[1])
        month_number = \
            ConfigReader.get_inst().get_project_config().months[month]
        return DateUtils.get_date(year, month_number)
