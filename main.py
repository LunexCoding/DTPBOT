from parser import g_parser
from fileSystem import g_fileSystem


def main():
    g_parser.start()


if __name__ == '__main__':
    g_fileSystem.initTree([
        'sets',
        'data',
        'data/train',
        'data/processing'
    ])

    main()
