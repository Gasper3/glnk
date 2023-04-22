from datetime import datetime, timedelta
import more_itertools

import sqlalchemy as sa
from sa_repository import BaseRepository

from .models import Url, UrlVisits


class UrlRepository(BaseRepository[Url]):
    MODEL_CLASS = Url


class UrlVisitsRepository(BaseRepository[UrlVisits]):
    MODEL_CLASS = UrlVisits

    def get_stats(self, url: Url) -> dict:
        return {
            'monthly_visits': self.get_monthly(url),
            'visits_count': self.count(url),
        }

    def get_monthly(self, url: Url) -> dict[int, int]:
        visits_query = (
            self.get_query(
                UrlVisits.url == url, UrlVisits.created > datetime.today() - timedelta(days=90),
                select=(sa.func.extract('month', UrlVisits.created), sa.func.count())
            )
            .group_by(sa.func.extract('month', UrlVisits.created))
        )
        monthly = self.session.execute(visits_query).all()
        return dict(monthly)

    def count(self, url: Url):
        query = self.get_query(UrlVisits.url == url, select=(sa.func.count(),))
        return more_itertools.first(self.session.execute(query).first(), 0)
