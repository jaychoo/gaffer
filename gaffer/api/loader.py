import os
import sys
import re

DEFAULT_PATH = './modules'
INVALID = ('~', '__init__', '.pyc')


def get_modules(path=DEFAULT_PATH):
    regex = re.compile(r'~|__init__|pyc')
    # Generator chain
    items = (i for i in os.listdir(path))
    filenames = (i for i in items if not regex.search(i))
    modules = map(lambda j: j[0], map(os.path.splitext, filenames))
    return set(modules)

if __name__ == '__main__':
    modules = get_modules()
    sys.path.insert(0, 'modules')

    for m in modules:
        mod = __import__(m)
        mod.run()

