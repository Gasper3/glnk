from fastapi import APIRouter

from app.db import db_session
from app.schemas import StatisticsResponse

from ..dependencies import UrlDep
from ..repositories import UrlVisitsRepository

api_router = APIRouter(prefix='/api/url/{short_url}', tags=['statistics'])


@api_router.get('/stats', response_model=StatisticsResponse)
async def get_visits(url: UrlDep):
    with db_session() as session:
        rep = UrlVisitsRepository(session)
        return {'url': url.url, 'stats': rep.get_stats(url)}


@api_router.get('/stats/monthly')
async def get_visits_monthly(url: UrlDep):
    with db_session() as session:
        rep = UrlVisitsRepository(session)
        monthly_visits = rep.get_monthly(url)
        return {'url': url.url, 'monthly_visits': monthly_visits}
