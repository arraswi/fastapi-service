from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
import jwt
import os

app = FastAPI(title="FastAPI Service", version="2.0.0", docs_url="/docs")

security = HTTPBearer()
SECRET_KEY = os.environ.get("SECRET_KEY", "")
if (
    len(SECRET_KEY.strip().encode("utf-8")) < 32
    or SECRET_KEY.strip() in {"your-secret-key", "your-secret-key-here"}
):
    raise RuntimeError(
        "Set SECRET_KEY to a unique random value of at least 32 bytes."
    )

class Item(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    description: Optional[str] = None
    created_at: Optional[datetime] = None

class User(BaseModel):
    username: str
    email: str
    active: bool = True

items = []
users = []

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = jwt.decode(credentials.credentials, SECRET_KEY, algorithms=["HS256"])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Invalid token")

@app.get("/", tags=["Root"])
async def root():
    return {"message": "FastAPI Service Running", "version": "2.0.0"}

@app.get("/items", response_model=List[Item], tags=["Items"])
async def get_items():
    return items

@app.post("/items", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: Item):
    item.id = len(items) + 1
    item.created_at = datetime.now()
    items.append(item)
    return item

@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, updated: Item):
    for i, item in enumerate(items):
        if item.id == item_id:
            updated.id = item_id
            updated.created_at = item.created_at
            items[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}", tags=["Items"])
async def delete_item(item_id: int):
    for i, item in enumerate(items):
        if item.id == item_id:
            items.pop(i)
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")

@app.post("/login", tags=["Auth"])
async def login(username: str, password: str):
    token = jwt.encode({"sub": username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}
