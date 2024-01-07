#!/usr/bin/python3
""" This scripts GETS a header variable """
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        value = response.headers.get('X-Request-Id')
        print(value)
