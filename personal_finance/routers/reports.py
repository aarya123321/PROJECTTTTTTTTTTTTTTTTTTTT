from fastapi import APIRouter, Depends
from sqlmodel import Session, select, func
from ..auth import get_current_user
from ..db import engine
from ..models import Expense

router = APIRouter(prefix="/reports", tags=["reports"])


@router.get("/summary")
def summary(user=Depends(get_current_user)):
    with Session(engine) as session:
        q = session.exec(select(func.sum(Expense.amount)).where(Expense.user_id == user.id))
        total = q.first()
        return {"total_spent": total or 0}
