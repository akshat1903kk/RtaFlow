from pathlib import Path
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import settings

# Make sure the /data directory exists
db_path = Path(settings.DATABASE_URL.replace("sqlite:///", "")).parent
db_path.mkdir(parents=True, exist_ok=True)


# SQLAlchemy Base
class Base(DeclarativeBase):
    pass


# Engine (SQLite for now)
engine = create_engine(
    settings.DATABASE_URL,
    connect_args={"check_same_thread": False},  # SQLite threading quirk
    echo=False,  # Set to True if you want query logs
    future=True,
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
