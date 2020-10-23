#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-22 
"""
from fastapi import APIRouter

from eagle_web.eagle_web.app.api.v1.items import router as router_item

router = APIRouter()

router.include_router(router_item, tags=["items"], prefix="/items")
