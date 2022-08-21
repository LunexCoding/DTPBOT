import os
from Calendar import g_calendar


class FileSystem:

    def __init__(self, root='assets'):
        self._root = root
        self._lastWorkingDirectory = self.root
        self._initRoot()

    def chdir(self, path):
        try:
            os.chdir(path)
            self._lastWorkingDirectory = path
        except (FileNotFoundError, OSError) as e:
            print(e)

    def checkFileExists(self, filename):
        return os.path.exists(filename)

    def getFileLastModifiedGMTDate(self, filename):
        return g_calendar.getGMTFromFloat(os.path.getmtime(filename))

    def _initRoot(self):
        if not os.path.exists(self.root):
            os.makedirs(self.root)
        self.chdir(self.root)

    def initTree(self, tree=None):
        for path in tree:
            if not os.path.exists(path):
                os.makedirs(path)

    @property
    def root(self):
        return self._root


g_fileSystem = FileSystem('assets')
