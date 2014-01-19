# -*- coding: utf-8 -*-

import os
import sys
import re
import logging

from gaffer.config import logger, MODULE_PATH, MODULE_EXMPT_REGEX
from gaffer.api.error import GafferError


def get_modules(path):
    regex = re.compile(MODULE_EXMPT_REGEX)
    items = (i for i in os.listdir(path))
    filenames = (i for i in items if not regex.search(i))
    modules = map(lambda j: j[0], map(os.path.splitext, filenames))
    return set(modules)


def handlers():
    api_modules = []
    for path in MODULE_PATH:
        for module_name in get_modules(path):
            try:
                module = __import__(module_name)
                logging.debug('%s loaded' % module)
                dispatch = module.dispatch()
                if dispatch:
                    api_modules.append(dispatch)
            except GafferError as e:
                logger.exception(e)
    return api_modules
