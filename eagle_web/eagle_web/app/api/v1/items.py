#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-22 
"""
from typing import Optional, List, Tuple, Dict, Set
from pydantic import BaseModel, validator, root_validator, Field, HttpUrl, EmailStr
from pydantic.errors import PydanticValueError
from fastapi import APIRouter, HTTPException, Query, Path, Body, Header, Cookie, Form, File, UploadFile, BackgroundTasks

router = APIRouter()
from eagle_web.eagle_web.app.item.demo_items import Item
from eagle_web.eagle_web.app.tasks.demo_tasks import process_item

@router.post("/items")
async def add_item(item: Item):
  print(333333333333)
  return {"message": "Item received"}
