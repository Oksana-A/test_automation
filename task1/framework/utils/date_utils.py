import datetime


class DateUtils:

    @staticmethod
    def get_new_date_from_today(delta):
        return datetime.datetime.now() + datetime.timedelta(int(delta))

    @staticmethod
    def get_date(year, month=1, day=1):
        return datetime.datetime(year, month, day)
