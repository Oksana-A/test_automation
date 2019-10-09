from framework.elements.label import Label
from framework.base_page.base_page import BasePage
from projects.aviasales.models.ticket import Ticket


class SearchResultsPage(BasePage):

    counter_label = Label("//div[@class='countdown']")
    ticket_label = Label("//div[@class='segment-route__body']")

    def wait_for_search_to_finish(self):
        self.counter_label.wait_for_is_invisible()

    def get_fastest_flight(self):
        element_text_list = self.ticket_label.get_elements_text()
        tickets = []
        i = 0
        while i < len(element_text_list):
            ticket = Ticket(element_text_list[i], element_text_list[i+1])
            tickets.append(ticket)
            i = i + 2
        tickets.sort()
        return tickets[0]
