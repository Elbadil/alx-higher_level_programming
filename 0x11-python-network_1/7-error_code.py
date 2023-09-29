#!/usr/bin/python3
"""Python script that sends a request to a URL, displays the body of the reponse
and handles errors"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        req = requests.get(argv[1])
        print(req.text)
    except requests.HTTPError as e:
        print(e.status_code)
