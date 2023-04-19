import random
from datetime import datetime

import pytest

from app.models import Url
from app.repositories import UrlVisitsRepository

from . import factories


class TestUrlVisitsRepository:
    @pytest.fixture()
    def url(self):
        return factories.UrlFactory()

    @pytest.fixture()
    def repository(self, db_session):
        return UrlVisitsRepository(db_session)

    def test_monthly(self, url, repository: UrlVisitsRepository):
        factories.UrlVisitsFactory.create_batch(random.randint(1, 10), url=url, created=datetime(2022, 12, 25))
        visits_april = factories.UrlVisitsFactory.create_batch(
            random.randint(1, 10),
            url=url,
            created=datetime(2023, 4, 1)
        )
        visits_march = factories.UrlVisitsFactory.create_batch(
            random.randint(1, 10),
            url=url,
            created=datetime(2023, 3, 1)
        )

        monthly_visits = repository.get_monthly(url)

        expected_result = {
            3: len(visits_march),
            4: len(visits_april),
        }
        assert monthly_visits == expected_result
