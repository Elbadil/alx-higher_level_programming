#!/usr/bin/python3
"""Python scrpt that sends a request to a URL and displays the value
of X-Request-Id"""
from urllib import request
from sys import argv

if __name__ == "__main__":
    with request.urlopen(argv[1]) as resp:
        headers = resp.headers
        for header, value in headers.items():
            if header == "X-Request-Id":
                print(headers[header])
