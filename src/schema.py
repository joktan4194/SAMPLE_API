from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str

class UserList(BaseModel):
    user_me: str

class CreateUser(BaseModel):
    id: int
    name: str
    


class User(UserBase):
    id: int
    name: str

    class Config:
        orm_mode = True
