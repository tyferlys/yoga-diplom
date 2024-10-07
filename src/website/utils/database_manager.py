from config import get_settings


class DataBaseManager:
    def __init__(self):
        settings = get_settings()
        self.db_config = {
            'user': settings.USER_DB,
            'password': settings.PASSWORD_DB,
            'database': settings.DATABASE_DB,
            'host': settings.HOST_DB,
            'port': settings.PORT_DB
        }