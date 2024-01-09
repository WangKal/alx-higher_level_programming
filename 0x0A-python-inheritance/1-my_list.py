#!/usr/bin/python3
"""
defines class mylist
"""
class MyList(list):
    """ mylist class """
    def print_sorted(self):
        """ print sorted func """
        print(sorted(self))
