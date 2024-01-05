from datetime import datetime
from pydantic import Field, BaseModel, validator
from typing import Optional, List


class CreateUser(BaseModel):
    username: str = Field(min_length=3, max_length=15)
    password: str = Field(min_length=6, max_length=24)
