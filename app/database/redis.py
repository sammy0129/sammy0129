import aioredis
import os
from aioredis import Redis


async def sys_cache() -> Redis:
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f'redis://localhost:6379',
        db=0,
        encoding='utf8',
        decode_responses=True
    )
    return Redis(connection_pool=sys_cache_pool)


async def code_cache() -> Redis:
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f'redis://localhost:6379',
        db=1,
        encoding='utf8',
        decode_responses=True
    )
    return Redis(connection_pool=sys_cache_pool)