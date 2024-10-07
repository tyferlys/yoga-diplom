import asyncpg
from asyncpg import Connection

from src.utils.database_manager import DataBaseManager


class NetworkRepository(DataBaseManager):
    def __init__(self):
        super().__init__()
