# -*- coding: utf-8 -*-


def response_wrapper(fn):
    def _wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return _wrapper
