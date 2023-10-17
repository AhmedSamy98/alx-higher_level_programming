#!/usr/bin/python3
"""
    Module: Base Class
"""

import json
import csv
import turtle


class Base:
    """
        The base model

        Attributes:
            __nb_objects (int): The number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initialize Base Class Objects

            Args:
                id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
            Write the JSON serialization of a list of objects to a file.

            Args:
                list_objs (list): A list of inherited Base instances.
        """

        filename = cls.__name__ + ".json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """
            Returns list of the JSON string representation
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
            Return a class instantied from a dictionary of attributes

            Args:
                **dictionary (dict): Key/value pairs of attribute to init
        """

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)

            return new

    @classmethod
    def load_from_file(cls):
        """
            Return a list of classes instantiated from a file of JSON strings

            Reads from `<cls.__name__>.json`

            Returns:
                If the file does not exist - an empty list
                Otherwise - a list of instantiated classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            Serializes in CSV
        """

        fname = cls.__name__ + ".csv"

        if list_objs is None:
            with open(fname, "w") as cfile:
                cfile.write("[]")
        else:
            with open(fname, "w") as cfile:
                writer = csv.writer(cfile)
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == "Square":
                        writer.writerow([obj.id, obj.width, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """
            Return a list of classes instantiated from a CSV file

            Reads from `<cls.__name__>.csv`

            Returns:
                If the file does not exist - an empty list
                Otherwise - a list of instantiated classes
        """

        filename = cls.__name__ + ".csv"

        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
            Draw Rectangle and Square
        """
        t = turtle.Turtle()
