#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:09:17 2022
@author: Biruke Sisay
         Phillip Kyule
"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class inherits from BaseModel
    Attributes:
        name (str): Public class attribute for City's name
        state_id (str): Public class attribute for City's state_id
    """
    state_id = ""
    name = ""
