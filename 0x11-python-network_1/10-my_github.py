#!/usr/bin/python3
"""Python script that takes your Github credentials (username and password) \
and uses the Github API to display your id"""

import sys
import requests

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]

    req = requests.get('https://api.github.com/user', auth=(username, password))
    reqjson = req.json()
    print(reqjson.get('id'))
