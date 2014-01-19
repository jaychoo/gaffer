# -*- coding: utf-8 -*-

# Default settings for Gaffer

import os
import sys
import logging

DEBUG = True
MODULE_PATH = [os.path.abspath(os.path.join(os.path.dirname(__file__), './api/modules'))]

for path in MODULE_PATH:
    sys.path.insert(0, MODULE_PATH)

LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT, datefmt='%m-%d %H:%M')
logger = logging.getLogger('gaffer')
