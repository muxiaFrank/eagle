#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-22 
"""
from fastapi import APIRouter

router = APIRouter()
from gino_fastapi_demo.tasks.task import process_item
from gino_fastapi_demo.items.demo_items import Item

@router.post("/items")
async def add_item(item: Item):
  process_item.delay(id=item.id, price=item.price, quantity=item.quantity)

  return {"message": "Item received"}
