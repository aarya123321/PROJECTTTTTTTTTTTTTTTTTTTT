from sqlmodel import SQLModel, create_engine, Session
from pathlib import Path

DB_FILE = Path(__file__).parent.parent / "database.db"
DATABASE_URL = f"sqlite:///{DB_FILE}"

engine = create_engine(DATABASE_URL, echo=False)

def init_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
