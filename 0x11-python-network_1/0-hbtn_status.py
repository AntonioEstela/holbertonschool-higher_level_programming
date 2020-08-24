#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    content = response.read()
    utf8_content = content.decode('utf-8')

print('Body response:')
print('\t- type: {}'.format(type(content)))
print('\t- content: {}'.format(content))
print('\t- utf8 content: {}'.format(utf8_content))
