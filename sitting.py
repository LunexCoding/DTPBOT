import configparser


class Config:

    def __init__(self, filename):
        self._filename = filename
        self._config = configparser.ConfigParser(default_section='DEFAULT')
        self._config.optionxform = str

    def addSection(self, sectionName):
        self._config.add_section(sectionName)

    def addOption(self, sectionName, optionName, value):
        self._config.set(sectionName, optionName, value)

    def read(self):
        self._config.read(self._filename, 'utf-8')

    def getValue(self, sectionName, optionName):
        return self._config.get(sectionName, optionName)

    def write(self):
        with open(self._filename, 'w') as configFile:
            self._config.write(configFile, space_around_delimiters=True)


config = Config('config.ini')

config.addSection('Downloading')
config.addOption('DEFAULT', 'option', 'value')
config.addOption('Downloading', 'isAutoDownload', 'False')
config.write()

config.read()
print(config.getValue('Downloading', 'isAutoDownload'))
print(config.getValue('DEFAULT', 'option'))
