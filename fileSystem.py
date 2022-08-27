import os
from Calendar import g_calendar
from Logger import logger
from pathlib import Path, PurePath


LOGGER = logger.getLogger(__name__)


class FileSystem:

    def __init__(self, root='assets'):
        self._root = root
        self._lastWorkingDirectory = self.root

    def chdir(self, path):
        try:
            os.chdir(path)
            self._lastWorkingDirectory = Path(PurePath(Path.cwd()).parents[0].name)
            LOGGER.debug(f'Chdir [{self._lastWorkingDirectory}] -> [{Path(self.root, path) if path != self.root else self.root}]')
        except (FileNotFoundError, OSError) as e:
            LOGGER.error(e)

    def checkFileExists(self, filename):
        return os.path.exists(filename)

    def getFileLastModifiedGMTDate(self, filename):
        return g_calendar.getGMTFromFloat(os.path.getmtime(filename))

    def _initRoot(self):
        if not os.path.exists(self.root):
            os.mkdir(self.root)
            LOGGER.debug(f'Root [{Path(self.root)}] has been created!')
        self.chdir(self.root)

    def initTree(self, tree=None):
        for path in tree:
            if not os.path.exists(path):
                os.makedirs(path)
                LOGGER.debug(f'Directory [{Path(path)}] has been created!')
        self.chdir(self.root)

    @property
    def root(self):
        return self._root


g_fileSystem = FileSystem('assets')
