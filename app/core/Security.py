from datetime import timedelta, datetime
import jwt
from fastapi import HTTPException, Request, Depends, status, Header
from fastapi.security import SecurityScopes
from fastapi.security.oauth2 import OAuth2PasswordBearer
from jwt import PyJWTError
from pydantic import ValidationError
from config import settings
from models.base import User, Access
from passlib.handlers.pbkdf2 import pbkdf2_sha256


def encode_password(password: str):
    '''
    :param password:
    :return:
    '''
    password = pbkdf2_sha256.hash(password)
    return password


def verify_password(password: str, hashed_password: str) -> bool:
    '''
    :param password: 用户输入的密码
    :param hashed_password: 加密后的密码
    :return:
    '''

    verify = pbkdf2_sha256.verify(password, hashed_password)
    return verify


def create_access_token(data: dict):
    token_data = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.JWT_EXPIRE_TIME)
    token_data.update({'exp': expire})
    jwt_schema = jwt.encode(token_data, settings.JWT_SECRET_KEY,'HS256')
    return jwt_schema


async def verify_access_token(token: str = Header()):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET_KEY, algorithms='HS256')
        if payload:
            username = payload.get('sub')
            user = await User.get_or_none(username=username)
            return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='凭证已过期',
        )
    except (PyJWTError, ValidationError):
        raise  HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='无效凭证'
        )






