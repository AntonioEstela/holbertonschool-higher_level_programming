#!/usr/bin/python3
import json


"""creating"""


def load_from_json_file(filename):
    """creating"""

    with open(filename, 'r') as f:
        content = f.read()

    return json.loads(content)
