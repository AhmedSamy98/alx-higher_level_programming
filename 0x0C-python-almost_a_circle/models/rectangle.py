#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
import sys
from models.base import Base
sys.path.append("..")

if __name__ == "__main__":
    """ Do Not run Dirctly """


class Rectangle(Base):
    """ This is a child class that would inherit from The base class """
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ This is the width getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the width setter """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ This is the height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the height setter """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ This is x getter func """
        return self.__x

    @x.setter
    def x(self, value):
        """ This is x setter func """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ This is y getter func """
        return self.__y

    @y.setter
    def y(self, value):
        """ This is y setter func """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ This would return the Area of the rectangle """
        return self.height * self.width

    def display(self):
        """ this would Display the instance of the Rectangle """
        for space in range(self.__y):
            print("")
        for row in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for items in range(self.__width):
                print("#", end="")
            print("")

    def __str__(self):
        """ This function overrides the __str__ call """
        return f"[Rectangle] ({self.id})" \
               f" {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ This function Updates The class/instance attr """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
        if len(args) > 1:
            if args[1] is not None:
                self.__width = args[1]
        if len(args) > 2:
            if args[2] is not None:
                self.__height = args[2]
        if len(args) > 3:
            if args[3] is not None:
                self.__x = args[3]
        if len(args) > 4:
            if args[4] is not None:
                self.__y = args[4]
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'width':
                    self.__width = value
                elif key == 'height':
                    self.__height = value
                elif key == 'x':
                    self.__x = value
                elif key == 'y':
                    self.__y = value

    def to_dictionary(self):
        """ will return a dictionary containing all the attributer """
        diction = {
                'x': self.__x,
                'y': self.__y,
                'id': self.id,
                'height': self.__height,
                'width': self.__width
                }
        return diction
