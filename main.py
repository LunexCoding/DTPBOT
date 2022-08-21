from parser import g_parser
from fileSystem import g_fileSystem
from Logger import logger
from pathlib import Path


LOGGER = logger.getLogger(__name__)


def main():
    g_parser.start()


if __name__ == '__main__':
    LOGGER.debug('Start log')
    g_fileSystem.initTree([
        Path('sets'),
        Path('data'),
        Path('data', 'train'),
        Path('data', 'processing')
    ])

    main()
