# -*- coding: utf-8 -*-

import re

from flask import request, render_template

from gaffer.api.error import GafferError


def slugify(s):
    return re.sub(r'\W+','-', s.strip().lower())


class GafferAPIBase(object):
    def __init__(self, dispatch, service_name, version='v1'):
        self.name = service_name
        self.slug = slugify(self.name)
        self.version = version

        dispatch_prefix = '/%s/%s/' % (self.slug, self.version)

        self.dispatch = {dispatch_prefix: self.index}
        for url_pattern, fn in dispatch.items():
            self.dispatch['%s%s' % (dispatch_prefix, url_pattern)] = fn

    def index(self, *args, **kwargs):
        api_list = [{'url':i[0], 'fn': i[1]} for i in self.dispatch.items()]
        context = {'title': self.name, 
        'version': self.version, 
        'api_list': api_list}
        
        return render_template('index.html', **context) 

    def __call__(self, *args, **kwargs):
        try:
            fn = self.dispatch.get(request.path)
            return fn(*args, **kwargs)
        except Exception as e:
            raise GafferError(e)
