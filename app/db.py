import contextlib

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from config import settings, IS_RUNNING_TESTS

engine = create_engine(settings.db_url)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionTest = scoped_session(sessionmaker())


@contextlib.contextmanager
def db_session():
    if IS_RUNNING_TESTS:
        session = SessionTest()
    else:
        session = Session()

    try:
        yield session
        if session.in_transaction():
            session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
