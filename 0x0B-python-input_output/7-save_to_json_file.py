#!/usr/bin/python3
import json


"""save to json file"""


def save_to_json_file(my_obj, filename):
    """save to json file"""

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
