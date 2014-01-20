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
            for k, v in handler.dispatch.items():
                app.add_url_rule('/%s/%s' % (handler.version, k), k, v)
        except Exception as e:
            logger.exception(e)
