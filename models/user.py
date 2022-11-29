#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 08:29:17 2022
@author: Biruke sisay
         phillip kyule
"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class inherits from BaseModel
    Attributes:
        email (str): Public class attribute for User's email
        password (str): Public class attribute for User's password
        first_name (str): Public class attribute for User's first name
        last_name (str): Public class attribute for User's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
