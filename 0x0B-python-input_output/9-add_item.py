#!/usr/bin/python3
"""asdasdas"""


import os.path
import sys

save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file

args = sys.argv[1:]

nl = []

if os.path.exists('./add_item.json'):
    nl = load('add_item.json')

save(nl + args, 'add_item.json')
