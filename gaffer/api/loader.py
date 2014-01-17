# -*- coding: utf-8 -*-

import os
import sys
import re

from gaffer.config import logger, MODULE_PATH


def get_modules(path):
    regex = re.compile(r'~|__init__|pyc')
    # Generator chain
    items = (i for i in os.listdir(path))
    filenames = (i for i in items if not regex.search(i))
    modules = map(lambda j: j[0], map(os.path.splitext, filenames))
    return set(modules)


def handlers():
    api_module = []
    for m in get_modules(MODULE_PATH):
        try:
            mod = __import__(m)
            logger.debug('%s loaded' % mod)
            api_module.append(mod.dispatch())
        except Exception as e:
            logger.exception(e)
    return api_module