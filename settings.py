import configparser
from fileSystem import g_fileSystem
from Logger import logger


LOGGER = logger.getLogger(__name__)


class Config:

    def __init__(self, filename):
        self._filename = filename
        self._config = configparser.ConfigParser(default_section='DEFAULT')
        self._config.optionxform = str

        self.isAutoDownload = None

    def load(self):
        if g_fileSystem.checkFileExists(self._filename):
            self._read()
        else:
            self._createConfig()

        self.isAutoDownload = eval(self._config.get('Downloading', 'isAutoDownload'))

    def _createConfig(self):
        self._addSection('Downloading')
        self._addOption('DEFAULT', 'option', 'value')
        self._addOption('Downloading', 'isAutoDownload', 'False')
        self._write()
        LOGGER.debug('Config has been created!')

    def _addSection(self, sectionName):
        self._config.add_section(sectionName)

    def _addOption(self, sectionName, optionName, value):
        self._config.set(sectionName, optionName, value)

    def _read(self):
        self._config.read(self._filename, 'utf-8')

    def _write(self):
        with open(self._filename, 'w') as configFile:
            self._config.write(configFile, space_around_delimiters=True)


g_config = Config('config.ini')
