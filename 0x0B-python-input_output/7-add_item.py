#!/usr/bin/python3
import sys
import os.path

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    elements = []

    if os.path.isfile("add_item.json"):
        elements = load_from_json_file("add_item.json")

    args = len(sys.argv) - 1
    for i in range(args):
        elements.append(sys.argv[i + 1])
    save_to_json_file(elements, "add_item.json")
