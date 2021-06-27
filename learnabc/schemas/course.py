from learnabc.database import Base
from typing import List, Optional
from pydantic import BaseModel
from .base import User


class RequestCourse(BaseModel):
    name: str
    description: str

    class Config():
        orm_mode = True


class InscriptionUser(BaseModel):
    user: User

    class Config():
        orm_mode = True


class ShowCourse(BaseModel):
    id: int
    name: str
    description: str
    creator: User
    inscriptions: List[InscriptionUser] = []

    class Config():
        orm_mode = True


class CalificationRequest(BaseModel):
    calification: int
