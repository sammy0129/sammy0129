from datetime import datetime
from pydantic import BaseModel
from typing import Optional, List


class CreateUser(BaseModel):
    username: str
    password: str



    class Config:
        from_attributes = True


class UserInfo(BaseModel):
    username: str
    avatar: str

    class Config:
        from_attributes = True
