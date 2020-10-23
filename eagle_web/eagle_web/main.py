#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-22 
"""
import uvicorn

from eagle_web.eagle_web.app import get_app

app = get_app()

if __name__ == '__main__':
    # uvicorn.run(app, host="0.0.0.0", port=8000)
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001)