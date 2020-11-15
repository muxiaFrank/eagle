#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-23 
"""
from pydantic import BaseModel

class Item(BaseModel):
    id: int
    quantity: int
    price: float
