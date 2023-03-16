from fastapi.routing import APIRouter

api_router = APIRouter(prefix='api/url')


@api_router.post('')
async def create_short_url():
    pass
