#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user with the letter
as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if argv[1]:
        req = requests.post(url, data={"q": argv[1]})
    else:
        req = requests.post(url, data={"q": ""})
    
    try:
        data_json = req.json()
        if len(data_json) == 0:
            print("No result")
        else:
            print(data_json)

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
