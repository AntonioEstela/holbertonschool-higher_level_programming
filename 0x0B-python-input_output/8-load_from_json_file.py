#!/usr/bin/python3
"""creating"""


import json


def load_from_json_file(filename):
    """creating"""

    with open(filename, 'r') as f:
        content = f.read()

    return json.loads(content)
