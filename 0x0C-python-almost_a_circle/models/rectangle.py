#!/usr/bin/python3
"""
    Module: Rectangle extends Base class
"""

from models.base import Base


class Rectangle(Base):
    """
        Class: Rectangle extends  Base class

        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Init Rectangle instance

            Args:
                width: width of the rectangle
                height: height of the rectangle
                x: x coordinate of the rectangle
                y: y coordinate of the rectangle
                id: id of the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            Getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Setter for width
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @property
    def height(self):
        """
            Getter for height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            Setter for height
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            Getter for x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            Setter for x
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """
            Getter for y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            Setter for y
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value

    def area(self):
        """
            Returns area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
            Prints rectangle to stdout with instance "#"
        """
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """
            Returns a string format of the rectangle class
        """
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.__x, self.__y,
                                                self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
            Assigns key/value argument to attributes

            kwargs is skipped if args is not empty

            Args:
                *args -  variable number of no-keyword args
                **kwargs - variable number of keyworded args
        """
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return

        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """
            Returns the dict representation of Rectangle class
        """
        return {"x": self.__x,
                "y": self.__y,
                "id": self.id,
                "height": self.__height,
                "width": self.__width
                }
