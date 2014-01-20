# -*- coding: utf-8 -*-

# Default settings for Gaffer

import os
import sys
import logging


DEBUG = True
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

MODULE_EXMPT_REGEX = r'~|__init__|pyc'
MODULE_PATH = [os.path.abspath(os.path.join(BASE_DIR, 'gaffer/modules'))]

LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt='%m-%d %H:%M')

for path in MODULE_PATH:
    sys.path.insert(0, path)
