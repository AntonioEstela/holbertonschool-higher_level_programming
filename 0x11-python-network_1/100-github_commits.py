#!/usr/bin/python3
"""
Get the 10 most recent commits from the repository specified
"""

if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = 'https://api.github.com/repos/{}/{}/commits'.format(argv[2], argv[1])

    try:
        req = get(url)
        j = req.json()
        for commit in j[:10]:
            print('{}: {}'.format(commit.get('sha'),
                                  commit.get('commit')
                                  .get('author')
                                  .get('name')))
    except IndexError as err:
        print(err)