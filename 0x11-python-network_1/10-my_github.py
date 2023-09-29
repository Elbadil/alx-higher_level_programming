#!/usr/bin/python3
"""Python script that Takes you Github Credentials
and uses Github Api to display your id"""
import requests
from sys import argv
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = argv[1]
    password = argv[2]

    # API Github URL
    url = "https://api.github.com/user"

    # Authentication to the REST API
    authentication = HTTPBasicAuth(username=username, password=password)

    # Get request to the Github API
    req = requests.get(url, auth=authentication)
    print(req.json().get('id'))
