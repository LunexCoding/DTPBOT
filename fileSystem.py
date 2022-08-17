import os
from Calendar import g_calendar


class FileSystem:

    def __init__(self, root='assets'):
        self._root = root
        self._initRoot()

    def chdir(self, path):
        if os.path.exists(path):
            os.chdir(path)

    def checkFileExists(self, filename):
        if os.path.exists(filename):
            return self._getFileLastModifiedDate(filename)
        return False

    def _getFileLastModifiedDate(self, filename):
        return g_calendar.timeToGMT(os.path.getmtime(filename))

    def _initRoot(self):
        if not os.path.exists(self.root):
            os.makedirs(self.root)
        self.chdir(self.root)

    def _createTree(self, tree=None):
        for path in tree:
            if not os.path.exists(path):
                os.makedirs(path)

    @property
    def root(self):
        return self._root


g_fileSystem = FileSystem('assets')
g_fileSystem._createTree([
    'sets',
    'data',
    'data/train',
    'data/processing'
])
