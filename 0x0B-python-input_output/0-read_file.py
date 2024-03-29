#!/usr/bin/python3
"""
Reads from a file and prints.
"""


def read_file(filename=""):
    """function function that reads a text file (UTF8)
    its contents to stdout.
    Args:
        - filename: name of the file
    """

    with open(filename) as f:
        read_text = f.read()
        print(read_text, end="")
