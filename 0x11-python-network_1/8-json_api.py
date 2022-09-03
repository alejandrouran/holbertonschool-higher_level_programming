#!/usr/bin/python3
"""
takes in a letter and sends a POST
"""

if __name__ == "__main__":
    import requests
    import sys
    let = "" if len(sys.argv) == 1 else sys.argv[1]
    pl = {"q": let}

    r = requests.post("http://0.0.0.0:5000/search_user", data=pl)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
