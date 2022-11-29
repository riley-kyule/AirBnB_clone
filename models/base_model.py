#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Creation date: Nov 25, 2022
Authors: Biruke sisay
        Phillip Kyule
"""
from uuid import uuid
from datetime import datetime


class BaseModel:
    """
    base_model that defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):

        """init method for BaseModel Class
        Attributes:
            args (list): inputted arguments as a list.
            kwargs (dict): inputted arguments as a dict.
            id (str) - assign with an uuid when an instance is created.
            created_at (time): datetime - assign with the current datetime when
                an instance is created.
            updated_at (time): datetime - assign with the current datetime when
                n instance is created and it will be updated every time you
                change your object.
        """

        from models import storage
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ('created_at', 'updated_at'):
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)
    def __str__(self):
        """
        String Rep of a BaseModel Object
            Return:
                string (str): string descriptor for BaseModel Class
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """

        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        of the instance
        Return:
            dictionary (dict): Dictionary object that contains __dict__
        """

        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if k in ("created_at", "updated_at"):
                v = self.__dict__[k].isoformat()
                dict_1[k] = v
        retuen dict_1
