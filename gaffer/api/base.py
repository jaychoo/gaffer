# -*- coding: utf-8 -*-

import re

from flask import request

from gaffer.api.error import GafferError


def slugify(s):
    return re.sub(r'\W+','-', s.strip().lower())


class GafferAPIBase(object):
    def __init__(self, dispatch, service_name, version='v1'):
        self.name = service_name
        self.service_name_slug = slugify(self.name)
        self.version = version

        dispatch_prefix = '/%s/%s/' % (self.service_name_slug, self.version)

        self.dispatch = {dispatch_prefix: self.index}
        for url_pattern, fn in dispatch.items():
            self.dispatch['%s%s' % (dispatch_prefix, url_pattern)] = fn

    def index(self, *args, **kwargs):
        return '<h1>%s %s</h1>' % (self.name, self.version)

    def __call__(self, *args, **kwargs):
        try:
            print request.path
            fn = self.dispatch.get(request.path)
            return fn(*args, **kwargs)
        except Exception as e:
            raise GafferError(e)
