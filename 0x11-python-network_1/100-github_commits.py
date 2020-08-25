#!/usr/bin/python3
"""Python script that lists 10 commits (from the most recent to oldest) \
from a given repository of a given user in github"""

import sys
import requests

if __name__ == "__main__":

    repository = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        owner, repository)

    req = requests.get(url)
    reqjson = req.json()

    for commit in reqjson[:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get(
            'commit').get('author').get('name')))
