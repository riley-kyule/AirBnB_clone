#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 13:56:04 2022
@authors: Phillip Kyule
          Biruke sisay
"""
import json

from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    FileStorage class for serializing and deserializing objects into and from
    files.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns dict objects
        """
        return self.__objects

    def new(self, obj):
        """
        set `obj` with <obj class name>.id key in __objects
        """
        
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serialize __objects to JSON file
        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {}
            for k, v in self.__objetcs.items():
                dict_storage[k] = v.to_dict()
            json.dump(dict_storage, f)

    def reload(self):
        """
        deserializes JSON file to __objects if it exists
        """

        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            return
