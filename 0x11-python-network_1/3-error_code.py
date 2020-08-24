#!/usr/bin/python3
"""Python script that takes in a URL, sends a request to\
 the URL and displays the body of the response."""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    try:
        with urllib.request.urlopen(req) as request:
            print(request.read().decode('utf-8'))

    except urllib.error.HTTPError as error:
        print('Error code: {}'.format(error.code))
