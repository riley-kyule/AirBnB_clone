#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:05:17 2022
@author: Biruke sisay
         phillip kyule
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class inherits from BaseModel
    Attribute:
        name (str): Public class attribute for Amenity's name
    """
    name = ""
