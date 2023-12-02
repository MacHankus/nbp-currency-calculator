from typing import List

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "NBP CURRENCY CALCULATOR"
    PROJECT_HOST: str = "localhost"
    PROJECT_PORT: int = 9000

    BACKEND_CORS_ORIGINS: List[str] = []
    DB_HOST: str
    DB_PORT: str
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
