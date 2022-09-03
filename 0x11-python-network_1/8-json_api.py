#!/usr/bin/python3
"""
takes in a letter and sends a POST
"""

if __name__ == "__main__":
    import requests
    import sys
    url = "http://0.0.0.0:5000/search_user"
    try:
        a = sys.argv[1]
    exept Exception:
        a = ""
    q = {"q": a}
    response = requests.post(url, data=q)
    try:
        result = response.json()
    except Exception:
        print("Not a valid JSON")
        exit()
    try:
        print("[{}] {}".format(result['id'], result['name']))
    except Exeption:
        print("No result")
