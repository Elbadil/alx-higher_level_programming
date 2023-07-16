#!/usr/bin/python3
"""Defining a class called Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format("width"))

        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))

        self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format("height"))

        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))

        self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format("x"))

        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))

        self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if not type(value) == int:
            raise TypeError("{} must be an integer".format("y"))

        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))

        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """string representation of a Rectangle"""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y "
        "- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """assigns a key/value argument to attributes"""
        attributes = [self.id, self.width, self.height, self.x, self.y]
        if args and len(args) != 0:
            for i, arg in enumerate(args[:5]):
                attributes[i] = arg
            self.id, self.width, self.height, self.x, self.y = attributes

        elif kwargs and len(kwargs) != 0:
            for attr, value in kwargs.items():
                setattr(self, attr, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {"x": self.x, "y": self.y, "id": self.id,
                "height": self.height, "width": self.width}
