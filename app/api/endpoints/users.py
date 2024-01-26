from typing import List, Optional
from tortoise.queryset import F
from models.base import *
from schemas.users import CreateUser
from fastapi import APIRouter, Request, Depends, Cookie, Response
from core.Response import err_response, ok_response
from database.redis import sys_cache
from aioredis import Redis
from schemas.users import CreateUser, UserInfo
from core.Security import encode_password, verify_password, create_access_token, verify_access_token
from fastapi.responses import JSONResponse
from config import settings


router = APIRouter(prefix='/user')


@router.post('')
async def add_user(post: CreateUser):
    get_user = await User().get_or_none(username=post.username)
    if get_user:
        return err_response(msg=f'{post.username}已存在.')
    post.password = encode_password(post.password)
    create_user = await User.create(**post.dict())

    if not create_user:
        return err_response(msg=f'{post.username}创建失败.')
    return ok_response(msg='创建成功')


@router.post('/login')
async def user_login(post: CreateUser):
    get_user = await User().get_or_none(username=post.username)
    if not get_user:
        return ok_response(data='', msg='4001')
    elif not verify_password(password=post.password, hashed_password=get_user.password):
        return ok_response(data='', msg='4001')
    else:
        jwt_token = create_access_token(data={'sub': get_user.username})
        resp = JSONResponse(
            status_code=200,
            content={
                'code': 200,
                'msg': 'login success',
                'data': UserInfo.model_validate(get_user).model_dump()
            }
        )
        resp.headers['Access-Control-Expose-Headers'] = 'X-TOKEN'
        resp.headers['X-TOKEN'] = jwt_token
        return resp


@router.get('/avatar')
async def get_avatar(path: str):
    avatar_url = settings.STATIC_DIR + '/images/avatar/' + path
    avatar = open(avatar_url, 'rb').read()
    return Response(content=avatar, status_code=200)













@router.get('/rules')
async def check_rules(request: Request, user_id: int):
    '''
    :param request:
    :param user_id:
    :return:
    '''
    user_role = await Role.filter(user__id=user_id).values('role_name')
    user_access_list = await Access.filter(role__user__id=user_id, is_check=True).values('id', 'scopes')
    print(user_access_list)
    is_pass = await Access.get_or_none(role__user__id=user_id, is_check=True, scopes='user_info', role__role_status=True)
    data = {
        'user_role': user_role,
        'pass': True if is_pass else False,
        'user_access_list': user_access_list
    }
    return ok_response(msg='用户权限', data=data)



