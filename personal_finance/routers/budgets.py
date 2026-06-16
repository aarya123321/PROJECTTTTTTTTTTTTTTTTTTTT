from fastapi import APIRouter, Depends
from sqlmodel import Session
from ..models import Budget
from ..auth import get_current_user
from ..db import engine

router = APIRouter(prefix="/budgets", tags=["budgets"])


@router.post("/")
def set_budget(budget: dict, user=Depends(get_current_user)):
    with Session(engine) as session:
        b = Budget(user_id=user.id, month=budget.get("month"), amount=budget.get("amount"), category_id=budget.get("category_id"))
        session.add(b)
        session.commit()
        session.refresh(b)
        return {"id": b.id}
