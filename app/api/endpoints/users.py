from typing import List
from tortoise.queryset import F
from models.base import User
from schemas.users import CreateUser
from fastapi import APIRouter, Request, Depends
from core.Response import err_response, ok_response
from database.redis import sys_cache
from aioredis import Redis
from schemas.users import CreateUser

router = APIRouter(prefix='/user')


@router.post('')
async def add_user(post: CreateUser):
    get_user = await User().get_or_none(username=post.username)
    if get_user:
        return err_response(msg=f'{post.username}已存在.')
    create_user = await User.create(**post.dict())
    if not create_user:
        return err_response(msg=f'{post.username}创建失败.')
    return ok_response(msg='创建成功')


@router.get('/cache')
async def test_cache(request: Request):
    users = await User.get(username='sammy123')
    users = CreateUser.model_validate(users).model_dump_json()
    print(users)




@router.get('/cache_dependency')
async def test_depend(redis: Redis = Depends(sys_cache)):
    return await redis.get(name='test')



