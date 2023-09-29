#!/usr/bin/python3
"""Python script that sends a request to a URL and manages errors"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as resp:
            data = resp.read()
            data_decoded = data.decode("UTF-8")
            print(data_decoded)
    except urllib.error.HTTPError as e:
        print(e.code)
