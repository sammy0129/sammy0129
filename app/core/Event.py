from typing import Callable
from fastapi import FastAPI
from database.mysql import register_mysql
from database.redis import sys_cache, code_cache


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        await register_mysql(app)
        app.state.cache = await sys_cache()
        app.state.code_cache = await code_cache()

        print('服务启动完毕')
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    async def app_stop() -> None:
        print('服务已停止')
        pass
    return app_stop
