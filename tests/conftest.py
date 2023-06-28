import pytest
from fastapi.testclient import TestClient
from app.api import app
from app.db import SessionTest
from app.models import Base
from config import settings
from sqlalchemy import create_engine, text
from unittest import mock


TEST_DB_URL = f'{settings.postgres_url}/glnk_test'


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.fixture(autouse=True, scope='session')
def create_db():
    engine = create_engine(settings.postgres_url)
    connection = engine.connect()
    connection.execution_options(isolation_level="AUTOCOMMIT")

    connection.execute(text(f'DROP DATABASE IF EXISTS glnk_test;'))
    connection.execute(text(f'CREATE DATABASE glnk_test;'))

    try:
        yield
    finally:
        connection.execute(text(f'DROP DATABASE glnk_test;'))
    connection.close()


@pytest.fixture(scope='session')
def engine():
    _engine = create_engine(TEST_DB_URL)

    with _engine.begin() as conn:
        Base.metadata.create_all(bind=conn)
    SessionTest.configure(bind=_engine)
    yield _engine
    with _engine.begin() as conn:
        Base.metadata.drop_all(bind=conn)
    _engine.dispose()


@pytest.fixture(scope='session')
def prepare_db(engine):
    # SessionTest.configure(bind=engine)
    yield


@pytest.fixture(autouse=True)
def db_session(prepare_db):
    ses = SessionTest()
    ses.begin_nested()
    with mock.patch.object(ses, 'commit'):
        with mock.patch.object(ses, 'rollback'):
            with mock.patch.object(ses, 'close'):
                yield ses
    ses.rollback()
    ses.close()
