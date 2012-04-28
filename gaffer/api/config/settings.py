# Default settings for Gaffer API

import logging

logger = logging.getLogger('gaffer.api')

# Path to function modules
MOUDLES = '../modules'

# Default API port
PORT = 8088

# Default broker url, add user specific settings in /modules folder e.g. config.py
BROKER = 'localhost'
BROKER_PORT = 1234
BROKER_USER = 'user'
BROKER_PASSWORD = 'password'

