import sys

from pydantic import BaseSettings

IS_RUNNING_TESTS = 'pytest' in sys.modules


class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_pass: str
    db_name: str
    db_port: int

    secret_key: str

    @property
    def db_url(self):
        return f'postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'


settings = Settings()
