import json
import requests
from bs4 import BeautifulSoup as bs
from fileSystem import g_fileSystem
from Calendar import g_calendar


class Parser:

    def __init__(self, url=None):
        self._url = url
        self._soup = None
        self._dataSetsLinks = None
        self._dataSetRegions = None

    def _generateSoup(self):
        page = requests.get(self._url)
        self._soup = bs(page.text, 'html.parser')

    def _getDataSetLinks(self):
        dataSetsLinks = self._soup.find_all('td', {'class': 'text-center'})
        return [link.find('a').get('href') for link in dataSetsLinks]

    def _getDataSetRegions(self):
        namesRegions = self._soup.find_all('td')
        return [region.find('b').getText() for region in namesRegions if region.find('b') is not None]

    def _downloadFile(self, filename, data):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False)
            print(f'Region [{filename.split(".json")[0]}] downloaded!')

    def _downloadDataSets(self):

        g_fileSystem.chdir('sets')

        for dataSet in zip(self._dataSetLinks, self._dataSetRegions):

            url, region = dataSet
            filename = region + '.json'

            responce = requests.get(url)

            if (fileStatus := g_fileSystem.checkFileExists(filename)) is not False:
                serverDate = g_calendar.timeToGMT(responce.headers['Last-Modified'])
                localDate = fileStatus

                if g_calendar.checkRelevance(serverDate, localDate):
                    self._downloadFile(filename, data=responce.json())

            else:
                self._downloadFile(filename, data=responce.json())

        g_fileSystem.chdir(g_fileSystem.root)

    def run(self):
        self._generateSoup()
        self._dataSetLinks = self._getDataSetLinks()
        self._dataSetRegions = self._getDataSetRegions()
        self._downloadDataSets()


g_parser = Parser('https://dtp-stat.ru/opendata/')
