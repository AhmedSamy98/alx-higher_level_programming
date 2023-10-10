#!/usr/bin/python3
"""
    Module: append_write
"""


def append_write(filename="", text=""):
    """
        Appends a string at the end of a text file
    """

    appended = 0

    with open(filename, "a", encoding="utf-8") as f:
        appended = f.write(text)

    return appended
