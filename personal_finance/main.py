from fastapi import FastAPI
from .routers import auth as auth_router
from .routers import expenses as expenses_router
from .routers import budgets as budgets_router
from .routers import reports as reports_router
from .db import init_db

app = FastAPI(title="Personal Finance API")

app.include_router(auth_router.router)
app.include_router(expenses_router.router)
app.include_router(budgets_router.router)
app.include_router(reports_router.router)


@app.on_event("startup")
def on_startup():
    init_db()


@app.get("/")
def root():
    return {"ok": True}
