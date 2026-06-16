from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    username: str
    email: Optional[EmailStr]
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class ExpenseCreate(BaseModel):
    amount: float
    description: Optional[str]
    date: Optional[date]
    category_id: Optional[int]
