# -*- coding: utf-8 -*-

import os
import sys
import re
import logging

from flask import Flask, current_app

from gaffer.api.error import GafferError
from config import MODULE_PATH, MODULE_EXMPT_REGEX


logger = logging.getLogger(__name__)


def handlers():
    def get_module_names(path):
        regex = re.compile(MODULE_EXMPT_REGEX)
        items = (i for i in os.listdir(path))
        filenames = (i for i in items if not regex.search(i))
        modules = map(lambda j: j[0], map(os.path.splitext, filenames))
        return set(modules)

    api_modules = []
    for path in MODULE_PATH:
        for module_name in get_module_names(path):
            try:
                module = __import__(module_name)
                logger.debug('%s loaded' % module)
                dispatch = module.dispatch()
                if dispatch:
                    api_modules.append(dispatch)
            except GafferError as e:
                logger.exception(e)
    return api_modules
