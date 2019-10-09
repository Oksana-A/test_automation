import re
from functools import total_ordering


@total_ordering
class Ticket:
    REGEX_DAY = r"(\d+)д"
    REGEX_HOUR = r"(\d+)ч"
    REGEX_MINUTES = r"(\d+)м"

    def __init__(self, inf_flight_1, inf_flight_2):
        self.inf_flight_1 = inf_flight_1
        self.inf_flight_2 = inf_flight_2
        self.time_to_destination = self.__get_time(inf_flight_1)
        self.time_back = self.__get_time(inf_flight_2)

    def __str__(self):
        return '\n{inf_flight_1}\n********\n{inf_flight_2}' \
               '\n********\nОбщее время в пути: {time}'\
            .format(inf_flight_1=self.inf_flight_1,
                    inf_flight_2=self.inf_flight_2,
                    time=self.time_to_destination + self.time_back)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if isinstance(other, Ticket):
            return self.time_to_destination + self.time_back \
                   == other.time_to_destination + other.time_back
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Ticket):
            return self.time_to_destination + self.time_back \
                   > other.time_to_destination + other.time_back
        return NotImplemented

    def __get_time(self, inf):
        time = 0
        try:
            match = re.findall(self.REGEX_DAY, inf)
            time = time + int(match[0]) * 24 * 60
        except IndexError:
            pass
        try:
            match = re.findall(self.REGEX_HOUR, inf)
            time = time + int(match[0]) * 60
        except IndexError:
            pass
        try:
            match = re.findall(self.REGEX_MINUTES, inf)
            time = time + int(match[0])
        except IndexError:
            pass
        return time
