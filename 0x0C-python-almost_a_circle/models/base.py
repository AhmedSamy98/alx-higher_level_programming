#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
    This is a class module
    Author: Peter Ekwere

"""
import sys
import json
import csv
import os
sys.path.append("..")

if __name__ == "__main__":
    """ Do not run Directly """


class Base:
    """ This is a base class that would serve as a super class """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ will return a json string representation of list_dict """
        if list_dictionaries is None or list_dictionaries is []:
            return "[]"
        else:
            json_string = json.dumps(list_dictionaries)
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """ will save a json string representation of list_objs to  file """
        json_list = []
        if list_objs is None or list_objs is []:
            json_list.append([])
        else:
            for object in list_objs:
                json_list.append(object.to_dictionary())
            json_string = cls.to_json_string(json_list)

        filename = f"{cls.__name__}.json"
        with open(filename, mode='w', encoding="utf-8") as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ this function converts the json string """
        if json_string is None or json_string is []:
            return []
        else:
            json_list = json.loads(json_string)
            return json_list

    @classmethod
    def create(cls, **dictionary):
        """ This is a function that creates and returns an instance """
        from models.rectangle import Rectangle
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2, 3)
        else:
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ This function loads a list from a json fil """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, mode='r', encoding='utf-8') as a_file:
                json_string = a_file.read()

            json_list = cls.from_json_string(json_string)
            a_list = []

            for diction in json_list:
                dummy = cls.create(**diction)
                a_list.append(dummy)

            return a_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ This Function converts an obj or list of objs to a csv file """
        if not list_objs:
            return []
        else:
            my_list = []
            filename = f"{cls.__name__}.csv"
            if not os.path.exists(filename):
                return
            else:
                if cls.__name__ == 'Rectangle':
                    field = ['id', 'width', 'height', 'x', 'y']
                else:
                    field = ['id', 'size', 'x', 'y']

                    for objects in list_objs:
                        my_list.append(objects.to_dictionary())

                    with open(filename, mode='w', newline='',
                              encoding='utf-8') as a:
                        content = csv.DictWriter(a, fieldnames=field)
                        content.writeheader()
                        content.writerows(my_list)

    @classmethod
    def load_from_file_csv(cls):
        """ This Function loads objects from a csv file """
        data = []
        filename = f"{cls.__name__}.csv"
        content = ""
        if not os.path.exists(filename):
            return []
        else:
            with open(filename, mode='r', encoding='utf-8') as a_file:
                content = csv.DictReader(a_file)
                conv_line = {}
                for line in content:
                    for key, value in line.items():
                        if key != 'id':
                            conv_line[key] = int(value)
                dummy = cls.create(**conv_line)
                data.append(dummy)
                return data
