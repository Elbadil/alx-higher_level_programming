#!/usr/bin/python3
"""Python script that sends a POST request to the passed URL
with an email as parameter"""
from urllib import request, parse
from sys import argv


if __name__ == "__main__":
    # Defining the data to post
    emails = {'email': argv[2]}

    # Encoding the data for the POST request
    data = parse.urlencode(emails).encode("utf-8")

    # Creating a request object
    req = request.Request(argv[1], data=data, method="POST")

    # Sending the POST request
    with request.urlopen(req) as resp:
        resp_data = resp.read().decode("utf-8")
        print(resp_data)
