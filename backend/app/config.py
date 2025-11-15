from pathlib import Path

from pydantic_settings import BaseSettings

# Root project directory (one level up from /app)
BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    APP_NAME: str = "RtaFlow"

    # Use SQLite by default, override via .env later
    DB_NAME: str = "rtaflow.db"
    DATABASE_URL: str = f"sqlite:///{BASE_DIR / 'data' / DB_NAME}"

    # Security
    SECRET_KEY: str = "8AB7F5E3393B9A12E0F46309EC1B839E1E74677B507E50AB23C7223BB16AFD38"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    ALGORITHM: str = "HS256"  # ← added this (your auth.py was using settings.algo)

    class Config:
        env_file = BASE_DIR / ".env"


settings = Settings()
