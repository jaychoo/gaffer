# -*- coding: utf-8 -*-

from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from gaffer.api import loader
from gaffer.config import logger

api_handlers = loader.handlers()
if api_handlers:
    for handler in api_handlers:
        try:
            for k, v in handler.dispatch.items():
                app.add_url_rule('/%s/%s' % (handler.version, k), k, v)
        except Exception as e:
            logger.exception(e)
