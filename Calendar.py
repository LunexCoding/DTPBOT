from datetime import datetime
import enum
import time


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
        self._uploadDateDataSets = None

    def generateDate(self, dateString):
        dateString = dateString.title().split()
        month, year = dateString[0], int(dateString[1])
        month = MONTHS[month].value + 1
        if month > 12:
            month %= 12
            year += 1
        return datetime.strptime(f'{month}/{year}', "%m/%Y").strftime("%m/%Y")

    def checkRelevance(self, date):
        # self._uploadDateDataSets, ':::', 
        # print(datetime.fromtimestamp(date).strftime('%Y-%m-%d %H:%M:%S'))
        # print(time.ctime(date))
        pass

    @property
    def uploadDateDataSets(self):
        return self._uploadDateDataSets

    @uploadDateDataSets.setter
    def uploadDateDataSets(self, date):
        self._uploadDateDataSets = date


g_calendar = Calendar()
