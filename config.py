from functools import lru_cache

from pydantic.v1 import BaseSettings
from dotenv import find_dotenv


class Settings(BaseSettings):
    USER_DB: str
    PASSWORD_DB: str
    DATABASE_DB: str
    HOST_DB: str
    PORT_DB: str

    class Config:
        env_file = find_dotenv(".env")


@lru_cache()
def get_settings():
    return Settings()