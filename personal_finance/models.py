from __future__ import annotations

from sqlmodel import SQLModel, Field


class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    email: str | None = None
    hashed_password: str


class Category(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)


class Expense(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    category_id: int | None = Field(default=None, foreign_key="category.id")
    amount: float
    description: str | None = None


class Budget(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    month: str  # YYYY-MM
    amount: float
    category_id: int | None = Field(default=None, foreign_key="category.id")
