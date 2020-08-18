#!/bin/bash
# Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -sIX OPTIONS "$1" | grep -e "Allow" | cut -d":" -f2 | sed -e 's/^ //'
