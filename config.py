import os
import sys

from pydantic import BaseSettings

IS_RUNNING_TESTS = 'pytest' in sys.modules

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))


class Settings(BaseSettings):
    db_host: str
    db_user: str
    db_pass: str
    db_name: str
    db_port: int

    secret_key: str

    short_url_size: int = 5

    class Config:
        env_file = os.path.join(ROOT_DIR, '.env')

    @property
    def db_url(self):
        return f'postgresql://{self.db_user}:{self.db_pass}@{self.db_host}:{self.db_port}/{self.db_name}'


settings = Settings()
