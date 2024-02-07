#!/usr/bin/python3
"""Module
Reads a file and print
"""


def read_file(filename=""):
    """Reads filename and prints
    to stdout.

    Args:
        - filename: name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")i
