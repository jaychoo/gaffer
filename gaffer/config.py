# -*- coding: utf-8 -*-

# Default settings for Gaffer

import os
import sys
import logging

DEBUG = True
MODULE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './api/modules'))
LOGGING_LEVEL = logging.DEBUG
LOGGING_FORMAT = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

sys.path.insert(0, MODULE_PATH)

logging.basicConfig(format=LOGGING_FORMAT, datefmt='%m-%d %H:%M')
logger = logging.getLogger('gaffer')
logger.setLevel(LOGGING_LEVEL)
