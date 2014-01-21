# -*- coding: utf-8 -*-

"""
Sample API module
"""

import logging

from flask import request

from gaffer.api.base import GafferAPIBase


def dispatch():
    """
    Return APIHandler object
    """
    def sample1():
        return "Sample 1"

    def sample2():
        return "Sample 2"

    return GafferAPIBase({'sample1': sample1,
        'sample2': sample2},
        'Sample API',
        'v1')
