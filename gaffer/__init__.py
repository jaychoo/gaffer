from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from gaffer.api import loader


api_handlers = loader.handlers()
for handler in api_handlers:
    for k, v in handler.dispatch.items():
        app.add_url_rule('/%s/%s' % (handler.version, k), k, v)
