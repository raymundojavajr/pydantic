from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional

class OrderSchema(BaseModel):
    item: str = Field(..., min_length=3, max_length=100)
    quantity: int = Field(..., gt=0)

class UserSchema(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8, max_length=128)

class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    orders: Optional[List[OrderSchema]] = []

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str
