# -*- coding: utf-8 -*-

"""
GafferAPI module template
"""

import logging

from flask import request

from gaffer.api.base import GafferAPIBase
from gaffer.api.utils import get_dispatch


def dispatch():
    """
    Return GafferAPIBase instance

    e.g.

    def product_name():
        return 'Product V1'

    api_fns = [product_name]
    return GafferAPIBase(get_dispatch(api_fns), 'Sample API', 'v1')

    """
    return None
