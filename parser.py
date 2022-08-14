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

    def _getDataSetsUploadDate(self):
        return self._soup.find('td', {'class': 'small'}).text.split('- ')[1]

    def _downloadDataSets(self, FTP=None):
        g_fileSystem.chdir('sets')
        for dataSet in zip(self._dataSetLinks, self._dataSetRegions):

            urlToDataSet, region = dataSet
            filename = region + '.json'

            responce = requests.get(urlToDataSet)

            with open(filename, 'w', encoding='utf-8') as file:
                json.dump(responce.json(), file, ensure_ascii=False)
                print(f'Region [{region}] downloaded!')

        g_fileSystem.chdir(g_fileSystem.root)

    def run(self):
        self._generateSoup()
        g_calendar.uploadDateDataSets = self._getDataSetsUploadDate()
        self._dataSetLinks = self._getDataSetLinks()
        self._dataSetRegions = self._getDataSetRegions()
        self._downloadDataSets()


g_parser = Parser('https://dtp-stat.ru/opendata/')
