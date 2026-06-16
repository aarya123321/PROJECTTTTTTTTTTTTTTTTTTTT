from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from ..db import engine, init_db
from ..models import User
from ..schemas import UserCreate, Token
from ..auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.on_event("startup")
def on_startup():
    init_db()


@router.post("/register", status_code=201)
def register(payload: UserCreate):
    with Session(engine) as session:
        existing = session.query(User).filter(User.username == payload.username).first()
        if existing:
            raise HTTPException(status_code=400, detail="Username already exists")
        user = User(username=payload.username, email=payload.email, hashed_password=get_password_hash(payload.password))
        session.add(user)
        session.commit()
        session.refresh(user)
        return {"id": user.id, "username": user.username}


@router.post("/token", response_model=Token)
def token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect credentials")
    access_token = create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}
