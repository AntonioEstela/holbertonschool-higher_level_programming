#!/usr/bin/python3
"""Script that takes URL and a email, sends POST reques tto the URL"""

import requests
from sys import argv

if __name__ == "__main__":
    if len(argv) == 1:
        q = ""
    else:
        q = argv[1]

    res = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})

    try:
        data = res.json()
        if data:
            print("[{}] {}".format(data["id"], data["name"]))
        else:
            print("No result")
    except:
        print("Not a valid JSON")
