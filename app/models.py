from pydantic import BaseModel
from typing import Optional

class Item(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    description: Optional[str] = None

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: str
    active: bool = True
