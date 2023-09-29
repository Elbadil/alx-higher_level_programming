#!/usr/bin/python3
"""Python script that sends a request to a URL, displays the body
of the reponse and handles errors"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        req = requests.get(argv[1])
        req.raise_for_status()
        print(req.text)
    except requests.exceptions.HTTPError as e:
        print(f"Error code: {e.response.status_code}")
