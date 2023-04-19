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
        grouped_visits = rep.get_grouped_by_date(url)
        return {'url': url.url, 'stats': grouped_visits}


@api_router.get('/stats/monthly')
async def get_visits_monthly(url: UrlDep):
    with db_session() as session:
        rep = UrlVisitsRepository(session)
        monthly_visits = rep.get_monthly(url)
        return {'url': url.url, 'monthly': monthly_visits}