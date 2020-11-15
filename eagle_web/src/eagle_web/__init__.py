#!/usr/bin/python
# -*- coding: UTF-8 -*-
""" 
@author: Muxia
@time: 2020-10-22 
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .router import router
from .worker import celery_app


def get_app() -> FastAPI:
    app = FastAPI(title="EAGLE WEB")

    origins = [
        "http://localhost.tiangolo.com",
        "https://localhost.tiangolo.com",
        "http://localhost",
        "http://localhost:8080",
    ]

    # 开启cors（跨源资源共享）
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # 500字节以上才开启gzip
    app.add_middleware(
        GZipMiddleware,
        minimum_size=500
    )

    # # 添加中间件计算程序运行时间
    # @eagle_web.middleware("http")
    # async def add_process_time_header(request: Request, call_next):
    #     start_time = time.time()
    #     response = await call_next(request)
    #     process_time = time.time() - start_time
    #     response.headers["X-Process-Time"] = str(process_time)
    #     mylogger.info(process_time)
    #     return response

    app.include_router(router, prefix="/api")

    # # 添加数据库连接和关闭事件
    # @eagle_web.on_event("startup")
    # async def startup():
    #     # eagle_web.start(argv=['celery', 'worker', '--eagle_web=code.worker.eagle_web', '-l', 'info'])
    #     import asyncio
    #     asyncio.create_task(celery_app.start(argv=['celery', 'worker', '--eagle_web=code.worker.celery_app', '-l', 'info']))
    #
    #     # await celery_app.start(argv=['celery', 'worker', '--eagle_web=code.worker.celery_app', '-l', 'info'])
    # #
    # @eagle_web.on_event("shutdown")
    # async def shutdown():
    #     await celery_app.close()

    return app