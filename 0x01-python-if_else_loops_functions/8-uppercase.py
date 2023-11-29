#!/usr/bin/python3

def uppercase(s):

    for a in s:
        if ord(a) >= 97 and ord(a) <= 122:
            a = chr(ord(a) - 32)
        print("{}".format(a), end="")
    print("")
