import aioredis
import os
from aioredis import Redis


async def sys_cache() -> Redis:
    sys_cache_pool = aioredis.ConnectionPool.from_url(
        f'redis://localhost:3679',
        db=0,

    )