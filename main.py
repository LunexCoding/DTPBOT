from parser import g_parser
from Logger import logger
from fileSystem import g_fileSystem
from pathlib import Path
from settings import g_config


LOGGER = logger.getLogger(__name__)


def main():
    g_parser.start()


if __name__ == '__main__':
    LOGGER.debug('Start log')
    g_config.load()
    g_fileSystem.initTree([
        Path('assets'),
        Path('assets', 'sets'),
        Path('assets', 'data'),
        Path('assets', 'data', 'train'),
        Path('assets', 'data', 'processing')
    ])

    main()
