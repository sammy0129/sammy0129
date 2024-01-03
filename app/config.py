from typing import List
from pydantic import BaseSettings
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


settings = Config()
