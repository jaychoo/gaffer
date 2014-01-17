from flask import request

from gaffer.config import logger


class APIHandler(object):
    def __init__(self, dispatch, name, version='v1'):
        self.dispatch = dispatch
        self.name = name
        self.version = version

    def default(self, *args, **kwargs):
        return '%s %s' % (self.name, self.version)

    def __call__(self, *args, **kwargs):
        try:
            fn = self.dispatch.get(request.path.strip('/'))
            return fn(*args, **kwargs)
        except Exception as e:
            logger.exception(e)
            return self.default()
