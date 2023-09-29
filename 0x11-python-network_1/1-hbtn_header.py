#!/usr/bin/python3
"""Python scrpt that sends a request to a URL and displays the value
of X-Request-Id"""
import urllib.request
import sys


with urllib.request.urlopen(sys.argv[1]) as resp:
    headers = resp.headers
    for header, value in headers.items():
        if header == "X-Request-Id":
            print(headers[header])
