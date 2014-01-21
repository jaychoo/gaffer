# -*- coding: utf-8 -*-

"""
GafferAPI module template
"""

import logging

from flask import request

from gaffer.api.base import GafferAPIBase
from gaffer.api.utils import get_dispatch


def dispatch():
    return GafferAPIBase({}, 'Gaffer', 'v1')
