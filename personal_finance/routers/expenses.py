from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlmodel import Session, select

from ..db import get_session, engine
from ..models import Expense, Category
from ..schemas import ExpenseCreate
from ..auth import get_current_user

router = APIRouter(prefix="/expenses", tags=["expenses"])


@router.post("/", response_model=dict)
def create_expense(payload: ExpenseCreate, user=Depends(get_current_user)):
    with Session(engine) as session:
        exp = Expense(user_id=user.id, amount=payload.amount, description=payload.description, date=payload.date or None, category_id=payload.category_id)
        session.add(exp)
        session.commit()
        session.refresh(exp)
        return {"id": exp.id}


@router.get("/", response_model=List[dict])
def list_expenses(user=Depends(get_current_user)):
    with Session(engine) as session:
        expenses = session.exec(select(Expense).where(Expense.user_id == user.id)).all()
        return [ {"id": e.id, "amount": e.amount, "description": e.description, "date": str(e.date)} for e in expenses ]
