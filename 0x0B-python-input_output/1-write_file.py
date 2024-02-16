#!/usr/bin/python3
"""Module 1-write_file.
"""


def write_file(filename="", text=""):
    """Writes text in filename.
    Args:
        filename: name of the file
        text: string to write in the file
    Returns: number of characters written
    """

    with open(filename, 'w+') as f:
        return f.write(text)