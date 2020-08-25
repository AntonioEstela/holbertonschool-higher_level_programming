#!/usr/bin/python3
"""
Get the 10 most recent commits from the repository specified
"""


import sys
import requests
if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repository)

    req = requests.get(url)

    reqjson = req.json()

    try:
        if not reqjson or reqjson.get('message') == 'Not Found':
            print('Not Found')
            exit()

    except AttributeError:
        pass

    for count, commit in enumerate(reqjson):
        if count == 10:
            break

        print('{}: {}'.format(commit.get('sha'), commit.get(
            'commit').get('author').get('name')))
