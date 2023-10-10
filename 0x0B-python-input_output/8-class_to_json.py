#!/usr/bin/python3
"""
    Module: class_to_json
"""


def class_to_json(obj):
    """
        Function that retuns the dictionary description of an obj
    """

    result = {}
    if hasattr(obj, "__dict__"):
        result = obj.__dict__.copy()
    return result
