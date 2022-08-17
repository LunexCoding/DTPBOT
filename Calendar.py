from datetime import datetime
import enum


class MONTHS(enum.IntEnum):
    Январь = 1
    Февраль = 2
    Март = 3
    Апрель = 4
    Май = 5
    Июнь = 6
    Июль = 7
    Август = 8
    Сентябрь = 9
    Октябрь = 10
    Ноябрь = 11
    Декабрь = 12


class Calendar:

    def __init__(self):
        self._serverDate = None

    def timeToGMT(self, data):
        if isinstance(data, float):
            dtUTC = datetime.utcfromtimestamp(data)
            timeStringFormatFromdDT = datetime.strftime(dtUTC, "%a, %d %b %Y %H:%M:%S GMT")
            return datetime.strptime(timeStringFormatFromdDT, "%a, %d %b %Y %H:%M:%S GMT")

        elif isinstance(data, str):
            return datetime.strptime(data, "%a, %d %b %Y %H:%M:%S GMT")

    def checkRelevance(self, server, local):
        return True if server > local else False

    @property
    def serverDate(self):
        return self._serverDate

    @serverDate.setter
    def serverDate(self, date):
        self._serverDate = date


g_calendar = Calendar()
