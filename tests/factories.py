from factory.alchemy import SQLAlchemyModelFactory, SESSION_PERSISTENCE_FLUSH
import factory
from app.db import SessionTest
from app import models
from app.utils import generate_short_url


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = SessionTest
        sqlalchemy_session_persistence = SESSION_PERSISTENCE_FLUSH


class UrlFactory(BaseFactory):
    class Meta:
        model = models.Url

    short_url = factory.LazyFunction(generate_short_url)
    url = factory.Sequence(lambda i: f'https://example{i}.com')
