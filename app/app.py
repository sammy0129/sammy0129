import os

from starlette.middleware.cors import CORSMiddleware
from core.Router import AllRouter
from config import settings
from fastapi import FastAPI, HTTPException
from core.Event import startup, stopping
from core.Exception import http_error_handler, unicorn_exception_handler
from core.Middleware import BaseMiddleware
from fastapi.exceptions import RequestValidationError
from starlette.middleware.sessions import SessionMiddleware

import uvicorn

application = FastAPI(
    debug=settings.APP_DEBUG,
    description=settings.DESCRIPTION,
    version=settings.VERSION,
    title=settings.PROJECT_NAME
)


# event_handler
application.add_event_handler('startup', startup(application))
application.add_event_handler('shutdown', stopping(application))

# exception_handler
application.add_exception_handler(HTTPException, http_error_handler)
application.add_exception_handler(RequestValidationError, http_error_handler)


# add_middleware
application.add_middleware(
    BaseMiddleware,
)

application.add_middleware(
    SessionMiddleware,
    secret_key=settings.SECRET_KEY,
    session_cookie=settings.SESSION_COOKIE,
    max_age=settings.SESSION_MAX_AGE,

)

application.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=settings.CORS_ALLOW_CREDENTIALS,
    allow_methods=settings.CORS_ALLOW_HEADERS,
    allow_headers=settings.CORS_ALLOW_HEADERS,
)




# routers
application.include_router(AllRouter)


if __name__ == '__main__':
    uvicorn.run('app:application', reload=True)
