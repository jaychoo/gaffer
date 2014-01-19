# -*- coding: utf-8 -*-


def get_dispatch(*fn):
    return {f.__name__: f  for f in fn}
