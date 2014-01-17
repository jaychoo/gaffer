from gaffer.api.base import APIHandler

def dispatch():
    def sample1():
        return "Sample 1"
    def sample2():
        return "Sample 2"
    return APIHandler({'sample1': sample1,
        'sample2': sample2}, 
        'Sample API',
        'v1')