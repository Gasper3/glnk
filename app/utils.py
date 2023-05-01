import uuid

from config import settings
from . import schemas


common_responses = {
    400: {'model': schemas.BadRequestSchema, 'description': 'Bad request'},
    500: {'model': schemas.ErrorSchema, 'description': 'Internal server error'},
}

get_responses = {404: {'model': schemas.BadRequestSchema, 'description': 'Item not found'}, **common_responses}


def generate_short_url() -> str:
    return uuid.uuid4().hex[: settings.short_url_size].upper()
