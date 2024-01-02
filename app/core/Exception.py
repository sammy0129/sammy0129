from fastapi import HTTPException, Request, status
from fastapi.responses import JSONResponse
from typing import Union
from fastapi.exceptions import RequestValidationError
from pydantic import ValidationError


async def http_error_handler(_: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=dict(code=exc.status_code, message=exc.detail, data=exc.detail)
    )


class UnicornException(Exception):
    def __init__(self, code, message, data=None):
        if data is None:
            data = {}
        self.code = code
        self.message = message
        self.data = data


async def unicorn_exception_handler(_: Request, exc: UnicornException):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=dict(code=exc.code, message=exc.message, data=exc.data)
    )

