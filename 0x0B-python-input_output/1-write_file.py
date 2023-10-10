#!/usr/bin/python3
"""
    Module: write_file
"""


def write_file(filename="", text=""):
    """Write a string to a text file"""

    wrote = 0

    with open(filename, "w", encoding="utf-8") as f:
        wrote = f.write(text)

    return wrote
