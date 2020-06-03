#!/usr/bin/python3
"""save to json file"""


import json


def save_to_json_file(my_obj, filename):
    """save to json file"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
