#!/usr/bin/python3
"""Write a Python script that takes in a letter and sends a POST\
 request to http://0.0.0.0:5000/search_user \
with the letter as a parameter."""

import sys
import requests

if __name__ == "__main__":

    if len(sys.argv) == 1:
        letter = ""

    else:
        letter = sys.argv[1]

    req = requests.post("http://0.0.0.0:5000/search_user", data={"q": letter})

    try:
        reqjson = req.json()
        if reqjson:
            print("[{}] {}".format(reqjson["id"], reqjson["name"]))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
