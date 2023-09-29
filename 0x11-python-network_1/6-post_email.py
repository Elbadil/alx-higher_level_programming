#!/usr/bin/python3
"""Python script thet sends a POST request to the Passed URL
with an email as parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    req_post = requests.post(argv[1], data={'email': argv[2]})
    req_get = requests.get(argv[1])
    print(req_get.text)
