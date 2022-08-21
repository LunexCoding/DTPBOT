from datetime import datetime


class Calendar:

    def __init__(self):
        self._serverDate = None

    def getGMTFromFloat(self, data):
        dtUTC = datetime.utcfromtimestamp(data)
        timeStringFormatFromdDT = datetime.strftime(dtUTC, "%a, %d %b %Y %H:%M:%S GMT")
        return datetime.strptime(timeStringFormatFromdDT, "%a, %d %b %Y %H:%M:%S GMT")

    def getGMTFromStr(self, data):
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
