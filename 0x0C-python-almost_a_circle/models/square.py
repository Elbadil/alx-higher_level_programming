#!/usr/bin/python3
"""Defining a class called Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def __str__(self):
        """string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        attributes = [self.id, self.size, self.x, self.y]
        if args and len(args) != 0:
            for i, arg in enumerate(args[:4]):
                attributes[i] = arg
            self.id, self.size, self.x, self.y = attributes

        elif kwargs and len(kwargs) != 0:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """that returns the dictionary representation of a Square"""
        return {"id": self.id, "x": self.x, "size": self.size,
                "y": self.y}
