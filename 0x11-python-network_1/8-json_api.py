#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST\
 request to http://0.0.0.0:5000/search_user\
 with the letter as a parameter."""

import sys
import requests

if __name__ == '__main__':

    try:
        letter = sys.argv[1]
    except IndexError:
        letter = ""

    url = 'http://0.0.0.0:5000/search_user'
    value = {'q': letter}

    req = requests.post(url, value)

    try:
        reqjson = req.json()
        if reqjson == {}:
            print('No result')
        else:
            print('[{}] {}'.format(reqjson.get('id'), reqjson.get('name')))
    except ValueError:
        print('Not a valid result')
