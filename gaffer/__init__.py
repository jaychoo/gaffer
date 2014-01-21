# -*- coding: utf-8 -*-

import logging

from flask import Flask

from gaffer.api import loader


app = Flask(__name__)
app.config.from_object('config')
logger = logging.getLogger(__name__)

api_handlers = loader.handlers()
if api_handlers:
    for handler in api_handlers:
        try:
            for key in handler.dispatch:
                app.add_url_rule(key, key, handler)
        except Exception as e:
            logger.exception(e)
