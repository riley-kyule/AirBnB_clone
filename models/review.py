#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 08:23:07 2022
@author: Biruke Sisay
         phillip kyule
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class inherits from BaseModel
    Attributes:
        place_id (str): Public class attribute for Review's place_id
        user_id (str): Public class attribute for Review's user_id
        text (str): Public class attribute for Review's text
    """
    place_id = ""
    user_id = ""
    text = ""
