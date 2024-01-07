from typing import List
from pydantic_settings import BaseSettings
import os


class Config(BaseSettings):
    APP_DEBUG: bool = True
    VERSION: str = '0.0.1'
    PROJECT_NAME: str = 'fast_demo'
    DESCRIPTION: str = 'fast_demo'
    STATIC_DIR: str = os.path.join(os.getcwd(), './static')
    TEMPLATES_DIR: str = os.path.join(os.getcwd(), './templates')
    CORS_ORIGINS: List[str] = ['*']
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: List[str] = ['*']
    CORS_ALLOW_HEADERS: List[str] = ['*']
    SECRET_KEY: str = 'session'
    SESSION_COOKIE: str = 'session_id'
    SESSION_MAX_AGE: int = 14 * 24 * 60 * 60
    JWT_EXPIRE_TIME: int = 60 * 24 * 7
    JWT_SECRET_KEY: str = '74548109c4688c3260a0b01f486035545dc48c7202708b369ee284f84e5bf5f2'


settings = Config()
