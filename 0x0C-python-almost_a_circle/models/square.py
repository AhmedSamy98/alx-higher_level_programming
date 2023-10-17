#!/usr/bin/python3
"""
    Module: Square class inherits Rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class inheirts rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            Initializes the instance of Square class

            Args:
                size: size of the square
                x: x coordinate of the square
                y: y coordinate of the square
                id: id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
            Getter for size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Setter for size
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
            Assign an argument to each attribute
        """
        if args:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """
            Returns dict representation of Square Class
        """
        return {'id': getattr(self, "id"),
                'size': getattr(self, "width"),
                'x': getattr(self, "x"),
                'y': getattr(self, "y")}
