from dotenv import load_dotenv
import os
from typing import Any, Dict, Optional
from pydantic import PostgresDsn, validator

load_dotenv()


def get_url():
    user = os.getenv("POSTGRES_USER", "postgres")
    password = os.getenv("POSTGRES_PASSWORD", "postgres")
    server = os.getenv("POSTGRES_SERVER", "db")
    db = os.getenv("POSTGRES_DB", "app")
    return f"postgresql://{user}:{password}@{server}/{db}"


class Settings:
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SECRET_KEY = os.getenv("SECRET_KEY")
    FIRST_SUPERUSER = os.getenv("FIRST_SUPERUSER")
    FIRST_SUPERUSER_PASSWORD = os.getenv("FIRST_SUPERUSER_PASSWORD")
    SQLALCHEMY_DATABASE_URI = get_url()


settings = Settings()
