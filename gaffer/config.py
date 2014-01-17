# -*- coding: utf-8 -*-

# Default settings for Gaffer

import os
import sys
import logging

DEBUG = True
MODULE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), './api/modules'))

sys.path.insert(0, MODULE_PATH)
logger = logging.getLogger('gaffer')
