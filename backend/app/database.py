import logging
from pathlib import Path
from typing import Annotated
from venv import logger

from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import settings

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s in %(module)s: %(message)s]",
    handlers=[logging.StreamHandler()],
)
logger = logging.getLogger(settings.APP_NAME)


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
    echo=False,
    future=True,
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except SQLAlchemyError as e:
        db.rollback()
        logger.error(f"Database transction Failed : {e}")
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]
