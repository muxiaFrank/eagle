#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-23 
"""
import os
from time import sleep
from celery import Celery, current_task



celery_app = Celery(
    "worker",
    broker="redis://127.0.0.1:6379/6"
    # include=['code.worker.celery_app']
)
celery_app.conf.task_routes = {
    "app.worker.celery_worker.queue": "items"}

celery_app.conf.update(task_track_started=True)




