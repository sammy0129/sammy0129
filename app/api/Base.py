from fastapi import APIRouter, Request
from api.endpoints import users
router = APIRouter(prefix='/api/v1')

router.include_router(users.router, prefix='/admin', tags=['用户管理'])


@router.get('/')
async def home(request: Request):
    return 'fastapi router'
