#!/usr/bin/python3
"""
takes your GitHub credentials
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'https://api.github.com/user'
    re = requests.get(url, auth=(argv[1], argv[2])).json()

    print(re.get('id'))
