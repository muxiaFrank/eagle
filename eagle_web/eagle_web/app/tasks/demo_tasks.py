#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-23 
"""

from eagle_web.eagle_web.app.worker import celery_app
from celery import current_task


@celery_app.task(acks_late=True)
def process_item(id: int,quantity: int, price: float) -> str:
    # for i in range(1, 11):
    current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': 10})

    print(333333333333)
    return f"finished processing item: {id} | {quantity} | {price}"