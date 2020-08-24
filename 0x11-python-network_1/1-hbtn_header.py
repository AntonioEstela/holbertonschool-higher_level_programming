#!/usr/bin/python3
from sys import argv
import urllib.request

url = argv[1]

with urllib.request.urlopen(url) as response:
    headers = response.headers

print(headers['X-Request-Id'])
