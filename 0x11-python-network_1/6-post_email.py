#!/usr/bin/python3
"""
script that takes in a URL and an email address
"""

if __name__ == "__main__":
    import requests
    import sys
    pyl = {"email": sys.argv[2]}
    response = requests.post(sys.argv[1], data=pyl)
    print(response.text)
