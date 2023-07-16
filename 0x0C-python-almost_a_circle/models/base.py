#!/usr/bin/python3
"""Defining a class called Base"""
import json
import os


class Base:
    """Class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="utf-8") as JsonFile:
            if list_objs is None:
                JsonFile.write("[]")
            else:
                dict_list = [obj.to_dictionary() for obj in list_objs]
                JsonFile.write(Base.to_json_string(dict_list))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy_inst = cls(1)
        if cls.__name__ == "Rectangle":
            dummy_inst = cls(1, 1)

        dummy_inst.update(**dictionary)
        return dummy_inst

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filname = cls.__name__ + ".json"
        if not os.path.exists(filname):
            return []

        with open(filname, "r", encoding="utf-8") as File:
            json_data = File.read()

        data_list = cls.from_json_string(json_data)
        instances_list = [cls.create(**attr) for attr in data_list]
        return instances_list
