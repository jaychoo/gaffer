# -*- coding: utf-8 -*-

"""
Sample API module
"""

from gaffer.api.base import APIHandler

def dispatch():
    """
    Return APIHandler object
    """
    def sample1():
        return "Sample 1"
    def sample2():
        return "Sample 2"
    return APIHandler({'sample1': sample1,
        'sample2': sample2}, 
        'Sample API',
        'v1')