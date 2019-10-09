from framework.browser.browser import Browser
from framework.utils.config_reader import ConfigReader
from projects.aviasales.pages.home_page import HomePage
from projects.aviasales.pages.search_results_page import SearchResultsPage


class TestFastFlightSearch:
    home_page = HomePage()
    search_result_page = SearchResultsPage()
    project_config = ConfigReader.get_inst().get_project_config()

    def test_fast_flight_search(self):
        self.home_page.find_ticket(self.project_config.departure_city,
                                   self.project_config.city_of_arrival,
                                   self.project_config.start_offset_from_today,
                                   self.project_config.end_offset_from_today,
                                   self.project_config.class_of_service)
        Browser.get_inst().switch_to_tab(1)
        self.search_result_page.wait_for_search_to_finish()
        x = self.search_result_page.get_fastest_flight()
        print('\nСамый быстрый рейс:')
        print(x)
