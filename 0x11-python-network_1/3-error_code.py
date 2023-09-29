#!/usr/bin/python3
"""Python script that sends a request to a URL and manages errors"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        data = resp.read()
        data_decoded = data.decode("UTF-8")
