#!/usr/bin/python3
# -*- encoding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
import sys
from models.rectangle import Rectangle
sys.path.append("..")

if __name__ == "__main__":
    """ Do Not run Dirctly """


class Square(Rectangle):
    """ This is a child class that would inherit from The base class """
    def __init__(self, size, x=0, y=0, id=None):
        """ This is the __init__ function """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Getter for Size """
        return self.width

    @size.setter
    def size(self, value):
        """ This is Size setter """
        self.width = value
        self.height = value

    def __str__(self):
        """ This function overrides the __str__ call """
        return f"[Square] ({self.id})" \
               f" {self.x}/{self.y} - {self.height}"

    def update(self, *args, **kwargs):
        """ This function Updates The class/instance attr """
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
        if len(args) > 1:
            if args[1] is not None:
                self.width = args[1]
                self.height = args[1]
        if len(args) > 2:
            if args[2] is not None:
                self.x = args[2]
        if len(args) > 3:
            if args[3] is not None:
                self.y = args[3]
        if len(kwargs) > 0:
            for key, value in kwargs.items():
                if key == 'id':
                    self.id = value
                elif key == 'size':
                    self.width = value
                    self.height = value
                elif key == 'x':
                    self.x = value
                elif key == 'y':
                    self.y = value

    def to_dictionary(self):
        """ This is a dictionary function """
        diction = {
                'id': self.id,
                'size': self.width,
                'x': self.x,
                'y': self.y
                }
        return diction
