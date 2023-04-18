from datetime import datetime, timedelta
from sa_repository import BaseRepository

from .models import UrlVisits, Url
import more_itertools



class UrlRepository(BaseRepository[Url]):
    MODEL_CLASS = Url


class UrlVisitsRepository(BaseRepository[UrlVisits]):
    MODEL_CLASS = UrlVisits

    def get_grouped_by_date(self, url: Url) -> dict:
        visits = self.find(UrlVisits.url == url, UrlVisits.created > datetime.today() - timedelta(days=90))
        monthly = more_itertools.groupby_transform(
            sorted(visits, key=lambda item: item.created),
            keyfunc=lambda v: v.created.month,
            valuefunc=lambda v: v.created.month,
            reducefunc=lambda g: len(list(g))
        )
        return {
            'monthly': dict(monthly)
        }
