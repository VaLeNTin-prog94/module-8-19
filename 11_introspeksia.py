import sys
from pprint import pprint


def introspection_info(obj):
    a = {'type': type(obj), 'attributes': dir(introspection_info),
         'methods': list(dir(obj)), 'module': __name__}
    return a


number_info = introspection_info(42)
pprint(number_info)
