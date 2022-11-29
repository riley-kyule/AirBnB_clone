#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:26:07 2022
@author: Biruke Sisay
         Phillip Kyule
"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class inherits from BaseModel
    Attribute:
        name (str): Public class attribute for State's name
    """
    name = ""
