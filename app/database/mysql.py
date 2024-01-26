from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

import os

DB_ORM_CONFIG = {
    'connections': {
        'base': {
            'engine': 'tortoise.backends.mysql',
            'credentials': {
                'host': 'localhost',
                'user': 'root',
                'password': '123456',
                'port': 3306,
                'database': 'fast'
            }
        }
    },
    'apps': {
        'base': {'models': ['models.base', 'models.sites', 'aerich.models'], 'default_connection': 'base'}
    },
    'use_tz': False,
    'timezone': 'Asia/Shanghai'
}


async def register_mysql(app: FastAPI):
    register_tortoise(
        app,
        config=DB_ORM_CONFIG,
        generate_schemas=True,
        add_exception_handlers=False,

    )
