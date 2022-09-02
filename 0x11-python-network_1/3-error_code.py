#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL
and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.error as error
    import urllib.request as request
    from sys import argv
    re = request.Request(argv[1])
    try:
        with request.urlopen(re) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.ecode))
