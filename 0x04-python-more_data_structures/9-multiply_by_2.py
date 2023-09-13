#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    newDir = a_dictionary.copy()
    listKeys = list(newDir.keys())
    for i in listKeys:
        newDir[i] *= 2
    return (newDir)
