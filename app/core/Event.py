from typing import Callable
from fastapi import FastAPI


def startup(app: FastAPI) -> Callable:
    async def app_start() -> None:
        print('服务启动完毕')
        pass
    return app_start


def stopping(app: FastAPI) -> Callable:
    async def app_stop() -> None:
        print('服务已停止')
        pass
    return app_stop
