#!/usr/bin/python3
def uppercase(str):
    for x in str:
        up = ord(x)
        if up >= 97 and up <= 122:
            up -= 32
            print("{:c}".format(up), end='')
        print()
