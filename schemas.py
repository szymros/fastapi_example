from typing import List, Optional
from pydantic import BaseModel


class ItemBase(BaseModel):  # reading from json schema
    name: str
    qty: int

class ItemCreate(ItemBase): # creating schema
    pass

class Item(ItemBase): # reading from api schema
    id: int
    user_id: int

    class Config:
        orm_mode = True
        # orm_mode allows pydantic to read data not only by accesing it like its a dict ex: Dict[key]
        # but also as a object ex: Object.key


class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    items: List[Item] = []

    class Config:
        orm_mode = True
