from sa_repository import BaseRepository

from .models import UrlVisits, Url


class UrlRepository(BaseRepository[Url]):
    MODEL_CLASS = Url


class UrlVisitsRepository(BaseRepository[UrlVisits]):
    MODEL_CLASS = UrlVisits
