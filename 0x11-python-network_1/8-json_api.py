#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) < 2:
        req = requests.post(url, data={"q": ""})
    else:
        req = requests.post(url, data={"q": argv[1]})

    data_json = req.json()
    if type(data_json) != dict:
        print("Not a valid JSON")
    else:
        if len(data_json) == 0:
            print("No result")
        else:
            print(f"[{data_json['id']}] {data_json['name']}")
