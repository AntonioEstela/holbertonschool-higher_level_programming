#!/usr/bin/python3
import sys
import urllib.request

url = sys.argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers

print(headers['X-Request-Id'])
