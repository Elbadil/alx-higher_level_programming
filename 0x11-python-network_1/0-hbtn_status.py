#!/usr/bin/python3
"""Python script that fetches a URL"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
        data = resp.read()
        print("Body response:\n\t" +
              f"- type: {type(data)}\n\t" +
              f"- content: {data}\n\t" +
              f"- utf8 content: {data.decode('UTF-8')}")
